import time
class ComplexElevator:
    def __init__(self):
        self.maxp=20
        self.maxf=20
        self.minp=1
        self.minf=1
        self.curf=1
        self.desf=0
        self.passf=0
        self.destination_list=[0 for x in range(20)]
        self.listofloors=[]
    
    def startsimulation(self):
        print("welcome to elevator")
        print("please enjoy")
        print("Copyright © Vandana")
        self.delay(0.5)
    
    def askPassenger(self,numOfPass,lof):
        self.startsimulation()
        self.isdooropen=False
        print("Elevator opening...")
        self.delay(0.5)
        self.numOfPass=numOfPass
        self.lof=lof
        if self.numOfPass<self.minp or self.numOfPass>self.maxp:
            print("Error, valid number of passengers [1-20]")
            
        #isvalidentry=False
        for a in range(0,self.numOfPass):
            self.floor=self.lof[a]
            print("Passenger # ",a+1,"floor number :",self.floor,"| F")
            if self.floor<self.minf or self.floor>self.maxf:
                print("Error floor[1-20]")
            elif self.floor==self.curf:
                print("You are already in the", self.curf, "floor")
            else:
                self.destination_list[self.floor-1]=self.destination_list[self.floor-1]+1
                #self.isvalidentry=True
            if self.floor not in self.listofloors:
                self.listofloors.append(self.floor)
                    
        print("all destinations", self.destination_list)
        print("unique destinations", self.listofloors)
        print("Elevator closing...")
        self.delay(0.5)
        self.isdooropen=False
        self.initialize_elevator()
     
    #uncomment if yoou want to take input from command line
    #def askPassenger(self):
    #    self.startsimulation()
    #    self.isdooropen=False
    #    print("Elevator opening...")
    #    self.delay(0.5)
    #    print(self.curf,"| F","how many passengers :")
    #    self.numOfPass =int(input())
    #    if self.numOfPass<self.minp or self.numOfPass>self.maxp:
    #        print("Error, valid number of passengers [1-20]")
    #        self.askPassenger()
    #    else:
    #        self.lof=[]
    #        for a in range(0,self.numOfPass):
    #            self.floor=self.askPassFloor(a)
    #            if self.floor not in self.listofloors:
    #                self.listofloors.append(self.floor)
    #    print("all destinations", self.destination_list)
    #    print("unique destinations", self.listofloors)
    #    print("Elevator closing...")
    #    self.delay(0.5)
    #    self.isdooropen=False
    #    self.initialize_elevator()
        
    #uncomment if you want to take input from command line
    #def askPassFloor(self,pid):
    #    self.isvalidentry=False
    #    self.floor=0
    #    while not self.isvalidentry:
    #        print("Passenger # ",pid+1,"enter your floor :")
    #        self.floor=int(input())
    #        if self.floor<self.minf or self.floor>self.maxf:
    #            print("Error you have entered out of range floor, valid [1-20]")
    #        elif self.floor==self.curf:
    #            print("You are already in the", self.curf, "floor")
    #        else:
    #            self.destination_list[self.floor-1]=self.destination_list[self.floor-1]+1
    #            self.isvalidentry=True
    #    return self.floor
    
    def initialize_elevator(self):
        for a in range(0,len(self.listofloors)):
            self.shortest=self.findshortest()
            print("Next destination :",self.shortest, "| F passenger count(",self.destination_list[self.shortest-1],")")
            self.delay(0.5)
            while self.curf<self.shortest:
                self.up()
            while self.curf>self.shortest:
                self.down()
            while self.destination_list[self.shortest-1]>0:
                print(self.curf, "F | unloading passenger (",self.destination_list[self.shortest-1], ") at", self.curf,"| F")
                self.destination_list[self.shortest-1]=self.destination_list[self.shortest-1]-1
                self.delay(0.5)
        #askPassenger() # uncomment to run continous (means after 1 batch finished will ask inputs for other batch
                
        
    
    def findshortest(self):
        
        self.id1=0
        self.sh=abs(self.curf-self.listofloors[0])
        print("currr",self.curf,self.sh)
        for a in range(0,len(self.listofloors)):
             if self.sh>abs(self.curf-self.listofloors[a]):
                self.sh=abs(self.curf-self.listofloors[a])
                self.id1=a
        self.sh=self.listofloors[self.id1]
        self.listofloors[self.id1]=100
        return self.sh
    
                
    
    def up(self):
        self.curf=self.curf+1
        print(self.curf," | F Going up...")
        
    def down(self):
        self.curf=self.curf-1
        print(self.curf," | FGoing up...")
    
    def delay(self,ms):
        time.sleep(ms)
