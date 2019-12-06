import random
Agent = 1
Pit = 2
Wumpus = 3
Gold = 4
MapSize = 4

class WumpusWorldGenerator():

    def __init__(self, agent, gold):
        self.x_agent, self.y_agent = agent
        self.x_gold, self.y_gold = gold
        self.Indexes =[]
        self.Indexes = self.getIndexes()
        for i in range (0,3):
            rindex_x = (self.x_agent,i) #remove index from agent x path to gold
            rindex_y = (i,self.y_gold) #remove index
            print (rindex_x)
            self.Indexes.remove(rindex_x)
            self.Indexes.remove(rindex_y)
        self.agent = agent
        self.gold = gold
        self.setAgent(self.agent)
        self.setGold(self.gold)
        self.setWumpus()
        self.setPit()
        self.block_information = {"0,0": [2, 2, 2, 2, 2, 0], "0,1": [2, 2, 2, 2, 2, 0], "0,2": [2, 2, 2, 2, 2, 0],
                                  "0,3": [2, 2, 2, 2, 2, 0],
                                  "1,0": [2, 2, 2, 2, 2, 0], "1,1": [2, 2, 2, 2, 2, 0], "1,2": [2, 2, 2, 2, 2, 0],
                                  "1,3": [2, 2, 2, 2, 2, 0],
                                  "2,0": [2, 2, 2, 2, 2, 0], "2,1": [2, 2, 2, 2, 2, 0], "2,2": [2, 2, 2, 2, 2, 0],
                                  "2,3": [2, 2, 2, 2, 2, 0],
                                  "3,0": [2, 2, 2, 2, 2, 0], "3,1": [2, 2, 2, 2, 2, 0], "3,2": [2, 2, 2, 2, 2, 0],
                                  "3,3": [2, 2, 2, 2, 2, 0]}
        self.createD()
        
    def format_block(self, x, y):
        return "%d,%d" % (x, y)

    def getIndexes(self):
        """ Fills 'Indexes' list with all potential coordinate locations in
            map. This will act as an index set for the Wumpus World
            map. Indexes = [(0,0), (0,1), ..., (3,2), (3,3)] """
        self.Indexes = []
        for x in range(MapSize):
            for y in range(MapSize):
                self.Indexes.append((x, y))
        return self.Indexes


    def getMatrix(item):
        matrix = []
        try:
            copy = getattr(item, 'copy')
        except AttributeError:
            copy = None
        for i in range(MapSize):
            matrix.append([])
            for j in range(MapSize):
                if copy:
                    matrix[i].append(copy())
                else:
                    matrix[i].append(item)
        return matrix


    world = getMatrix(1)
    #self.Indexes = getIndexes()

    def setElement(self, index, value):
        """ Sets env[index] to value and then removes this index from the
            main index set """
        x, y = index
        self.world[x][y] = value
        # Removes location from Indexes after it is used.
        if index in self.Indexes:
            self.Indexes.remove(index)

    def setPit(self):
        pit_probability = [1, 0, 0, 0, 0]
        for self.index in self.Indexes:
            self.setPit = random.choice(pit_probability)
            if self.setPit:
                self.setElement(self.index, Pit)


    def setWumpus(self):
        """ Places a Wumpus at a randomly selected square """
        self.index = random.choice(self.Indexes)
        self.setElement(self.index, Wumpus)


    def setGold(self, g):
        """ Places a block of gold at a square requested by user"""
        self.setElement(g, Gold)

    def setAgent(self, a):
        """ Places the agent at square requested by user """
        self.setElement(a, Agent)

    def createD(self):
        # [isPit, isWumpus, ispitWarning, iswumpusWarning, isgoldsin, visited]
        for i in range(0,4):
            for j in range(0,4):
                if self.world[i][j] == 2:
                    self.block_information[self.format_block(i, j)][0] = 1
                    self.block_information[self.format_block(i, j)][1] = 0
                    self.block_information[self.format_block(i, j)][2] = 0
                    self.block_information[self.format_block(i, j)][3] = 0
                    self.block_information[self.format_block(i, j)][4] = 0
                    temp = self.get_neighborhood(self.format_block(i,j))

                if self.world[i][j] == 3:
                    self.block_information[self.format_block(i, j)][0] = 0
                    self.block_information[self.format_block(i, j)][1] = 1
                    self.block_information[self.format_block(i, j)][2] = 0
                    self.block_information[self.format_block(i, j)][3] = 0
                    self.block_information[self.format_block(i, j)][4] = 0
                    temp = self.get_neighborhood(self.format_block(i,j))

                if self.world[i][j] == 4:
                    self.block_information[self.format_block(i, j)][0] = 0
                    self.block_information[self.format_block(i, j)][1] = 0
                    self.block_information[self.format_block(i, j)][2] = 0
                    self.block_information[self.format_block(i, j)][3] = 0
                    self.block_information[self.format_block(i, j)][4] = 1
        print(self.block_information) 

    def get_neighborhood(self, position):

        x = int(position[0])
        y = int(position[2])
        n_list = []
        x_range = x
        y_range = y

        for i in range(-1, 2, 2):
            if 3 >= x_range + i >= 0:
                n_list += [self.format_block(x + i, y)]
            if 3 >= y_range + i >= 0:
                n_list += [self.format_block(x, y + i)]
        return n_list


''' Test the code
A = (0, 0)  # agent location
G = (3, 3)  # gold location
wworld = WumpusWorldGenerator(A, G)
print(wworld.world) '''
