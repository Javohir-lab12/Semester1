from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    player_id: str
    games_played: int = 0
    points: list[int] = field(default_factory=list)
    def record_game(self, pts: int):
        self.games_played += 1
        self.points.append(pts)
    def avg_points(self) -> float:
        if not self.games_played:
            return 0
        return sum(self.points)/len(self.points)

@dataclass
class Team:
    team_name: str
    coach: str
    max_roster: int
    players: list[Player] = field(default_factory=list)
    roster_size: int = field(init=False)
    def __post_init__(self):
        self.roster_size_updater()
    def roster_size_updater(self):
        self.roster_size = len(self.players)
    def sign(self, player: Player) -> bool:
        if len(self.players) + 1 > self.max_roster:
            return False
        self.players.append(player)
        self.roster_size_updater()
        return True
    def mvp(self) -> str:
        if not self.players:
            return "No data"
        mvp = sorted(self.players, key=lambda x: x.avg_points(), reverse=True)[0]
        if mvp.avg_points() == 0:
            return "No data"
        return mvp.name
    def team_stats(self) -> str:
        result = f"{self.team_name} ({self.coach}):\n"
        for player in self.players:
            result += f"  {player.name} - {player.games_played} games, avg {player.avg_points():.1f} pts\n"
        result += f"Roster: {self.roster_size}/{self.max_roster}"
        return result

p1 = Player("Alex", "P01")
p2 = Player("Jordan", "P02")
p3 = Player("Sam", "P03")

p1.record_game(18)
p1.record_game(24)
p1.record_game(21)
p2.record_game(30)
p2.record_game(27)
p3.record_game(12)

t = Team("Thunder", "Coach Rivers", 3)
print(t.sign(p1))
print(t.sign(p2))
print(t.sign(p3))
print(t.sign(Player("Taylor", "P04")))
print(t.roster_size)
print(t.mvp())
print(t.team_stats())