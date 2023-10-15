from django.conf import settings

"""Context processor introducing dev mode boolean for a development mode view of the app"""
def development_mode(request):
    return {
        "development_mode": settings.DEBUG
    }
