from django.shortcuts import render

# Create your views here.
def about(request):
    """Renders the about page."""
    return render(request, "shopping_list/about.html")