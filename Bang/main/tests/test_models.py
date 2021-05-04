from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from main.models import School, Party, Bar, About


class TestModels(TestCase):
    def setUp(self) -> None:
        self.school = School.objects.create(text="test_text")
        self.bar = Bar.objects.create(text="test_text")
        self.about = About.objects.create(text="test_text")
        picture = SimpleUploadedFile(
            "party_picture.jpg", content=b"", content_type="image/jpg"
        )
        self.party = Party.objects.create(text="test_text", picture=picture)

    def test_add_information_to_DB(self):
        self.assertEquals(School.objects.get(text="test_text"), self.school)
        self.assertEquals(Bar.objects.get(text="test_text"), self.bar)
        self.assertEquals(About.objects.get(text="test_text"), self.about)
        self.assertEquals(Party.objects.all().last(), self.party)

    def test_models_str(self):
        self.assertEqual(str(self.school), "test_text")
        self.assertEqual(str(self.bar), "test_text")
        self.assertEqual(str(self.about), "test_text")
        self.assertEqual(str(self.party), "test_text")
