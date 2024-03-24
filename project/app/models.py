import os
from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.exceptions import ValidationError

def validate_file_size(value):
    # Limit file size to 10 MB
    max_size = 10 * 1024 * 1024  # 10 MB in bytes
    if value.size > max_size:
        raise ValidationError("File size cannot exceed 10 MB.")
    
def user_image_path(instance, filename):
    # Use the username as the filename
    _, ext = os.path.splitext(filename)
    return f'Author/{instance.username}{ext}'

def bg_image_path(instance, filename):
    # Use the username as the filename
    _, ext = os.path.splitext(filename)
    return f'AuthorBg/{instance.username}{ext}'

def services_icon(instance, filename):
    # Use the username as the filename
    _, ext = os.path.splitext(filename)
    return f'ServicesIcon/{instance.name}{ext}'

def projects(instance, filename):
    # Use the username as the filename
    _, ext = os.path.splitext(filename)
    return f'Projects/{instance.name}{ext}'

def Tetimonials(instance, filename):
    # Use the username as the filename
    _, ext = os.path.splitext(filename)
    return f'Tetimonials/{instance.name}{ext}'

class Author(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.FileField(
        upload_to=user_image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg']),
            validate_file_size
        ]
    )

    bg_image = models.FileField(
        upload_to=bg_image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'svg']),
            validate_file_size
        ]
    )
    designation = models.TextField(max_length=500)

    def __str__(self):
        return self.username


class Social(models.Model):
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twiter = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='socials')
    def __int__(self):
        return self.id
    
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.FileField(
        upload_to=projects,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg','svg']),
            validate_file_size
        ]
    )
    link = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='projects')
    def __str__(self):
        return self.name


class Testimonials(models.Model):
    name   = models.CharField(max_length=100)
    image = models.FileField(
        upload_to=Tetimonials,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg','svg']),
            validate_file_size
        ]
    )
    title  = models.CharField(max_length=100)
    recomendation   = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='testimonials')
    def __str__(self):
        return self.name

class Abouts(models.Model):
    text   = models.TextField(max_length=700)
    position   = models.CharField(max_length=100)
    birth  = models.CharField(max_length=100)
    phone  = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='abouts')

class Educations(models.Model):
    degree = models.CharField(max_length=100)
    institution  = models.CharField(max_length=100)
    duaration  = models.CharField(max_length=50)
    website  = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='education')

class Experiances(models.Model):
    role = models.CharField(max_length=100, null=True)
    company  = models.CharField(max_length=100, null=True)
    duaration  = models.CharField(max_length=50, null=True)
    website  = models.CharField(max_length=100, null=True)
    work   = models.TextField(max_length=400, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='experiance')

class Services(models.Model):
    icon = models.FileField(
        upload_to=services_icon,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg','svg']),
            validate_file_size
        ]
    )
    name  = models.CharField(max_length=100, null=True)
    description  = models.TextField(max_length=300, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='services')
    def __str__(self):
        return self.name


class Contact(models.Model):
    text = models.TextField(max_length=700, null=True)
    location = models.CharField(max_length=100, null=True)
    email  = models.CharField(max_length=50, null=True)
    phone  = models.CharField(max_length=50, null=True)
    map  = models.TextField(max_length=700, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='contacts')

class Message(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200, null=True)
    msg = models.TextField(max_length=500, null=True)