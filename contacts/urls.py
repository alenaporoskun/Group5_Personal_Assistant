from django.urls import path
from .views import (
    ContactUpcomingBirthdayListView,
    ContactSearchResultsView,
    ContactUpdateView,
    ContactDeleteView,
    ContactCreateView,
    IndexView,
    ContactListView, note_list, note_create, note_update, note_delete
)

app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('contacts/list/', ContactListView.as_view(), name='list'),
    path('contacts/create/', ContactCreateView.as_view(), name='create'),
    path('contacts/update/<int:pk>/', ContactUpdateView.as_view(), name='update'),
    path('contacts/delete/<int:pk>/', ContactDeleteView.as_view(), name='delete'),
    path('contacts/search/', ContactSearchResultsView.as_view(), name='search'),
    path('birthdays/', ContactUpcomingBirthdayListView.as_view(), name='birthdays'),
    path('notes/', note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/<int:pk>/update/', note_update, name='note_update'),
    path('notes/<int:pk>/delete/', note_delete, name='note_delete'),
]