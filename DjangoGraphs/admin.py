from django.contrib import admin

from .models import *

admin.site.register(Display)
admin.site.register(Graph)
admin.site.register(GraphSelector)
admin.site.register(Type)
admin.site.register(Instance)

admin.site.register(DataEntry)
