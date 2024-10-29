import pyautogui as pg
import constants
import time
import math
import random
from pynput import keyboard

def eat_food():
    pg.press('p')
    #print('Comendo food...')

def check_status(name, delay, x, y, rgb, button_name):
    #print(f'checando {name}... ')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button_name)

def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG', region=constants.REGION_BATTLE)

def get_loot():
    pg.press('y')

def check_followmode():
    return pg.locateOnScreen('imgs/follow_mode.PNG', region=constants.REGION_FOLLOW_MODE)

def tempo_movimento_aleatorio():
    return(random.uniform(0.1, 0.3))

def change_followmode():
    followmode = pg.locateOnScreen('imgs/disabled_follow_mode.PNG', confidence=0.8, region=constants.REGION_HABILITAR_FOLLOW_MODE)
    if followmode:
        x, y = pg.center(followmode)
        pg.moveTo(x, y, duration=0.05)  # Mover rapidamente
        pg.leftClick()

def check_player_position():
    return pg.locateOnScreen('imgs/point_player.png', confidence=0.7, region=constants.REGION_MAP)


def humanized_move(x, y, duration):
    # Pega a posição inicial
    start_x, start_y = pg.position()

    # Calcula a distância total
    total_distance = math.sqrt((x - start_x)**2 + (y - start_y)**2)
    
    # Número de etapas (mais etapas tornam o movimento mais suave)
    steps = 10

    # Cria uma curva de aceleração e desaceleração (ease-in, ease-out)
    for i in range(steps):
        # Calcula a fração do movimento (0 a 1)
        t = i / steps
        
        # Aplicar função de suavização (t^3 para suavizar o início e o fim)
        t_smooth = t ** 3 * (t * (6 * t - 15) + 10)  # Ease-in-out

        # Calcula a posição intermediária
        current_x = start_x + (x - start_x) * t_smooth
        current_y = start_y + (y - start_y) * t_smooth

        # Move o mouse para a posição intermediária
        pg.moveTo(current_x, current_y)

        # Introduz uma pequena pausa para suavizar o movimento
        time.sleep((duration / steps) * random.uniform(0.1, 0.2))

    # Garante que o mouse vá exatamente para o ponto final
    pg.moveTo(x, y)


#while True:
#    print(pg.locateOnScreen('imgs/disabled_follow_mode.PNG'))