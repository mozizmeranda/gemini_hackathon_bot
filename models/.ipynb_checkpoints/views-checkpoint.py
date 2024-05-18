from .models import Doctor,  Disease
from .serializers import DiseaseSerializer, DoctorSerializer, UserSerializer
from rest_framework import viewsets, views
from .models import User
import google.generativeai as genai
from rest_framework import status
from rest_framework.response import Response

GOOGLE_KEY = "AIzaSyBfNmZ-U0pnEPLS80Euylgav85tVJBbFDc"

genai.configure(api_key=GOOGLE_KEY)
model = genai.GenerativeModel('gemini-pro')
his = None
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DiseaseViewSet(viewsets.ModelViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()

    def create(self, request, *args, **kwargs):
        # 
        id = request.POST['user'][0]
        description = request.POST['description'][0]
        user = User.objects.get(id=id)   
        serializeredUser = UserSerializer(user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        try:
            %%time
            response = model.generate_content(description)
            response.resolve()
            for i in response:
                print(i.text)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print(f'{type(e).__name__}: {e}')

        


class ChatView(views.APIView):
    def post(self, request):
        request['data']['description']
