from django.urls import path
from drivers.views import AllDriversResource, AddDriverResource, DriversResource

urlpatterns = [
    path('drivers/all', AllDriversResource.as_view()),
    path('driver', AddDriverResource.as_view()),
    path('driver/<int:driver_id>', DriversResource.as_view())
]
