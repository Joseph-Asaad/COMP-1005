import pytest


@pytest.fixture
def example_branch():
    from branch import Branch
    return Branch(1, "412 Hindley St.", "048265973", True)


@pytest.fixture
def example_client(example_branch):
    from client import Client
    from datetime import datetime

    return Client(["John", "Citizen"],
                  Client.Titles.MR,
                  datetime.date(2026, 5, 4),
                  "0412 558 903",
                  "john.citizen2000@gmail.com",
                  "10 Downing St., London, England",
                  [],
                  example_branch
                  )


@pytest.fixture
def basic_savings_account(example_client):
    from savingsAccount import SavingsAccount

    return SavingsAccount(0, example_client, 0.01, 1000)


@pytest.fixture
def basic_everyday_account(example_client):
    from everydayAccount import EverydayAccount

    return EverydayAccount(0, example_client, 1000)
