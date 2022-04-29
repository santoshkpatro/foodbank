from django.shortcuts import render
from core.models import Booking, Item, Slot


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user, is_active=True)

    context = {
        'bookings': bookings
    }

    return render(request, 'bookings/list.html', context)


def booking_create(request):
    if request.method == 'POST':
        item_id = request.POST['item']
        slot_id = request.POST['slot']
        
        booking = Booking(user=request.user, item_id=item_id, slot_id=slot_id)
        booking.save()

    items = Item.objects.filter(is_available=True)
    slots = Slot.objects.filter(is_active=True)

    context = {
        'items': items,
        'slots': slots
    }
    return render(request, 'bookings/create.html', context)