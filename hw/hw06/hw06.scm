;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= b 1) 1)
    ((= n 1) b)
    ((even? n) (square (pow b (/ n 2)))) 
    ((odd? n) (* b (pow b (- n 1))))
    )
)

(define (unique s)
    (cond 
      ((null? s) nil)
      (else (cons (car s) (unique (filter  (lambda (x) (not (eq? x (car s)))) s))))
    )
)