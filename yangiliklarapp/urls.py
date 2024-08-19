from django.urls import path, include

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view()),
    path('create/', NewsCreateAPIView.as_view()),
    path('update/<int:pk>/', NewsUpdateAPIView.as_view()),
    path('delete/<int:pk>/', NewsDeleteAPIView.as_view()),

    # path('category/create&list/', CategoryListCreateAPIView.as_view()),
    # path('category/update&delete/<int:pk>', CategoryUpdateDeleteAPIView.as_view()),

    path('category/', CategoryAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteAPIView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    # ViewSet URLs
    # path('news/', NewsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('news/<int:pk>/', NewsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                # 'patch': 'partial_update', 'delete': 'destroy'})),
    # path('', include(news_router.urls)),

    # path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
    #                                                     'patch': 'partial_update', 'delete': 'destroy'})),
    # path('', include(category_router.urls)),

]
