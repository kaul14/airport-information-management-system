from django.contrib import admin
from . models import AircraftTypeModel,NewLocationModel,NewwOperatorModel,NewAircraftModel,NewDepartureModel,NewArrivalModel
# Register your models here.
admin.site.register(AircraftTypeModel)
admin.site.register(NewLocationModel)
admin.site.register(NewwOperatorModel)
admin.site.register(NewAircraftModel)
admin.site.register(NewDepartureModel)
admin.site.register(NewArrivalModel)
