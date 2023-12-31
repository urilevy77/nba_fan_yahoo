import pandas as pd
import pyodbc

from YahooLeague import YahooLeague
from TeamAnalyzer import TeamAnalyzer


class LeagueAnalyzer:
    def __init__(self, league_id):
        self.league = YahooLeague(league_id)
        self.league_id = league_id
        data = {'FG_PCT': [], 'FT_PCT': [], 'FG3M': [], 'PTS': [], 'REB': [], 'AST': [], 'STL': [], 'BLK': [],
                'TOV': []}
        self.df_league = pd.DataFrame(data)

    def __len__(self):
        return len(self.league)

    def league_name(self):
        return self.league.league_name()

    def league_Stats(self, count=0):
        for i in self.league.league_teams_id().split("\n"):
            cur_team = TeamAnalyzer(self.league_id, i[-1])
            df_cur_team = cur_team.pg_avg_stats_team()  # current team stats
            self.df_league = pd.concat([self.df_league,df_cur_team])
        return self.df_league



# self.team_total_df.at[count, column] = float(fantasy_df[column])
