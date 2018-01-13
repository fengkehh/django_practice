from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]

# urlpatterns = [
#     #post views
#     url(r'^$', views.post_list, name='post_list'), # <- doesn't take any arguments, mapped to the post_list view
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2])/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'), # <- takes year (4 digits), month (2 digits), day (2 digits, need leading 0 if single digit date), post (composed of words and hyphens)
# ]