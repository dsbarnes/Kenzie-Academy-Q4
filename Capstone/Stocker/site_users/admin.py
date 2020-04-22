from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Custom_User

# # https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Custom_User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('deposits', 'withdraws')}),
    )


admin.site.register(Custom_User, MyUserAdmin)
