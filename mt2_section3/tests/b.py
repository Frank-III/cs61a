test = {'name': 'b',
 'points': 5,
 'suites': [{'cases': [{'code': '    >>> b0 = Tree(2, [Tree(3, [Tree(4), '
                                'Tree(5)])])\n'
                                '    >>> b1 = Tree(6, [Tree(7), Tree(8, '
                                '[Tree(9)])])\n'
                                '    >>> t = Tree(1, [b0, b1])\n'
                                '    >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)\n'
                                "    'success!'\n"
                                '    >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)\n'
                                "    'success!'\n"
                                '    >>> pluck(t)(2)\n'
                                "    'Nope, not valid!'\n"
                                '    >>> pluck(t)(5)(9)(7)(6)\n'
                                "    'Nope, not valid!'\n"
                                '    ',
                        'hidden': False,
                        'locked': False}],
             'scored': True,
             'setup': 'from order import *',
             'teardown': '',
             'type': 'doctest'}]}