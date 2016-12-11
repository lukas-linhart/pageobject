from pageobject import PageObjectList


def test_text_values_return_text_attributes_of_children(monkeypatch):

    class ChildPo:
        def __init__(self, text):
            self.text = text

    class MockPoList(PageObjectList):
        def __init__(self): pass
        _log_id_long = None

    mock_po_list = MockPoList()
    children_values = ['spam', 'eggs', 'ham']
    children = [ChildPo(x) for x in children_values]
    monkeypatch.setattr(mock_po_list.__class__, 'children', children)
    assert mock_po_list.text_values == children_values

