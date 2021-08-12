# Elevator functioning code in python

How to run

# create an object

e = ComplexElevator()

# calling the function 

e.askPassenger(5,[3,7,5,20,12]) #this will run till all 5 passenger reach their destination and program stops

# when using inputs from command line 

e.askPassenger()

# function description



askPassenger()

This function is reponsible for taking inputs as further execution

askPassFloor()

This function reposnsible for taking floor number creating list of destinations with unique floor number 
Suppose we have floor number requests as 2,2,4,5
destination list is :

[0,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

findshortest()

This function is responsible for selecting the next destination. It will choose the floor which is closest from the current floor
Can be modified if you want to add any other algorithm for selecting the next destination (eg if current floor is 6 and we have destinations as 4,8 both are equidistant from current floor, we can add some more code to make decision based on number of passenger that has opted for the two destinations )

initialize_elevator()

This function gets destination from finshortest() and goes either up() till current floor is less than the destination, goes down() till current floor is greater than destination and if current floor is same as destination floor drops passengers on floor and substracts 1 from value of appropriate floor index in destination list 



