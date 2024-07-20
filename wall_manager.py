from turtle import Turtle
import random


class WallManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def generate_random_list(self, total, num_elements, max_diff, max_value_limit, min_value=100):
        while True:
            try:
                if total < num_elements:
                    raise ValueError("Total must be at least as large as the number of elements.")

                values = []
                remaining = total

                min_value = max(min_value, (total - (num_elements - 1) * max_diff) // num_elements)
                if min_value * num_elements > total:
                    raise ValueError("Cannot create valid random values with given total and number of elements.")

                first_value = min_value
                values.append(first_value)
                remaining -= first_value

                for i in range(1, num_elements - 1):
                    min_value = max(min_value, values[-1] - max_diff)
                    max_value = min(remaining - (num_elements - len(values) - 1), values[-1] + max_diff,
                                    max_value_limit)
                    if max_value < min_value:
                        raise ValueError("Cannot create valid random values with given total and number of elements.")

                    value = random.randint(min_value, max_value)
                    values.append(value)
                    remaining -= value

                values.append(remaining)
                if any(value > max_value_limit for value in values):
                    raise ValueError("Generated values exceed the maximum limit.")

                if remaining < min_value:
                    raise ValueError("Remaining value is less than the minimum value.")

                random.shuffle(values)
                print(f"List values: {values}")
                return values

            except ValueError as e:
                print(f"Error encountered: {e}. Retrying...")

    # Space between each brick
    def create_wall_row(self, y_pos, color_list, size_list, space=3):
        walls = []
        current_x = - self.screen_width / 2
        for size in size_list:
            new_wall = Turtle("square")
            new_wall.shapesize(stretch_wid=90 / 20, stretch_len=size / 20)
            new_wall.penup()
            new_wall.color(random.choice(color_list) if isinstance(color_list, list) else color_list)
            new_wall.goto(current_x + size / 2, y_pos)
            current_x += size + space
            walls.append(new_wall)
        return walls

    def create_all_walls(self):
        NUM_ELEMENTS = 11
        TOTAL = 1600

        COLOR_ROW1 = ["#D6EFD8", "#80AF81", "#508D4E", "#1A5319"]
        COLOR_ROW2 = "#2C3333"
        COLOR_ROW3 = ["#0A2647", "#144272", "#205295", "#2C74B3"]
        COLOR_ROW4 = ['#C40C0C', '#FF6500', '#FF8A08', '#FFC100']

        WALL1 = self.generate_random_list(TOTAL, NUM_ELEMENTS, 20, 300)
        WALL2 = [214, 139, 116, 150, 140, 146, 132, 142, 130, 145, 146]

        walls = self.create_wall_row(90, COLOR_ROW1, WALL1)
        second_walls = self.create_wall_row(190, COLOR_ROW2, WALL2)
        third_walls = self.create_wall_row(290, COLOR_ROW3, random.sample(WALL2, len(WALL2)))
        fourth_walls = self.create_wall_row(390, COLOR_ROW4, random.sample(WALL1, len(WALL1)))

        all_walls = walls + second_walls + third_walls + fourth_walls
        return all_walls
