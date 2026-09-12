from django.urls import path
from apps.testapp.views import (
                                CustomTokenObtainPairView, GoogleAuthView,
                                PublicDataView,
                                RegisterView,
                                SecretModeratorView)


urlpatterns = [
    path('public/', PublicDataView.as_view(), name='public-data'),
    path('secret/', SecretModeratorView.as_view(), name='secret-data'),

    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('google-auth/', GoogleAuthView.as_view(), name='google-auth'),
]
