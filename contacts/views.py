
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Contact, Note, Tag
from .forms import ContactForm, NoteForm
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'contacts/index.html'

class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/list.html'
    context_object_name = 'list'
    paginate_by = 10

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/create.html'
    success_url = reverse_lazy('contacts:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/update.html'
    success_url = reverse_lazy('contacts:list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contacts/delete.html'
    success_url = reverse_lazy('contacts:list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ContactSearchResultsView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/search.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Contact.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(additional_data__icontains=query) |
                Q(birthday__icontains=query),
                user=self.request.user
            )
        return Contact.objects.filter(user=self.request.user)

class ContactUpcomingBirthdayListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/birthdays.html'
    context_object_name = 'birthdays'

    def get_queryset(self):
        days_ahead = self.request.GET.get('days_ahead', 30)
        today = timezone.now().date()
        end_date = today + timezone.timedelta(days=int(days_ahead))
        return Contact.objects.filter(
            Q(birthday__day__gte=today.day, birthday__month=today.month) |
            Q(birthday__day__lte=end_date.day, birthday__month=end_date.month),
            user=self.request.user
        )

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