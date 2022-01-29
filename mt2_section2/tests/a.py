test = {'name': 'a',
 'points': 2,
 'suites': [{'cases': [{'code': '    >>> s = Link(3, Link(5, Link(7)))\n'
                                '    >>> sum_link(s, lambda x: x)       # 3 + '
                                '5 + 7\n'
                                '    15\n'
                                '    >>> double = lambda x: 2 * x\n'
                                '    >>> sum_link(s, double)            # '
                                'double(3) + double(5) + double(7)\n'
                                '    30\n'
                                '    >>> sum_link(Link.empty, double)\n'
                                '    0\n'
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from purchase import *',
             'teardown': '',
             'type': 'doctest'}]}