"""
Challenge (due 3/18/19)
-Functional
-Cleaned code
-Tested

"""
class PacMan:
    points = 5000
    lives = 3
    ghostie = 200

    def eat(food):
        PacMan.points += food
        return PacMan.points

    def consume():
        PacMan.points += PacMan.ghostie
        PacMan.ghostie *= 2
        if PacMan.ghostie == 1600:
            PacMan.ghostie = 200
    
    def die():
        PacMan.lives -= 1

    def extra():
        PacMan.lives += 1

foods = {
    'dot' : 10,
    'cherry' : 100,
    'strawberry' : 300,
    'orange' : 500,
    'apple' : 700,
    'melon' : 1000,
    'galaxian' : 2000,
    'bell' : 3000,
    'key' : 5000,
    }

threshold = 10000

if __name__ == '__main__':
    text = open('input.txt', 'r')
    instruct = text.read().split(',')

    for item in instruct:
        direct = item.lower()
        if direct == 'invincibleghost':
            PacMan.die()
            print('ouch!')
        elif direct == 'vulnerableghost':
            PacMan.consume()
            print('ate a ghost!')
        else:
            for key, value in foods.items():
                if direct == key:
                    PacMan.eat(value)

        if PacMan.points >= threshold:
            PacMan.extra()
            print('extra life!')
            threshold += 10000
        if PacMan.lives == 0:
            break

    print("Game Over")
    print(f"Lives: {PacMan.lives}\n"
        f"Points: {PacMan.points}")

    text.close()
