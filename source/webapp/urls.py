from django.urls import path, include
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('advert/', include([
        path('<int:pk>/', include([
            path('', AdvertView.as_view(), name='advert_view'),
            path('update/', AdvertUpdateView.as_view(), name='advert_update'),
            path('delete/', AdvertDeleteView.as_view(), name='advert_delete'),
            # path('comments/add/', ArticleCommentCreateView.as_view(),
            #      name='article_comment_add'),
        ])),

        path('add/', AdvertCreateView.as_view(), name='advert_create'),
        path('mass-action/', AdvertMassActionView.as_view(), name='advert_mass_action'),
    ])),

    # path('comment/', include([
    #     path('<int:pk>/', include([
    #         path('update/', CommentUpdateView.as_view(), name='comment_update'),
    #         path('delete/', CommentDeleteView.as_view(), name='comment_delete'),
    #     ]))
    # ]))
]


