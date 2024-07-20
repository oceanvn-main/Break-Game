# Wall settings
# NUM_ELEMENTS = 11
# Y = 90
# Y2 = 190
# Y3 = 290
# Y4 = 390
#
# #Four walls
# COLOR_ROW1 = ["#D6EFD8", "#80AF81", "#508D4E", "#1A5319"]
# COLOR_ROW2 = "#2C3333"
# COLOR_ROW3 = ["#0A2647", "#144272", "#205295", "#2C74B3"]
# COLOR_ROW4 = ['#C40C0C', '#FF6500', '#FF8A08', '#FFC100']
#
# SPACE = 3
# TOTAL = 1600
# ball = Ball()
#
#
# #Get random list for shape of walls
# def generate_random_list(total, num_elements, max_diff, max_value_limit):
#     while True:
#         try:
#             if total < num_elements:
#                 raise ValueError("Total must be at least as large as the number of elements.")
#
#             values = []
#             remaining = total
#
#             # Đảm bảo có ít nhất giá trị tối thiểu cho mỗi phần tử
#             min_value = max(50, (total - (num_elements - 1) * max_diff) // num_elements)
#             if min_value * num_elements > total:
#                 raise ValueError("Cannot create valid random values with given total and number of elements.")
#
#             # Khởi tạo giá trị đầu tiên
#             first_value = min_value
#             values.append(first_value)
#             remaining -= first_value
#
#             for i in range(1, num_elements - 1):
#                 # Xác định min_value và max_value cho phần tử tiếp theo
#                 min_value = max(50, values[-1] - max_diff)
#                 max_value = min(remaining - (num_elements - len(values) - 1), values[-1] + max_diff, max_value_limit)
#                 if max_value < min_value:
#                     raise ValueError("Cannot create valid random values with given total and number of elements.")
#
#                 value = random.randint(min_value, max_value)
#                 values.append(value)
#                 remaining -= value
#
#             values.append(remaining)
#             if any(value > max_value_limit for value in values):
#                 raise ValueError("Generated values exceed the maximum limit.")
#
#             random.shuffle(values)
#             print(values)
#             return values
#
#         except ValueError as e:
#             print(f"Error encountered: {e}. Retrying...")
#
#
#
# def create_wall_row(y_pos, color_list, size_list):
#     walls = []
#     current_x = - 800
#     for size in size_list:
#         new_wall = turtle.Turtle("square")
#         new_wall.shapesize(stretch_wid=Y / 20, stretch_len=size / 20)
#         new_wall.penup()
#         new_wall.color(random.choice(color_list) if isinstance(color_list, list) else color_list)
#         new_wall.goto(current_x + size / 2, y_pos)
#         current_x += size + SPACE
#         walls.append(new_wall)
#     return walls
#
#
# WALL1 = generate_random_list(TOTAL, NUM_ELEMENTS, 20, 300)
# walls = create_wall_row(Y, COLOR_ROW1, WALL1)
#
# WALL2 = [214, 139, 116, 150, 140, 146, 132, 142, 130, 145, 146]
# second_walls = create_wall_row(Y2, COLOR_ROW2, WALL2)
#
# WALL3 = random.sample(WALL2, len(WALL2))
# third_walls = create_wall_row(Y3, COLOR_ROW3, WALL3)
#
# WALL4 = random.sample(WALL1, len(WALL1))
# fourth_walls = create_wall_row(Y4, COLOR_ROW4, WALL4)
#
# # All walls
# all_walls = walls + second_walls + third_walls + fourth_walls
#
# #Create paddle
#
# position = (-200,-430)
# paddle = Paddle(position)
#
#
# def check_collision_with_paddle(ball, paddle):
#
#     ball_radius = 10
#     ball_left = ball.xcor() - ball_radius
#     ball_right = ball.xcor() + ball_radius
#     ball_top = ball.ycor() + ball_radius
#     ball_bottom = ball.ycor() - ball_radius
#
#     paddle_width = paddle.shapesize()[1] * 20
#     paddle_height = paddle.shapesize()[0] * 20
#     paddle_left = paddle.xcor() - paddle_width / 2
#     paddle_right = paddle.xcor() + paddle_width / 2
#     paddle_top = paddle.ycor() + paddle_height / 2
#     paddle_bottom = paddle.ycor() - paddle_height / 2
#
#     if paddle_left < ball_right and ball_left < paddle_right and paddle_bottom < ball_top and ball_bottom < paddle_top:
#         hit_position = (ball.xcor() - paddle.xcor()) / (paddle_width / 2)
#         angle = hit_position * 45
#         ball.setheading(180 - angle)
#         return True
#     return False
#
#
#
#
# def check_collision_with_wall(ball, wall):
#     ball_left = ball.xcor() - 10
#     ball_right = ball.xcor() + 10
#     ball_top = ball.ycor() + 10
#     ball_bottom = ball.ycor() - 10
#
#     wall_left = wall.xcor() - wall.shapesize()[1] * 10
#     wall_right = wall.xcor() + wall.shapesize()[1] * 10
#     wall_top = wall.ycor() + wall.shapesize()[0] * 10
#     wall_bottom = wall.ycor() - wall.shapesize()[0] * 10
#
#     if wall_left < ball_right < wall_right and wall_bottom < ball_top < wall_top:
#         return True
#     if wall_left < ball_left < wall_right and wall_bottom < ball_bottom < wall_top:
#         return True
#     return False
#
#
# is_game_on = True
# while is_game_on:
#     screen.update()
#     ball.move()
#     screen.listen()
#     screen.onkey(paddle.move_right, "d")
#     screen.onkey(paddle.move_left, "a")
#     time.sleep(0.01)
#     #Detect ball over the wall
#     if ball.ycor() < -440:
#         ball.reset_position()
#         # Detect collision with walls1
#     if ball.ycor() > 450:
#         ball.bounce_y()
#
#     for wall in all_walls:
#         if check_collision_with_wall(ball, wall):
#             ball.bounce_y()
#             wall.hideturtle()
#             all_walls.remove(wall)
#             score.point()
#
#
#
#
#         # Detect collision with paddle
#     if check_collision_with_paddle(ball, paddle):
#         ball.bounce_y()
#
#     #Detect collision with right or left
#     if ball.xcor() < -780 or ball.xcor() > 780:
#         ball.bounce_x()
#
#         #Detect  paddale misses
#     if ball.ycor() < -430:
#         ball.reset_position()
#
#     if len(all_walls) == 0:
#         score.game_over()
#         is_game_on = False


# screen.update()
# screen.mainloop()

