from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
from .models import Contact, Note, Tag
from .forms import ContactForm, NoteForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main(request):
    return render( request, "contacts/index.html")


@login_required
def edit(request):
    return render(request, "contacts/edit.html")


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/create.html'
    success_url = reverse_lazy('main')


class ContactSearchResultsView(ListView):
    model = Contact
    template_name = 'contacts/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Contact.objects.filter(name__icontains=query)
        return Contact.objects.all()


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/update.html'
    success_url = reverse_lazy('main')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contacts/delete.html'
    success_url = reverse_lazy('main')


class BirthdayContactsListView(ListView):
    model = Contact
    template_name = 'contacts/birthday_list.html'

    def get_queryset(self):
        current_date = timezone.now().date()
        days_ahead = 7  # Задана кількість днів
        return Contact.objects.filter(
            birthday__gte=current_date,
            birthday__lte=current_date + timedelta(days=days_ahead))

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'contacts/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            # Парсинг строки тегов и добавление их в note
            tag_names = form.cleaned_data['tags'].split(',')
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name.strip())
                note.tags.add(tag)
            return redirect('contacts:note_list')
    else:
        form = NoteForm()
    return render(request, 'contacts/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = form.save(commit=False)
            updated_note.save()
            updated_note.tags.clear()

            tag_names = form.cleaned_data['tags'].split(',')
            for name in tag_names:
                
                name = name.strip()
                if name:
                    tag, created = Tag.objects.get_or_create(name=name)
                    updated_note.tags.add(tag)
    
            return redirect('contacts:note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'contacts/note_form.html', {'form': form, 'note': note})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('contacts:note_list')
    return render(request, 'contacts/note_confirm_delete.html', {'object': note})