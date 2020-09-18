import pytest

from ..models import Item

@pytest.mark.django_db
def test_create_items():
    """Test all ok to create items"""
    Item.objects.create(result=[1, 2, 3])
    Item.objects.create(result=[4, 5, 6])
    Item.objects.create(result=[7, 8, 9])

    assert Item.objects.count() == 3
