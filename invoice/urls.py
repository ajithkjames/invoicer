from django.conf.urls import url,include
from invoice import views

urlpatterns = [
    url(r"^pdf$", views.PDFView.as_view()),
    url(r"^email$", views.sendmail),
    url(r"^pdfmail$", views.pdfmail.as_view()),
    url(r"^file$", views.file.as_view()),

]