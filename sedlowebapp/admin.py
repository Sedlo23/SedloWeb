from django.contrib import admin

from sedlowebapp.models import RelatedPDF, BinaryFile, STLModel
from .models import Telegram, TelegramPDF

# Register your models here.
class RelatedPDFInline(admin.TabularInline):
    model = RelatedPDF
    extra = 1

@admin.register(BinaryFile)
class BinaryFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc', 'uploaded_at')
    inlines = [RelatedPDFInline]


@admin.register(STLModel)
class STLModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')

class TelegramPDFInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = TelegramPDF
    extra = 1  # Number of empty forms to display for adding new PDFs

@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    inlines = [TelegramPDFInline]