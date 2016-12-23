from tests.unit.fixtures import mock_commands_po as mock_po


def test_is_visible_method_uses_is_displayed_method(mock_po):
    mock_po.webelement.is_displayed = lambda log=True: True
    assert mock_po.is_visible() == mock_po.is_displayed()
    mock_po.webelement.is_displayed = lambda log=True: False
    assert mock_po.is_visible() == mock_po.is_displayed()

