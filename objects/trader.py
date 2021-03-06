import numpy as np


class Trader:
    """Class holding low frequency trader properties"""
    def __init__(self, name, variables, parameters, expectations):
        """
        Initialize trader class
        :param name: integer number which will be the name of the trader
        :param variables: object Tradervariables
        :param parameters: object TraderParameters
        :param expectations: object TraderExpectations
        """
        self.name = name
        self.var = variables
        self.par = parameters
        self.exp = expectations

    def __repr__(self):
        """
        :return: String representation of the trader
        """
        return 'Trader' + str(self.name)

    def sell(self, amount, price):
        """
        Sells `amount` of stocks for a total of `price`
        :param amount: int Number of stocks sold.
        :param price: float Total price for stocks.
        :return: -
        """
        if self.var.stocks[-1] < amount:
            raise ValueError("not enough stocks to sell this amount")
        self.var.stocks[-1] -= amount
        self.var.money[-1] += price

    def buy(self, amount, price):
        """
        Buys `amount` of stocks for a total of `price`
        :param amount: int number of stocks bought.
        :param price: float total price for stocks.
        :return: -
        """
        if self.var.money[-1] < price:
            raise ValueError("not enough money to buy this amount of stocks")

        self.var.stocks[-1] += amount
        self.var.money[-1] -= price


class TraderExpectations:
    """
    Holds the agent expectations for several variables
    """
    def __init__(self, price):
        """
        Initializes trader expectations
        :param price: float
        """
        self.price = price
        self.returns = {'stocks': 0.0, 'money': 0.0}


class TraderVariables:
    """
    Holds the initial variables for the traders
    """
    def __init__(self, money, stocks, covariance_matrix, init_price):
        """
        Initializes variables for the trader
        :param weight_fundamentalist: float fundamentalist expectation component
        :param weight_chartist: float trend-following chartism expectation component
        :param weight_random: float random or heterogeneous expectation component
        :param weight_mean_reversion: float mean-reversion chartism expectation component
        """
        self.money = [money]
        self.stocks = [stocks]
        self.wealth = [money + stocks * init_price]
        self.covariance_matrix = covariance_matrix
        self.active_orders = []


class TraderParameters:
    """
    Holds the the trader parameters for the distribution model
    """

    def __init__(self, ref_horizon):
        """
        Initializes trader parameters
        :param ref_horizon: integer horizon over which the trader can observe the past
        :param max_spread: Maximum spread at which the trader will submit orders to the book
        :param risk_aversion: float aversion to price volatility
        """
        self.horizon = ref_horizon
        self.risk_aversion = 1.0
