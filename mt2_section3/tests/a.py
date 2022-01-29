test = {'name': 'a',
 'points': 3,
 'suites': [{'cases': [{'code': '    >>> order(Tree(1, [Tree(2, [Tree(3, '
                                '[Tree(4)])])]))               # The only '
                                'valid plucking order.\n'
                                '    [4, 3, 2, 1]\n'
                                '    >>> order(Tree(1, [Tree(2), Tree(3)])) in '
                                '[[2, 3, 1], [3, 2, 1]]  # There are 2 valid '
                                'orders.\n'
                                '    True\n'
                                '    >>> o = order(Tree(1, [Tree(2, '
                                '[Tree(3)]), Tree(4, [Tree(5)])]))  # There '
                                'are many valid orders,\n'
                                '    >>> o.index(5) < '
                                'o.index(4)                                       '
                                '# but all have 5 before 4,\n'
                                '    True\n'
                                '    >>> o.index(3) < '
                                'o.index(2)                                       '
                                '# and 3 before 2,\n'
                                '    True\n'
                                '    >>> '
                                'o[4:]                                                         '
                                '# and 1 at the end.\n'
                                '    [1]\n'
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from order import *',
             'teardown': '',
             'type': 'doctest'}]}