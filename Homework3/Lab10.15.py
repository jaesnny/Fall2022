#JenniferChu
#1873159

class Team:
    def __init__(self) -> object:
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    team_name = input()
    team_wins = int(input())
    team_losses: int = int(input())
    team_score = Team()

    team_score.team_name = team_name
    team_score.team_wins = team_wins
    team_score.team_losses = team_losses

    if team_score.get_win_percentage() >= 0.5:
        print("Congratulations, Team", team_score.team_name, "has a winning average!")
    else:
        print('Team', team_score.team_name, "has a losing average.")
