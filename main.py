import pygame
import os
import random

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
MAX_BULLETS = 20

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Secret Door Game")
bg = pygame.image.load(os.path.join('resources', 'background.jpg'))
char = pygame.image.load(os.path.join('resources', 'player_standing.png'))

font = pygame.font.SysFont('comicsans', 30, True, False)
clock = pygame.time.Clock()
score = 0


class Statusbar(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = SCREEN_WIDTH
        self.height = 30

    def draw(self, win):
        pygame.Surface.fill(win, (0, 0, 0), (self.x, self.y, self.width, self.height))

        text = font.render('Health: ', 1, (255, 255, 255))
        win.blit(text, (round(text.get_width()/4), round(self.height/2 - (text.get_height()/2))))

        text = font.render('Score: ' + str(score), 1, (255, 255, 255))
        win.blit(text, (1000, round(self.height/2 - (text.get_height()/2))))


class Player(object):
    walkUp = pygame.image.load(os.path.join('resources', 'player_behind.png'))
    walkDown = pygame.image.load(os.path.join('resources', 'player_front.png'))
    walkRight = [
        pygame.image.load(os.path.join('resources', 'player_R1.png')),
        pygame.image.load(os.path.join('resources', 'player_R2.png')),
        pygame.image.load(os.path.join('resources', 'player_R3.png')),
        pygame.image.load(os.path.join('resources', 'player_R4.png')),
        pygame.image.load(os.path.join('resources', 'player_R5.png')),
        pygame.image.load(os.path.join('resources', 'player_R6.png')),
        pygame.image.load(os.path.join('resources', 'player_R7.png')),
        pygame.image.load(os.path.join('resources', 'player_R8.png')),
        pygame.image.load(os.path.join('resources', 'player_R9.png'))
        ]

    walkLeft = [
        pygame.image.load(os.path.join('resources', 'player_L1.png')),
        pygame.image.load(os.path.join('resources', 'player_L2.png')),
        pygame.image.load(os.path.join('resources', 'player_L3.png')),
        pygame.image.load(os.path.join('resources', 'player_L4.png')),
        pygame.image.load(os.path.join('resources', 'player_L5.png')),
        pygame.image.load(os.path.join('resources', 'player_L6.png')),
        pygame.image.load(os.path.join('resources', 'player_L7.png')),
        pygame.image.load(os.path.join('resources', 'player_L8.png')),
        pygame.image.load(os.path.join('resources', 'player_L9.png'))
        ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.walkCount = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        # self.standing = True
        self.health = 9
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(self.walkUp, (self.x, self.y))
        elif self.down:
            win.blit(self.walkDown, (self.x, self.y))
        else:
            win.blit(self.walkDown, (self.x, self.y))

        # health bar
        pygame.draw.rect(win, (255, 0, 0), (120, round(statusBar.height/2 - 5), 50, 10))  # red
        pygame.draw.rect(win, (0, 255, 0), (120, round(statusBar.height/2 - 5), 50 - round(((50/9)*(9 - self.health))), 10))  # green

        # hitbox
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw hitbox

    def hit(self):
        self.x = round(SCREEN_WIDTH/2 - 32)
        self.y = round((SCREEN_HEIGHT)/2 - 32)
        self.walkCount = 0
        pygame.display.update()

        # take damage
        if self.health > 0:
            self.health -= 1
            pygame.display.update()
        else:  # dead
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('Game Over', 1, (255, 0, 0))
            win.blit(text, (round(SCREEN_WIDTH/2 - (text.get_width()/2)), round(SCREEN_HEIGHT/2 - (text.get_height()/2))))
            pygame.display.update()
            i = 0
            while i < 200:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():  # prevent delay if exiting program
                    if event.type == pygame.quit:
                        i = 51
                        pygame.quit()
                if i == 49:
                    pygame.quit()


class Enemy(object):
    walkUp = pygame.image.load(os.path.join('resources', 'enemy_behind.png'))
    walkDown = pygame.image.load(os.path.join('resources', 'enemy_front.png'))
    walkRight = [
        pygame.image.load(os.path.join('resources', 'enemy_R1.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R2.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R3.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R4.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R5.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R6.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R7.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R8.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R9.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R10.png')),
        pygame.image.load(os.path.join('resources', 'enemy_R11.png'))
    ]

    walkLeft = [
        pygame.image.load(os.path.join('resources', 'enemy_L1.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L2.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L3.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L4.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L5.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L6.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L7.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L8.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L9.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L10.png')),
        pygame.image.load(os.path.join('resources', 'enemy_L11.png'))
        ]

    def __init__(self, x, y, verticalDirection, end):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.verticalDirection = verticalDirection
        self.end = end
        if verticalDirection:
            self.path = [self.y, self.end]
        else:
            self.path = [self.x, self.end]
        # self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        # healthbar
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 15, self.hitbox[1] - 10, 50, 5))  # red
        pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0] - 15, self.hitbox[1] - 10, 50 - round(((50/9)*(9 - self.health))), 5))  # green

        # hitbox
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw hitbox

    def move(self):
        if self.vel > 0:
            if self.verticalDirection:
                if self.y + self.vel < self.path[1]:
                    self.y += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
        else:
            if self.verticalDirection:
                if self.y - self.vel > self.path[0]:
                    self.y += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            enemies.pop(enemies.index(enemy))
            global score
            score += 5


class projectile(object):
    def __init__(self, x, y, radius, color, facingx, facingy):
        self.x = x  # starting position
        self.y = y  # starting position
        self.radius = radius
        self.color = color
        self.facingx = facingx  # projectile goes left or right
        self.facingy = facingy  # projectile goes up or down
        self.xvel = 12 * facingx
        self.yvel = 12 * facingy

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Door(object):
    doorImage = pygame.image.load(os.path.join('resources', 'door.png'))

    def __init__(self, x, y, width, height, color, visible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = visible
        self.enabled = True
        self.hitbox = (self.x, self.y, width, height)

    def draw(self, win):
        if self.visible:
            # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)  # draw hitbox
            win.blit(self.doorImage, (self.x, self.y))

    def enter(self):
        if self.enabled:
            print('Entered door!')


shootLoop = 0
bullets = []
enemies = []
doors = []
player1 = Player(round(SCREEN_WIDTH/2 - 32), round(SCREEN_HEIGHT/2 - 32), 64, 64)
statusBar = Statusbar()
# enemies.append(Enemy(100, 410, False, 450))
# enemies.append(Enemy(300, 700, True, 450))


def createRandomEnemies(number):
    global enemies

    for n in range(number):
        startx = random.randint(0+64, SCREEN_WIDTH-64)
        starty = random.randint(0+64, SCREEN_HEIGHT-64)

        # prevent enemy from spawning on the player
        while player1.hitbox[0] + player1.hitbox[2] > startx and player1.hitbox[0] < startx + 64:
            startx = random.randint(0+64, SCREEN_WIDTH-64)
            starty = random.randint(0+64, SCREEN_HEIGHT-64)

        vertical = random.randint(0, 1)
        if vertical:
            end = starty + 300
        else:
            end = startx + 300

        enemies.append(Enemy(startx, starty, vertical, end))


def redrawGameWindow():
    win.blit(bg, (0, 0))  # background
    statusBar.draw(win)

    for door in doors:
        door.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    player1.draw(win)

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def checkTasks():
    if len(enemies) == 0 and len(doors) == 0:
        doors.append(Door(50, 50, 42, 64, (150, 150, 150), True))


createRandomEnemies(10)

""" main loop """
run = True
while run:
    clock.tick(27)

    # Quit game when clicking 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Hit when touching enemies
    for enemy in enemies:
        if player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > enemy.hitbox[1]:
            if player1.hitbox[0] + player1.hitbox[2] > enemy.hitbox[0] and player1.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                player1.hit()

    # Prevent multi-shooting
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    # Bullets
    for bullet in bullets:
        # hit enemies
        for enemy in enemies:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    enemy.hit()
                    bullets.pop(bullets.index(bullet))

        # move bullet
        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
            bullet.x += bullet.xvel
        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
            bullet.y += bullet.yvel

        if bullet.x >= SCREEN_WIDTH or bullet.x <= 0 or bullet.y >= SCREEN_HEIGHT or bullet.y <= 0:
            bullets.pop(bullets.index(bullet))  # remove bullet

    # Key bindings
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        # Enter door if player's hitbox touches door's hitbox
        for door in doors:
            if player1.hitbox[1] < door.hitbox[1] + door.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > door.hitbox[1]:
                if player1.hitbox[0] + player1.width > door.hitbox[0] and player1.hitbox[0] < door.hitbox[0] + door.hitbox[2]:
                    door.enter()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if player1.right:
            facingx = 1
        elif player1.left:
            facingx = -1
        else:
            facingx = 0

        if player1.up:
            facingy = -1
        elif player1.down:
            facingy = 1
        else:
            facingy = 0

        if not(facingx or facingy):  # bullets must have a direction
            facingy = 1

        if len(bullets) < MAX_BULLETS:
            bullets.append(projectile(
                round(player1.x + player1.width // 2),
                round(player1.y + player1.height // 2),
                6,  # radius
                (0, 0, 0),  # bullet color
                facingx,
                facingy
                ))
        shootLoop = 1

    if keys[pygame.K_LEFT] and player1.x > player1.vel:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        # player1.standing = False
        if not(keys[pygame.K_UP] or keys[pygame.K_DOWN]):  # reset u/d
            player1.up = False
            player1.down = False

    if keys[pygame.K_RIGHT] and player1.x < SCREEN_WIDTH - player1.vel - player1.width:
        player1.x += player1.vel
        player1.left = False
        player1.right = True
        # player1.standing = False
        if not(keys[pygame.K_UP] or keys[pygame.K_DOWN]):  # reset u/d
            player1.up = False
            player1.down = False

    if keys[pygame.K_UP] and player1.y > player1.vel and player1.y > statusBar.height:
        player1.y -= player1.vel
        # player1.standing = False
        player1.down = False
        player1.up = True
        if not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):  # reset l/r
            player1.left = False
            player1.right = False

    if keys[pygame.K_DOWN] and player1.y < SCREEN_HEIGHT - player1.vel - player1.height:
        player1.y += player1.vel
        # player1.standing = False
        player1.down = True
        player1.up = False
        if not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):  # reset l/r
            player1.left = False
            player1.right = False

    # default position
    # if not(keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP]):
    #     player1.standing = True

    # Check win conditions, spawn door
    checkTasks()

    # Update screen
    redrawGameWindow()

""" main loop end """
pygame.quit()
