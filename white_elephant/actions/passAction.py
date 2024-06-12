from .action import Action
from .record import Record
from state import game as Game

class PassAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def do(game: Game) -> Record:
        game.passCount+=1
        game.unlockedPlayerCount-=1
        game.players[game.index].isLocked = True
        game.index+=1
        
        data = { "type": "pass" }
        passRecord = Record(data)
        return passRecord

    def undo(game: Game, record: Record) -> None:
        if(record.data['type'] != "pass"):
            #TODO create log class and capture error
            print("Error, non pass value: %s" % (record.data['type'] != "pass"))
        game.index-=1
        game.players[game.index].isLocked = False
        game.unlockedPlayerCount+=1
        game.passCount-=1