from django.shortcuts import render


def handler404(request, exception=None):
    """Error page 404"""
    return render(request, "errors/404.html", status=404)


def handler500(request, exception=None):
    """Error page 500"""
    return render(request, "errors/500.html", status=500)
