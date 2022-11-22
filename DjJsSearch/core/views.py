from django.shortcuts import render
import json
from django.views.generic import ListView

# Create your views here.
from .models import Posts


# from django.http import JsonResponse
# def list_view(request):
#     '''
#         these two lines returning json data
#     '''
#     data = list(Posts.objects.values())
#     return JsonResponse(data, safe=False)


class HomeListView(ListView):
    context_object_name = 'data'
    queryset = Posts.objects.all()
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["js_data"] = json.dumps(list(Posts.objects.values()))
        return context
