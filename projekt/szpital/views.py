from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from .forms import LoginForm, RegisterForm
from .models import *
from .serializers import *

class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

def index(request):
    return HttpResponse("UI Rejestracji.")

# Rejestracja, Logowanie, Strona Główna

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('base')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')      

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form})   
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('base')
        else:
            return render(request, 'users/register.html', {'form': form})
        
def base_view(request):
    return render(request, 'users/base.html')

# CRUD

@api_view(['GET'])
@permission_classes([IsAdminUser])
def patient_list(request):
    if request.method == 'GET':
        autorzy = Pacjent.objects.all()
        serializer = PacjentSerializer(autorzy, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def patient_detail(request, pesel):
    try:
        autor = Pacjent.objects.get(pesel=pesel)
    except Pacjent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PacjentSerializer(autor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PacjentSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def staff_list(request):
    if request.method == 'GET':
        autorzy = PersonelMedyczny.objects.all()
        serializer = PersonelMedycznySerializer(autorzy, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def staff_detail(request, numer_identyfikacyjny):
    try:
        autor = PersonelMedyczny.objects.get(numer_identyfikacyjny=numer_identyfikacyjny)
    except PersonelMedyczny.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonelMedycznySerializer(autor)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visits_list(request):
    if request.method == 'GET':
        autorzy = RejestracjaWizyt.objects.all()
        serializer = RejestracjaWizytSerializer(autorzy, many=True)
        return Response(serializer.data)

# Ponad CRUD

@api_view(['GET'])
@permission_classes([IsAdminUser])
def visits_count(request, pesel):
    try:
        patient = Pacjent.objects.get(pesel=pesel)
    except Pacjent.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)

    visits_count = RejestracjaWizyt.objects.filter(pacjent=patient).count()

    return Response({'patient': PacjentSerializer(patient).data, 'visits_count': visits_count})

@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAdminUser])
def staff_in_department(request, department_name):
    try:
        department = OddzialSzpitalny.objects.get(nazwa_oddzialu=department_name)
    except OddzialSzpitalny.DoesNotExist:
        return Response({'error': 'Department not found'}, status=404)

    staff_count = department.personel.count()  # Ilość pracowników w danym oddziale
    staff_members = department.personel.all()
    
    serializer = PersonelMedycznySerializer(staff_members, many=True)

    return Response({'department': department.nazwa_oddzialu, 'staff_count': staff_count, 'staff_members': serializer.data})