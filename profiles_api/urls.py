from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # base_name implied by qs


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls)),
]
