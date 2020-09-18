

def convert_nested_list_in_flattens_list(nested):
    """Convert Nested list in flattens list"""
    list_end = []
    for element in nested:
        if type(element) == list:
            list_end.extend( 
                convert_nested_list_in_flattens_list(element) 
            )
        else:
            list_end.append(element)
    return list_end
