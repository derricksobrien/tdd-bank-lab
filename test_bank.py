import pytest
from bank import transfer_funds


def make_accounts():
    from_account = {"id": 1, "balance": 100.0, "owner": "Alice"}
    to_account = {"id": 2, "balance": 50.0, "owner": "Bob"}
    return from_account, to_account


def test_transfer_amount_must_be_greater_than_zero():
    from_account, to_account = make_accounts()
    with pytest.raises(ValueError):
        transfer_funds(from_account, to_account, 0)


def test_transfer_negative_amount_raises():
    from_account, to_account = make_accounts()
    with pytest.raises(ValueError):
        transfer_funds(from_account, to_account, -10)


def test_transfer_insufficient_funds_raises():
    from_account, to_account = make_accounts()
    with pytest.raises(ValueError):
        transfer_funds(from_account, to_account, 1000)


def test_transfer_same_account_raises():
    from_account, _ = make_accounts()
    with pytest.raises(ValueError):
        transfer_funds(from_account, from_account, 10)


def test_transfer_decreases_source_balance():
    from_account, to_account = make_accounts()
    transfer_funds(from_account, to_account, 30)
    assert from_account["balance"] == 70.0


def test_transfer_increases_destination_balance():
    from_account, to_account = make_accounts()
    transfer_funds(from_account, to_account, 30)
    assert to_account["balance"] == 80.0


def test_transfer_returns_transaction_record():
    from_account, to_account = make_accounts()
    result = transfer_funds(from_account, to_account, 30)
    assert result["from_id"] == 1
    assert result["to_id"] == 2
    assert result["amount"] == 30
    assert result["from_balance_after"] == 70.0
    assert result["to_balance_after"] == 80.0
