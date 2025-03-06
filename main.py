# This is made from the documentation of Manim Community
# https://docs.manim.community/en/stable/installation/index.html


from manim import *  # import the Manim Library

# Animating a circle: https://docs.manim.community/en/stable/tutorials/quickstart.html#animating-a-circle


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


# To run the script, use the following command: manim -pql main.py CreateCircle
# -p: preview the animation
# -q: don't show the progress bar
# -l: show the code in the animation
# The animation will look like garbage, so, change settings in the manim.cfg file
