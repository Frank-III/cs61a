student_email = "frank0705"

##############
# QUESTION 2 #
##############

"""A: (2 pts) Implement sum_link, which takes a Link instance s and a
one-argument function transform that takes an element of s and returns a number.
The sum_link function returns the sum of the results of calling transform on
each element of the linked list s.

Check the doctests with: python3 ok -q a
"""
def sum_link(s, transform):
    """Sum the result of calling transform on each element of Link s.

    >>> s = Link(3, Link(5, Link(7)))
    >>> sum_link(s, lambda x: x)       # 3 + 5 + 7
    15
    >>> double = lambda x: 2 * x
    >>> sum_link(s, double)            # double(3) + double(5) + double(7)
    30
    >>> sum_link(Link.empty, double)
    0
    """
    if _____:
        return 0
    else:
        return _____

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    # if _____:
    #     return 0
    # else:
    #     return _____


"""B: (3 pts) Implement CreditCard, a class whose methods are described below.

Check the doctests with: python3 ok -q b
"""
class CreditCard:
    """A CreditCard.

    >>> c = CreditCard(50)
    >>> c.purchase(5)      # 45 remaining
    45
    >>> c.purchase(30)     # now only 15 remaining
    15
    >>> c.purchase(30)
    'declined'
    >>> c.pay_bill()       # current balance is 35
    35
    >>> c.purchase(30)     # 20 remaining
    20
    >>> [CreditCard(10), CreditCard(20, 5)]
    [CreditCard(10, 0), CreditCard(20, 5)]
    """

    def __init__(self, maximum, balance=0):
        """A CreditCard is constructed from a maximum and an optional balance,
        which defaults to 0. The maximum represents the greatest value that
        balance is allowed to take after a purchase.
        """
        assert balance <= maximum
        self.maximum = maximum
        self.balance = balance

    def purchase(self, amount):
        """When the CreditCard is used to make a purchase, the purchase amount
        is added to the balance unless the purchase is declined. A purchase is
        declined if the result of adding the amount to the current balance would
        exceed the maximum. If the purchase is not declined, return the highest
        amount of the next purchase that would not be declined.
        """
        assert amount > 0
        if _____:
            return 'declined'
        _____
        return _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # if _____:
        #     return 'declined'
        # _____
        # return _____

    def pay_bill(self):
        """Reduce the balance to 0 and return the value of the balance before
        it was reset to 0.
        """
        _____
        _____
        return _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # _____
        # _____
        # return _____

    def __repr__(self):
        return 'CreditCard(' + repr(self.maximum) + ', ' + repr(self.balance) + ')'


"""C: (4 pts) Implement Purse, a class whose methods are described below.

Check the doctests with: python3 ok -q c
"""
class Purse:
    """A Purse with a linked list of CreditCards.

    >>> a = Purse(Link(CreditCard(1000), Link(CreditCard(2000))))
    >>> a.total_available
    3000
    >>> a.buy(10).buy(30).buy(1000).buy(160)
    Purse(Link(CreditCard(1000, 200), Link(CreditCard(2000, 1000))))
    >>> a.total_available
    1800
    >>> a.buy(1500)
    'No CreditCard can purchase an item of that amount.'
    """
    def __init__(self, s):
        """A Purse is constructed from a linked list of CreditCard instances s.
        """
        assert s is Link.empty or isinstance(s, Link)
        self.cards = _____

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # self.cards = _____

    @property
    def total_available(self):
        """The sum of the difference between the maximum and balance for all
        CreditCards held by the Purse.
        """
        return sum_link(_____, _____)

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # return sum_link(_____, _____)

    def buy(self, amount):
        """Attempt to purchase at amount using each CreditCard in order, continuing
        as long as the purchase is declined. Return the Purse if buy resulted
        in a successful purchase for one of the CreditCards, or otherwise return
        a string describing that no CreditCard can purchase at that amount.

        IMPORTANT: The amount cannot be split between multiple CreditCards.
        """
        _____
        while _____:
            if _____ != 'declined':
                _____
            _____
        return 'No CreditCard can purchase an item of that amount.'

        # ORIGINAL TEMPLATE for your reference (do not edit this part)
        # _____
        # while _____:
        #     if _____ != 'declined':
        #         _____
        #     _____
        # return 'No CreditCard can purchase an item of that amount.'

    def __repr__(self):
        return 'Purse(' + repr(self.cards) + ')'

##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'