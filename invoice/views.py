from django.shortcuts import render
import easy_pdf
from rest_framework.views import APIView
from django.views.generic import View
from easy_pdf.views import PDFTemplateView
from rest_framework import views
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from cStringIO import StringIO

from rest_framework import status
from rest_framework.views import APIView

from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse

from reportlab.pdfgen import canvas



class PDFView(APIView):

    def post(self,request, *args, **kwargs):
        customer = request.data.get('customer', None)
    	context={
    	'from':request.data.get('company', None),
    	'to':request.data.get('customer', None),
    	'logo': request.data.get('logo', None),
    	'items': request.data.get('items', None),
    	'subtotal':request.data.get('subtotal', None),
    	'taxtitle':request.data.get('taxtitle'),
    	'tax':request.data.get('tax'),
    	'taxamount':request.data.get('taxamount'),
    	'grandtotal':request.data.get('grandtotal'),
    	'notes':request.data.get('notes'),
    	'terms':request.data.get('terms'),
    	}
    	return easy_pdf.rendering.render_to_pdf_response(request, template="pdf.html", context=context, encoding=u'utf-8')