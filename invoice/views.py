from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import loader, Context, RequestContext
from rest_framework.views import APIView
import easy_pdf
from easy_pdf.views import PDFTemplateView


class PDFView(APIView):

    def post(self,request, *args, **kwargs):
        customer = request.data.get('customer', None)
        products= request.data.get('items', None)
        count= len(products)
        num= 11-count
        print num
    	context={
    	'loop_times' : range(1, num),
    	'number':request.data.get('number', None),
    	'from_text':request.data.get('from_text', None),
    	'to_text':request.data.get('to_text', None),
    	'from':request.data.get('company'),
    	'to':request.data.get('customer'),
    	'logo': request.data.get('logo', None),
    	'items': request.data.get('items', None),
    	'subtotal':request.data.get('subtotal', None),
    	'taxtitle':request.data.get('taxtitle'),
    	'tax':request.data.get('tax'),
    	'taxamount':request.data.get('taxamount'),
    	'taxtitle1':request.data.get('taxtitle1'),
    	'tax1':request.data.get('tax1'),
    	'taxamount1':request.data.get('taxamount1'),
    	'grandtotal':request.data.get('grandtotal'),
    	'notes':request.data.get('notes'),
    	'terms':request.data.get('terms'),
    	'currency':request.data.get('currency'),
    	'additionaltax':request.data.get('additionaltax'),
    	}
    	return easy_pdf.rendering.render_to_pdf_response(request, template="pdf.html", context=context, encoding=u'utf-8')


class send(APIView):

    def post(self,request, *args, **kwargs):
		to=request.data.get('to', None)
		sender =request.data.get('from', None)
		message =request.data.get('message', None)
		context={
    	'number':request.data.get('number', None),
    	'from_text':request.data.get('from_text', None),
    	'to_text':request.data.get('to_text', None),
    	'from':request.data.get('company'),
    	'to':request.data.get('customer'),
    	'logo': request.data.get('logo', None),
    	'items': request.data.get('items', None),
    	'subtotal':request.data.get('subtotal', None),
    	'taxtitle':request.data.get('taxtitle'),
    	'tax':request.data.get('tax'),
    	'taxamount':request.data.get('taxamount'),
    	'taxtitle1':request.data.get('taxtitle1'),
    	'tax1':request.data.get('tax1'),
    	'taxamount1':request.data.get('taxamount1'),
    	'grandtotal':request.data.get('grandtotal'),
    	'notes':request.data.get('notes'),
    	'terms':request.data.get('terms'),
    	'currency':request.data.get('currency'),
    	'additionaltax':request.data.get('additionaltax'),
    	}
		filestr1 = loader.render_to_string("pdf.html", context)
		filestr = easy_pdf.rendering.html_to_pdf(content=filestr1, encoding=u'utf-8')

		try:
			email = EmailMessage(
			'Invoice from '+sender,
			message,
			"Invoice Generator",
			[to],
			headers={'Message-ID': 'foo'},
			)
			email.attach('invoice.pdf', filestr, 'application/pdf')
			email.send()
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return HttpResponse('success')
