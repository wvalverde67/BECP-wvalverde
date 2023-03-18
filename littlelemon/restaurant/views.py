from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from .forms import BookingForm
from rest_framework.permissions import IsAuthenticated
import json
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# view for menu page
def menu(request):
    menu_items = Menu.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'restaurant/menu.html', context)

#view for booking page
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
    context = {'form': form}
    return render(request, 'restaurant/book.html', context)

# view for about page
def about(request):
    return render(request, 'restaurant/about.html', {})

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
    