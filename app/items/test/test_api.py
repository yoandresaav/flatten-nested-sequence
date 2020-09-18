import pytest
from rest_framework.test import APIClient
from ..models import Item

@pytest.mark.django_db
def test_home_urls():
    """Test the / get endpoint"""
    INPUT = {"items": [1, 2, [3, 4, [5, 6], 7], 8]}
    OUTPUT = {"result": [1, 2, 3, 4, 5, 6, 7, 8]}
    client = APIClient()
    response = client.post('/', data=INPUT, format='json')
    
    assert response.status_code == 200
    assert response.data == OUTPUT

@pytest.mark.django_db
def test_list():
    """Test the list/ get endpoint"""
    LIST_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    LIST_2 = [8, 7, 6, 5, 4, 3, 2, 1]
    Item.objects.create(result=LIST_1)
    Item.objects.create(result=LIST_2)
    
    OUTPUT = [{'result': LIST_1}, {'result': LIST_2}]
    client = APIClient()
    response = client.get('/list/')
    
    assert response.status_code == 200
    assert response.data == OUTPUT
