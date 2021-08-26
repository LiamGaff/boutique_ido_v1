from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JSey2IdhFlB16DTWznPmmrt7w62ooXMT0k9IJgc42ZklkYeq9D2TQX9haat8Z2qYvhY49DSzcpMC2VKC9mvzmOt00NAd8fdeU',
        }

    return render(request, template, context)
