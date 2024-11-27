from django.contrib import admin
from .models import User,Rating,Recipe

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Rating)

