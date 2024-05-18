from .models import Doctor,  Disease
from .serializers import DiseaseSerializer, DoctorSerializer, UserSerializer
from rest_framework import viewsets, views
from .models import User
import google.generativeai as genai
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions



GOOGLE_KEY = "AIzaSyBfNmZ-U0pnEPLS80Euylgav85tVJBbFDc"

genai.configure(api_key=GOOGLE_KEY)
model = genai.GenerativeModel('models/gemini-pro')
his = None
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    parser_classes = [MultiPartParser, FormParser]



    def create(self, request, *args, **kwargs):
       
       return super().create(request, *args, **kwargs)


class DiseaseViewSet(viewsets.ModelViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()

    def create(self, request, *args, **kwargs):
        id = request.POST['user']
        description = request.POST['description']
        user = User.objects.get(id=id)   
        serializeredUser = UserSerializer(user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        try:
            for m in genai.list_models():
              if 'generateContent' in m.supported_generation_methods:
                print(m.name)
            result = model.generate_content(description)
            return Response({"response": result.text, "data": serializer.data, "user": serializeredUser.data}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print(f'{type(e).__name__}: {e}')

