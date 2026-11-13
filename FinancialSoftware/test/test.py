import pytest
from pytest import approx
from client import Client
from account import Account
from datetime import datetime
from transaction import Transaction
from hasUUID import hasUUID
OperationError = Transaction.OperationError


class TestAccount:
    """
    Everything is in one file because for some reason pytest wouldn't run more than one file and I couldn't figure out why, so Anamika told me to put everything in the one class.
    """

    def test_owner(self, basic_everyday_account, example_client):
        assert basic_everyday_account.owner == example_client

    # should be "John's account"
    def test_default_name(self, basic_savings_account):
        assert basic_savings_account.name.find("John's Savings Account") > -1

    def test_balance_add(self, basic_everyday_account):
        prev_balance = basic_everyday_account.get_balance()
        basic_everyday_account.increase_balance(504.3)
        assert basic_everyday_account.get_balance() == pytest.approx(
            prev_balance + 504.3)

    def test_balance_subtract(self, basic_everyday_account):
        prev_balance = basic_everyday_account.get_balance()
        basic_everyday_account.increase_balance(5000)
        basic_everyday_account.decrease_balance(100)
        assert basic_everyday_account.get_balance() == pytest.approx(4900)

    def test_balance_overdraft(self, basic_everyday_account):
        acct = basic_everyday_account
        acct.increase_balance(10)

        with pytest.raises(Account.WithdrawalError) as e:
            acct.decrease_balance(11)
        assert str(e.value).find("overdraft") > -1

    def test_max_withdrawal_limit(self, basic_everyday_account):
        with pytest.raises(Account.WithdrawalError) as e:
            acct = basic_everyday_account
            # Make sure account is higher than max withdrawal to avoid overdraft.
            acct.increase_balance(acct.get_max_withdrawal() + 1000)
            acct.decrease_balance(acct.get_max_withdrawal() + 500)

        assert str(e.value).find(str(acct.get_max_withdrawal())) > -1

    def test_min_balance(self, basic_savings_account):
        # Make sure account is higher than min balance to avoid overdraft.
        basic_savings_account.increase_balance(
            basic_savings_account.get_min_balance() + 1000)

        with pytest.raises(Account.WithdrawalError) as e:
            basic_savings_account.decrease_balance(
                basic_savings_account.get_balance() - 0.5*basic_savings_account.get_min_balance())
        assert str(e.value).find(
            str(basic_savings_account.get_min_balance())) > -1

    def test_account_str(self, basic_everyday_account):
        account = basic_everyday_account
        s = str(basic_everyday_account)
        assert account.get_name() in s
        assert str(account.get_balance()) in s

    def test_account_repr(self, basic_everyday_account):
        account = basic_everyday_account
        s = repr(basic_everyday_account)
        assert account.get_name() in s
        assert str(account.get_balance()) in s

    def test_adding_removing_balance(self, basic_savings_account):
        acct = basic_savings_account
        bal_init = acct.get_balance()
        acct.increase_balance(20000)
        assert acct.get_balance() == bal_init + 20000
        acct.decrease_balance(10000)
        assert acct.get_balance() == bal_init + 10000

    def test_account_only_has_one_owner_at_once(self, basic_savings_account, example_client, example_branch):
        new_owner = Client(["Samantha", "Hodgekins"],
                           Client.Titles.MS,
                           datetime(1836, 2, 13),
                           "0412 563 923",
                           "samantha.hodgekins@hotmail.com",
                           "The Moon",
                           [],
                           example_branch
                           )
        assert basic_savings_account.owner == example_client
        basic_savings_account.set_owner(new_owner)
        assert basic_savings_account.owner == new_owner
        assert basic_savings_account not in example_client._Client__accounts

    def test_transaction_history(self, basic_savings_account):
        basic_savings_account.increase_balance(100000)
        basic_savings_account.decrease_balance(123)
        basic_savings_account.increase_balance(456)
        s = basic_savings_account.get_history()
        assert "$10000" in s
        assert "$123" in s
        assert "$456" in s

    def test_interest_rate_setting(self, basic_savings_account):
        with pytest.raises(ValueError) as e:
            basic_savings_account.set_interest_rate(-5)
        with pytest.raises(ValueError) as e:
            basic_savings_account.set_interest_rate(105)

    # Transaction Testing:

    def test_process_pending(self, withdrawal):
        withdrawal.process()
        assert withdrawal.get_status() == Transaction.TransactionStatuses.PROCESSED

    def test_cancel_pending(self, withdrawal):
        withdrawal.cancel()
        assert withdrawal.get_status() == Transaction.TransactionStatuses.CANCELLED

    def test_process_processed(self, withdrawal):
        withdrawal.process()
        with pytest.raises(OperationError) as e:
            withdrawal.process()
        assert isinstance(e.value, Exception)

    def test_process_cancelled(self, withdrawal):
        withdrawal.cancel()
        with pytest.raises(OperationError) as e:
            withdrawal.process()

    def test_cancel_processed(self, withdrawal):
        withdrawal.process()
        with pytest.raises(OperationError) as e:
            withdrawal.cancel()

    def test_cancel_cancelled(self, withdrawal):
        withdrawal.cancel()
        with pytest.raises(OperationError) as e:
            withdrawal.cancel()

    def test_transaction_str(self, withdrawal):
        s = str(withdrawal)
        assert str(withdrawal.get_status().value) in s
        assert str(withdrawal.get_amount()) in s

    def test_transaction_repr(self, withdrawal):
        s = repr(withdrawal)
        assert str(withdrawal.get_status().value) in s
        assert str(withdrawal.get_ID()) in s

    # Client Testing:

    def test_client_name_printing(self, example_client):
        assert example_client.print_name(Client.NameFormats.CASUAL) == "John"
        assert example_client.print_name(
            Client.NameFormats.DEFAULT) == "John Citizen"
        assert example_client.print_name(
            Client.NameFormats.FORMAL) == "Mr. Citizen"
        assert example_client.print_name(
            Client.NameFormats.FULL) == "John William Citizen"

    def test_client_name_setting(self, example_client):
        cl = example_client
        with pytest.raises(TypeError) as e:
            cl.set_name("Alice")
        with pytest.raises(TypeError) as e:
            cl.set_name("Alice Smith")
        with pytest.raises(TypeError) as e:
            cl.set_name(None)
        with pytest.raises(TypeError) as e:
            cl.set_name(["Alice", 11, "Smith"])

    def test_client_str(self, example_client):
        cl = example_client
        s = str(cl)
        assert cl.print_name(Client.NameFormats.FULL) in s
        assert str(cl.get_ID()) in s

    def test_client_repr(self, example_client):
        cl = example_client
        s = repr(cl)
        assert cl.print_name(Client.NameFormats.FULL) in s
        assert str(cl.get_ID()) in s

    # Testing branch.

    def test_open_close(self, example_branch):
        example_branch.open()
        assert example_branch.is_open()
        example_branch.close()
        assert not example_branch.is_open()

    def test_branch_str(self, example_branch):
        br = example_branch
        s = str(br)
        assert br.name in s
        assert str(br.get_ID()) in s

    def test_branch_repr(self, example_branch):
        br = example_branch
        s = repr(br)
        assert br.name in s
        assert str(br.get_ID()) in s

    def test_hasUUID(self, example_branch):
        assert hasUUID.get_from_UUID(example_branch.get_ID()) == example_branch

    # Testing random getters and setters because I need over 95% coverage and this program is so basic and WET that only like 30% of it actually has any logic; even calling the rest boilerplate is generous.

    def test_set_transaction_status(self, withdrawal):
        withdrawal.set_status("chicken")
        assert withdrawal.get_status().value == "Pending"

    def test_client_init(self, example_branch):
        with pytest.raises(TypeError) as e:
            client = Client(15,
                            Client.Titles.MS,
                            datetime(1836, 2, 13),
                            "0412 563 923",
                            "samantha.hodgekins@hotmail.com",
                            "The Moon",
                            [],
                            example_branch
                            )
        with pytest.raises(TypeError) as e:
            client = Client(["Samantha", "Hodgekins"],
                            "apple",
                            datetime(1836, 2, 13),
                            "0412 563 923",
                            "samantha.hodgekins@hotmail.com",
                            "The Moon",
                            [],
                            example_branch
                            )
        with pytest.raises(TypeError) as e:
            client = Client(["Samantha", "Hodgekins"],
                            Client.Titles.MS,
                            4,
                            "0412 563 923",
                            "samantha.hodgekins@hotmail.com",
                            "The Moon",
                            [],
                            example_branch
                            )
        with pytest.raises(TypeError) as e:
            new_owner = Client(["Samantha", "Hodgekins"],
                               Client.Titles.MS,
                               datetime(1836, 2, 13),
                               4,
                               "samantha.hodgekins@hotmail.com",
                               "The Moon",
                               [],
                               example_branch
                               )
        with pytest.raises(TypeError) as e:
            new_owner = Client(["Samantha", "Hodgekins"],
                               Client.Titles.MS,
                               datetime(1836, 2, 13),
                               "0412 563 923",
                               example_branch,
                               "The Moon",
                               [],
                               example_branch
                               )
        with pytest.raises(TypeError) as e:
            new_owner = Client(["Samantha", "Hodgekins"],
                               Client.Titles.MS,
                               datetime(1836, 2, 13),
                               "0412 563 923",
                               "samantha.hodgekins@hotmail.com",
                               4,
                               [],
                               example_branch
                               )
        with pytest.raises(TypeError) as e:
            new_owner = Client(["Samantha", "Hodgekins"],
                               Client.Titles.MS,
                               datetime(1836, 2, 13),
                               "0412 563 923",
                               "samantha.hodgekins@hotmail.com",
                               "The Moon",
                               example_branch,
                               example_branch
                               )
        with pytest.raises(TypeError) as e:
            new_owner = Client(["Samantha", "Hodgekins"],
                               Client.Titles.MS,
                               datetime(1836, 2, 13),
                               "0412 563 923",
                               "samantha.hodgekins@hotmail.com",
                               "The Moon",
                               [],
                               4
                               )
