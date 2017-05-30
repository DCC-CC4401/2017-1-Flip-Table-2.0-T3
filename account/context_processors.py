from account.models import Client, Established, Peddler
from django.contrib.auth.models import User


def user_profile_image(request):
    current_user = request.user
    is_client = False
    if current_user.is_authenticated():
        try:
            current_user_profile = Client.objects.get(user=current_user)
            is_client = True
        except:
            try:
                current_user_profile = Established.objects.get(user=current_user)
            except:
                current_user_profile = Peddler.objects.get(user=current_user)
    else:
        current_user_profile = current_user

    return {'current_user_profile': current_user_profile, 'is_client': is_client}
