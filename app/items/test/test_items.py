
from ..utils import convert_nested_list_in_flattens_list

def test_convert_nested_list_in_flattens_list():
    """Test convert nested list in new flattens list"""
    NESTED_LIST = [1, 2, [3, 4, [5, 6], 7], 8]
    FLATTENS_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
    CONVERTED_LIST = convert_nested_list_in_flattens_list(NESTED_LIST)
    assert CONVERTED_LIST == CONVERTED_LIST
