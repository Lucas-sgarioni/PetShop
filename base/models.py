from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_lenght=50)
    email = models.EmailField(max_lenght=75)
    mensagem = models.TextField()
    data = models.DataTimeField(auto_now_add=True)
    lido = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f'Nome: {self.nome} - E-mail: {self.email}'
    
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['nome']

class Reserva(models.Model):
    nomeDoPet = models.CharField(max_lenght=50, verbose_name='Nome do PET')
    telefone = models.CharField(max_lenght=15)
    dia = models.DateField(verbose_name='Dia da Reserva')
    observacoes = models.TextField(verbose_name='Observações')