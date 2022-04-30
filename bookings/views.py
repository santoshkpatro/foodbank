from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Booking, Item, Slot


@login_required(login_url='index')
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user, is_active=True)

    context = {
        'bookings': bookings
    }

    return render(request, 'bookings/list.html', context)


@login_required(login_url='index')
def booking_create(request):
    if request.method == 'POST':
        item_id = request.POST['item']
        slot_id = request.POST['slot']
        additional_item_id = request.POST.get('additional_item', None)
        
        slot = Slot.objects.get(id=slot_id)

        if slot.available == 0:
            messages.warning(request, 'Slot is full')
            return redirect('booking_create')

        booking = Booking(user=request.user, item_id=item_id, additional_item_id=additional_item_id, slot_id=slot_id)
        booking.save()
        slot.available = slot.available - 1
        slot.save()
        
        messages.success(request, 'Booking done')
        return redirect('booking_list')

    items = Item.objects.filter(is_available=True)
    slots = Slot.objects.filter(is_active=True)

    context = {
        'items': items,
        'slots': slots
    }
    return render(request, 'bookings/create.html', context)