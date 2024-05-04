from .models import Todo
from .serializer import TodoSerializer

# rest framework packages
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    if request.method == 'GET':
        return Response(serializer.data)