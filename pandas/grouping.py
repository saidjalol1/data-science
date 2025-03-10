import pandas as pd

team_list = ['Los Angeles Lakers', 'Toronto Raptors', 'Golden State Warriors',
  'Golden State Warriors', 'Cleveland Cavaliers', 'Golden State Warriors',
  'San Antonio Spurs', 'Miami Heat', 'Miami Heat', 'Dallas Mavericks',
  'Los Angeles Lakers', 'Los Angeles Lakers', 'Boston Celtics',
  'San Antonio Spurs', 'Miami Heat', 'San Antonio Spurs', 'Detroit Pistons',
  'San Antonio Spurs', 'Los Angeles Lakers', 'Los Angeles Lakers',
  'Los Angeles Lakers', 'San Antonio Spurs', 'Chicago Bulls', 'Chicago Bulls',
  'Chicago Bulls', 'Houston Rockets', 'Houston Rockets', 'Chicago Bulls',
  'Chicago Bulls', 'Chicago Bulls', 'Detroit Pistons', 'Detroit Pistons',
  'Los Angeles Lakers', 'Los Angeles Lakers', 'Boston Celtics',
  'Los Angeles Lakers', 'Boston Celtics', 'Philadelphia 76ers',
  'Los Angeles Lakers', 'Boston Celtics', 'Los Angeles Lakers',
  'Seattle Supersonics', 'Washington Bullets', 'Portland Trail Blazers',
  'Boston Celtics', 'Golden State Warriors', 'Boston Celtics','New York Knicks',
  'Los Angeles Lakers', 'Milwaukee Bucks', 'New York Knicks', 'Boston Celtics',
  'Boston Celtics', 'Philadelphia 76ers', 'Boston Celtics', 'Boston Celtics',
  'Boston Celtics', 'Boston Celtics', 'Boston Celtics', 'Boston Celtics',
  'Boston Celtics', 'Boston Celtics', 'St. Louis Hawks', 'Boston Celtics',
  'Philadelphia Warriors', 'Syracuse Nationals', 'Minneapolis Lakers',
  'Minneapolis Lakers', 'Minneapolis Lakers', 'Rochester Royals',
  'Minneapolis Lakers', 'Minneapolis Lakers', 'Baltimore Bullets',
  'Philadelphia Warriors']


series = pd.Series(index= team_list, data= range(2020, 1946, -1))
print(series.head())

series_group = series.groupby(by=series.index)
print(series_group.count())

series_sort= series_group.count().sort_values(ascending=False).head()
print(series)

groups = series_group.get_group("Los Angeles Lakers")
print(groups)

first_wins = series_group.min()
print(first_wins)


longest_period_without_trophy = (series_group.max() - series_group.min()).sort_values(ascending=False).head(10)
print(longest_period_without_trophy)