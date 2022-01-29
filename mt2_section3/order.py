student_email = "frank0705"

##############
# QUESTION 3 #
##############

"""This question involves plucking the leaves off a tree one by one.

Definitions:

1) A "number tree" is a Tree whose labels are _unique_ positive integers.
   No repeated labels appear in a number tree.

2) A "plucking order" for a number tree t is a sequence of unique positive
   integers that are all labels of t.

3) A plucking order is "valid" if both of these conditions are true:
   (a) the plucking order contains all labels of t, and
   (b) in the plucking order, the label for each node of t appears after
       the labels of all its descendant nodes. Thus, leaves appear first.

Note: elm, olive, and fir are all kinds of trees.
"""

"""A: (3 pts) Implement order, which takes a number tree called elm. It returns
a valid plucking order as a list of numbers. If there is more than one valid
plucking order for elm, your order function can return any one of them.

IMPORTANT: You do not need to return EVERY valid plucking order; just one.

Check the doctests with: python3 ok -q a
"""
def order(elm):
    """Return a list containing a valid plucking order for the labels of t.

    >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
    [4, 3, 2, 1]
    >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
    True
    >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
    >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
    True
    >>> o.index(3) < o.index(2)                                       # and 3 before 2,
    True
    >>> o[4:]                                                         # and 1 at the end.
    [1]
    """
    plucking_order = []
    for b in _____:
        _____
    return _____

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    # for b in _____:
    #     _____
    # return _____


"""B: (5 pts) Implement pluck, which takes a number tree called olive and returns
a function that is called repeatedly on the elements of a plucking order. If that
plucking order is valid, the final call returns 'success!'. Otherwise, if one of
the repeated calls is on a number that is not part of a valid plucking order, the
error string 'Nope, not valid!' is returned.

Since olive is a number tree and the values passed to plucker form a plucking
order, you can assume that:
- The labels of olive are unique,
- All values k passed to the plucker function are unique for a given olive, and
- All values k are labels of olive.

Check the doctests with: python3 ok -q b
"""
def pluck(olive):
    """Return a function that returns whether a plucking order is valid
    for a number tree t when called repeatedly on elements of a plucking order.

    Calling the function returned by pluck should not mutate olive.

           +---+
           | 1 |
           +---+
           /   \----\
          /          \
       +---+         +---+
       | 2 |         | 6 |
       +---+         +---+
         |            / \
         |           /   \
       +---+      +---+ +---+
       | 3 |      | 7 | | 8 |
       +---+      +---+ +---+
        / \               |
       /   \              |
    +---+ +---+         +---+
    | 4 | | 5 |         | 9 |
    +---+ +---+         +---+

    >>> b0 = Tree(2, [Tree(3, [Tree(4), Tree(5)])])
    >>> b1 = Tree(6, [Tree(7), Tree(8, [Tree(9)])])
    >>> t = Tree(1, [b0, b1])
    >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)
    'success!'
    >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)
    'success!'
    >>> pluck(t)(2)
    'Nope, not valid!'
    >>> pluck(t)(5)(9)(7)(6)
    'Nope, not valid!'
    """
    def plucker(k):
        def pluck_one_leaf(fir):
            """Return a copy of fir without leaf k and check that k is a
            leaf label, not an interior node label.
            """
            if _____:
                _____
            plucked_branches = []
            for b in fir.branches:
                skip_this_leaf = _____ and _____
                if not skip_this_leaf:
                    plucked_branch_or_error = pluck_one_leaf(b)
                    if isinstance(plucked_branch_or_error, str):
                        return plucked_branch_or_error
                    else:
                        _____
            return Tree(_____, plucked_branches)
        nonlocal olive
        if olive.is_leaf():
            assert k == olive.label, 'all k must appear in olive'
            return 'success!'
        _____
        if isinstance(olive, str):
            return olive
        return plucker
    return plucker

    # ORIGINAL TEMPLATE for your reference (do not edit this part)
    #         if _____:
    #             _____
    #         plucked_branches = []
    #         for b in fir.branches:
    #             skip_this_leaf = _____ and _____
    #             if not skip_this_leaf:
    #                 plucked_branch_or_error = pluck_one_leaf(b)
    #                 if isinstance(plucked_branch_or_error, str):
    #                     return plucked_branch_or_error
    #                 else:
    #                     _____
    #         return Tree(_____, plucked_branches)
    #     nonlocal olive
    #     if olive.is_leaf():
    #         assert k == olive.label, 'all k must appear in olive'
    #         return 'success!'
    #     _____
    #     if isinstance(olive, str):
    #         return olive
    #     return plucker
    # return plucker

##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches