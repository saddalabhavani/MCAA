from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import FacultyModel  
from .forms import FacultyForm
#display form & save data  typed in form 
def insert_faculty(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = FacultyForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_faculty.html", context)  
#view faculty data
def view_faculty(request):
    ob=FacultyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_faculty.html')
    return HttpResponse(temp.render(context,request))
def delete_faculty(request,pk):
   FacultyModel.objects.get(id=pk).delete()
   return render(request, "delete_faculty.html")
   
from django.shortcuts import get_object_or_404, redirect
def update_faculty(request,pk):
    obe = get_object_or_404(FacultyModel, id=pk)
    if request.method == 'POST':
        obf = FacultyForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_faculty')#, id=pk
    else:
        formdata=FacultyForm(instance=obe)
    return render(request, "update_faculty.html", {'form':formdata})


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


