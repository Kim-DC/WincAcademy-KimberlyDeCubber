# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# 1 variabele voor iedere speler die gescoord heeft
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
print(player_0)
print(player_1)

# 2 variabele voor iedere goal + minuut
goal_0 = 32
goal_1 = 54

# 3 Using the +-operator, create a string that reports on who scored when, according to the format:
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>

scorers = (player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1))
print(scorers)

# test scorers2 = (speler_1) +  str(goal_1), (speler_2) +  str(goal_2)
#test print(scorers2)

# 4 Use f-strings or the +-operator to create a single string with information about who scored when in the format:
report = (f'{player_0} scored in the {goal_0}nd minute \n{player_1} scored in the {goal_1}th minute')
print(report)

# Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'John Bosman'

# first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name = player[player.find("John"):4]
print(first_name)

# last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[player.find("B"):])
print(last_name_len)

# name_short: isolate and store the player's name in this format: G. von Examplestein
name_short = player[0:1] + "." + player[5:11]
print(name_short)

#chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an
#exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the
#last character of this string is not a space! For our example player:
chant = (" " + first_name + "!") * len(first_name)
print(chant)

#good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=).
good_chant = print(chant) if chant[24:] != " " else print("Try again")


