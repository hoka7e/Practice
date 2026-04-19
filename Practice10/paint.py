import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 10
    mode = 'line'
    color = (0, 0, 255)
    drawing = False
    start_pos = None
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                # режимы
                if event.key == pygame.K_l:
                    mode = 'line'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                
                # цвета
                if event.key == pygame.K_1:
                    color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)
                elif event.key == pygame.K_5:
                    color = (255, 255, 255)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                elif event.button == 3:
                    radius = max(1, min(50, radius + 2))
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    
                    if mode == 'rect':
                        rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.rect(screen, color, rect, radius)
                    
                    elif mode == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        r = int((dx**2 + dy**2)**0.5)
                        pygame.draw.circle(screen, color, start_pos, r, radius)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == 'line':
                        points.append(event.pos)
                        if len(points) > 1:
                            pygame.draw.line(screen, color, points[-2], points[-1], radius)
                    
                    elif mode == 'eraser':
                        pygame.draw.circle(screen, (0,0,0), event.pos, radius)
        
        pygame.display.flip()
        clock.tick(60)

main()
