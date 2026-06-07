from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='inicio'),
    path('robots.txt', robots_txt, name='robots_txt'),



    path('staff/', staff, name='staff'),

#---------////--------------Turnos---------////----------------------#

    path('turnos/', turnos , name='turnos'),   


#---------////--------------FINTurnos---------////----------------------#

]