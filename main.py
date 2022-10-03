import pygame

pygame.font.init()

screen_width = 1000
screen_height = 500
game_window = pygame.display.set_mode((screen_width, screen_height))
game_title = pygame.display.set_caption("Second Class Game")
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
main_font = 'Engravers MT'
main_font_size = 30

button_list = []

class Rectangle:
    def __init__(self, position, size, fill_colour=white):
        self.rect_position = position
        self.rect_size = size
        self.fill_colour = fill_colour
        self.rect = pygame.Rect(self.rect_position[0], self.rect_position[1], self.rect_size[0], self.rect_size[1])

class Button(Rectangle):
    def __init__(self, position, size, fill_colour, button_text, text_font=main_font, text_size=main_font_size, text_colour=black, design_details=None, button_text_position=None, id=None):
        super().__init__(position, size, fill_colour)
        self.id = id
        self.button_text = button_text
        self.button_text_font = pygame.font.SysFont(text_font, text_size)
        self.button_text = self.button_text_font.render(button_text, True, text_colour)

        if button_text_position is None:
            self.button_text_position = [(position[0] + (position[0] + size[0]))/2 - self.button_text.get_width()/2, (position[1] + (position[1] + size[1]))/2 - self.button_text.get_height()/2]

        else:
            self.button_text_position = button_text_position

        if design_details is not None:
            for item in design_details:
                print(item)


    def function(self):
        new_rectangle.fill_colour = (255, 0, 0)
        print(f"{self.id} pressed")


#modes (splash screen, campaign overview, pre-scenario, scenario, equipment inspection, calibration)
# #main menu features splashpage and options for settings, start and exit
# #settings tbc
# exit exits
# #start button opens existing campaign overview
# #campaign overview details campaign targets and progress with option to explore collected data
# #start again to proceed to next event#load up event
# #event is pre-defined tile array
# #set within certain screen bounds, outside bounds reserved for information overlay
# #user has set of options based on available equipment
# #user has access to 'deck' to choose appropriate equipment
# #equipment details imported from text files with set attributes (tbc, but will include tags)
# #user assigns organisation of equipment
# #once user presses start, scenario proceeds
# #based on rate, user can interact with equipment in order
#

new_rectangle = Rectangle(position=[250, 250], size=[100, 50], fill_colour=black)

def draw_window():
    game_window.fill(white)

    for button in button_list:
        pygame.draw.rect(game_window, button.fill_colour, button.rect)
        game_window.blit(button.button_text, (button.button_text_position[0], button.button_text_position[1]))
        pygame.draw.rect(game_window, new_rectangle.fill_colour, new_rectangle.rect)

    pygame.display.update()

def process_mouse_click(mouse_position):
    # if mouse button pressed, find position of mouse press and reset tile selection mode / visibility
    for button in button_list:
        if mouse_position[0] >= button.rect.bottomleft[0] and mouse_position[1] <= button.rect.bottomleft[1] and mouse_position[0] <= button.rect.topright[0] and mouse_position[1] >= button.rect.topright[1]:
            print(f"{button.id} pressed")
            button.function()

def run_main():
    clock = pygame.time.Clock()
    run = True
    while run:
        # tick game_instance
        clock.tick(FPS)
        # collect events in pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                # detect mouse button presses
                left_mouse_button, middle, right = pygame.mouse.get_pressed()
                #find mouse position
                mouse_position = pygame.mouse.get_pos()

                # if left mouse button or arrow key press detected
                if left_mouse_button:
                    #print(f"Mouse button down")
                    process_mouse_click(mouse_position)

        draw_window()



if __name__ == '__main__':
    game_start_button = Button(id="start button", position=[50, 50], size=[200, 100], fill_colour=(150, 150, 50),
                               button_text="Start", text_size=60)
    game_quit_button = Button(id="quit button", position=[50, 200], size=[200, 100], fill_colour=(150, 150, 50),
                               button_text="Quit", text_size=60)

    button_list.append(game_start_button)
    button_list.append(game_quit_button)
    run_main()