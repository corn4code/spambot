# print("How many years will you be saving?")
# years = int(input("Enter years: "))

# print("How much money is currently on your account?")
# principal = float(input("Enter current amount in account: "))

# print("What are your yearly interests of this investment?")
# interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

# print("How much money do you want to reach?")
# goal = int(input("Enter rounded amount (50.05 --> 50): "))

    
# for i in range(0, goal):
#     invest_yearly = i
#     for i in range(0, years):
#         principal = (principal + invest_yearly) * (1+ interest)
#         if principal == goal:
#            #monthly_invest = invest_yearly / 12
#            break
#         else:
#            continue

# monthly_invest = invest_yearly / 12


# print("You need to invest", monthly_invest, "per month to have a credit of", goal, "after", years, "years.")
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(floor_surface, (0, 0))

    pygame.display.update()
    clock.tick(120)



pygame.quit()