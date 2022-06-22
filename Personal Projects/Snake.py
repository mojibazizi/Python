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
        self.direction = Vector2(0,0)
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
        
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            # what direction is the face heading
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block 
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: # Snake turning graphics logic
                        screen.blit(self.back_left,block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: #code is looking at the next and previous position of the head to figure out what image to use.
                        screen.blit(self.turn_left,block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.back_right,block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.turn_right,block_rect)
                    
    def update_head_graphics(self):                                     # Snake head update feature
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
    
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

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0) #starts the snake from no direction


class Main:
    
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit() 

    def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print("snack")
            self.fruit.randomize()
            self.snake.add_block()
        
        for block in self.snake.body:           # Check if the fruit is spawning on snake position
            if block == self.snake.body[1:]:
                self.fruit.randomize()
    
    def check_fail(self):
        # check if the snake is outside of the screen 
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]: # check if snake hits itself
                self.game_over()        
    
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)   
        else:
            if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)  
    
    def game_over(self):
        self.snake.reset()
        
    def draw_score(self):
        # The scoreboard
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 12,apple_rect.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,3)


# game interface
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) 
clock = pygame.time.Clock()
clock = pygame.time.Clock()
apple = pygame.image.load('Personal Projects/Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font(None, 27)

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

    screen.fill((135,210,45))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    