from django.contrib import admin
from .models import Habitat, Criatura

# Register your models here.
admin.site.site_header = "Administracion del Bestiario"
admin.site.site_title = "Bestiario de Mobius"
admin.site.index_title = "Gestion de criaturas y habitats"

class CriaturaInline(admin.TabularInline):
    model = Criatura
    extra = 1
    fields = ('nombre', 'tipo', 'peligro', 'tamano_cm', 'visible')
    show_change_link = True


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clima', 'total_criaturas')
    list_filter = ('clima',)
    search_fields = ('nombre',)
    inlines = [CriaturaInline]

    @admin.display(description='Criaturas')
    def total_criaturas(self, obj):
        return obj.criaturas.count()

@admin.register(Criatura)
class CriaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'habitat', 'tipo', 'peligro', 'nivel',
                    'tamano_cm', 'visible')
    list_filter = ('tipo', 'habitat', 'visible', 'domesticable')
    search_fields = ('nombre', 'descripcion')
    ordering = ('habitat', 'nombre')
    list_editable = ('visible',)
    list_select_related = ('habitat',)
    actions = ['mostrar', 'ocultar']

    fieldsets = (
        ('Identificacion', {
            'fields':('nombre', 'habitat', 'tipo')
        }),
        ('Caracteristicas', {
            'fields':(('peligro', 'tamano_cm'),'domesticable'),
            'description': 'El peligro va de 1 (inofensivo) a 10 (muy peligroso).'
        }),
        ('Publicacion', {
            'fields':('visible', 'descripcion')
        }),
    )

    @admin.display(description='Nivel', ordering='peligro')
    def nivel(self, obj):
        return obj.nivel_peligro

    @admin.action(description="Mostrar en el sitio")
    def mostrar(self, request, queryset):
        n = queryset.update(visible=True)
        self.message_user(request, f"{n} criaturas ahora son visibles")

    @admin.action(description="Ocultar del sitio")
    def ocultar(self, request, queryset):
        n = queryset.update(visible=False)
        self.message_user(request, f"{n} criaturas ocultadas del sitio")