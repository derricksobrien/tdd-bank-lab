def transfer_funds(from_account, to_account, amount):
    """
    Transfer amount from from_account to to_account.

    Each account is a dict: {"id": int, "balance": float, "owner": str}

    Returns a transaction dict on success.
    Raises ValueError for invalid inputs.
    """
    required_keys = {"id", "balance", "owner"}

    if not isinstance(from_account, dict) or not isinstance(to_account, dict):
        raise ValueError("Accounts must be dictionaries.")
    if not required_keys.issubset(from_account) or not required_keys.issubset(to_account):
        raise ValueError("Accounts must include id, balance, and owner.")
    if from_account is to_account or from_account["id"] == to_account["id"]:
        raise ValueError("Cannot transfer to the same account.")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
        raise ValueError("Transfer amount must be greater than zero.")
    if from_account["balance"] < amount:
        raise ValueError("Insufficient funds.")

    from_account["balance"] -= amount
    to_account["balance"] += amount

    return {
        "from_id": from_account["id"],
        "to_id": to_account["id"],
        "amount": amount,
        "from_balance_after": from_account["balance"],
        "to_balance_after": to_account["balance"],
    }
