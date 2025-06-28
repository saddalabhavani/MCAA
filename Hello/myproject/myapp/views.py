from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import StudentModel  
from .forms import StudentForm
#display form & save data  typed in form 
def insert_student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  
#view student data
def view_student(request):
    ob=StudentModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_student.html')
    return HttpResponse(temp.render(context,request))
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    return result if not pisa_status.err else HttpResponse('PDF generation failed')

def pdf_view(request):
    data = {
        'name': 'Praveen Choudhary',
        'course': 'Django Development',
        'date': '2025-06-27'
    }
    return render_to_pdf('pdf_template.html', data)



