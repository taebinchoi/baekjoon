(do ((n (read) (- n 1)) (a 0 (max a (* (read) (read))))) ((= n 0) (print a)))