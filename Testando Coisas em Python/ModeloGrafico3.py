import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600)) 
relogio = pygame.time.Clock()

jogador_pos = [400, 500]
jogador_vel = 5

rodando = True
while rodando: 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            rodando = False

    # Movimentação fora do for
    teclas = pygame.key.get_pressed() 
    if teclas[pygame.K_LEFT]: 
        jogador_pos[0] -= jogador_vel
    if teclas[pygame.K_RIGHT]: 
        jogador_pos[0] += jogador_vel
    if teclas[pygame.K_UP]: 
        jogador_pos[1] -= jogador_vel
    if teclas[pygame.K_DOWN]: 
        jogador_pos[1] += jogador_vel
            
    # Desenhar e atualizar a tela dentro do loop principal
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), (jogador_pos[0], jogador_pos[1], 50, 50)) 
    pygame.display.update()
    relogio.tick(60)

pygame.quit()
