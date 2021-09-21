from django.urls import path
from django.contrib import admin
from mobile import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('carougeBachet', views.carougeBachet, name="carougeBachet"),
    path('carougeBachet/info', views.carougeBachet, name="carougeBachet"),
    path('carougeBachet/map', views.carougeBachetMap, name="carougeBachetMap"),

    path('champelHopital', views.champelHopital, name="champelHopital"),
    path('champelHopital/info', views.champelHopital, name="champelHopital"),
    path('champelHopital/map', views.champelHopitalMap, name="champelHopitalMap"),

    path('cheneBourg', views.cheneBourg, name="cheneBourg"),
    path('cheneBourg/info', views.cheneBourg, name="cheneBourg"),
    path('cheneBourg/map', views.cheneBourgMap, name="cheneBourgMap"),

    path('cornavin', views.cornavin, name="cornavin"),
    path('cornavin/info', views.cornavin, name="cornavin"),
    path('cornavin/map', views.cornavinMap, name="cornavinMap"),

    path('geneveEauxVives', views.geneveEauxVives, name="geneveEauxVives"),
    path('geneveEauxVives/info', views.geneveEauxVives, name="geneveEauxVives"),
    path('geneveEauxVives/map', views.geneveEauxVivesMap, name="geneveEauxVivesMap"),

    path('lancyPontRouge', views.lancyPontRouge, name="lancyPontRouge"),
    path('lancyPontRouge/info', views.lancyPontRouge, name="lancyPontRouge"),
    path('lancyPontRouge/map', views.lancyPontRougeMap, name="lancyPontRougeMap"),
]

