import random
from PIL import Image
import sys
import pygame as displayer
from pygame.locals import *
from class_drawer import PaintObjects
import pygame.gfxdraw as gfx
from skimage import io, filters, util

def pre_proc(img_name):
    my_img = io.imread(img_name)
    g_filter = filters.gaussian(my_img)
    sharpened = filters.unsharp_mask(g_filter, radius=2, amount=3)
    reformatted = util.img_as_ubyte(sharpened)
    io.imsave(f"filtered_{img_name}", reformatted)
    return f"filtered_{img_name}"

def main_loop(main_filtered_image, horizontal_width, vertical_height, main_canvas_paper, no_triangles_per_pop, total_population):

    with open("func_1.txt", "r") as f1:
        template_function = f1.read()

    with open("func_2.txt", "r") as f2:
        final_function = f2.read()

    def best_fit(painting):    # Function to return the fitness of the provided object
        return painting.fitness

    main_population = []      # list to hold the paint objects or the population

    for _ in range(total_population):
        # Creating and appending triangle paintings to the main population list as per the count provided
        main_population.append(PaintObjects(no_triangles_per_pop, horizontal_width, vertical_height, main_filtered_image, main_canvas_paper))

    counter_for_generation = 0  # Iteration tracker

    difference_track = []  # Keeps track of the closeness of the art to the image

    print("Starting the generation...")

    with open("dynamic.txt", "r") as j:
        j_dat = j.read()
    exec(j_dat)             # Dynamic execution for fast performance

def caller(f_name):
    main_filtered_image = Image.open(f_name)

    horizontal_width = main_filtered_image.size[0]
    vertical_height = main_filtered_image.size[1]

    displayer.init()
    main_canvas_paper = displayer.display.set_mode((horizontal_width, vertical_height))
    displayer.display.set_caption(f"Generating art for: {f_name}")

    no_triangles_per_pop = int(input("Enter how many triangles you want per painting(40-60 is a good range): "))
    main_canvas_paper.fill((255, 255, 255, 255))
    main_loop(main_filtered_image, horizontal_width, vertical_height,main_canvas_paper, no_triangles_per_pop, 6)

def menu():
    print("1. bird1.jpg")
    print("2. bird2.jpg")
    print("3. tom_n_jerry.jpg")
    u_in = int(input("Provide the image number to generate art of: "))
    p_choice = input("Enter Y for processing or N to proceed normally, if the image is too noisy or complex, it will improve it a bit: ")
    if u_in == 1:
        if p_choice == "Y":
            dat = pre_proc("bird1.jpg")
            caller(dat)
        else:
            caller("bird1.jpg")
    elif u_in == 2:
        if p_choice == "Y":
            dat = pre_proc("bird2.jpg")
            caller(dat)
        else:
            caller("bird2.jpg")
    elif u_in == 3:
        if p_choice == "Y":
            dat = pre_proc("tom_n_jerry.jpg")
            caller(dat)
        else:
            caller("tom_n_jerry.jpg")
menu()