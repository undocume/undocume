from django.contrib import admin
from home.models import *

# Register your models here.
class CategoryTranslateInline(admin.StackedInline):
    model = CategoryTranslate
    extra = 2

class ServiceTranslateInline(admin.StackedInline):
    model = ServiceTranslate
    extra = 2

class TypeOrganizationTranslateInline(admin.StackedInline):
    model = TypeOrganizationTranslate
    extra = 2

class TypeOrganizationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [TypeOrganizationTranslateInline]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [CategoryTranslateInline]

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [ServiceTranslateInline]

admin.site.register(Language)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(TypeOrganization,TypeOrganizationAdmin)
admin.site.register(Information)
