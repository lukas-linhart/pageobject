from tests.unit.fixtures import mock_commands_po as mock_po


def test_click_method_delegates_to_webelement_and_returns_self(mock_po):
    mock_po.webelement.click = lambda: None
    assert mock_po.click() == mock_po

