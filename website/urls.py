from django.urls import path
from django.contrib import admin
from website import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('lynch/explication', views.lynch_explication, name="lynch_explication"),
    path('lynch/limites', views.lynch_limites, name="lynch_limites"),
    path('lynch/noeuds', views.lynch_noeuds, name="lynch_noeuds"),
    path('lynch/points_repere', views.lynch_points_repere, name="lynch_points_repere"),
    path('lynch/quartiers', views.lynch_quartiers, name="lynch_quartiers"),
    path('lynch/voies', views.lynch_voies, name="lynch_voies"),
    path('gare/cornavin/map', views.cornavinM, name="cornavinM"),
    path('gare/cornavin/patern', views.cornavinP, name="cornavinP"),
    path('gare/cornavin/description', views.cornavinD, name="cornavinD"),
    path('gare/cornavin/map_description', views.cornavinDM, name="cornavinDM"),
    path('gare/pontRouge/map', views.pontRougeM, name="pontRougeM"),
    path('gare/pontRouge/patern', views.pontRougeP, name="pontRougeP"),
    path('gare/pontRouge/description', views.pontRougeD, name="pontRougeD"),
    path('gare/pontRouge/map_description', views.pontRougeDM, name="pontRougeDM"),
    path('gare/bachet/map', views.bachetM, name="bachetM"),
    path('gare/bachet/patern', views.bachetP, name="bachetP"),
    path('gare/bachet/description', views.bachetD, name="bachetD"),
    path('gare/bachet/map_description', views.bachetDM, name="bachetDM"),
    path('gare/champel/map', views.champelM, name="champelM"),
    path('gare/champel/patern', views.champelP, name="champelP"),
    path('gare/champel/description', views.champelD, name="champelD"),
    path('gare/champel/map_description', views.champelDM, name="champelDM"),
    path('gare/eauxvives/map', views.eauxVivesM, name="eauxVivesM"),
    path('gare/eauxvives/patern', views.eauxVivesP, name="eauxVivesP"),
    path('gare/eauxvives/description', views.eauxVivesD, name="eauxVivesD"),
    path('gare/eauxvives/map_description', views.eauxVivesDM, name="eauxVivesDM"),
    path('gare/chenebourg/map', views.cheneBourgM, name="cheneBourgM"),
    path('gare/chenebourg/patern', views.cheneBourgP, name="cheneBourgP"),
    path('gare/chenebourg/description', views.cheneBourgD, name="cheneBourgD"),
    path('gare/chenebourg/map_description', views.cheneBourgDM, name="cheneBourgDM"),
    path('formulaire', views.formulaire, name="formulaire"),
]

