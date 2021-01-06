from tkinter import * # Import tkinter
import AVL
import math

class Main:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Recursive Tree") # Set a title

        self.width = 800
        self.height = 800
    
        self.canvas = Canvas(window, 
        width = self.width, height = self.height,bg="white")
        self.canvas.pack()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()

        Label(frame1, 
            text = "Enter the depth: ").pack(side = LEFT)
        self.depth = StringVar()
        Entry(frame1, textvariable = self.depth,
            justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "submit", 
            command = self.submit).pack(side = LEFT)
        Button(frame1, text = "Debug",
            command = self.debugForAVL).pack(side = LEFT)

        self.angleFactor = math.pi/5
        self.sizeFactor = 1

        window.mainloop() # Create an event loop

    def drawLine(self, x1,y1, x2,y2):
        self.canvas.create_line(x1,y1, x2,y2, tags = "line")    

    def drawCircle(self, x1, y1, radious):
        self.canvas.create_oval(x1 - radious, y1 - radious, x1 + radious, y1 + radious, tags = "line", fill ="white")  

    def debugForAVL(self):
        myTree = AVL.AVL_Tree()
        root = None
        
        root = myTree.insert(root, 10)
        root = myTree.insert(root, 20) 
        root = myTree.insert(root, 30) 
        root = myTree.insert(root, 40)
        root = myTree.insert(root, 50) 
        root = myTree.insert(root, 25) 
        print("QQ", myTree.preOrder(root, 0), root)

        self.canvas.delete("line")
        print(root, self.width/2, self.height, 30)
        self.display(root, 30)

    def paintBranch(self, x1, y1, root, length, angle = math.pi / 2, deeph = 0):            # 極座標~~
        if root:
            x2 = x1 + int(math.cos(angle) * length)
            y2 = y1 - int(math.sin(angle) * length)

            print(root)
            # Draw the line

            if deeph != 0:
                self.drawLine(x1,y1, x2,y2)
            deeph += 1
            
            if not root.left:
                angle1 = angle + self.angleFactor
                self.drawCircle(x1 + int(math.cos(angle) * length), y1 - int(math.sin(angle) * length), length / 3)
            if not root.right:
                angle1 = angle - self.angleFactor
                self.drawCircle(x1 + int(math.cos(angle) * length), y1 - int(math.sin(angle) * length), length / 3)
                
            
            self.paintBranch(x2, y2, root.left, length * self.sizeFactor, angle + self.angleFactor, deeph)
            self.paintBranch(x2, y2, root.right, length * self.sizeFactor, angle - self.angleFactor, deeph)

            return
            
    def paintCircle(self, x1, y1, root, length, angle = math.pi / 2, deeph = 0):            # 極座標~~
        if root:
            x2 = x1 + int(math.cos(angle) * length)
            y2 = y1 - int(math.sin(angle) * length)

            self.drawCircle(x2 ,y2, length / 3)
            self.canvas.create_text(x2, y2, text = root.val, tags = "line")


            self.paintCircle(x2, y2, root.left, length * self.sizeFactor, angle + self.angleFactor)
            self.paintCircle(x2, y2, root.right, length * self.sizeFactor, angle - self.angleFactor)

            return

    def display(self, root, length):
        x1, y1 = self.width/2, self.height
        self.canvas.delete("line")
        self.paintBranch(x1, y1, root, length)
        self.paintCircle(x1, y1, root, length)
        return 

    def submit(self):
        input = self.depth.get()
        inputs = input.split(',')

        myTree = AVL.AVL_Tree()
        root = None

        for i in inputs:
            root = myTree.insert(root, i)

        self.canvas.delete("line")
        self.display(root, 30)
Main()