test = {'name': 'b',
 'points': 3,
 'suites': [{'cases': [{'code': '    >>> c = CreditCard(50)\n'
                                '    >>> c.purchase(5)      # 45 remaining\n'
                                '    45\n'
                                '    >>> c.purchase(30)     # now only 15 '
                                'remaining\n'
                                '    15\n'
                                '    >>> c.purchase(30)\n'
                                "    'declined'\n"
                                '    >>> c.pay_bill()       # current balance '
                                'is 35\n'
                                '    35\n'
                                '    >>> c.purchase(30)     # 20 remaining\n'
                                '    20\n'
                                '    >>> [CreditCard(10), CreditCard(20, 5)]\n'
                                '    [CreditCard(10, 0), CreditCard(20, 5)]\n'
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from purchase import *',
             'teardown': '',
             'type': 'doctest'}]}