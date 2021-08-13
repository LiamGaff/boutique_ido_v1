from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ return view_bag """
    return render(request, 'bag/bag.html')
