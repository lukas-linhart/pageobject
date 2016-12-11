from tests.unit.fixtures import mock_commands_po as mock_po


def test_is_visible_method_delegates_to_webelement_and_returns_bool(mock_po):
    mock_po.webelement.is_displayed = lambda log=True: True
    assert isinstance(mock_po.is_visible(), bool)

