from .views import TaskList
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskList)

app_name = 'tasks'
urlpatterns = [
    path('', include(router.urls)),
]