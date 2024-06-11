from .rules import Rules
from .player import Player

class Game:
    def __init__(self, id: int, rules: Rules, players: list[Player]) -> None:
        self.id = id
        self.rules = rules
        self.players = players
        self.index = None
        self.passCount = None
        self.unlockedPlayerCount = None
        self.playerCount = None
        self.closedGiftCount = None
        self.isStarted = False
        
    def startGame(self):
        self.index = 0
        self.passCount = 0
        self.unlockedPlayerCount = len(self.players)
        self.playerCount = len(self.players)
        self.closedGiftCount = len(self.players)
        self.isStarted = True
        
    def __str__(self) -> str:
        output = ""
        output += "Game(id: %d\n"
        output += str(self.rules)
        for p in self.players:
            output += str(p)
        output += "currentIndex: %d\npasscount: %d\nunlockedPlayers: %d\nplayers: %d\nclosedGifts: %d\ngameStarted: %r)" % (
            self.index,self.passCount,self.unlockedPlayerCount,self.playerCount,
            self.closedGiftCount,self.isStarted
        )
        return output
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Game):
            return False
        return (
            self.id == value.id and
            self.rules == value.rules and
            self.players == value.players and
            self.index == value.index and
            self.passCount == value.passCount and
            self.unlockedPlayerCount == value.unlockedPlayerCount and
            self.playerCount == value.playerCount and
            self.closedGiftCount == value.closedGiftCount and
            self.isStarted == value.isStarted
        )
        