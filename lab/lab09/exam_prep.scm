(define (digit-prod n)
    (if (= n 0)
        1
        (* (modulo n 10) (digit-prod (quotient n 10)))
    
    )
)

(define (merge lst1 lst2)
    (cond
        ((null? lst1) lst2)
        (else (cons (car lst1) (merge (cdr lst1) lst2)))
        )
)

(define (mulxy x y)
    (cond
        ((< y 0) (- (mulxy x (- y))))
        ((= y 0) 0)
        (else (+ x (mulxy x (- y 1))))
    )
)

(define (mul s) (reduce mulxy s))

(define (mul-expr e)
    (if (number? e) e
        (mul (map mul-expr (cdr x)))))
    
