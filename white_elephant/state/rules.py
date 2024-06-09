class Rules:
    def __init__(self, name: str, maxStealCount: int,
                randomizeRoundOrder: bool, bonusGift: bool,
                bonusSteal: bool, stealFailChance: float) -> None:
        self.name = name
        self.maxStealCount = maxStealCount
        self.randomizeRoundOrder = randomizeRoundOrder
        self.bonusGift = bonusGift
        self.bonusSteal = bonusSteal
        self.stealFailChance = stealFailChance
        #TODO pull max players, etc from a config file
        self.maxPlayers = 10
        
    def __str__(self) -> str:
        return "Rules(name: %s\nmaxSteals: %d\nrandomOrder: %r\nbonusGift: %r\nbonusSteal: %r\nstealFailChance: %d)" % (
            self.name,self.maxStealCount,self.randomizeRoundOrder,self.bonusGift,self.bonusSteal,self.stealFailChance)
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Rules):
            return False
        return (
            self.name == value.name and
            self.maxStealCount == value.maxStealCount and
            self.randomizeRoundOrder == value.randomizeRoundOrder and
            self.bonusGift == value.bonusGift and
            self.bonusSteal == value.bonusSteal and
            self.stealFailChance == value.stealFailChance
        )