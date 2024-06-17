from .action import Action
from .record import Record
import white_elephant.state.game as Game

class PassAction(Action):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def do(game: Game.Game) -> Record:
        game.passCount+=1
        game.unlockedPlayerCount-=1
        game.players[game.index].isLocked = True
        game.index+=1
        
        data = { "type": "pass" }
        passRecord = Record(data)
        return passRecord

    @staticmethod
    def undo(game: Game.Game, record: Record) -> int:
        if(record.data['type'] != "pass"):
            #TODO create log class and capture error
            print("Error, non pass value: %s" % (record.data['type'] != "pass"))
            return 1
        game.index-=1
        game.players[game.index].isLocked = False
        game.unlockedPlayerCount+=1
        game.passCount-=1
        return 0