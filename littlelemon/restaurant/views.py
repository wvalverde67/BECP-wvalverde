from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from .forms import BookingForm
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes
import json
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
def index(request):
    current_year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})

# view for menu page
def menu(request):
    menu_items = Menu.objects.all()
    current_year = datetime.now().year
    context = {'menu_items': menu_items, 'current_year': current_year}
    return render(request, 'restaurant/menu.html', context)

#view for booking page
# this view is for authenticated users only
@login_required
@permission_classes([IsAuthenticated])
def book(request):
    if request.method == 'POST':
        # Decodificar los datos JSON enviados en la solicitud POST
        data = json.loads(request.body)

        # Crear una instancia de BookingForm con los datos decodificados
        form = BookingForm(data)
        if not form.is_valid():
            # Devolver una respuesta JSON en caso de error en la validación
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)

        form.save()
        # Devolver una respuesta JSON en caso de éxito
        return JsonResponse({"status": "success"}, status=201)
    # El código original para manejar solicitudes GET u otros métodos
    form = BookingForm()
    current_year = datetime.now().year
    context = {'form': form, 'current_year': current_year}
    return render(request, 'restaurant/book.html', context)

# view for about page
def about(request):
    current_year = datetime.now().year
    return render(request, 'restaurant/about.html', {'current_year': current_year})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    