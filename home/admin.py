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

class InformationTypeTranslateInline(admin.StackedInline):
    model = InformationTypeTranslate
    extra = 2

class InformationTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [InformationTypeTranslateInline]

class TypeOrganizationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [TypeOrganizationTranslateInline]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [CategoryTranslateInline]

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [ServiceTranslateInline]

class InformationTranslateInline(admin.StackedInline):
    model = InformationTranslate
    extra = 2

class InformationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    inlines = [InformationTranslateInline]

admin.site.register(Language)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(TypeOrganization,TypeOrganizationAdmin)
admin.site.register(Information,InformationAdmin)
admin.site.register(InformationType,InformationTypeAdmin)

