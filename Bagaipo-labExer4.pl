female(scarlet).
female(white).
female(peacock).
female(orchid).

male(plum).
male(mustard).
male(green).

hates(scarlet,green).
hates(green,scarlet).
hates(plum,white).
hates(white,plum).
hates(mustard,B) :- female(B).
hates(mustard,plum).

likes(scarlet,orchid).
likes(peacock,orchid).
likes(orchid,peacock).
likes(scarlet,white).
likes(scarlet,plum).
likes(plum,scarlet).
likes(plum,A) :- hates(mustard,A).
    
enemies(A,B) :- hates(A,B), hates(B,A).
friends(A,B) :- likes(A,B), likes(B,A). 
friends(A,B) :- enemies(A,C), enemies(C,B).