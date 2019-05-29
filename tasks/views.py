
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import viewsets
# Create your views here.


class TaskList(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().filter(status__gt=0).order_by("-dt_create")
    serializer_class = TaskSerializer
