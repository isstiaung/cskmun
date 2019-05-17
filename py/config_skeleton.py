csk_dir = ''
mun_dir = ''
unified_dir = ''
unified_file = 'unified_data.csv'
data_unification=False
draw = "#ffffdd"
loss = "#ffdddd"
win = "#ffdddd"

csvs = "./output_*.csv"

lxml = "lxml"

base_utd_url = 'https://en.wikipedia.org'
start_utd_url = 'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._seasons'
base_csk_url = 'http://stats.espncricinfo.com'
start_csk_url = 'http://stats.espncricinfo.com/indian-premier-league-2014/engine/records/team/match_results_year.html?class=6;id=4343;type=team'

mun_seasons = 12
mun_table_type = "class"
mun_table_attrs = "wikitable sortable"
mun_link_type = "class"
mun_link_attrs = "external text"
mun_span_type = "id"
mun_span_attrs = "Matches"
mun_span_alt_attrs = "Premier_League"
mun_bgcolor = "bgcolor"
unified_date_column = 'Date'
combined_mun_file ="combined_mun.csv"
mun_filler = '/output_mun_'
mun_to_drop = ["Attendance","Leagueposition","Leagueposition[23]","Leagueposition[27]","Scorers"]

csk_link_type = "class"
csk_link_attrs = "QuoteSummary"
default_date_column = "Match Date"
combined_csk_file = "combined_csk.csv"
csk_to_drop = ["Margin","Scorecard"]
csk_filler = '/output_csk_'

new_column = 'played_first'
default_column_value = 'csk'
ctable = "table"
ctable_row = "tr"
ctable_header = "th"
clinks = 'a'
chref = 'href'
span = "span"
c_sep= ","
csv = ".csv"
utf8 = "utf-8"
t_win = "win"
t_draw = "draw"
t_loss = "loss"
mun_text = "United"
csk_text = "CSK"
