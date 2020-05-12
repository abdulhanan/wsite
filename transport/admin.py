from django.contrib import admin
from .models import transport, TransportBooking
# Register your models here.
admin.site.register(transport)
admin.site.register(TransportBooking)
