from django.contrib import admin

# Register your models here.
from .models import Enquiry , Product , Service , Category , Employee , Customer

admin.site.register(Employee)
admin.site.register(Enquiry)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Category)

admin.site.register(Customer)