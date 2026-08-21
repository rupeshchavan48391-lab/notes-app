from django.shortcuts import render, redirect
from .models import Note


def note_list(request):
    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'notes/note_list.html', {
        'notes': notes
    })


def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(
            title=title,
            content=content
        )

        return redirect('note_list')

    return render(request, 'notes/note_create.html')


def note_edit(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()

        return redirect('note_list')

    return render(request, 'notes/note_edit.html', {
        'note': note
    })


def note_delete(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'notes/note_delete.html', {
        'note': note
    })
