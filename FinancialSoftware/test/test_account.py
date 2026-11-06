import pytest
from pytest import approx
from client import Client


class TestAccount:

    def test_owner(self, example_account, example_client):
        assert example_account.owner == example_client.print_name(
            Client.NameFormats.DEFAULT)

    def test_balance_add_subtract(self, basic_everyday_account):
        prev_balance = basic_everyday_account.get_balance()
        basic_everyday_account.increase_balance("504.3")

    def test_balance_overdraft(self):
        pass

    def test_max_withdrawal_limit(basic_everyday_account):
        pass
