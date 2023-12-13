from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include("lib_app1.urls"))
    path('',views.home,name="home"),
    path('all_emp',views.all_emp,name="all_emp"),
    path('remv_emp',views.remv_emp,name="remv_emp"),
    path('remv_emp/<int:emp_id>',views.remv_emp,name="remv_emp"),
    path('add_emp',views.add_emp,name="add_emp"),
    path('filter_emp',views.filter_emp,name="filter_emp"),
]
