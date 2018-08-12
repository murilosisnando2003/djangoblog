from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person
from .models import Post


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

# Register your models here.

admin.site.register(Post)
