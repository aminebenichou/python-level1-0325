import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))

running = True

cell_size = 160
cells_coord = [
    (0,0),
    (0,166),
    (166,166),
    (166,0),
    (166*2,0),
    (166*2,166),
    (166*2,166*2),
    (0,166*2),
    (166,166*2),
    ]

def draw_O(coord):
    pygame.draw.circle(window, "red", coord, 40, 5)

o_points = []
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            # o_points.append(pos)
            for coord in cells_coord:
                
                if coord[0]<pos[0]<coord[0]+160 and coord[1]<pos[1]<coord[1]+160:
                    o_points.append((coord[0]+80, coord[1]+80))
                    break
    
    window.fill("black")

    for coord in cells_coord:
        pygame.draw.rect(window, 'white', pygame.Rect(coord[0], coord[1],cell_size,cell_size))

    for point in o_points:
        draw_O(point)

    pygame.display.update()
    pygame.display.flip()

pygame.quit()