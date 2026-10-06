students(riya).
students(amit).
students(sam).
students(neha).
learner(X) :- students(X).
knowseeker(X) :- learner(X).
futurepro(X) :- knowseeker(X).
