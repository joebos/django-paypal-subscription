from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from views import subscription_detail, subscription_list, account, subscribe

urlpatterns = patterns('subscription.views',
    url(r'^subscribe/$', subscribe, name='subscribe'),

    url(r'^$', account, name='account'),


    #url(r'^(?P<object_id>\d+)/$', subscription_detail, name='subscription_detail'),
    #url(r'^(?P<object_id>\d+)/(?P<payment_method>(standard|pro))$', name='subscription_detail2'),
    )

urlpatterns += patterns('',
    #url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^done/', TemplateView.as_view(template_name='subscription/subscription_done.html'), name='subscription_done'),
    #(r'^change-done/', TemplateView.as_view('subscription_change_done.html', {"cancel_url": views.cancel_url}), 'subscription_change_done'),
    url(r'^change-done/', TemplateView.as_view(template_name='subscription/subscription_change_done.html'), name='subscription_change_done'),
    url(r'^cancel/', TemplateView.as_view(template_name='subscription/subscription_cancel.html'), name='subscription_cancel'),
)
