from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from blog.models import Category, Post, Tag


class TagApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name="python", slug="python")

    def test_tag_list(self):
        response = self.client.get(reverse("api:tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id": self.tag.pk, "name": "python", "slug": "python"}])

    def test_create_tag(self):
        response = self.client.post(
            reverse("api:tag_list"), {"name": "vscode", "slug": "vscode"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["slug"], "vscode")
        self.assertEqual(Tag.objects.count(), 2)

    def test_invalid_tag(self):
        response = self.client.post(reverse("api:tag_list"), {"name": "missing-slug"}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_tag_detail(self):
        response = self.client.get(reverse("api:tag_detail", args=[self.tag.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "python")

    def test_tag_not_found(self):
        response = self.client.get(reverse("api:tag_detail", args=[99]))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "No Tag matches the given query.")

    def test_update_tag(self):
        response = self.client.put(
            reverse("api:tag_detail", args=[self.tag.pk]),
            {"name": "django", "slug": "django"}, format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.slug, "django")

    def test_delete_tag(self):
        response = self.client.delete(reverse("api:tag_detail", args=[self.tag.pk]))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())

    def test_stats_only_counts_published_posts(self):
        author = User.objects.create_user(username="nigar", password="test12345")
        category = Category.objects.create(name="Kod", slug="kod")
        Post.objects.create(title="Public", author=author, category=category, content="Test", is_published=True)
        Post.objects.create(title="Draft", author=author, category=category, content="Test", is_published=False)
        response = self.client.get(reverse("api:stats"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"post_count": 1, "category_count": 1, "tag_count": 1})

    def test_stats_get_only(self):
        self.assertEqual(self.client.post(reverse("api:stats"), {}, format="json").status_code, 405)

    def test_post_list_and_create(self):
        author = User.objects.create_user(username="murad", password="test12345")
        category = Category.objects.create(name="News", slug="news")
        response = self.client.post(
            reverse("api:post_list"),
            {"title": "Hello", "author": author.pk, "category": category.pk, "content": "Hello World"},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.client.get(reverse("api:post_list")).json()[0]["title"], "Hello")
