test = {'name': 'a',
 'points': 3,
 'suites': [{'cases': [{'code': '    >>> is_power(5, 625)  # pow(5, 4) = 5 * 5 '
                                '* 5 * 5 = 625\n'
                                '    True\n'
                                '    >>> is_power(5, 1)    # pow(5, 0) = 1\n'
                                '    True\n'
                                '    >>> is_power(5, 5)    # pow(5, 1) = 5\n'
                                '    True\n'
                                '    >>> is_power(5, 15)   # 15 is not a power '
                                "of 5 (it's a multiple)\n"
                                '    False\n'
                                '    >>> is_power(3, 9)\n'
                                '    True\n'
                                '    >>> is_power(3, 8)\n'
                                '    False\n'
                                '    >>> is_power(3, 10)\n'
                                '    False\n'
                                '    >>> is_power(1, 8)\n'
                                '    False\n'
                                '    >>> is_power(2, 0)    # 0 is not a power '
                                'of any positive base.\n'
                                '    False\n'
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from power import *',
             'teardown': '',
             'type': 'doctest'}]}