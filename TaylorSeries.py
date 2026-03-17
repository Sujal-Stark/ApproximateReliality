from manim import * 
import numpy as np

class Test1(Scene):
    def construct(self):
        xy_line = Axes(
            x_range = [-2, 5, 1], x_length = 8,
            y_range = [0, 10, 1], y_length = 6,
            axis_config = {
                "include_tip" : True
            }
        ).add_coordinates()

        labels = xy_line.get_axis_labels(
            x_label = MathTex("x"), y_label = MathTex(r"f(x) = e^x")
        )

        graph = xy_line.plot(
            lambda x : np.pow(np.e, x), x_range = [-2, 2], color = RED
        )

        const = xy_line.plot(
            lambda x : 1, x_range = [-2, 2], color = GREEN
        )

        dydx = xy_line.plot(
            lambda x : 1 + x, x_range = [-2, 2], color = GREEN
        )

        d2ydx2 = xy_line.plot(
            lambda x : 1 + x + (x*x)/2, x_range = [-2, 2], color = GREEN
        )

        d3ydx3 = xy_line.plot(
            lambda x : 1 + x + (x*x)/2 + (x**3)/6, x_range = [-2, 2], color = GREEN
        )

        d4ydx4 = xy_line.plot(
            lambda x : 1 + x + (x*x)/2 + (x**3)/6 + (x**4)/24, x_range = [-2, 2], color = GREEN
        )

        d5ydx5 = xy_line.plot(
            lambda x : 1 + x + (x*x)/2 + (x**3)/6 + (x**4)/24 + (x**5)/120, x_range = [-2, 2], color = GREEN
        )

        title_1 = MathTex(r"e^x = 1").scale(0.5).move_to(xy_line.c2p(4, 10)).set_color(WHITE)
        title_2 = MathTex(r" + x").scale(0.5).next_to(title_1, buff = 0.1).set_color(WHITE)
        title_3 = MathTex(r" + \frac{x^2}{2!}").scale(0.5).next_to(title_2, buff = 0.1).set_color(WHITE)
        title_4 = MathTex(r" + \frac{x^3}{3!}").scale(0.5).next_to(title_3, buff = 0.1).set_color(WHITE)
        title_5 = MathTex(r" + \frac{x^4}{4!}").scale(0.5).next_to(title_4, buff = 0.1).set_color(WHITE)
        title_6 = MathTex(r" + \frac{x^5}{5!}").scale(0.5).next_to(title_5, buff = 0.1).set_color(WHITE)

        self.play(Write(xy_line), run_time = 2)
        self.wait()

        self.play(Write(graph), Write(labels), run_time = 2)
        self.wait()

        self.play(Write(const), Write(title_1), run_time = 2)
        self.wait()

        self.play(Transform(const, dydx), Write(title_2), run_time = 2)
        self.wait()

        self.play(Transform(const, d2ydx2), Write(title_3), run_time = 2)
        self.wait()

        self.play(Transform(const, d3ydx3), Write(title_4), run_time = 2)
        self.wait()

        self.play(Transform(const, d4ydx4), Write(title_5), run_time = 2)
        self.wait()

        self.play(Transform(const, d5ydx5), Write(title_6), run_time = 2)
        self.wait(2)
        return super().construct()
    pass