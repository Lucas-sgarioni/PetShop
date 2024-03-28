from django.contrib import admin, messages
from base.models import Contato

@admin.action(description='Marcar Formulário(s) como Lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulário(s) de contato(s) marcado(s) como lido!', messages.SUCCESS)

@admin.action(description='Marcar Formulário(s) como NÃO lido(s)')
def marcar_como_nao_lido(modeladmin, request, queryset):
    queryset.update(lido=False)
    modeladmin.message_user(request, 'Formulário(s) de contato(s) marcado(s) como NÃO lido!', messages.SUCCESS)

#register yout models here
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'mensagem', 'lido']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]