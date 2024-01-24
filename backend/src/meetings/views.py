from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meeting
from projects.models import Project
from .serializers import MeetingSerializer
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class ManageMeetingsView(APIView):
    def get(self, request):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

class CreateMeetingView(APIView):
    def post(self, request, slug):
        try:
            slug = slug
            user = request.user
            if not slug:
                return Response(
                    {'error': 'Must provide slug'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not Project.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'Published Project with this slug does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
            if user.is_founder:
                return Response(
                    {'error': 'Founders cannot create meetings'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                data = request.data
                project = Project.objects.get(slug = slug).project_name
                
                founder = Project.objects.get(slug = slug).founder
                data["invitee"] = user.email
                
                option_1_time = data["option_1_time"]
                option_2_time = data["option_2_time"]
                option_3_time = data["option_3_time"]
                description = data["description"]
                
                is_accepted = data["is_accepted"]

                if is_accepted == "true":
                    is_accepted = True
                else:
                    is_accepted = False    

                data = {
                    "option_1_time": option_1_time,
                    "option_2_time": option_2_time,
                    "option_3_time": option_3_time,
                    "description": description,
                    "is_accepted": is_accepted,
                    "project": project,
                    "chosen_time": None,
                    "link": None,
                    "founder": founder,
                    "invitee": user.email,

                }     
                serializer = MeetingSerializer(data=data)

                if not serializer.is_valid():
                    return Response(
                        {'error': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                serializer.save()       

               
                Meeting.objects.create(
                    founder=founder,
                    invitee=user.email,
                    option_1_time=option_1_time,
                    option_2_time=option_2_time,
                    option_3_time=option_3_time,
                    is_accepted=is_accepted,
                    description=description,
                    project = project,
                    chosen_time = None,
                    link = None,                    
                   
                )
                send_mail("Meeting requested", " You have requested a meeting. Please wait for the founder to accept", 'settings.EMAIL_HOST_USER', [user.email], fail_silently=False)
                send_mail("Meeting_request", "Hi! You have a meeting invitation. Please visit seedstartups.tech to see more", 'settings.EMAIL_HOST_USER', [founder], fail_silently=False)
               
                return Response(
                    {'success': 'Meeting created successfully, wait for the founder to accept'},
                    status=status.HTTP_201_CREATED
                )
                
                
           
        except:
            return Response(
                {'error': 'Something went wrong when creating a meeting' },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AcceptAndChooseTimeView(APIView):
    def post(self, request, id):
        try:
            user = request.user
            if Meeting.objects.get(id=id).founder != user.email:
                return Response(
                    {'error': 'You are not the founder of this project'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not user.is_founder:
                return Response(
                    {'error': 'Only founders can accept meetings'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            chosen_time = request.data.get('chosen_time')
            link = request.data.get('link')
            is_accepted = request.data.get('is_accepted')
            if is_accepted == "true":
                is_accepted = True
            else:
                is_accepted = False
            Meeting.objects.filter(id=id).update(chosen_time=chosen_time, link=link, is_accepted=is_accepted)
            project = Meeting.objects.get(id=id).project
            invitee = Meeting.objects.get(id=id).invitee
            founder = Meeting.objects.get(id=id).founder
            send_mail("Meeting accepted", "Founder of {project} accepted the meeting. Please visit seedstartups.tech for more details", 'settings.EMAIL_HOST_USER', [invitee], fail_silently=False)
            send_mail("Meeting accepted", "Hi! You have accepted meeting with {invitee} on {chosen_time}. See seedstartup.tech for more details", 'settings.EMAIL_HOST_USER', [founder], fail_silently=False)

            return Response({'success': 'Date chosen successfully'}, status=status.HTTP_200_OK)
        except Meeting.DoesNotExist:
            return Response({'error': 'Meeting not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CancelMeetingView(APIView):
    def delete(self, request, id):
        try:
            Meeting.objects.filter(id=id).delete()
            return Response({'success': 'Meeting canceled successfully'}, status=status.HTTP_200_OK)
        except Meeting.DoesNotExist:
            return Response({'error': 'Meeting not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AcceptedMeetingsView(APIView):
    def get(self, request):
        try: 
            user = request.user
            meetings = Meeting.objects.filter(founder = user.email, is_accepted=True)
            serializer = MeetingSerializer(meetings, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {'error': 'Something went wrong when getting meetings' },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PendingMeetingsView(APIView):
    def get(self, request):
        meetings = Meeting.objects.filter(is_accepted=False)
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

class RescheduleMeetingsView(APIView):
    def put(self, request, id):
        try:
            id = id
            option_1_time = request.data.get('option_1_time')
            option_2_time = request.data.get('option_2_time')
            option_3_time = request.data.get('option_3_time')
            description = request.data.get('description')
            Meeting.objects.filter(id=id).update(option_1_time=option_1_time, option_2_time=option_2_time, option_3_time=option_3_time, is_accepted=False, description=description)
            return Response({'success': 'Meeting rescheduled successfully, wait for founders response'}, status=status.HTTP_200_OK)
        except Meeting.DoesNotExist:
            return Response({'error': 'Meeting not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



