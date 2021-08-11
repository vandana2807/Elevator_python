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
        self.delay(0.5)
    
    def askPassenger(self,numOfPass,lof):
        self.isdooropen=False
        print("Elevator opening...")
        self.delay(0.5)
        self.numOfPass=numOfPass
        self.lof=lof
        if self.numOfPass<self.minp or self.numOfPass>self.maxp:
            print("Error, valid number of passengers [1-20]")
        self.listofloors=[]
        #self.floor=0
        
        #isvalidentry=False
        for a in range(0,self.numOfPass):
            #self.floor=self.askPassFloor(a)
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
        
    #def askPassFloor(self,pid):
    #        self.isvalidentry=False
    #        self.floor=0
    #        while not isvalidentry:
    #           self.floor=self.lof[pid]
    #            print("Passenger # ",pid+1,"floor number :",self.floor)
    #            if self.floor<self.minf or self.floor>self.maxf:
    #                print("Error floor[1-20]")
    #            elif self.floor==self.curf:
    #                print("You are already in the", self.curf, "floor")
    #            else:
    #                self.destination_list[self.floor-1]=self.destination_list[self.floor-1]+1
    #                self.isvalidentry=True
    #        return self.floor
    
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
        #askPassenger()
                
        
    
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
