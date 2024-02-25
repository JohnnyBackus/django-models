from django.views.generic import TemplateView

class Base(TemplateView):
    template_name = 'base.html'
    
class SnackListView(TemplateView):
    template_name = 'snack_list.html'

class SnackDetail(TemplateView):
    template_name = 'snack_detail.html'
