from django.views.generic import *
from .models import *
# Create your views here.
class HomeView(TemplateView):
	template_name="index.html"