import pandas as pd

# Load the dataset
nba_data = pd.read_csv("NBA Finals and MVP.csv")

# Count variables
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_g = 0
count_f = 0
count_c = 0
count_champs = 0
count_yes = 0
count_no = 0
count_MVP = 0
championship_years = []  # List to store championship years
MVP_years = [] # List to store MVP years

# Sweep analysis
for each_team in nba_data.values:
    result = each_team[3]
    year = each_team[0]
    if str(year).isdigit():
        first_score = int(result[0])
        second_score = int(result[2])
        if first_score < second_score:
            if first_score == 0:
                    count_0 += 1
            elif first_score == 1:
                    count_1 += 1
            elif first_score == 2:
                    count_2 += 1
            elif first_score == 3:
                    count_3 += 1
        elif first_score > second_score:
            if second_score == 0:
                    count_0 += 1
            elif second_score == 1:
                    count_1 += 1
            elif second_score == 2:
                    count_2 += 1
            elif second_score == 3:
                    count_3 += 1

# Sweep analysis result
q_result = input("Do you want know how many sweeps are there in NBA history? Take a guess from the integers from 0 ~ 20. ")
while True:
    if q_result.isdigit():
        if int(q_result) == int(count_0):
            print()
            print(f"Your guess is absolutely correct!")
            print(f"There are {count_0} sweeps in NBA history in the finals.")
            print(f"There are {count_1} 4-1 in NBA history in the finals.")
            print(f"There are {count_2} 4-2 in NBA history in the finals.")
            print(f"There are {count_3} 4:3 in NBA history in the finals.")
            print()
            break
        elif -5 < (int(q_result.lower()) - count_0) < 5:
            print()
            print(f"Your guess of {str(q_result)} is almost correct.")
            print(f"There are {count_0} sweeps in NBA history in the finals.")
            print(f"There are {count_1} 4-1 in NBA history in the finals.")
            print(f"There are {count_2} 4-2 in NBA history in the finals.")
            print(f"There are {count_3} 4:3 in NBA history in the finals.")
            print()
            break
        else:
            print()
            print(f"Oops, it seems your guess is a little far from the answer.")
            print(f"There are {count_0} sweeps in NBA history in the finals.")
            print(f"There are {count_1} 4-1 in NBA history in the finals.")
            print(f"There are {count_2} 4-2 in NBA history in the finals.")
            print(f"There are {count_3} 4:3 in NBA history in the finals.")
            print()
            break
    else:
         print("The thing you entered is not a number! Please enter it again!")
         q_result = input("Do you want know how many sweeps are there in NBA history? Take a guess from the integers from 0 ~ 20. ")


# MVP position analysis
q_fmvp = input("Do you know which position on the court wins the most MVP in the NBA history? If you think it's guards, type 'g', fowards, type 'f', centers, type 'c'.  ")
for each_team in nba_data.values:
    position = str(each_team[10])
    if "Guard" in position:
        count_g += 1
        if each_team[4] == each_team[11]:
             count_yes += 1
        else:
             count_no += 1
    elif "Forward" in position:
        count_f += 1
        if each_team[4] == each_team[11]:
             count_yes += 1
        else:
             count_no += 1
    elif "Center" in position:
        count_c += 1
        if each_team[4] == each_team[11]:
             count_yes += 1
        else:
             count_no += 1
# MVP position analysis result
if q_fmvp.lower() == "c":
    print()
    print(f"You're correct!")
    print(f"Among all the MVPs in the NBA history, there are {count_g} times that a guard wins it,")
    print(f"{count_f} times that a forward wins it,")
    print(f"and {count_c} times that a center wins it.")
    print(f"As a result, the centers win the most ammount of MVPs in the NBA history.")
    percentage = count_yes / (count_yes + count_no) * 100.0 
    print(f"In addition, the percentage of the MVP team winning the championship is {percentage:.2f}%.")
    print()
elif q_fmvp.lower() == "g"  :
    print()
    print(f"Oops, you're wrong!")
    print(f"Among all the MVPs in the NBA history, there are {count_g} times that a guard wins it,")
    print(f"{count_f} times that a forward wins it,")
    print(f"and {count_c} times that a center wins it.")
    if q_fmvp.lower() == "g":
         mvp = "guards"
    elif q_fmvp.lower() == "f":
         mvp = "forwards"
    print(f"As a result, centers win the most ammount of MVPs in the NBA history, but not {mvp}.")
    percentage = count_yes / (count_yes + count_no) * 100.0  # Calculate the percentage as a float
    print(f"In addition, the percentage of the MVP team winning the championship is {percentage:.2f}%.")
    print()
elif q_fmvp.lower() == "f" :
    print()
    print(f"Oops, you're wrong!")
    print(f"Among all the MVPs in the NBA history, there are {count_g} times that a guard wins it,")
    print(f"{count_f} times that a forward wins it,")
    print(f"and {count_c} times that a center wins it.")
    if q_fmvp.lower() == "g":
         mvp = "guards"
    elif q_fmvp.lower() == "f":
         mvp = "forwards"
    print(f"As a result, centers win the most ammount of MVPs in the NBA history, but not {mvp}.")
    percentage = count_yes / (count_yes + count_no) * 100.0  # Calculate the percentage as a float
    print(f"In addition, the percentage of the MVP team winning the championship is {percentage:.2f}%.")
    print()
else:
    print()
    print(f"Oops, you're wrong!")
    print(f"Among all the MVPs in the NBA history, there are {count_g} times that a guard wins it,")
    print(f"{count_f} times that a forward wins it,")
    print(f"and {count_c} times that a center wins it.")
    print(f"As a result, centers win the most ammount of MVPs in the NBA history.")
    percentage = count_yes / (count_yes + count_no) * 100.0  # Calculate the percentage as a float
    print(f"In addition, the percentage of the MVP team winning the championship is {percentage:.2f}%.")
    print()
# Favorite team championship analysis
q_team = input("What is the full name or partial name of your favorite team in the NBA? ")
matching_teams = []

for each_team in nba_data.values:
    team = str(each_team[4])
    year = each_team[0]
    if len(q_team) < 4:
        print()
        print("Please enter at least four characters for the team name.")
        print()
        q_team = input("What is the full name or partial name of your favorite team in the NBA? ")
    else:
        if q_team.lower() in team.lower() :
            count_champs += 1
            championship_years.append(str(year))
            matching_teams.append(team)
# Favorite team championship analysis result
if count_champs == 0:
    print()
    print(f"It seems that your favorite NBA team hasn't won any championships in history!")
    print()
else:
    print()
    print(f"Your favorite team has won {count_champs} NBA championship(s) until 2018!")
    print("Championship Years:")
    print(", ".join(championship_years))
    print("Matching Team(s):")
    print(", ".join(matching_teams))
    print()

# Favorite player MVP analysis
q_player = input("What is the last name of your favorite player in the NBA? For example: Bryant. ")
match_player = []
for each_team in nba_data.values:
    players = str(each_team[7])
    year = each_team[0]
    if len(q_player) < 4:
        print()
        print("Please enter at least four characters for the player's name.")
        break
    else:
        if q_player.lower() in players.lower():
            count_MVP += 1
            MVP_years.append(str(year))
            match_player.append(players)
        if q_player.lower() == players.lower():
            count_MVP += 1
            MVP_years.append(str(year))
            match_player.append(players)
# Favorite team championship analysis result
if count_MVP == 0:
    print()
    print(f"It seems that your favorite NBA player hasn't won any MVPs in history!")
    print()
else:
    print()
    print(f"Your favorite player '{q_player.title()}' has won {count_MVP} MVP(s) until 2018!")
    print("MVP Years:")
    print(", ".join(MVP_years))
    print("MVP players:")
    print(", ".join(match_player))
    print()

# Read the NBA player stats data from the CSV file
season_stats = pd.read_csv("NBA_Player_Stats.csv")

# Start an infinite loop that will continue until the user chooses to quit
while True:
    season = input("Choose an NBA season to check the data of that NBA season(from 1997~2022). For example: 2021-2022 (or enter 'quit' to exit): ")
    
    # If the user enters 'quit', break out of the loop and exit the program
    if season.lower() == 'quit':
        break
    
    # Prompt the user to enter an NBA player name
    player = input("Choose an NBA player to check the data of that NBA season you typed in: ")
    print()
    # Iterate over each row (each_stats) in the season_stats dataframe
    for each_stats in season_stats.values:
        year_AE = str(each_stats[30])
        player_B = str(each_stats[1])
        fg_per = f"{str(each_stats[10]*100)}%"
        three_per = f"{str(each_stats[13]*100)}%"

        # Check if the current row matches the specified season and player
        if season == str(year_AE) and player in player_B:

            if each_stats[4] == "TOT":
                print(f"{player_B} scored {str(each_stats[29])} points, {str(each_stats[23])} rebounds, {str(each_stats[24])} assists, {str(each_stats[25])} steals, and {str(each_stats[26])} blocks with {fg_per} field goal percentage and {three_per} 3-point percentage in {str(each_stats[4])}.")
                print()
                break
            else:
                print(f"{player_B} scored {str(each_stats[29])} points, {str(each_stats[23])} rebounds, {str(each_stats[24])} assists, {str(each_stats[25])} steals, and {str(each_stats[26])} blocks with {fg_per} field goal percentage and {three_per} 3-point percentage in {str(each_stats[4])}.")
                print()