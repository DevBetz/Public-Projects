import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

#### ToDo: ####
# check if the guess is amoung the 50 states
# write the correct guess onto the map
# use a loop to allow the user to keep guessing
# record the correct guesses in a list
# keep track of score/ have an end of game


### For testing where state coor is: ###
# def get_mouse_click_coor(x, y):
#     print(x,y)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()


correct_guesses = []
total_states = 50


while len(correct_guesses) < 50:
    # Ask the user to guess a state
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    # Check if the guessed state is valid and hasn't been guessed before
    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)

        # Find the coordinates of the guessed state
        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        # Create a turtle to mark the guessed state on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

# def checker():
# for answer_state in data:
# move(answer_state x,y)


### Data Stuff that will prob be useful later: ###
### Figure out where this goes later: ###



#print(data.title())

# data[""]
# print(header)


# data_dict = {
  
# }

# df=pd.DataFrame(data_dict)
# df.to_csv("something.csv")

#turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

screen.exitonclick()
