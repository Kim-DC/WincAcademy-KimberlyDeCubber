# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# 1 variabele voor iedere speler die gescoord heeft
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
print(scorer_1)
print(scorer_2)

# 2 variabele voor iedere goal + minuut
goal_0 = 32
goal_1 = 54

# 3 Using the +-operator, create a string that reports on who scored when, according to the format:
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>

scorers = (scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1))
print(scorers)

# 4 Use f-strings or the +-operator to create a single string with information about who scored when in the format:
report = (f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute')
print(report)

# Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'John Bosman'

# first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name = player[:player.find(' ')]
print(first_name)
first_name_len = (len(first_name))
print(first_name_len)

# last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name = player[player.find(' ')+1:]
last_name_len = (len(last_name))
print(last_name_len)

# name_short: isolate and store the player's name in this format: G. von Examplestein
name_short = ((first_name[0]) + '.' + ' ' + (last_name))
print(name_short)

#chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an
#exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the
#last character of this string is not a space! For our example player:
x = (first_name_len - 1)
chant = (x * (first_name + '! ') + (first_name + '!'))
print(chant)

#good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=).
#good_chant = print(chant) if chant[24:] != " " else print("Try again")
good_chant = chant[-1] != ' '
print(good_chant)


