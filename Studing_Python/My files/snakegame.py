import pygame
import sys
import random
import time


class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkColision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position[0] == bodyPart:
                return 1
            return 0

    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body


class FoodSpawer():
    def __init__(self):
        self.position = [random.randrange(
            1, 50)*10, random.randrange(1, 50)*10]
        self.isFoodONScreen = True

    def spawnFood(self):
        if self.isFoodONScreen == False:
            self.position = [random.randrange(
                1, 50)*10, random.randrange(1, 50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodonTheScreen(self, b):
        self.isFoodONScreen = b


window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("WoW Snake")
fps = pygame.time.Clock()

score = 0

snake = Snake
foodSpawner = FoodSpawer()


def gameOver():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT')
            if event.key == pygame.K_UP:
                snake.changeDirTo('UP')
            if event.key == pygame.K_DOWN:
                snake.changeDirTo('DOWN')
            if event.key == pygame.K_LEFT:
                snake.changeDirTo('LEFT')
    FoodPos = foodSpawner.spawnFood()
    if(snake.move(FoodPos) == 1):
        score += 1
        foodSpawner.setFoodOnTheScreen(False)

    window.fill(pygame.Color(255, 255, 255))
    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0, 255, 0),
                         pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(window, pygame.Color(255, 0, 0),
                         pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if(snake.checkColision() == 1):
        gameOver()
    pygame.display.set_caption("WoW Snake | Score: " + str(score))
    pygame.display.flip()
    fps.tick(24)
