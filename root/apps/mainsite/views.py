from django.conf import settings
from django.template.response import SimpleTemplateResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context



##
#
#  Error Handler Views
#
##

class Error404(TemplateView):
    template_name = '404.html'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.update({'status': 404})
        return super(Error404, self).render_to_response(context, **response_kwargs)
error404 = Error404.as_view()


class Error500(TemplateView):
    template_name = '500.html'
    response_class = SimpleTemplateResponse  # Doesn't call context_processors (which could be where the 500 came from in the first place)

    def get_context_data(self, **kwargs):
        # We must add STATIC_URL manually because context_processors aren't being called
        context_data = super(TemplateView, self).get_context_data(**kwargs)
        context_data['STATIC_URL'] = settings.STATIC_URL
        return context_data

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.update({'status': 500})
        return super(Error500, self).render_to_response(context, **response_kwargs)
error500 = Error500.as_view()