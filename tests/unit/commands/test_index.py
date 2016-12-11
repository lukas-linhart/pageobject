from pageobject import PageObjectList


def test_index_command_indexes_text_values(monkeypatch):

    class ChildPo: pass

    class MockPoList(PageObjectList):
        def __init__(self): pass
        _log_id_short = None
        _log_id_long = None

    mock_po_list = MockPoList()
    text_values = ['spam', 'eggs', 'ham']
    monkeypatch.setattr(mock_po_list.__class__, 'text_values', text_values)
    assert mock_po_list.index('ham') == 2

