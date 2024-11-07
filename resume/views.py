from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Resume
from .serializers import ResumeSerializer
from authentication.authentication import CustomAuthentication

class ResumeView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

    def post(self, request):
        request.data['created_by'] = request.user.id
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            resume = get_object_or_404(Resume, id=id)
            if resume.created_by != request.user:
                return Response({"detail": "You do not have permission to view this resume."},
                                status=status.HTTP_403_FORBIDDEN)

            serializer = ResumeSerializer(resume)
        else:
            resumes = Resume.objects.filter(created_by=request.user)
            serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        resume = get_object_or_404(Resume, id=id)

        if resume.created_by != request.user:
            return Response({"detail": "You do not have permission to edit this resume."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = ResumeSerializer(resume, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        resume = get_object_or_404(Resume, id=id)
        
        if resume.created_by != request.user:
            return Response({"detail": "You do not have permission to edit this resume."},
                            status=status.HTTP_403_FORBIDDEN)

        resume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
