from django.test import TestCase
from .forms import ItemForm
# Create your tests here.


class TestToDoItemForm(TestCase):
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({"name": "Create Tests"})
        self.assertTrue(form.is_valid())
