from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view  # Correct import

@api_view(['GET', 'POST'])  # Correct decorator usage
def index(request):
     if request.method == 'GET':
              
        courses = [
            {'id': 1, 'title': 'Python Programming', 'description': 'Learn Python'},
            {'id': 2, 'title': 'Django Web Framework', 'description': 'Learn Django'}
        ]
        return Response(courses)
     elif request.method == 'POST':
        print(request.data)
        return Response({'message': 'Data created'}, status=201)