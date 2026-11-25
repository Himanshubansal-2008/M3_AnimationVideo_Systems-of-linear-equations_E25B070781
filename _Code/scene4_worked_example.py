"""
_Code/scene4_worked_example.py
Scene 4: Worked Example : Systematic Solution via Gaussian Elimination
Duration: 65.0 seconds (2:30 - 3:35)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene4WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Top Chapter Banner (1.0s)
        # ----------------------------------------------------
        top_bar = create_top_banner(4, 6, "Worked Example : Step-by-Step Gaussian Elimination", "2:30 - 3:35")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total: 1.0s

        # ----------------------------------------------------
        # Part 1: Augmented Matrix Setup & EROs (3.0s + 10.0s = 13.0s)
        # ----------------------------------------------------
        ero_card = make_card(
            "Elementary Row Operations",
            [
                "1. Row Swap:  Rᵢ ↔ Rⱼ",
                "2. Row Scale: Rᵢ ← k Rᵢ  (k ≠ 0)",
                "3. Row Addition: Rᵢ ← Rᵢ + k Rⱼ",
                "Invariant: EROs preserve the exact",
                "solution set of the original system!"
            ],
            width=5.6,
            height=3.8,
            border_color=PRIMARY_BLUE
        ).shift(LEFT * 3.6 + DOWN * 0.3)

        # Initial augmented matrix [A | b]
        aug0 = make_augmented_matrix_mobject([[2, -1], [1, 1]], [[1], [5]], bracket_color=ACCENT_CYAN, font_size=28, h_buff=0.9, v_buff=0.7).shift(RIGHT * 3.4 + DOWN * 0.1)
        aug0_lbl = Text("Augmented Matrix  [ A | b ]", font_size=18, weight=BOLD, color=ACCENT_CYAN).next_to(aug0, UP, buff=0.35)
        aug0_group = VGroup(aug0, aug0_lbl)

        self.play(FadeIn(ero_card, shift=RIGHT * 0.2), FadeIn(aug0_group, shift=LEFT * 0.2), run_time=3.0)
        # Total: 4.0s
        self.wait(10.0)  # Voiceover introduces augmented matrix and ERO principles
        # Total: 14.0s

        # ----------------------------------------------------
        # Part 2: Step 1 - Swap R1 <-> R2 (2.0s + 8.0s = 10.0s)
        # ----------------------------------------------------
        # Replace ERO card with Step tracker panel
        self.play(FadeOut(ero_card), run_time=0.5)
        # Total: 14.5s

        op_badge1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=ACCENT_YELLOW, stroke_width=2).shift(LEFT * 3.6 + UP * 1.8)
        op_text1 = Text("Step 1:  R₁ ↔ R₂  (Pivot Selection)", font_size=16, weight=BOLD, color=ACCENT_YELLOW).move_to(op_badge1)
        step_header1 = VGroup(op_badge1, op_text1)

        expl1 = make_card(
            "Pivot Selection Strategy",
            [
                "• Swap rows to place 1 in pivot (1, 1)",
                "• Avoids fractional arithmetic early",
                "• Enhances numerical stability",
                "• Row 1 becomes leading reference row"
            ],
            width=5.6,
            height=3.0,
            border_color=ACCENT_YELLOW
        ).shift(LEFT * 3.6 + DOWN * 0.4)

        aug1 = make_augmented_matrix_mobject([[1, 1], [2, -1]], [[5], [1]], bracket_color=ACCENT_YELLOW, font_size=28, h_buff=0.9, v_buff=0.7).shift(RIGHT * 3.4 + DOWN * 0.1)
        aug1_lbl = Text("After Row Swap  (R₁ ↔ R₂)", font_size=18, weight=BOLD, color=ACCENT_YELLOW).next_to(aug1, UP, buff=0.35)
        aug1_group = VGroup(aug1, aug1_lbl)

        self.play(
            FadeIn(step_header1), FadeIn(expl1),
            Transform(aug0_group, aug1_group),
            run_time=1.5
        )
        # Total: 16.0s
        self.wait(8.0)  # Voiceover on Step 1
        # Total: 24.0s

        # ----------------------------------------------------
        # Part 3: Step 2 - Elimination R2 <- R2 - 2 R1 (2.0s + 13.0s = 15.0s)
        # ----------------------------------------------------
        op_badge2 = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=ACCENT_RED, stroke_width=2).shift(LEFT * 3.6 + UP * 1.8)
        op_text2 = Text("Step 2:  R₂ ← R₂ - 2 R₁  (Elimination)", font_size=16, weight=BOLD, color=ACCENT_RED).move_to(op_badge2)
        step_header2 = VGroup(op_badge2, op_text2)

        calc_card = make_card(
            "Arithmetic Elimination",
            [
                "• Col 1:  2 - 2(1) = 0   (Entry zeroed!)",
                "• Col 2: -1 - 2(1) = -3",
                "• RHS:    1 - 2(5) = -9",
                "• System is now in Row Echelon Form!",
                "• Triangular structure revealed"
            ],
            width=5.6,
            height=3.0,
            border_color=ACCENT_RED
        ).shift(LEFT * 3.6 + DOWN * 0.4)

        aug2 = make_augmented_matrix_mobject([[1, 1], [0, -3]], [[5], [-9]], bracket_color=ACCENT_RED, font_size=28, h_buff=0.9, v_buff=0.7).shift(RIGHT * 3.4 + DOWN * 0.1)
        aug2_lbl = Text("Echelon Form  (R₂ ← R₂ - 2R₁)", font_size=18, weight=BOLD, color=ACCENT_RED).next_to(aug2, UP, buff=0.35)
        aug2_group = VGroup(aug2, aug2_lbl)

        self.play(
            Transform(step_header1, step_header2), Transform(expl1, calc_card),
            Transform(aug0_group, aug2_group),
            run_time=2.0
        )
        # Total: 26.0s
        self.wait(13.0)  # Voiceover on elimination math
        # Total: 39.0s

        # ----------------------------------------------------
        # Part 4: Step 3 - Scale R2 <- -1/3 R2 (2.0s + 8.0s = 10.0s)
        # ----------------------------------------------------
        op_badge3 = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=ACCENT_PURPLE, stroke_width=2).shift(LEFT * 3.6 + UP * 1.8)
        op_text3 = Text("Step 3:  R₂ ← -1/3 R₂  (Scaling)", font_size=16, weight=BOLD, color=ACCENT_PURPLE).move_to(op_badge3)
        step_header3 = VGroup(op_badge3, op_text3)

        expl3 = make_card(
            "Normalize Second Pivot",
            [
                "• Divide row 2 by -3 (multiply by -1/3)",
                "• Pivot in (2, 2) becomes leading 1",
                "• Row 2 translates directly to:  x₂ = 3",
                "• Second variable is uniquely found!"
            ],
            width=5.6,
            height=3.0,
            border_color=ACCENT_PURPLE
        ).shift(LEFT * 3.6 + DOWN * 0.4)

        aug3 = make_augmented_matrix_mobject([[1, 1], [0, 1]], [[5], [3]], bracket_color=ACCENT_PURPLE, font_size=28, h_buff=0.9, v_buff=0.7).shift(RIGHT * 3.4 + DOWN * 0.1)
        aug3_lbl = Text("Normalized Pivot 2  (x₂ = 3)", font_size=18, weight=BOLD, color=ACCENT_PURPLE).next_to(aug3, UP, buff=0.35)
        aug3_group = VGroup(aug3, aug3_lbl)

        self.play(
            Transform(step_header1, step_header3), Transform(expl1, expl3),
            Transform(aug0_group, aug3_group),
            run_time=2.0
        )
        # Total: 41.0s
        self.wait(8.0)  # Voiceover on normalization
        # Total: 49.0s

        # ----------------------------------------------------
        # Part 5: Step 4 - Back-Substitution / RREF (2.0s + 12.0s = 14.0s)
        # ----------------------------------------------------
        op_badge4 = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=ACCENT_GREEN, stroke_width=2).shift(LEFT * 3.6 + UP * 1.8)
        op_text4 = Text("Step 4:  R₁ ← R₁ - R₂  (RREF Result)", font_size=16, weight=BOLD, color=ACCENT_GREEN).move_to(op_badge4)
        step_header4 = VGroup(op_badge4, op_text4)

        expl4 = make_card(
            "Reduced Row Echelon (RREF)",
            [
                "• Subtract R₂ from R₁: 5 - 3 = 2",
                "• Leading entries are 1; zeros elsewhere",
                "• Direct readout:  x₁ = 2,  x₂ = 3",
                "• Verification in original equations:",
                "    2(2) - (3) = 1    (Verified!)",
                "    1(2) + 1(3) = 5   (Verified!)"
            ],
            width=5.6,
            height=3.4,
            border_color=ACCENT_GREEN
        ).shift(LEFT * 3.6 + DOWN * 0.5)

        aug4 = make_augmented_matrix_mobject([[1, 0], [0, 1]], [[2], [3]], bracket_color=ACCENT_GREEN, font_size=28, h_buff=0.9, v_buff=0.7).shift(RIGHT * 3.4 + UP * 0.2)
        aug4_lbl = Text("Reduced Row Echelon Form [ I | x ]", font_size=18, weight=BOLD, color=ACCENT_GREEN).next_to(aug4, UP, buff=0.35)

        # Solution callout box
        sol_box = RoundedRectangle(corner_radius=0.15, width=4.8, height=1.1, fill_color="#064e3b", fill_opacity=0.9, stroke_color=ACCENT_GREEN, stroke_width=2).next_to(aug4, DOWN, buff=0.45)
        sol_text = Text("Solution Vector :  x = [ 2 ,  3 ]ᵀ", font_size=19, weight=BOLD, color=TEXT_WHITE).move_to(sol_box)
        sol_group = VGroup(aug4, aug4_lbl, sol_box, sol_text)

        self.play(
            Transform(step_header1, step_header4), Transform(expl1, expl4),
            Transform(aug0_group, sol_group),
            run_time=2.0
        )
        # Total: 51.0s
        self.wait(12.0)  # Voiceover confirms the solution and substitution
        # Total: 63.0s

        # Fade out
        self.play(
            FadeOut(step_header1), FadeOut(expl1),
            FadeOut(aug0_group), FadeOut(top_bar),
            run_time=2.0
        )
        # Total: 65.0s
