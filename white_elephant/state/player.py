from .gift import Gift

class Player:
    def __init__(self, id: int, name: str, orignalGift: Gift) -> None:
        self.id = id
        self.name = name
        self.originalGift = orignalGift
        self.gameGift = None
        self.isLocked = False
        
    def __str__(self) -> str:
        return "Player(id: %d, name: %s, isLocked: %r,\noriginalGift: %s,\ngameGift: %s)" % (
            self.id,self.name,self.isLocked,str(self.originalGift),str(self.gameGift))
        
    def __eq__(self, value: object) -> bool:
        if(value is None):
            return False
        if(self.id is not value.id):
            return False
        if(self.name is not value.name):
            return False
        if(self.originalGift != value.originalGift):
            return False
        if(self.gameGift is not value.gameGift):
            return False
        if(self.isLocked is not value.isLocked):
            return False
        return True