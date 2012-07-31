from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^upload/(?P<id>\d+)$', benchmark_grade_upload),
    (r'^student_grade$', student_grade),
    (r'^family_grade$', family_grade),
    (r'^gradebook$', gradebook),
)
