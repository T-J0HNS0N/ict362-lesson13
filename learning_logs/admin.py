from django.contrib import admin

from .models import Topic, Entry

#Sets up the models to pull from other learning_logs
admin.site.register(Topic)
admin.site.register(Entry)
