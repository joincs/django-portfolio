from django.contrib import admin
from .models import Categorie, project, About, Contact, SampleAttachment, Resume

# Register your models here.

admin.site.register(Categorie)
admin.site.register(project)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(SampleAttachment)
admin.site.register(Resume)