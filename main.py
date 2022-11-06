################
# driver file
# DO NOT MODIFY THIS FILE
################

import functions as fn

def main():

    # create the sol system dictionary of planets and distances from the Sun
    planets = {"Uranus":[2750,3000,2880],
                        "Mercury":[46,70,57],
                        "Earth":[147,152,150],
                        "Venus":[107,109,108],
                        "Mars":[205,249,228],
                        "Saturn":[1350,1510,1430],
                        "Jupiter":[741,817,779],
                        "Pluto":[4440,7380,5910],
                        "Neptune":[4450,4550,4500]}

    print("All the planets...")
    fn.list_planets(fn.get_planets(planets))
    print()
    print("All the planets sorted...")
    fn.list_planets(fn.get_planets(planets, True))
    print()
    
    print("Disances from the Sun in millions of km...")
    print("==========================================")
    fn.display_planet_distances(planets)

    print("Disances from the Sun in millions of miles...")
    print("==========================================")
    fn.display_planet_distances(planets, True)

    print("The nearest planet to the sun by minimum distance is: ", fn.find_nearest(planets, fn.MIN))
    print("The nearest planet to the sun by maximum distance is: ", fn.find_nearest(planets, fn.MAX))
    # this next call is purposfully in error, but it will still work if find_nearest is done correctly
    print("The nearest planet to the sun by average distance is: ", fn.find_nearest(planets,10))
    print()
    print("The furthest planet from the sun by minimum distance is: ", fn.find_furthest(planets, fn.MIN))
    print("The furthest planet from the sun by maximum distance is: ", fn.find_furthest(planets, fn.MAX))
    print("The furthest planet from the sun by average distance is: ", fn.find_furthest(planets))
    print()

    print("But wait! Pluto is not a planet. Deleting Pluto...", end="")
    del planets["Pluto"]
    print("Done\n")

    print("All the planets...")
    fn.list_planets(fn.get_planets(planets))
    print()
    print("All the planets sorted...")
    fn.list_planets(fn.get_planets(planets, True))
    print()
    
    print("Disances from the Sun in millions of km...")
    print("==========================================")
    fn.display_planet_distances(planets)

    print("Disances from the Sun in millions of miles...")
    print("==========================================")
    fn.display_planet_distances(planets, True)

    print("The nearest planet to the sun by minimum distance is: ", fn.find_nearest(planets, fn.MIN))
    print("The nearest planet to the sun by maximum distance is: ", fn.find_nearest(planets, fn.MAX))
    print("The nearest planet to the sun by average distance is: ", fn.find_nearest(planets))
    print()
    print("The furthest planet from the sun by minimum distance is: ", fn.find_furthest(planets, fn.MIN))
    print("The furthest planet from the sun by maximum distance is: ", fn.find_furthest(planets, fn.MAX))
    # this next call is purposfully in error, but it will still work if find_furthest is done correctly
    print("The furthest planet from the sun by average distance is: ", fn.find_furthest(planets, 10))
    print()

main()
