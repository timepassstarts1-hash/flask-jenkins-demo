batsman(sachin).
batsman(virat).
batsman(rohit).
batsman(dhoni).
cricketer(X) :- batsman(X).
sportsman(X) :- cricketer(X).
famous(X) :- sportsman(X).
