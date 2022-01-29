(define (f x)
    (if (= x 0) 
        5
        (list x (f (- x 1)))))

(define (g x) 
    (if (list? x) (length x) x))
(map g '(1 (2 (3))) )