from tests.unit.fixtures import mock_commands_po as mock_po

def test_is_interactive_returns_False_if_only_displayed(mock_po):
    mock_po.is_displayed = lambda log=True: True
    mock_po.is_enabled = lambda log=True: False
    assert mock_po.is_interactive() == False


def test_is_interactive_returns_False_if_only_enabled(mock_po):
    mock_po.is_displayed = lambda log=True: False
    mock_po.is_enabled = lambda log=True: True
    assert mock_po.is_interactive() == False


def test_is_interactive_returns_True_if_both_displayed_and_enabled(mock_po):
    mock_po.is_displayed = lambda log=True: True
    mock_po.is_enabled = lambda log=True: True
    assert mock_po.is_interactive() == True

