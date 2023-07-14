from .models import favoritos

def user_favorites(request):
    user_favorites = []

    if request.user.is_authenticated:
        user_favorites = favoritos.objects.filter(user=request.user)

    return {'user_favorites': user_favorites}
