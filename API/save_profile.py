from User.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user.Profile
        if profile is None:
            profile = Profile(user=user)
        profile.gender = response.get('gender')
        profile.facebook_link = response.get('link')
        profile.save()


