import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))

running = True

cell_size = 160
cells_coord = [
    (0,0),
    (0,166),
    (0,166*2),

    (166,0),
    (166,166),
    (166,166*2),
    
    (166*2,0),
    (166*2,166),
    (166*2,166*2),
    ]
def displayText(text, screen, position=(200,200), rect_size=200):
    myfont = pygame.font.Font(None, 45)
    text_rendering = myfont.render(text, True, "blue")
    screen.blit(text_rendering, position, pygame.Rect(0,0,rect_size,rect_size))


def get_winner():
    if 2 < len(x_points):
        try:
            if x_points[0][0] == x_points[1][0] == x_points[2][0]:
                displayText("X Wins", window)
            if x_points[3][0] == x_points[4][0] == x_points[5][0]:
                displayText("X Wins", window)

        except:
            pass
    if 2 < len(o_points):
        try:
            if o_points[0][0] == o_points[1][0] == o_points[2][0]:
                displayText("O Wins", window)
            if o_points[3][0] == o_points[4][0] == o_points[5][0]:
                displayText("O Wins", window)
        except:
            pass
        

def draw_player():
    for coord in o_points:
        pygame.draw.circle(window, "red", coord, 40, 5)

    for coord in x_points:
        pygame.draw.lines(window, "blue", True, [(coord[0]-50,coord[1]-50),(coord[0]+50,coord[1]+50)], 3)
        pygame.draw.lines(window, "blue", True, [(coord[0]-50,coord[1]+50),(coord[0]+50,coord[1]-50)], 3)



o_points = []
x_points = []
turn = 1
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            # o_points.append(pos)
            for coord in cells_coord:
                
                if coord[0]<pos[0]<coord[0]+160 and coord[1]<pos[1]<coord[1]+160:
                    if turn%2 == 0:
                        x_points.append((coord[0]+80, coord[1]+80))
                    else:
                        o_points.append((coord[0]+80, coord[1]+80))
                    turn += 1
                    break
    
    window.fill("black")

    for coord in cells_coord:
        pygame.draw.rect(window, 'white', pygame.Rect(coord[0], coord[1],cell_size,cell_size))



    
    draw_player()
    get_winner()


    pygame.display.update()
    pygame.display.flip()

pygame.quit()