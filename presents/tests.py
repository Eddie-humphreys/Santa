from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Person, Idea


class PersonModelTests(TestCase):
    def test_person_creation(self):
        person = Person.objects.create(name="Testburg")
        now = timezone.now()
        self.assertLessEqual(person.created_at, now)


class IdeaModelTests(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name="Testburg")

    def test_idea_creation(self):
        idea = Idea.objects.create(
            title="Test idea ",
            description="Another grand idea from Edburg.",
            recipient=self.person
        )
        self.assertIn(idea, self.person.idea_set.all())


class CourseViewsTest(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name="Testburg1")
        self.person2 = Person.objects.create(name="Testburg2")
        self.idea = Idea.objects.create(
            title="Test idea ",
            description="Another grand idea from Edburg.",
            recipient=self.person1
        )

    def test_person_list_view(self):
        resp = self.client.get(reverse('presents:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.person1, resp.context['persons'])
        self.assertIn(self.person2, resp.context['persons'])
        self.assertTemplateUsed(resp, 'presents/person_list.html')
        self.assertContains(resp, self.person1.name)

    def test_idea_detail_view(self):
        resp = self.client.get(reverse('presents:idea_detail', kwargs={
            'pk': self.person1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.person1, resp.context['person'])
        self.assertTemplateUsed(resp, 'presents/idea_detail.html')
        self.assertContains(resp, self.idea.suggested_by)
