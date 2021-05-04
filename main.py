# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template

def greet(x, template = "Hello!"):
    template = "Hello, {}!".format(x) if template == "Hello!" else print(template + x)
    print(template)

greet('Doc')
greet("Doc", "What's up ")

#Part 2: Force

planets = {'sun':'274', 'jupiter':'25', 'neptune':'11', 'saturn':'10', 'earth':'9.8','uranus':'8.9','venus':'8.9','mars':'3.7','mercury':'3.7','moon':'1.6','uranus':'0.6'}

def force(mass, body = "earth"):
    gravity = planets.get(str(body))
    force = (mass * float(gravity))
    print(force)
    
force(10, "sun")

#Part 3: Gravity

def pull(m1, m2, d):
    G = 6.674 * 10 **-11
    F = G * (m1 * m2 / d**2)
    print(F)
    
pull(30000, 25000, 0.2)




