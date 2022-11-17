from django.contrib import admin
from .models import Juguetes
from .models import Alimentacion
from .models import Accesorios

admin.site.register(Juguetes)
admin.site.register(Accesorios)
admin.site.register(Alimentacion)


# Register your models here.
