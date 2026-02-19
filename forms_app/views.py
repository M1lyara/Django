from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm
from .models import Feedback
import csv
from openpyxl import Workbook
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 

@login_required
def export_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Заявки"
    headers = ['Имя', 'Фамилия', 'Телефон']
    ws.append(headers)

    for item in Feedback.objects.all():
        ws.append([item.first_name, item.last_name, item.phone])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename="Forma.xlsx"'
    wb.save(response)
    return response

def feedback_view(request):
    success = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = FeedbackForm()
    else:
        form = FeedbackForm()
    return render(request, 'forms_app/index.html', {'form': form, 'success': success})

@login_required
def dashboard_view(request):
    items = Feedback.objects.all().order_by('-created_at')
    sort_param = request.GET.get('sort')
    if sort_param:
        items = items.order_by(sort_param)
    
    search_query = request.GET.get('search')
    if search_query:
        items = items.filter(last_name__icontains=search_query)

    return render(request, 'forms_app/dashboard.html', {'items': items})

@login_required
def edit_feedback(request, pk):
    person = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
    else:
        form = FeedbackForm(instance=person)
    return render(request, 'forms_app/edit_person.html', {'form': form, 'person': person})


@login_required
def delete_feedback(request, pk):
    person = get_object_or_404(Feedback, pk=pk)
    person.delete()
    return redirect('dashboard')