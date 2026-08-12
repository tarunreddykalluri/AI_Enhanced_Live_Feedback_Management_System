# from django.contrib import admin
# from django.urls import path
# from django.conf import settings             # <--- Import settings
# from django.conf.urls.static import static   # <--- Import static helper
# from myapp.views import feedbackview

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('feed/', feedbackview),
# ]

# # This tells Django: "Please verify and serve the static files (CSS) correctly"
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urls.py
from django.contrib import admin
from django.urls import path
# Import the functions directly from your app's views
from myapp.views import feedbackview, analyze_ai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', feedbackview, name='feedbackview'),
    path('analyze/<int:feedback_id>/', analyze_ai, name='analyze_ai'),
]