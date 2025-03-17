from django.test import TestCase
from .models import Note

class NoteTests(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test content"
        )
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(str(note), "Test Note")
