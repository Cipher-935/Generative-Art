from class_triangle import Triangle
import random


class PaintObjects:

    def __init__(self, no_triangles_per_pop, horizontal_width, vertical_height, main_filtered_image, main_canvas_paper):
        self.no_triangles_per_pop = no_triangles_per_pop
        self.horizontal_width = horizontal_width
        self.vertical_height = vertical_height
        self.main_filtered_image = main_filtered_image
        self.main_canvas_paper = main_canvas_paper
        self.triangles = []
        for _ in range(self.no_triangles_per_pop):
            t = Triangle(horizontal_width, vertical_height)
            self.triangles.append(t)

    def euclidean_color_distance(self, first, second):
        red_difference = (first[0] - second[0]) ** 2
        blue_difference = (first[1] - second[1]) ** 2
        green_difference = (first[2] - second[2]) ** 2
        return red_difference + blue_difference + green_difference


    def r_mutation(self):
        triangle_pick = random.randint(0, self.no_triangles_per_pop - 1)  # This will help to pick random triangle from the triangles list
        if random.random() < 0.5:
            # This block will take care of the color mutation accross four channels
            color_index = random.randint(0, 3)
            color_change = random.randint(0, 255)
            if color_index == 3:
                self.triangles[triangle_pick].transparent_factor = color_change
            else:
                selected_c_list = list(self.triangles[triangle_pick].triangle_color)
                selected_c_list[color_index] = color_change
                self.triangles[triangle_pick].triangle_color = tuple(selected_c_list)

        else:
            # This block is responsible for positional mutation
            pos_index = random.randint(0, 2)
            vertex_1 = self.triangles[triangle_pick].vertices[0]
            vertex_2 = self.triangles[triangle_pick].vertices[1]
            vertex_3 = self.triangles[triangle_pick].vertices[2]
            horizontal_change = random.randint(0, self.horizontal_width)  # New X coordinate
            vertical_change = random.randint(0, self.vertical_height)  # New Y coordinate
            position_change = [vertex_1, vertex_2, vertex_3]
            position_change[pos_index] = (horizontal_change, vertical_change)
            self.triangles[triangle_pick].vertices = position_change

    def fit_calc(self):
        # Calculate difference in color intensity using euclidean technique
        pixel_color_difference = 0
        for x in range(self.horizontal_width):
            for y in range(self.vertical_height):
                pixel_color_difference += self.euclidean_color_distance(self.main_filtered_image.getpixel((x, y)), self.main_canvas_paper.get_at((x, y))[:3])
        self.fitness = pixel_color_difference

    def t_cross(self):
        color_crossover = random.randint(0, 2)
        random_partner_1 = random.randint(0, self.no_triangles_per_pop-1)
        random_partner_2 = random.randint(0, self.no_triangles_per_pop - 1)
        self.triangles[random_partner_1].triangle_color[color_crossover] = self.triangles[random_partner_2].triangle_color[color_crossover]
        self.triangles[random_partner_1].transparent_factor = self.triangles[random_partner_2].transparent_factor



