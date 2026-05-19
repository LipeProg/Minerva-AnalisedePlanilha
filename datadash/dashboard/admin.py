from django.contrib import admin
from .models import Venda, ArquivoImportado


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'produto', 'categoria', 'quantidade', 'preco_unitario', 'faturamento')
    list_filter = ('categoria', 'data')
    search_fields = ('produto', 'categoria')
    readonly_fields = ('data_importacao', 'faturamento')


@admin.register(ArquivoImportado)
class ArquivoImportadoAdmin(admin.ModelAdmin):
    list_display = ('nome_arquivo', 'data_upload', 'total_linhas')
    list_filter = ('data_upload',)
    readonly_fields = ('data_upload',)
