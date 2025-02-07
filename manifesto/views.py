from django.shortcuts import render, get_object_or_404
from .models import ManifestoSection

def home(request):
    sections = ManifestoSection.objects.all()
    return render(request, 'manifesto/home.html', {'sections': sections})

def section_detail(request, pk):
    section = get_object_or_404(ManifestoSection, pk=pk)
    return render(request, 'manifesto/section_detail.html', {'section': section})
