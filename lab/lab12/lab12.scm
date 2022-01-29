; Lab 14: Final Review

(define (compose-all funcs)
    (define func1 (lambda (x y) (y x)))
    (define (hof x)
        (define lst (cons x funcs))
        (reduce func1 lst))
    hof
)
