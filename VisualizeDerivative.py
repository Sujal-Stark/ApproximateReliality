from manim import * # type: ignore
import numpy as np
import math

class RoughDerivative(Scene):
    @staticmethod
    def target_func(x : float) -> float:
        # Function definition. A user can write any differentiable function
        # to proceed with animation.
        return x*x*x
    
    @staticmethod
    def grad_line(x : float, a : float) -> float:
        # Calculation of Tangent Line at x coordinate.
        graident = RoughDerivative.grad(a) # m
        y_0 = RoughDerivative.target_func(a) # c
        return graident * (x - a) + y_0 # y = m*(x-a) + c
    
    @staticmethod
    def grad(a : float) -> float:
        # calculation of derivative with definition.
        del_x : float = 0.000001 # play around with this value for accuracy.
        y2 : float = RoughDerivative.target_func(a + del_x)
        y1 : float = RoughDerivative.target_func(a - del_x)
        del_y = y2 - y1

        return del_y/(2 * del_x) # dy/dx
    
    def construct(self) -> None:
        left_start = -5;
        right_start = 5;
        xy_plane = NumberPlane(
            x_range = [left_start- 1, right_start + 1, 1], x_length = 14,
            y_range = [-160, 160, 50], y_length = 8,
            axis_config = {
                "include_tip" : True
            }
        ).add_coordinates()

        x_tracker = ValueTracker(left_start)

        main_graph = xy_plane.plot(
            lambda x : RoughDerivative.target_func(x),
            x_range = [left_start, right_start], color = GREEN
        )

        # shows where we are getting tangent.
        tangentialDot = always_redraw(
            lambda : Dot(
                radius = 0.05, color = WHITE
            ).shift(xy_plane.c2p(x_tracker.get_value(), RoughDerivative.target_func(x_tracker.get_value())))
        )

        # the tangent line
        tangentArc = always_redraw(
            lambda : xy_plane.plot(
                lambda x : RoughDerivative.grad_line(x, x_tracker.get_value()),
                x_range = [x_tracker.get_value() - 1, x_tracker.get_value() + 1], color = RED
            )
        )

        # the curve plotted with (x, dydx)
        derivative = always_redraw(
            lambda : xy_plane.plot(
                RoughDerivative.grad, x_range = [left_start, x_tracker.get_value()], color = YELLOW
            )
        )

        # Shows current grad value.
        grad_value = always_redraw(
            lambda : MathTex(
                r"\frac{dy}{dx} = " + f"{RoughDerivative.grad(x_tracker.get_value()):.2f}"
            ).move_to(xy_plane.c2p(-3, 100)).set_color(YELLOW)
        )

        self.play(Write(xy_plane))
        self.wait()

        self.play(Create(main_graph))
        self.wait()

        self.play(Write(tangentArc), Create(tangentialDot), Write(grad_value)) # type: ignore
        self.wait()

        self.add(derivative)

        self.play(x_tracker.animate.set_value(right_start), run_time = 2)
        self.wait(2)
        return super().construct()
    pass