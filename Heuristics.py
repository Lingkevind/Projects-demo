#the global functrion of comparing a board to the goal
def isGoal(lis):
    if lis==[1,2,3,8,"B",4,7,6,5]:
        return True
    else:
        return False
#Each state object represents a state of the board
class state:
#The constructor of the state, contains the board it self, the direction of last move(property, for the initial state will be set as "initial", depth(initiate as 0), as well as the node of successors(initiate set as None before generating))
    def __init__ (self, list, property,depth):
        self.board=list
        self.property=property
        self.depth=depth
        self.up=None
        self.down=None
        self.left=None
        self.right=None
#The swap method that generate the board value after each moves by swaping the position of "B" and other numbers
    def swapB (self, i):
        lis= self.board.copy()
        j= lis[i]
        k= lis.index("B")
        lis[i]="B"
        lis[k]=j
        return lis
#The boolean method that verified if each successor are allowed to be generated, i.e., if "B" positioned on the top row of the board, Up is not allowed to be generated
#Also in order to prevent redundancy, the direction opposite to last move is not allowed to be generated
    def canUp (self):
        i= self.board.index("B")
        if self.property=="Down":
            return False
        elif i>=0 and i<=2:
            return False
        else:
            return True
    def canDown (self):
        i= self.board.index("B")
        if self.property=="Up":
            return False
        elif i>=6 and i<=8:
            return False
        else:
            return True
    def canLeft (self):
        i= self.board.index("B")
        if self.property=="Right":
            return False
        elif i in [0,3,6]:
            return False
        else:
            return True
    def canRight (self):
        i= self.board.index("B")
        if self.property=="Left":
            return False
        elif i in [2,5,8]:
            return False
        else:
            return True
#The generator that construct new node of state objects        
    def genUp(self):
        i=self.board.index("B")
        lis=self.swapB(i-3)
        self.up= state(lis,"Up",self.depth+1)
    def genDown(self):
        i=self.board.index("B")
        lis=self.swapB(i+3)
        self.down= state(lis,"Down",self.depth+1)
    def genLeft(self):
        i=self.board.index("B")
        lis=self.swapB(i-1)
        self.left= state(lis,"Left",self.depth+1)
    def genRight(self):
        i=self.board.index("B")
        lis=self.swapB(i+1)
        self.right= state(lis,"Right",self.depth+1)
#The grand successor generater that merges the verifiers and generators of all four directions
    def genSuccessor (self):
        if self.canUp()is True:
            self.genUp()
        if self.canDown()is True:
            self.genDown()
        if self.canLeft()is True:
            self.genLeft()
        if self.canRight()is True:
            self.genRight()
#The method that calculates hamming distances value, by adding 1 on each tile that is not in correct position
    def hamming(self):
        i=0
        if self.board[0]!=1:
            i+=1
        if self.board[1]!=2:
            i+=1
        if self.board[2]!=3:
            i+=1
        if self.board[3]!=8:
            i+=1
        if self.board[5]!=4:
            i+=1
        if self.board[6]!=7:
            i+=1
        if self.board[7]!=6:
            i+=1
        if self.board[8]!=5:
            i+=1
        return i
#Calculates manhanttan distance value, by add 1/2 on each resectively incorrect rows/column base on distance
    def manhattan(self):
        i=0
        j=self.board.index(1)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [1,4,7]:
            i+=1
        if j in [2,5,8]:
            i+=2
        j=self.board.index(2)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [0,2,3,5,6,8]:
            i+=1
        j=self.board.index(3)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [1,4,7]:
            i+=1
        if j in [0,3,6]:
            i+=2
        j=self.board.index(8)
        if (j>=0 and j<=2) or (j>=6 and j<=8):
            i+=1
        if j in [1,4,7]:
            i+=1
        if j in [2,5,8]:
            i+=2
        j=self.board.index(4)
        if (j>=0 and j<=2) or (j>=6 and j<=8):
            i+=1
        if j in [1,4,7]:
            i+=1
        if j in [0,3,6]:
            i+=2
        j=self.board.index(7)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [1,4,7]:
            i+=1
        if j in [2,5,8]:
            i+=2
        j=self.board.index(6)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [0,2,3,5,6,8]:
            i+=1
        j=self.board.index(5)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [1,4,7]:
            i+=1
        if j in [0,3,6]:
            i+=2
        return i
#Calculates permutation inversion value, by generates the list of all objects on each number's right side and compare to the list of all numbers that suppose to appear on their left
    def permutation(self):
        i=0
        j=self.board.index(2)
        a=self.board[j+1:]
        b=[1]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(3)
        a=self.board[j+1:]
        b=[1,2]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(8)
        a=self.board[j+1:]
        b=[1,2,3]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(4)
        a=self.board[j+1:]
        b=[1,2,3,8]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(7)
        a=self.board[j+1:]
        b=[1,2,3,8,4]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(6)
        a=self.board[j+1:]
        b=[1,2,3,8,4,7]
        c=list(set(a)&set(b))
        i+=len(c)
        j=self.board.index(5)
        a=self.board[j+1:]
        b=[1,2,3,8,4,7,6]
        c=list(set(a)&set(b))
        i+=len(c)
        return i
#I created a fake Manhattan that cost three time if a tile is away from is original column than row
    def inadmissible(self):
        i=0
        j=self.board.index(1)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [1,4,7]:
            i+=3
        if j in [2,5,8]:
            i+=6
        j=self.board.index(2)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [0,2,3,5,6,8]:
            i+=3
        j=self.board.index(3)
        if j>=3 and j<=5:
            i+=1
        if j>=6 and j<=8:
            i+=2
        if j in [1,4,7]:
            i+=3
        if j in [0,3,6]:
            i+=6
        j=self.board.index(8)
        if (j>=0 and j<=2) or (j>=6 and j<=8):
            i+=1
        if j in [1,4,7]:
            i+=3
        if j in [2,5,8]:
            i+=6
        j=self.board.index(4)
        if (j>=0 and j<=2) or (j>=6 and j<=8):
            i+=1
        if j in [1,4,7]:
            i+=3
        if j in [0,3,6]:
            i+=6
        j=self.board.index(7)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [1,4,7]:
            i+=3
        if j in [2,5,8]:
            i+=6
        j=self.board.index(6)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [0,2,3,5,6,8]:
            i+=3
        j=self.board.index(5)
        if j>=3 and j<=5:
            i+=1
        if j>=0 and j<=2:
            i+=2
        if j in [1,4,7]:
            i+=3
        if j in [0,3,6]:
            i+=6
        return i
 #The game object holds the open list, closed list as well as the initial board   
class Game: 
    def __init__(self, init):
        self.initState=init
        self.openList=[self.initState]
        self.copyOpenList=[self.initState.board]
        self.closedList=[]
# pushing successors generated to the end of the openlist
    def appendChild(self,S):
        S.genSuccessor()
        if S.up != None:
            if S.up.board not in self.closedList and S.up.board not in self.copyOpenList:
                self.openList.append(S.up)
                self.copyOpenList.append(S.up.board)
        if S.down != None:
            if S.down.board not in self.closedList and S.down.board not in self.copyOpenList:
                self.openList.append(S.down)
                self.copyOpenList.append(S.down.board)
        if S.left !=None:
            if S.left.board not in self.closedList and S.left.board not in self.copyOpenList:
                self.openList.append(S.left)
                self.copyOpenList.append(S.left.board)
        if S.right !=None:
            if S.right.board not in self.closedList and S.right.board not in self.copyOpenList:
                self.openList.append(S.right)
                self.copyOpenList.append(S.right.board)
# pushing successors generated to the any position of the openlist
    def insertChild(self,S):
        S.genSuccessor()
        if S.up != None:
            if S.up.board not in self.closedList and S.up.board not in self.copyOpenList:
                self.openList.insert(1,S.up)
                self.copyOpenList.append(S.up.board)
        if S.down != None:
            if S.down.board not in self.closedList and S.down.board not in self.copyOpenList:
                self.openList.insert(1,S.down)
                self.copyOpenList.append(S.down.board)
        if S.left !=None:
            if S.left.board not in self.closedList and S.left.board not in self.copyOpenList:
                self.openList.insert(1,S.left)
                self.copyOpenList.append(S.left.board)
        if S.right !=None:
            if S.right.board not in self.closedList and S.right.board not in self.copyOpenList:
                self.openList.insert(1,S.right)
                self.copyOpenList.append(S.right.board)
# the steps of each search for bfs and dfs are: check if its goal, print, generates child, push to closed list, and pop from open list
    def bfs(self):
        while(len(self.openList))>0:
            if isGoal(self.openList[0].board)==True:
                print(self.openList[0].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[0].depth)
                return True
            else:
                print(self.openList[0].board)
                self.appendChild(self.openList[0])
                self.closedList.append(self.openList[0].board)
                self.openList.pop(0)
        
    
    def dfs(self):
        while (len(self.openList))>0:
            if isGoal(self.openList[0].board)==True:
                print(self.openList[0].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[0].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[0].board)
                self.closedList.append(self.openList[0].board)
                self.insertChild(self.openList[0])
                self.openList.pop(0)
# the informed searches has added a step that calculates the f(n), and find the entry with lowest value among open list to search
    def hbfs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.hamming())  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)
    
    def mbfs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.manhattan())  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)

    def pbfs(self):        
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.permutation())  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)

    def ibfs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.inadmissible())  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)

    def hAs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.hamming()+x.depth)  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)


    def mAs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.manhattan()+x.depth)  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)

    def pAs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.permutation()+x.depth)  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                print(len(self.closedList))
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)

    def iAs(self):
        while (len(self.openList))>0:
            xlist=[]
            for x in self.openList:
                xlist.append(x.inadmissible()+x.depth)  
            i=min(xlist)
            j=xlist.index(i)
            if isGoal(self.openList[j].board)==True:
                print(self.openList[j].board)
                print("Done! The program has reached the goal with ", len(self.closedList)+1," searches and the depth of ",self.openList[j].depth)
                return True
            else:
                print(self.openList[j].board)
                self.closedList.append(self.openList[j].board)
                copy=self.openList[j]
                self.openList.pop(j)
                self.appendChild(copy)
        
# The user interface
print ("Welcome to Runze's Mini-Project of 8-puzzles")
print("Please select one of the following initialboard:\n1.goal[1,2,3,8,B,4,7,6,5]\n2.easy[2,8,3,1,6,4,7,B,5]\n3.hard[5,1,4,7,B,6,3,8,2]")
initial=int(input())
if initial==1:
    Test=state([1,2,3,8,"B",4,7,6,5],"initial",0)
if initial==2:
    Test=state([2,8,3,1,6,4,7,"B",5],"initial",0)
if initial==3:
    Test=state([5,1,4,7,"B",6,3,8,2],"initial",0)
keep=True
while keep==True:
    Play=Game(Test)
    print("The puzzle is set up, please choose the search order you prefer to run\n1.(uninformed)breadth first search\n2.(uniformed)depth first search\n3.(informed)best first search\n4.(informed)A* algorithm search")
    choice=int(input())
    if choice==1:
        Play.bfs()
    if choice==2:
        Play.dfs()
    if choice==3:
        print("Please choose the heuristics you prefer to use\n1.Hamming distance\n2.Manhattan distance\n3.sum of permutation inversions\n4.(inadmissible)fake Manhattan distance")
        mchoice=int(input())
        if mchoice==1:
            Play.hbfs()
        if mchoice==2:
            Play.mbfs()
        if mchoice==3:
            Play.pbfs()
        if mchoice==4:
            Play.ibfs()
    if choice==4:
        print("Please choose the heuristics you prefer to use\n1.Hamming distance\n2.Manhattan distance\n3.sum of permutation inversions\n4.(inadmissible)fake Manhattan distance")
        mchoice=int(input())
        if mchoice==1:
            Play.hAs()
        if mchoice==2:
            Play.mAs()
        if mchoice==3:
            Play.pAs()
        if mchoice==4:
            Play.iAs()
    print("Do you want to perform another run? yes/no")
    echoice=input()
    if echoice=="no":
        keep=False
        print ("Shutting down the program, thanks for using.")
