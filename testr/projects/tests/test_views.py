from testr.core.test_helpers import AuthenticatedTestCase

from testr.core.models import Owner
from testr.projects.models import Project

class IndexTestCase(AuthenticatedTestCase):
    def test_render_projects_index(self):
        response = self.client.get('/projects/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, "projects/index.html")

    def test_projects_load_if_they_exist_for_user(self):
        owner = Owner.objects.create(user=self.user)
        Project.objects.create(name="Foo", owner_id=owner.id)
        response = self.client.get('/projects/')
        self.assertEquals(1, len(response.context["projects"]))
        project = response.context["projects"][0]
        self.assertEquals("Foo", project.name)


class NewTestCase(AuthenticatedTestCase):
    pass


class ShowTestCase(AuthenticatedTestCase):
    pass

