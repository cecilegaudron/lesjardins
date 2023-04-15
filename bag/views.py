from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """
    Basic view to return the bag contents page
    """
    return render(request, 'bag/bag.html')