from django.urls import path, include
from api import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'harvardjchs', views.JCHSDataViewSet)

schema_view = get_swagger_view(title='Housing API')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'schema/', schema_view)
]

