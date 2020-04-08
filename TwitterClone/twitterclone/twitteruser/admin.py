from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import TwitterUser

# https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
# And refactored with the help of Peter

class MyUserAdmin(UserAdmin):
    model = TwitterUser
    # That last , MUST be there.
    fieldsets = (('SOME TEST', {'fields': ('display_name', 'following')} ),) + UserAdmin.fieldsets  


admin.site.register(TwitterUser, MyUserAdmin)