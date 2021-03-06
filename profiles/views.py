from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm, CompanyProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    company = profile.company

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')

    form = UserProfileForm(instance=profile)
    company_form = CompanyProfileForm(instance=company)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'company_form': company_form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number: {order_number} .'
        ' A confirmation email was sent on the order date.'
        ' Please contact us if you did not recive one.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
