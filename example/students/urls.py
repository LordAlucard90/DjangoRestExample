from rest_framework import routers

from students import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
]

urlpatterns += router.urls
