from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import View, ContextMixin


class CustoomDispatchMinix(View):

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CustoomDispatchMinix, self).dispatch(request, *args, **kwargs)

class BaseClassContexMixin(ContextMixin):
    title = ''

    def get_context_data(self, **kwargs):
        context = super(BaseClassContexMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

class UserDispatchMixin(View):

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDispatchMixin, self).dispatch(request, *args, **kwargs)
