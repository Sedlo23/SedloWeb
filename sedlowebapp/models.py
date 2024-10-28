# sedloweb/models.py
from django.db import models


class BinaryFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='binaries/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    short_desc = models.TextField(default='')
    long_desc = models.TextField(default='')
    image = models.ImageField(upload_to='program_images/', null=True, blank=True)  # New optional image field

    def __str__(self):
        return self.name

class RelatedPDF(models.Model):
    binary_file = models.ForeignKey(BinaryFile, related_name='pdfs', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f"{self.binary_file.name} PDF"

class STLModel(models.Model):
    name = models.CharField(max_length=255)
    stl_file = models.FileField(upload_to='stl_models/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Telegram(models.Model):
    name = models.CharField(max_length=255)
    zip_file = models.FileField(upload_to='telegrams/zips/')

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class TelegramPDF(models.Model):
    telegram = models.ForeignKey(Telegram, related_name='pdfs', on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='telegrams/pdfs/')

    def __str__(self):
        return f"{self.telegram.name} PDF"