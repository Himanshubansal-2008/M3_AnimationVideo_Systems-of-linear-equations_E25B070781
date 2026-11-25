"""
_Code/scene2_concept.py
Scene 2: Concept Introduction : Formulating Ax = b
Duration: 45.0 seconds (0:45 - 1:30)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene2Concept(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Top Chapter Banner (1.0s)
        # ----------------------------------------------------
        top_bar = create_top_banner(2, 6, "Concept Introduction : Formulating A x = b", "0:45 - 1:30")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total: 1.0s

        # ----------------------------------------------------
        # Part 1: From Simultaneous Equations to Matrix Form (2.0s + 7.0s = 9.0s)
        # ----------------------------------------------------
        intro_text = Text(
            "Consider a classical system of 2 linear equations with 2 unknowns:",
            font_size=20,
            color=TEXT_MUTED
        ).shift(UP * 2.3)

        eq1 = Text("Equation 1 :    2 x₁  -   x₂   =   1", font_size=24, color=ACCENT_CYAN)
        eq2 = Text("Equation 2 :      x₁  +   x₂   =   5", font_size=24, color=ACCENT_YELLOW)
        eq_group = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(UP * 1.1)

        eq_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.5,
            height=1.8,
            fill_color=CARD_BG,
            fill_opacity=0.8,
            stroke_color=CARD_BORDER,
            stroke_width=1.5
        ).move_to(eq_group)

        self.play(FadeIn(intro_text), FadeIn(eq_box), FadeIn(eq_group), run_time=2.0)
        # Total: 3.0s
        self.wait(7.0)
        # Total: 10.0s

        # ----------------------------------------------------
        # Part 2: Factoring into A x = b (2.0s + 13.0s = 15.0s)
        # ----------------------------------------------------
        factor_intro = Text(
            "Factor the coefficients, variables, and constants into vectors & matrices:",
            font_size=20,
            weight=BOLD,
            color=TEXT_WHITE
        ).shift(DOWN * 0.3)

        # Matrix A
        mat_A = make_matrix_mobject([[2, -1], [1, 1]], bracket_color=PRIMARY_BLUE, font_size=26, h_buff=0.8, v_buff=0.6)
        label_A = Text("A  (2×2)", font_size=18, weight=BOLD, color=PRIMARY_BLUE).next_to(mat_A, DOWN, buff=0.25)
        desc_A = Text("Coefficient Matrix", font_size=14, color=TEXT_MUTED).next_to(label_A, DOWN, buff=0.1)
        group_A = VGroup(mat_A, label_A, desc_A)

        # Unknown vector x
        vec_x = make_matrix_mobject([["x₁"], ["x₂"]], bracket_color=ACCENT_YELLOW, font_size=26, v_buff=0.6)
        label_x = Text("x  (2×1)", font_size=18, weight=BOLD, color=ACCENT_YELLOW).next_to(vec_x, DOWN, buff=0.25)
        desc_x = Text("Unknown State", font_size=14, color=TEXT_MUTED).next_to(label_x, DOWN, buff=0.1)
        group_x = VGroup(vec_x, label_x, desc_x)

        # Equals sign
        eq_sign = Text("=", font_size=32, color=TEXT_WHITE)

        # Target vector b
        vec_b = make_matrix_mobject([[1], [5]], bracket_color=ACCENT_GREEN, font_size=26, v_buff=0.6)
        label_b = Text("b  (2×1)", font_size=18, weight=BOLD, color=ACCENT_GREEN).next_to(vec_b, DOWN, buff=0.25)
        desc_b = Text("Constraint Vector", font_size=14, color=TEXT_MUTED).next_to(label_b, DOWN, buff=0.1)
        group_b = VGroup(vec_b, label_b, desc_b)

        # Arrange the entire equation
        matrix_equation = VGroup(group_A, group_x, eq_sign, group_b).arrange(RIGHT, buff=0.45).shift(DOWN * 1.8)

        self.play(FadeIn(factor_intro), FadeIn(matrix_equation, shift=UP * 0.3), run_time=2.0)
        # Total: 12.0s
        self.wait(13.0)  # Voiceover explains A, x, b
        # Total: 25.0s

        # ----------------------------------------------------
        # Part 3: Row View vs Column View Foundations (2.0s + 16.0s + 2.0s = 20.0s)
        # ----------------------------------------------------
        self.play(
            FadeOut(intro_text), FadeOut(eq_box), FadeOut(eq_group),
            FadeOut(factor_intro), FadeOut(matrix_equation),
            run_time=1.5
        )
        # Total: 26.5s

        sub_dual = Text(
            "Two Dual Perspectives on Matrix-Vector Multiplication:",
            font_size=22,
            weight=BOLD,
            color=ACCENT_CYAN
        ).shift(UP * 2.1)
        self.play(FadeIn(sub_dual), run_time=0.5)
        # Total: 27.0s

        # Row perspective card
        card_row = make_card(
            "Row Perspective (Dot Product)",
            [
                "• Each row is a linear equation constraint",
                "• Row 1 • x = 2x₁ - x₂ = 1",
                "• Row 2 • x =  x₁ + x₂ = 5",
                "• Hyperplanes meeting in space",
                "• Finding the common intersection point"
            ],
            width=5.8,
            height=3.4,
            border_color=ACCENT_CYAN
        ).shift(LEFT * 3.3 + DOWN * 0.3)

        # Column perspective card
        card_col = make_card(
            "Column Perspective (Vector Combo)",
            [
                "• Each column is a basis direction vector",
                "• x₁ [2, 1]ᵀ + x₂ [-1, 1]ᵀ = [1, 5]ᵀ",
                "• Linear combination of column vectors",
                "• Synthesizing target vector b",
                "• Solvable if and only if b ∈ Col(A)"
            ],
            width=5.8,
            height=3.4,
            border_color=ACCENT_GREEN
        ).shift(RIGHT * 3.3 + DOWN * 0.3)

        self.play(FadeIn(card_row, shift=LEFT * 0.3), FadeIn(card_col, shift=RIGHT * 0.3), run_time=2.0)
        # Total: 29.0s
        self.wait(14.0)  # Voiceover compares the two viewpoints
        # Total: 43.0s
        self.play(FadeOut(card_row), FadeOut(card_col), FadeOut(sub_dual), FadeOut(top_bar), run_time=2.0)
        # Total: 45.0s
