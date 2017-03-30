from django.conf.urls import url,include
from invoice import views

urlpatterns = [
    url(r"^pdf$", views.PDFView.as_view()),
    url(r"^send$", views.send.as_view()),

]