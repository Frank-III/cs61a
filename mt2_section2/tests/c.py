test = {'name': 'c',
 'points': 4,
 'suites': [{'cases': [{'code': '    >>> a = Purse(Link(CreditCard(1000), '
                                'Link(CreditCard(2000))))\n'
                                '    >>> a.total_available\n'
                                '    3000\n'
                                '    >>> a.buy(10).buy(30).buy(1000).buy(160)\n'
                                '    Purse(Link(CreditCard(1000, 200), '
                                'Link(CreditCard(2000, 1000))))\n'
                                '    >>> a.total_available\n'
                                '    1800\n'
                                '    >>> a.buy(1500)\n'
                                "    'No CreditCard can purchase an item of "
                                "that amount.'\n"
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from purchase import *',
             'teardown': '',
             'type': 'doctest'}]}