import pygame
import random
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
ui = []


class Text:
    def __init__(self, text, text_position, id, text_size=main_font_size, text_font=main_font, text_colour=black, show=True):
        self.id = id
        self.show = show
        self.text_string = text
        self.text_position = text_position
        self.text_size = text_size
        self.font = text_font
        self.text_colour = text_colour
        self.text = pygame.font.SysFont(self.font, self.text_size).render(self.text_string, True, self.text_colour)

class Rectangle:
    def __init__(self, position, size, id, fill_colour=white, show=True):
        self.id = id
        self.show = show
        self.rect_position = position
        self.rect_size = size
        self.fill_colour = fill_colour
        self.update_button()

    def update_button(self):
        self.rect = pygame.Rect(self.rect_position[0], self.rect_position[1], self.rect_size[0], self.rect_size[1])


class Button(Rectangle, Text):
    def __init__(self, position, size, fill_colour, text, button_function=None, text_font=main_font, text_size=main_font_size, text_colour=black, text_position=None, id=None, show=True):
        Rectangle.__init__(self, position=position, size=size, fill_colour=fill_colour, id=id)
        Text.__init__(self, text=text, text_position=text_position, text_size=text_size, text_font=text_font, text_colour=text_colour, id=id)
        self.id = id
        self.button_function = button_function
        self.show = show
        if text_position is None:
            self.assign_text_position()

    def assign_text_position(self):
        self.text_position = [(self.rect_position[0] + (self.rect_position[0] + self.rect_size[0]))/2 - self.text.get_width()/2, (self.rect_position[1] + (self.rect_position[1] + self.rect_size[1]))/2 - self.text.get_height()/2]


def Show_Internal_Menu():
    for item in ui:
        if "internal" in item.id:
            item.show = True

        else:
            item.show = False


def Return_To_Main_Menu():
    for item in ui:
        if "main menu" in item.id:
            item.show = True

        else:
            item.show = False
def Show_Quit_Menu():
    print("Display Quit Menu")

def second_function():
    new_rectangle.show = not new_rectangle.show

    if new_rectangle.show is True:
        game_quit_button.button_function = fourth_function

    else:
        game_quit_button.button_function = third_function
    print("Second function called")

def third_function():
    some_text.text_position[0] += 10
    print("Third function called")

def fourth_function():
    some_text.text_position[0] -= 10
    print("fourth function called")





def draw_window():
    game_window.fill(white)

    for item in ui:

        if item.show is True:
            if isinstance(item, Rectangle):
                try:
                    pygame.draw.rect(game_window, item.fill_colour, item.rect)

                except:
                    print("Not rectangle")
            if isinstance(item, Text):
                try:
                    game_window.blit(item.text, (item.text_position[0], item.text_position[1]))

                except:
                    print("Not text")

    pygame.display.update()


def process_mouse_click(mouse_position):
    for button in button_list:
        if mouse_position[0] >= button.rect.bottomleft[0] and \
                mouse_position[1] <= button.rect.bottomleft[1] and \
                mouse_position[0] <= button.rect.topright[0] and \
                mouse_position[1] >= button.rect.topright[1] and \
                button.show is True:

            button.button_function()

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

            '''
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()

                if mouse_position[0] >= game_start_button.rect.bottomleft[0] and \
                        mouse_position[1] <= game_start_button.rect.bottomleft[1] and \
                        mouse_position[0] <= game_start_button.rect.topright[0] and \
                        mouse_position[1] >= game_start_button.rect.topright[1]:
                    game_start_button.rect_position = [random.randint(0, screen_width), random.randint(0, screen_height)]
                    game_start_button.update_button()
                    game_start_button.assign_text_position()
            '''

            if event.type == pygame.MOUSEBUTTONDOWN:
                # detect mouse button presses
                left_mouse_button, middle, right = pygame.mouse.get_pressed()
                #find mouse position
                mouse_position = pygame.mouse.get_pos()

                # if left mouse button or arrow key press detected
                if left_mouse_button:
                    process_mouse_click(mouse_position)

        draw_window()



if __name__ == '__main__':

    game_start_button = Button(id="main menu start button", position=[50, 50], size=[200, 100], fill_colour=(150, 150, 50),
                               text="Start", text_size=60, button_function=Show_Internal_Menu)
    game_quit_button = Button(id="main menu quit button", position=[50, 200], size=[200, 100], fill_colour=(150, 150, 50),
                               text="Quit", text_size=60, button_function=Show_Quit_Menu)
    new_rectangle = Rectangle(position=[250, 250], size=[100, 50], fill_colour=black, show=False, id="internal menu")

    functions = [second_function, second_function, Return_To_Main_Menu]
    for i in range(3):

        new_button = Button(id=f"internal menu button {i}", position=[screen_width-110, 60*i], size=[100, 50], fill_colour=black, text=f"Button {i}", text_colour=white, button_function=functions[i], show=False)
        ui.append(new_button)
        button_list.append(new_button)

    some_text = Text(text="Some sample text", text_position=[500, 250], id="main menu")

    ui.append(game_start_button)
    ui.append(game_quit_button)
    ui.append(new_rectangle)
    ui.append(some_text)

    button_list.append(game_start_button)
    button_list.append(game_quit_button)
    run_main()
