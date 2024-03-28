from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nomoDoPet', 'nomeDoDono', 'dia', 'turno']
    search_fields = ['nomeDoPet', 'nomeDoDono']
    list_filter = ['dia', 'turno', 'tamanho']