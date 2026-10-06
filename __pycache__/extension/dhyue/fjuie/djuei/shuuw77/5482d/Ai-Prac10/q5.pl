books(physics).
books(math).
books(history).
books(computer).
ksource(X) :- books(X).
ematerial(X) :- ksource(X).
vresource(X) :- ematerial(X).

