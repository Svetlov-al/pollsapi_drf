from django.urls import path, re_path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate

# drf-yasg imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Setup for schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Polls API",
        default_version='v1',
        description="API documentation for Polls API",
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    # Documentation urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
