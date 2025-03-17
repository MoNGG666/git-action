from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        note = Note.objects.create(title="Test", content="Test content")
        self.assertEqual(note.title, "Test")
        self.assertEqual(str(note), "Test")