from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # כל מה שקשור למשתמשים
    path('costs/', include('costs.urls')),  # כל מה שקשור לעלויות
]
