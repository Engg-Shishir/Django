from django.contrib import admin

from .models import Abouts, Author, Contact, Educations, Experiances, Projects, Services, Social, Testimonials

# Register your models here.
admin.site.register(Author)
admin.site.register(Social)
admin.site.register(Projects)
admin.site.register(Testimonials)
admin.site.register(Abouts)
admin.site.register(Educations)
admin.site.register(Experiances)
admin.site.register(Services)
admin.site.register(Contact)