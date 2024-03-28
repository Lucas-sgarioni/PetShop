from django.shortcuts import render
from reserva.forms import ReservaForm

def reserva(request):
  sucesso = False

  if request.method == 'GET':
    form = ReservaForm()
  elif request.method == 'POST':
    form = ReservaForm(request.POST)
    if form.is_valid():
      sucesso = True
      form.save()

  context = {
    'nome': 'Veterinária Mariana',
    'telefone': '53 99235-6458',
    'formulario': form,
    'sucesso': sucesso
  }
  
  return render(request, 'reserva_de_banho.html', context)