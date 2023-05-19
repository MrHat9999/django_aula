from contato.models import Contato
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContatoForm

# Create your views here.

def contato(request):
    if request.method == 'GET':
        return render(request, 'editar.html', { 'form': ContatoForm() })
    
    form = ContatoForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/contatos")
    
    return render(request, 'editar.html', { 'form': form })


def contatos(request):
    lista_contatos = Contato.objects.all().values('id', 'nome', 'fone')
    context = {"contatos": lista_contatos}
    return render(request, "contatos.html", context)


def detalhes(request, id):
    con = Contato.objects.get(pk=id)
    context = {"contato": con}
    return render(request, "detalhes.html", context)

