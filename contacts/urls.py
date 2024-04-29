from django.urls import path
from .views import (
    BirthdayContactsListView,
    ContactSearchResultsView,
    ContactUpdateView,
    ContactDeleteView,
    ContactCreateView,
    main,
    edit, note_list, note_create, note_update, note_delete
)

app_name = 'contacts'

urlpatterns = [
    path('', main, name='main'),
    path('edit/', edit, name='edit'),
    path('contacts/search/', ContactSearchResultsView.as_view(), name='contact-search'),
    path('contacts/update/<pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('contacts/delete/<pk>', ContactDeleteView.as_view(), name='contact-delete'),
    path('contacts/create/', ContactCreateView.as_view(), name='contact-create'),
    path('contacts/birthdays/', BirthdayContactsListView.as_view(), name='birthday-contacts'),
    path('notes/', note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/<int:pk>/update/', note_update, name='note_update'),
    path('notes/<int:pk>/delete/', note_delete, name='note_delete'),
]