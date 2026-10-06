dog(tommy).
dog(bruno).
dog(lucky).
dog(rocky).
animal(X) :-  dog(X).
pet(X) :- animal(X).
livebeing(X) :- pet(X).

