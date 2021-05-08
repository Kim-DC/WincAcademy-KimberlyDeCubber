# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template

#def greet(name, template = "Hello, "):
#    #template = "Hello, {}!".format(name) if template == "Hello, " else print(template + ", " + name + "!")
#    if template == "Hello, ":
#        template = "Hello, {}!".format(name)
#    else:
#        template = (template + ", " + name + "!")
#    #template = "Hello, {}!".format(name) if template == "Hello, " else template = (template + ", " + name + "!")
#    return template

def greet(name, template = 'Hello, <name>!'):
    template = template.replace("<name>", name)
    if template == 'Hello, ':
        template = 'Hello, {}!'.format(name)
    else:
        template = template 
    return template

#Part 2: Force

planets = {
           'sun':'274', 
           'jupiter':'24.9', 
           'neptune':'11.1', 
           'saturn':'10.4', 
           'earth':'9.8',
           'uranus':'8.9',
           'venus':'8.9',
           'mars':'3.7',
           'mercury':'3.7',
           'moon':'1.6',
           'pluto':'0.6'
        }

def force(mass, body = "earth"):
    gravity = planets.get(str(body))
    force = (mass * float(gravity))
    return int(force)

#Part 3: Gravity

def pull(m1, m2, d):
    G = 6.674 * 10 **-11
    F = G * (m1 * m2 / d**2)
    return F
        
pull(30000, 25000, 0.2)

# test print
if __name__ == "__main__":
    greet("Doc")
    greet("Bob", "What's up")
    
    print(force(10, "sun"))
    print(pull(30000, 25000, 0.2))
    
    print(greet("Doc"))
    print(greet('Bob', 'Testing, <name>!'))

    #'Testing, Alice!'