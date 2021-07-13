#
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from common.utils import bulk_get, FlashMessageUtil


@method_decorator(never_cache, name='dispatch')
class FlashMessageMsgView(TemplateView):
    template_name = 'flash_message_standalone.html'

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return HttpResponse('Not found the code')

        message_data = FlashMessageUtil.get_message_by_code(code)
        if not message_data:
            return HttpResponse('Message code error')

        title, message, redirect_url, confirm_button, cancel_url = bulk_get(
            message_data, 'title', 'message', 'redirect_url', 'confirm_button', 'cancel_url'
        )

        interval = message_data.get('interval', 3)
        auto_redirect = message_data.get('auto_redirect', True)
        has_cancel = message_data.get('has_cancel', False)
        context = {
            'title': title,
            'messages': message,
            'interval': interval,
            'redirect_url': redirect_url,
            'auto_redirect': auto_redirect,
            'confirm_button': confirm_button,
            'has_cancel': has_cancel,
            'cancel_url': cancel_url,
        }
        return self.render_to_response(context)