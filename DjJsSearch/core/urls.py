from django.urls import path
# from .views import list_view
from .views import HomeListView

app_name = 'core'

urlpatterns = [
    # path('', list_view, name='home'),
    path("", HomeListView.as_view(), name="home")
]
