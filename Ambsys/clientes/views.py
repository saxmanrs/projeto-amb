from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import PessoaModel,CboModel
from .forms import PessoasForm,CboForms

# Create your views here.

@login_required
def cbo_new (request):
    form = CboModel(request.POST or None, request.FILES or None)


    if form.is_valid():
        form.save()
        return redirect ('index')
    return render (request, 'cbo.html', {'form':form})
