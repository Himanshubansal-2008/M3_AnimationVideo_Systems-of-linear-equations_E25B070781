"""
_Code/scene5_interpretation.py
Scene 5: Interpretation : Solution Set Taxonomy & Vector Space Structure
Duration: 50.0 seconds (3:35 - 4:25)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene5Interpretation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Top Chapter Banner (1.0s)
        # ----------------------------------------------------
        top_bar = create_top_banner(5, 6, "Interpretation : Solution Set Taxonomy & Column Space", "3:35 - 4:25")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total: 1.0s

        # ----------------------------------------------------
        # Part 1: The Three Fundamental Solution Regimes (20.0s)
        # ----------------------------------------------------
        sec_title = Text(
            "Every Linear System A x = b Falls into Exactly One of Three Regimes:",
            font_size=20,
            weight=BOLD,
            color=TEXT_WHITE
        ).shift(UP * 2.2)

        # 3 side-by-side cards
        card_unique = make_card(
            "1. Unique Solution",
            [
                "• Geometry: Lines intersect at 1 point",
                "• Columns are linearly independent",
                "• det(A) ≠ 0  (Invertible matrix)",
                "• Null space is trivial: N(A) = {0}",
                "• Rank: rank(A) = rank([A|b]) = n"
            ],
            width=4.0,
            height=3.8,
            border_color=ACCENT_GREEN
        ).shift(LEFT * 4.3 + DOWN * 0.3)

        card_infinite = make_card(
            "2. Infinitely Many",
            [
                "• Geometry: Lines coincide (overlap)",
                "• Columns are linearly dependent",
                "• Free variables appear (t ∈ ℝ)",
                "• Null space is non-trivial: dim > 0",
                "• Rank: rank(A) = rank([A|b]) < n"
            ],
            width=4.0,
            height=3.8,
            border_color=ACCENT_YELLOW
        ).shift(DOWN * 0.3)

        card_none = make_card(
            "3. No Solution (Inconsistent)",
            [
                "• Geometry: Parallel non-intersecting lines",
                "• Inconsistent row emerges: [0 ... 0 | c]",
                "• Target vector b lies OUTSIDE Col(A)",
                "• No linear combination reaches b",
                "• Rank: rank(A) < rank([A|b])"
            ],
            width=4.0,
            height=3.8,
            border_color=ACCENT_RED
        ).shift(RIGHT * 4.3 + DOWN * 0.3)

        regime_group = VGroup(card_unique, card_infinite, card_none)

        self.play(FadeIn(sec_title), FadeIn(regime_group, shift=UP * 0.2), run_time=1.5)
        # Total: 2.5s
        self.wait(18.5)  # Voiceover window to discuss the three categories
        # Total: 21.0s

        # ----------------------------------------------------
        # Part 2: The Deep Linear Algebra Connection: Col(A) (27.0s)
        # ----------------------------------------------------
        self.play(FadeOut(sec_title), FadeOut(regime_group), run_time=1.5)
        # Total: 22.5s

        thm_box = RoundedRectangle(
            corner_radius=0.15,
            width=12.2,
            height=1.0,
            fill_color="#1e1b4b",
            fill_opacity=0.9,
            stroke_color=ACCENT_PURPLE,
            stroke_width=2
        ).shift(UP * 2.0)

        thm_text = Text(
            "The Solvability Criterion :  A x = b is Consistent   ⟺   b ∈ Col(A)",
            font_size=20,
            weight=BOLD,
            color=ACCENT_YELLOW
        ).move_to(thm_box)

        # Two explanatory panels
        panel_left = make_card(
            "The Column Space  Col(A)",
            [
                "• Col(A) = Span{ a₁, a₂, ..., aₙ }",
                "• All attainable outputs of the transformation",
                "• A x is literally a vector in Col(A)",
                "• If b is in the span, weights x exist!",
                "• If b is outside the span, distance > 0"
            ],
            width=5.8,
            height=3.5,
            border_color=ACCENT_CYAN
        ).shift(LEFT * 3.3 + DOWN * 0.6)

        panel_right = make_card(
            "Rouché–Capelli & Rank Theorem",
            [
                "• System has a solution if and only if:",
                "    rank(A) == rank([A | b])",
                "• If rank == n : Unique solution",
                "• If rank < n  : (n - rank) free variables",
                "• Complete Solution:  x = x_particular + x_null"
            ],
            width=5.8,
            height=3.5,
            border_color=ACCENT_GREEN
        ).shift(RIGHT * 3.3 + DOWN * 0.6)

        self.play(
            FadeIn(thm_box), Write(thm_text),
            FadeIn(panel_left, shift=RIGHT * 0.2), FadeIn(panel_right, shift=LEFT * 0.2),
            run_time=2.0
        )
        # Total: 24.5s
        self.wait(23.5)  # Voiceover on column space and rank theorem
        # Total: 48.0s

        self.play(
            FadeOut(thm_box), FadeOut(thm_text),
            FadeOut(panel_left), FadeOut(panel_right),
            FadeOut(top_bar),
            run_time=2.0
        )
        # Total: 50.0s
