from django.shortcuts import render, redirect

from exam_jun_2021.web.forms import ProfileCreateForm, AddNoteForm, EditNoteForm, NoteDeleteForm
from exam_jun_2021.web.models import Profile, Note


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()

    if profile is None:
        return add_profile(request)

    context = {
        'notes': Note.objects.all(),
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('home page')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'note_id': note_id,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        note.delete()
        return redirect('home page')

    context = {
        'form': form,
        'note_id': note_id,
    }

    return render(request, 'note-delete.html', context)


def note_details(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    context = {
        'note': note,
        'note_id': note_id,
    }

    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = get_profile()
    notes_count = Note.objects.count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('home page')
