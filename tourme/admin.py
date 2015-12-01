from django.contrib import admin

# Register your models here.

from.models import User, Landmarks

class SignUpAdmin(admin.ModelAdmin):
 list_display = ['email', 'name', 'password', 'timestamp', 'updated']
 class Meta:
    model = User
admin.site.register(User, SignUpAdmin)


class LandmarksAdmin(admin.ModelAdmin):
 list_display = ['place_name', 'address', 'place_desc','wiki_link', 'opening_days', 'admission', 'latitude', 'longtitude']
 class Meta:
    model = Landmarks
admin.site.register(Landmarks, LandmarksAdmin)