# type:ignore
from django.contrib import admin
from .models import Profile,Admin,Client,Cermon,ImpactCategory,Impact,Event,PaymentMethod,Gallery,Faq,Team


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Cermon)
admin.site.register(Event)
admin.site.register(Impact)
admin.site.register(ImpactCategory)
admin.site.register(PaymentMethod)
admin.site.register(Gallery)
admin.site.register(Team)
admin.site.register(Faq)



