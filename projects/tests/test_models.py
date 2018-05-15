from django.test import TestCase

from projects.models import Project
from core.models import Owner, User


class ProjectModelTests(TestCase):
    def setUp(self):
        user = User.objects.create(email="foo@bar.com")
        owner = Owner.objects.create(user_id=user.id)
        active_project = Project(name="foo", owner_id=owner.id)
        inactive_project = Project(name="bar", is_active=False, owner_id=owner.id)
        active_project.save()
        inactive_project.save()
        self.active_project = active_project
        self.inactive_project = inactive_project

    def test_is_active_defaults_to_true(self):
        self.assertTrue(self.active_project.is_active)

    def test_can_be_marked_inactive_when_created(self):
        self.assertFalse(self.inactive_project.is_active)

    def test_project_can_be_deactivated(self):
        self.active_project.deactivate()
        self.assertFalse(self.active_project.is_active)

    def test_can_see_when_project_was_deactivated(self):
        self.active_project.deactivate()
        self.assertIsNotNone(self.active_project.deactivated_at)

    def test_project_can_be_activated(self):
        self.inactive_project.activate()
        self.assertTrue(self.inactive_project.is_active)

    def test_can_see_when_project_was_activated(self):
        self.inactive_project.activate()
        self.assertIsNotNone(self.inactive_project.activated_at)

    def test_can_tell_if_project_has_been_abandoned(self):
        self.assertTrue(self.active_project.is_abandoned())

    def test_string_representation_includes_name(self):
        self.assertEqual(self.active_project.name, str(self.active_project))
