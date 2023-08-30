from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_view
# from .views import lesson

urlpatterns = [
    path("",index, name="main-page"),
    path('top-sellers/',top_sellers,name="top-sellers"),
    # path('lesson_4/',lesson)
    path('advertisement-post/',advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>',advertisement_view,name='adv')

]