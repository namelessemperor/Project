from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router =DefaultRouter();
router.register('champion', views.APIChampion)

urlpatterns = [
    path('views/',views.TestView, name = 'testview'),
    path('search/info/',views.ChampionInfo, name = 'info'),
    path('search/', views.SearchBar, name = 'search'),
    path('teambuild/', views.TeamBuilding, name = 'teambuild'),
    path('team/',views.TeamName, name = 'name'),
    path('save/', views.Save, name = 'save'),
    path('api/',include(router.urls)),
]
