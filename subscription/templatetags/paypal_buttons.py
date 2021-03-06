### -*- coding: utf-8 -*- ####################################################

import urllib

from django import template
from django.conf import settings

register = template.Library()

from subscription.models import UserSubscription
from subscription.views import _paypal_form

# http://paypaldeveloper.com/pdn/board/message?board.id=basicpayments&message.id=621
if settings.PAYPAL_TEST:
    cancel_url = 'https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_subscr-find&alias=%s' \
                    % urllib.quote(settings.PAYPAL_RECEIVER_EMAIL)
else:
    cancel_url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_subscr-find&alias=%s' \
                    % urllib.quote(settings.PAYPAL_RECEIVER_EMAIL)


@register.inclusion_tag("paypal/shortcut.html", takes_context=False)
def paypal_shortcut(user, subscription):
    try:
        us = user.usersubscription_set.get(
            active=True)
    except UserSubscription.DoesNotExist:
        change_denied_reasons = None
        us = None
    else:
        change_denied_reasons = us.try_change(subscription)

    if change_denied_reasons:
        form = None
    else:
        form = _paypal_form(subscription, user,
                    upgrade_subscription=(us is not None) and (us.subscription != subscription))

    current_plan_price = 0

    if us is not None:
        current_plan_price = us.subscription.price


    return {'form': form, 'change_denied_reasons': change_denied_reasons,
            'test': settings.PAYPAL_TEST,
            'subscription': subscription,
            'current_plan_price': current_plan_price,
            'current': us and (subscription == us.subscription) and us, 'cancel_url': cancel_url,
            'image_url': "https://www.paypal.com/en_US/i/btn/btn_unsubscribe_LG.gif"} 
    