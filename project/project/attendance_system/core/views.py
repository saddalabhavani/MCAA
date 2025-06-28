from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, Attendance
from .forms import StudentForm
from django.db.models import Q

@login_required
def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.filter(Q(name__icontains=query) | Q(roll_no__icontains=query)) if query else Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        date = request.POST['date']
        for student in Student.objects.all():
            status = request.POST.get(f'status_{student.id}')
            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={'status': status}
            )
        return redirect('student_list')
    students = Student.objects.all()
    return render(request, 'mark_attendance.html', {'students': students})

@login_required
def attendance_report(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance_report.html', {'records': records})
