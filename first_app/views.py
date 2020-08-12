from .models import project,Categorie,About,Contact,SampleAttachment,Resume
from django.shortcuts import render,get_object_or_404, Http404
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from .forms import SmapleAttachmentForm
from django.conf import settings
from urllib.parse import quote_plus
from . import models
from django.http import HttpResponseNotFound, HttpResponse



# Create your views here.

def home(request):
    form = project.objects.all()[:6]
    cat_form = Categorie.objects.all()
    context = {
        'forms':form,
        'cat_forms':cat_form
    }
    return render(request,'index.html',context)



def project_detail(request, slug):
    form = get_object_or_404(project, slug=slug)
    share_string = quote_plus(form.description)
    if request.method == "POST":
        email_form = SmapleAttachmentForm(request.POST,request.FILES)
        if email_form.is_valid():
            email_form.save()
            email = request.POST.get('email')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = email
            title = form.name
            sample_file = form.file_upload.path
            subject= f'Sample {title}'
            message = f'Sample file of {title}'
            email = EmailMessage(subject,message,email_from,[recipient_list])
            email.attach_file(str(sample_file))
            email.send()
    else:
        email_form = SmapleAttachmentForm()
    context = {
        'form':form,
        'email_form':email_form,
        'share_string':share_string
    }
    return render(request,'single-project.html',context)


def contact(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('message')
        form = Contact(name=name,email=email,subject=subject,description=description)
       
        try:
            my_subject = 'Thank You'
            my_message = 'We will contact you very soon.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = email
            send_mail(my_subject, my_message, email_from, [recipient_list])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        form.save()   
        
    return render(request,'contact.html')

def portfolio(request):
    form = project.objects.all()
    cat_form = Categorie.objects.all()
    context = {
        'forms':form,
        'cat_forms':cat_form
    }
    return render(request,'portfolio_page.html',context)

    
def services(request):
    return render(request,'services_page.html')
    

def About(request):
    about_form = models.About.objects.all()
    context = {
        'objects':about_form
    }
    return render(request,'about_page.html',context)


def pdf_resume(request):
    pdf_file = Resume.objects.all().first()
    filename = str(pdf_file.resume.path)
    with open(filename,'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={name}'.format(name=pdf_file.resume)
        return response
    raise Http404

    context = {
        'object_list':pdf_file
    }
    return render(request,'pdf.html',context)

