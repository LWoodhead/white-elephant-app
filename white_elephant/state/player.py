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
        if not isinstance(value, Player):
            return False
        return (
            self.id == value.id and
            self.name == value.name and
            self.originalGift == value.originalGift and
            self.gameGift == value.gameGift and
            self.isLocked == value.isLocked
        )