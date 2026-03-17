
import random as r
import time as t    


#Rank	Peak	Title	                    Worldwide gros  Year	
#1	    1	    Avatar	                    $2,923,710,708	2009  
#2	    1	    Avengers: Endgame	        $2,797,501,328	2019	
#3	    3	    Avatar: The Way of Water	$2,334,484,620	2022


class stuff:
    b=75
    r=35
    g=25
    def movie_program():
        print("do you want to know the top 3 most grousing movies of all time?")
        t.sleep(0.5)
        j=input("yes or no: " )
        while True:
            if j == "yes":
                k=input("which one do you want to know about? 1, 2 or 3: ")
                if k == "1":
                    print("Avatar | is the most grossing movie of all time with a worldwide gross o |f $2,923,710,708 in | 2009")
                elif k == "2":
                    print("Avengers: Endgame | is the second most grossing movie of all time with a worldwide gross of | $2,797,501,328 in | 2019")
                elif k == "3":
                    print("Avatar: The Way of Water | is the third most grossing movie of all time with a worldwide gross of | $2,334,484,620  |in 2022")
                print("want to know another one?")
                z=input("yes or no: ")
                if z == "yes":
                    continue
                if z == "no":
                    break
            




stuff.movie_program()