from django.contrib import admin

from exam_apr_2022.gamesplay.models import Profile, Game


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
