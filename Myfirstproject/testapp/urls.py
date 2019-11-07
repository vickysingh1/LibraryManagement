
from testapp import views
from django.conf.urls import url

urlpatterns=[
    url('employees',views.employees_info_view),
]