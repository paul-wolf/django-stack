from django.contrib import admin

from . models import Foo

class FooAdmin(admin.ModelAdmin):
     list_display = ('__unicode__' ,)
     search_fields = ['content']

admin.site.register(Foo,FooAdmin)
