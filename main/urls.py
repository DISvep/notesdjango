from django.urls import path, include
from .views import NoteDetailView, NoteListView, add_note


urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('add/', add_note, name='add-note'),
]
