from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateMeetingView, ManageMeetingsView, AcceptAndChooseTimeView, CancelMeetingView, AcceptedMeetingsView, PendingMeetingsView, RescheduleMeetingsView

urlpatterns = [
    path('create_meeting/<slug:slug>',CreateMeetingView.as_view()),
    path('all_meetings',ManageMeetingsView.as_view()),
    path('accept_time/<id>',AcceptAndChooseTimeView.as_view()),
    path('cancel_meeting/<id>',CancelMeetingView.as_view()),
    path('accepted_meetings',AcceptedMeetingsView.as_view()),
    path('pending_meetings',PendingMeetingsView.as_view()),
    path('reschedule_meeting/<id>',RescheduleMeetingsView.as_view()),


]