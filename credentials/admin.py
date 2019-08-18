from django.contrib import admin
from credentials.models import *


class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('Username','mobile',)
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    # list_per_page = 25
    def Username(self,object):
        return object.user.username
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)

class idCloneInfoAdmin(admin.ModelAdmin):
    list_display = ('Username','email','password')
    def Username(self,object):
        return object.user.username

admin.site.register(idClone, idCloneInfoAdmin)