from django.contrib import admin
from .models import UserAccount
from django.contrib.auth import get_user_model
admin.register(UserAccount)

User = get_user_model()
class UserAdmin(admin.ModelAdmin):
    using = 'accounts'
    list_display = ('id', 'name', 'email', )
    list_display_links = ('id', 'name', 'email', )
    search_fields = ('name', 'email', )
    list_per_page = 25

admin.site.register(User, UserAdmin)

