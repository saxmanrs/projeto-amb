from django.contrib import admin
from .models import CboModel
from .models import PessoaModel

# Register your models here.


admin.site.register(CboModel)
admin.site.register(PessoaModel)