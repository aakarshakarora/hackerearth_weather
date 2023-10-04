from rest_framework.routers import DefaultRouter

from .views import RecordViewSetWithOptions

# Create a router and register your viewset.
router = DefaultRouter()
router.register(r'weather', RecordViewSetWithOptions)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # ... other URL patterns specific to your app
]

# Include the router-generated URLs
urlpatterns += router.urls
