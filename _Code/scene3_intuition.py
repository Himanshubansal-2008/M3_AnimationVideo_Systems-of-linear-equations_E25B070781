"""
_Code/scene3_intuition.py
Scene 3: Geometric Intuition : The Row Picture vs The Column Picture
Duration: 60.0 seconds (1:30 - 2:30)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene3Intuition(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Top Chapter Banner (1.0s)
        # ----------------------------------------------------
        top_bar = create_top_banner(3, 6, "Geometric Intuition : Row Picture vs Column Picture", "1:30 - 2:30")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total: 1.0s

        # ----------------------------------------------------
        # Part 1: The Row Picture (Geometry of Intersecting Lines) (27.0s)
        # ----------------------------------------------------
        # Setup coordinate plane on the left
        plane = NumberPlane(
            x_range=[-1, 5.5, 1],
            y_range=[-1, 6.5, 1],
            x_length=6.0,
            y_length=5.0,
            background_line_style={"stroke_color": "#1e293b", "stroke_width": 1.5, "stroke_opacity": 0.8},
            axis_config={"color": TEXT_MUTED, "stroke_width": 2}
        ).shift(LEFT * 3.2 + DOWN * 0.3)

        # Coordinate axes labels with pure Text
        x_lbl = Text("x₁", font_size=16, color=TEXT_MUTED).next_to(plane.get_x_axis().get_end(), RIGHT, buff=0.15)
        y_lbl = Text("x₂", font_size=16, color=TEXT_MUTED).next_to(plane.get_y_axis().get_end(), LEFT, buff=0.2)

        # Grid tick number labels
        tick_nums = VGroup()
        for x_val in [1, 2, 3, 4, 5]:
            t = Text(str(x_val), font_size=12, color=TEXT_MUTED).next_to(plane.c2p(x_val, 0), DOWN, buff=0.1)
            tick_nums.add(t)
        for y_val in [1, 2, 3, 4, 5, 6]:
            t = Text(str(y_val), font_size=12, color=TEXT_MUTED).next_to(plane.c2p(0, y_val), LEFT, buff=0.1)
            tick_nums.add(t)

        row_header = Text("Part A : The Row Picture (Intersecting Constraints)", font_size=17, weight=BOLD, color=ACCENT_CYAN).next_to(plane, UP, buff=0.35)

        self.play(Create(plane), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(tick_nums), FadeIn(row_header), run_time=3.0)
        # Total: 4.0s

        # Line 1: 2x₁ - x₂ = 1  => x₂ = 2x₁ - 1
        p1_start = plane.c2p(0, -1)
        p1_end = plane.c2p(3.5, 6)
        line1 = Line(p1_start, p1_end, color=ACCENT_CYAN, stroke_width=3.5)
        label1 = Text("L₁: 2x₁ - x₂ = 1", font_size=14, weight=BOLD, color=ACCENT_CYAN).next_to(line1.point_from_proportion(0.8), RIGHT, buff=0.1)

        self.play(Create(line1), FadeIn(label1), run_time=4.0)
        # Total: 8.0s

        # Line 2: x₁ + x₂ = 5  => x₂ = 5 - x₁
        p2_start = plane.c2p(-0.5, 5.5)
        p2_end = plane.c2p(5.2, -0.2)
        line2 = Line(p2_start, p2_end, color=ACCENT_YELLOW, stroke_width=3.5)
        label2 = Text("L₂: x₁ + x₂ = 5", font_size=14, weight=BOLD, color=ACCENT_YELLOW).next_to(line2.point_from_proportion(0.2), UR, buff=0.1)

        self.play(Create(line2), FadeIn(label2), run_time=4.0)
        # Total: 12.0s

        # Intersection point at (2, 3)
        inter_pt = plane.c2p(2, 3)
        inter_dot = Dot(inter_pt, radius=0.1, color=ACCENT_ORANGE)
        inter_glow = Circle(radius=0.25, color=ACCENT_ORANGE, stroke_width=2).move_to(inter_pt)

        # Dashed projections to axes
        proj_x = DashedLine(inter_pt, plane.c2p(2, 0), color=TEXT_MUTED, stroke_width=1.5)
        proj_y = DashedLine(inter_pt, plane.c2p(0, 3), color=TEXT_MUTED, stroke_width=1.5)

        inter_badge = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.5, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=ACCENT_ORANGE, stroke_width=1.5).next_to(inter_pt, UR, buff=0.2)
        inter_text = Text("Solution: (2, 3)", font_size=14, weight=BOLD, color=TEXT_WHITE).move_to(inter_badge)

        self.play(
            FadeIn(inter_dot), Create(inter_glow),
            Create(proj_x), Create(proj_y),
            FadeIn(inter_badge), Write(inter_text),
            run_time=4.0
        )
        # Total: 16.0s

        # Row perspective summary card on the right
        row_card = make_card(
            "Row Picture Mechanics",
            [
                "• Each equation represents a line (hyperplane)",
                "• Line 1: all (x₁, x₂) where 2x₁ - x₂ = 1",
                "• Line 2: all (x₁, x₂) where x₁ + x₂ = 5",
                "• Solution = Intersection of all lines",
                "• Here lines meet at exactly ONE point (2, 3)",
                "• In 3D: Planes intersecting at a point",
                "• In nD: n hyperplanes intersecting"
            ],
            width=5.8,
            height=4.6,
            border_color=ACCENT_CYAN
        ).shift(RIGHT * 3.4 + DOWN * 0.3)

        self.play(FadeIn(row_card, shift=LEFT * 0.3), run_time=2.0)
        # Total: 18.0s
        self.wait(10.0)  # Voiceover window for row picture
        # Total: 28.0s

        # ----------------------------------------------------
        # Part 2: The Column Picture (Linear Combinations) (30.0s)
        # ----------------------------------------------------
        # Transition out row specific elements
        self.play(
            FadeOut(line1), FadeOut(label1),
            FadeOut(line2), FadeOut(label2),
            FadeOut(inter_dot), FadeOut(inter_glow),
            FadeOut(proj_x), FadeOut(proj_y),
            FadeOut(inter_badge), FadeOut(inter_text),
            FadeOut(row_card), FadeOut(row_header),
            run_time=3.0
        )
        # Total: 31.0s

        col_header = Text("Part B : The Column Picture (Linear Combination of Vectors)", font_size=17, weight=BOLD, color=ACCENT_GREEN).next_to(plane, UP, buff=0.35)
        self.play(FadeIn(col_header), run_time=0.5)
        # Total: 31.5s

        # Column vectors a1 = [2, 1]^T, a2 = [-1, 1]^T
        origin = plane.c2p(0, 0)
        vec_a1 = Arrow(origin, plane.c2p(2, 1), buff=0, color=ACCENT_GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        lbl_a1 = Text("a₁ = [2, 1]ᵀ", font_size=14, weight=BOLD, color=ACCENT_GREEN).next_to(vec_a1.get_end(), DR, buff=0.1)

        vec_a2 = Arrow(origin, plane.c2p(-1, 1), buff=0, color=ACCENT_PURPLE, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        lbl_a2 = Text("a₂ = [-1, 1]ᵀ", font_size=14, weight=BOLD, color=ACCENT_PURPLE).next_to(vec_a2.get_end(), UL, buff=0.1)

        self.play(GrowArrow(vec_a1), Write(lbl_a1), GrowArrow(vec_a2), Write(lbl_a2), run_time=3.5)
        # Total: 35.0s

        # Scale a1 by x1 = 2 => 2*a1 = [4, 2]
        scaled_a1 = Arrow(origin, plane.c2p(4, 2), buff=0, color=ACCENT_GREEN, stroke_width=5, max_tip_length_to_length_ratio=0.15)
        lbl_scaled_a1 = Text("2 a₁ = [4, 2]ᵀ", font_size=14, weight=BOLD, color=ACCENT_GREEN).next_to(scaled_a1.get_end(), DR, buff=0.1)

        self.play(Transform(vec_a1, scaled_a1), Transform(lbl_a1, lbl_scaled_a1), run_time=4.0)
        # Total: 39.0s

        # Add 3*a2 = [-3, 3] head-to-tail from (4, 2) to (1, 5)
        pt_42 = plane.c2p(4, 2)
        pt_15 = plane.c2p(1, 5)
        vec_3a2 = Arrow(pt_42, pt_15, buff=0, color=ACCENT_PURPLE, stroke_width=5, max_tip_length_to_length_ratio=0.15)
        lbl_3a2 = Text("+ 3 a₂ = [-3, 3]ᵀ", font_size=14, weight=BOLD, color=ACCENT_PURPLE).next_to(vec_3a2.get_center(), UR, buff=0.1)

        self.play(GrowArrow(vec_3a2), Write(lbl_3a2), run_time=4.0)
        # Total: 43.0s

        # Draw Target Vector b = [1, 5]^T from origin to (1, 5)
        vec_b = Arrow(origin, pt_15, buff=0, color=ACCENT_YELLOW, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        lbl_b = Text("b = [1, 5]ᵀ", font_size=16, weight=BOLD, color=ACCENT_YELLOW).next_to(vec_b.get_end(), UP, buff=0.15)

        # Target reached indicator
        target_dot = Dot(pt_15, radius=0.12, color=ACCENT_YELLOW)
        target_circle = Circle(radius=0.28, color=ACCENT_YELLOW, stroke_width=2.5).move_to(pt_15)

        # Column card on right
        col_card = make_card(
            "Column Picture Mechanics",
            [
                "• Equation rewritten as vector combination:",
                "    x₁ a₁ + x₂ a₂ = b",
                "• x₁ = 2 stretches column a₁ to [4, 2]ᵀ",
                "• x₂ = 3 stretches column a₂ to [-3, 3]ᵀ",
                "• Head-to-tail sum reaches [1, 5]ᵀ exactly!",
                "• Solution exists because b is in Col(A)",
                "• Column space covers the entire ℝ² plane"
            ],
            width=5.8,
            height=4.6,
            border_color=ACCENT_GREEN
        ).shift(RIGHT * 3.4 + DOWN * 0.3)

        self.play(
            GrowArrow(vec_b), Write(lbl_b),
            FadeIn(target_dot), Create(target_circle),
            FadeIn(col_card, shift=LEFT * 0.3),
            run_time=4.0
        )
        # Total: 47.0s
        self.wait(11.0)  # Voiceover explanation
        # Total: 58.0s

        # Fade out
        self.play(
            FadeOut(plane), FadeOut(x_lbl), FadeOut(y_lbl), FadeOut(tick_nums),
            FadeOut(col_header), FadeOut(vec_a1), FadeOut(lbl_a1),
            FadeOut(vec_a2), FadeOut(lbl_a2), FadeOut(vec_3a2), FadeOut(lbl_3a2),
            FadeOut(vec_b), FadeOut(lbl_b), FadeOut(target_dot), FadeOut(target_circle),
            FadeOut(col_card), FadeOut(top_bar),
            run_time=2.0
        )
        # Total: 60.0s
