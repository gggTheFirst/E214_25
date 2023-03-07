import random 
import pygame
import sys
import time
import highscore_info
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beyond Atmosphere!")

def run():
    x = 1

def main_menu():
    playing = True          #while this is true game will run

    title_font = pygame.font.SysFont("comicsans", 40)
    title = title_font.render("Beyond Atmosphere!", 1, (255,255,255))    

    WINDOW.blit(title, (WIDTH/2 - title.get_width()/2, 20))

    #Display high schores on the screen
    highscore_heading_font = pygame.font.SysFont("comicsans", 20)
    highscore_heading = highscore_heading_font.render('Highscores:', 1, (255,255,255))   
    WINDOW.blit(highscore_heading, (20, 80))

    
    highscore_font = pygame.font.SysFont("comicsans", 15)
    highscores = highscore_info.get_highscores()
    highscores = [['User 20','User 12','User 53','User 14','User 65' ],[4450650, 1320020, 322000, 752000, 15000]]
    highscore_info.save_highscores(highscores)

    for i in range(5):
        person_score = highscores[0][i] + ' - ' +  str(highscores[1][i])
        person_score = highscore_font.render(person_score, 1, (255,255,255))   
        WINDOW.blit(person_score, (20, i * 20 + 110))
    

    play_heading_font = pygame.font.SysFont("comicsans", 35)
    play_instructions_text = "Press 'spacebar' to stat playing!"
    play_instructions = play_heading_font.render(play_instructions_text, 1, (255,255,255))   
    WINDOW.blit(play_instructions, (WIDTH/2 - play_instructions.get_width()/2, 210))

    username_text_font = pygame.font.SysFont("comicsans", 25)
    username_text = "Enter username:"
    username_text_label= username_text_font.render(username_text, 1, (255,255,255))   
    WINDOW.blit(username_text_label, (WIDTH/2 - play_instructions.get_width()/2, 280))
        
    pygame.display.update()

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run()
    pygame.quit()

main_menu()