teacher(anita).
teacher(raj).
teacher(meera).
teacher(rahul).
employee(X) :- teacher(X).
human(X) :- employee(X).
livingbeing(X) :- human(X).
