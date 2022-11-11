from django.urls import path
from . import views


urlpatterns = [
    path('',views.Index,name='index'),
    path('u/<int:id>/<str:name>',views.Update,name='update'),
    path('changestate/<int:id>',views.ChangeState,name="changestate"),
    path('test/',views.Test,name='test'),
    ]