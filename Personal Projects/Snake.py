import pygame, sys, random
from pygame.math import Vector2


class Fruit:
    def __init__(self):
     # create an x and y position
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x *cell_size,self.pos.y *cell_size,cell_size,cell_size)
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
    def randomize(self):
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.pos = Vector2(self.x,self.y)



class Snake:
    
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        self.head_up = pygame.image.load("Personal Projects/Graphics/Snake_head_up.png")                    #Drawing the Snake
        self.head_down = pygame.image.load("Personal Projects/Graphics/Snake_head_down.png")
        self.head_right = pygame.image.load("Personal Projects/Graphics/Snake_head_right.png")
        self.head_left = pygame.image.load("Personal Projects/Graphics/Snake_head_left.png")
        
        self.body_horizontal = pygame.image.load("Personal Projects/Graphics/Snake_body_horizontal.png")
        self.body_vertical = pygame.image.load("Personal Projects/Graphics/Snake_body_vertical.png")
        
        self.tail_left = pygame.image.load("Personal Projects/Graphics/Snake_tail_left.png")
        self.tail_right = pygame.image.load("Personal Projects/Graphics/Snake_tail_right.png")
        self.tail_up = pygame.image.load("Personal Projects/Graphics/Snake_tail_up.png")
        self.tail_down = pygame.image.load("Personal Projects/Graphics/Snake_tail_down.png")
        
        self.turn_left = pygame.image.load("Personal Projects/Graphics/Snake_turn_left.png")
        self.turn_right = pygame.image.load("Personal Projects/Graphics/Snake_turn_right.png")
        self.back_left = pygame.image.load("Personal Projects/Graphics/Snake_back_left.png")
        self.back_right = pygame.image.load("Personal Projects/Graphics/Snake_back_right.png")
    
    def draw_snake(self):
        for index,block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            # what direction is the face heading
            if index == 0:
                screen.blit(self.head_right,block_rect)
            else:
                pygame.draw.rect(screen,(85,0,87), block_rect)


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)    
            self.body = body_copy[:]
            self.new_block = False
        
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)    
            self.body = body_copy[:]

    
    def add_block(self):
        self.new_block = True




class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit() 

    def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print("snack")
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        # check if the snake is outside of the screen 
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()        
        
    
    def game_over(self):
        pygame.QUIT
        sys.exit()

        # check if snake hits itself


# game interface
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) 
clock = pygame.time.Clock()
clock = pygame.time.Clock()
apple = pygame.image.load('Personal Projects/Graphics/apple.png').convert_alpha()

main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:                                                            # Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        
        if event.type == SCREEN_UPDATE:
            main_game.update()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((175,0,0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    