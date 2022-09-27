from . import views
from django.urls import re_path


urlpatterns = [

    re_path(r'^$',views.loginsave, name='loginsave'),
    re_path(r'^logouts$',views.logouts, name='logouts'),
   

    #------------------ADMIN-------------------------#

    re_path(r'^index_admin$',views.index_admin, name='index_admin'),
    re_path(r'^admin_dashboard$',views.admin_dashboard, name='admin_dashboard'),
   
   #-----------------------INSTITIUTE----------------#
    re_path(r'^institute_lead$',views.institute_lead, name='institute_lead'),
    re_path(r'^index_institute$',views.index_institute, name='index_institute'),
    re_path(r'^institute_dashboard$',views.institute_dashboard, name='institute_dashboard'),
    re_path(r'^institute_visitors$',views.institute_visitors, name='institute_visitors'),
    re_path(r'^institute_visitors_delete/(?P<id>\d+)$',views.institute_visitors_delete, name='institute_visitors_delete'),
    re_path(r'^institute_staff$',views.institute_staff, name='institute_staff'),
    re_path(r'^institute_staff_delete/(?P<id>\d+)$',views.institute_staff_delete, name='institute_staff_delete'),
    re_path(r'^institute_staff_update/(?P<id>\d+)$',views.institute_staff_update, name='institute_staff_update'),
    re_path(r'^institute_staff_updatesave/(?P<id>\d+)$',views.institute_staff_updatesave, name='institute_staff_updatesave'),
    re_path(r'^institute_admission$',views.institute_admission, name='institute_admission'),
    re_path(r'^institute_admission_delete/(?P<id>\d+)$',views.institute_admission_delete, name='institute_admission_delete'),
    re_path(r'^admin_institute_view$',views.viewinstitute, name='admin_institute_view'),
    re_path(r'^deleteinstitute/(?P<ins_id>\d+)$',views.deleteinstitute, name='deleteinstitute'),
    re_path(r'^institute_transport$',views.institute_transport, name='institute_transport'),
    re_path(r'^bus_details/(?P<id>\d+)$',views.bus_details, name='bus_details'),
    re_path(r'^institute_transport_delete/(?P<id>\d+)$',views.institute_transport_delete, name='institute_transport_delete'),
    re_path(r'^institute_bus$',views.institute_bus, name='institute_bus'),
    re_path(r'^driver_details$',views.driver_details, name='driver_details'),
    re_path(r'^driver_details_delete/(?P<id>\d+)$',views.driver_details_delete, name='driver_details_delete'),
    re_path(r'^exam_result$',views.exam_result, name='exam_result'),
    re_path(r'^details(?P<id>\d+)$',views.details, name='details'),
    re_path(r'^student_fee$',views.student_fee, name='student_fee'),
    re_path(r'^classes$',views.classes, name='classes'),
    re_path(r'^add_onlineclass$',views.add_onlineclass, name='add_onlineclass'),
    re_path(r'^add_recordedclass$',views.add_recordedclass, name='add_recordedclass'),
    re_path(r'^add_studymaterial$',views.add_studymaterial, name='add_studymaterial'),

    #-------------------------Student------------------------#
    re_path(r'^index_student$',views.index_student, name='index_student'),
    re_path(r'^index_student_dashboard$',views.index_student_dashboard, name='index_student_dashboard'),
    re_path(r'^student_pr$',views.student_pr, name='student_pr'),
    re_path(r'^student_recordedclass$',views.student_recordedclass, name='student_recordedclass'),
    re_path(r'^student_onlineclass$',views.student_onlineclass, name='student_onlineclass'),
    re_path(r'^student_studymaterial$',views.student_studymaterial, name='student_studymaterial'),
    re_path(r'^student_librarycard$',views.student_librarycard, name='student_librarycard'),







   #-------------------------Staff--------------------------#
    re_path(r'^index_staff$',views.index_staff, name='index_staff'),
    re_path(r'^index_staff_dashboard$',views.index_staff_dashboard, name='index_staff_dashboard'),





#------------------copies-----------------#
    re_path(r'^staff$',views.staff, name='staff'),
    re_path(r'^staff_delete/(?P<id>\d+)$',views.staff_delete, name='staff_delete'),
    re_path(r'^staff_update/(?P<id>\d+)$',views.staff_update, name='staff_update'),



    re_path(r'^visitor$',views.visitor, name='visitor'),
    re_path(r'^visitor_delete/(?P<id>\d+)$',views.visitor_delete, name='visitor_delete'),
    
    re_path(r'^lead$',views.lead, name='lead'),

    re_path(r'^admission$',views.admission, name='admission'),
    re_path(r'^admission_delete/(?P<id>\d+)$',views.admission_delete, name='admission_delete'),


    re_path(r'^transportation$',views.transportation, name='transportation'),
    re_path(r'^institute_transport_copy$',views.institute_transport_copy, name='institute_transport_copy'),
    re_path(r'^bus_details_copy/(?P<id>\d+)$',views.bus_details_copy, name='bus_details_copy'),

    re_path(r'^video_class$',views.video_class, name='video_class'),

]
