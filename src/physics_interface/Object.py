class Object:
    IDdictionary = {}
    
    
    def move(self, xmodifier, ymodifier, zmodifier):
        self.x = self.x + xmodifier
        self.y = self.y + ymodifier
        self.z = self.z + zmodifier
        
    
    def resize(self, widthmodifier, heightmodifier, depthmodifier):
        self.width = self.width + widthmodifier
        self.height = self.height + heightmodifier
        self.depth = self.depth + depthmodifier
        

    def rotate(self, r1modifier, r2modifier, r3modifier):
        self.r1 = self.r1 + r1modifier
        self.r2 = self.r2 + r2modifier
        self.r3 = self.r3 + r3modifier

    
    def moveto(self, newx=IDDictionary[ID].x, newy=IDDictionary[ID].y, newz=IDDictionary[ID].z):
        self.x = newx
        self.y = newy
        self.z = newz

   
    def setsize(self, newwidth=IDDictionary[ID].width, newheight=IDDictionary[ID].heigth, newdepth=IDDictionary[ID].depth):
        self.width = newwidth
        self.height = newheight
        self.depth = newdepth

  
    def setrotation(self, newr1=IDDictionary[ID].r1, newr2=IDDictionary[ID].r2, newr3=IDDictionary[ID].r3):
        self.r1 = newr1
        self.r2 = newr2
        self.r3 = newr3
        
    def _init_(self, ID, x, y, z, width, height, depth, r1, r2, r3):
        self.ID = ID
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        IDdictionary[self.ID] = self

