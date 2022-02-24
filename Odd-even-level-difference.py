# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) : self.root = None

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
    
    def OddEvenLevelDifference ( self , node ) :
        if node == None : return
        
        diff = node.data
        
        if node.left : diff -= self.OddEvenLevelDifference ( node.left )
        if node.right : diff -= self.OddEvenLevelDifference ( node.right )
        
        return diff
        
        
Obj = BinaryTree ()
Obj.root = Node ( 10 )
Obj.root.left = Node ( 20 )
Obj.root.right = Node ( 30 )
Obj.root.left.left = Node ( 40 )
Obj.root.left.right = Node ( 60 )
print ( Obj.OddEvenLevelDifference ( Obj.root ) )

Obj2 = BinaryTree ()
Obj2.root = Node (1)
Obj2.root.left = Node (2)
Obj2.root.right = Node (3)
print ( Obj2.OddEvenLevelDifference ( Obj2.root ) )
