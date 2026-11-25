"""
_Code/scene1_hook.py
Scene 1: Opening Frame & Hook / Motivation
Duration: 45.0 seconds (0:00 - 0:45)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene1Hook(Scene):
    def construct(self):
        # Background
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Part 1: Official Opening Title Frame (0:00 - 0:12 | 12s)
        # ----------------------------------------------------
        main_title = Text(
            "Systems of Linear Equations",
            font_size=46,
            weight=BOLD,
            color=TEXT_WHITE
        )

        equation_sub = Text(
            "A x = b",
            font_size=42,
            weight=BOLD,
            color=ACCENT_YELLOW
        )

        sub_desc = Text(
            "Connecting Equations, Coefficient Matrices & Solution Sets",
            font_size=20,
            color=TEXT_MUTED
        )

        title_content = VGroup(main_title, equation_sub, sub_desc).arrange(DOWN, buff=0.32).shift(UP * 0.5)

        title_box = RoundedRectangle(
            corner_radius=0.2,
            width=11.2,
            height=3.4,
            fill_color=CARD_BG,
            fill_opacity=0.75,
            stroke_color=PRIMARY_BLUE,
            stroke_width=2.5
        ).move_to(title_content)

        student_card = RoundedRectangle(
            corner_radius=0.15,
            width=9.5,
            height=0.85,
            fill_color="#172554",
            fill_opacity=0.9,
            stroke_color=ACCENT_CYAN,
            stroke_width=1.5
        ).shift(DOWN * 2.2)

        student_info = Text(
            "Name: Himanshu   |   URN: E25B070781",
            font_size=21,
            weight=BOLD,
            color=ACCENT_CYAN
        ).move_to(student_card)

        opening_group = VGroup(
            title_box, title_content, student_card, student_info
        )

        self.add(opening_group)
        self.wait(10.5)  # Direct first frame display from t=0.0s with student details
        self.play(FadeOut(opening_group), run_time=1.0)
        # Total elapsed: 11.5s

        # ----------------------------------------------------
        # Part 2: Sleek Scene Header & The Real-World Hook (0:12 - 0:28 | 16s)
        # ----------------------------------------------------
        top_bar = create_top_banner(1, 6, "Hook & Motivation : Why Linear Systems Matter", "0:00 - 0:45")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total elapsed: 12.5s

        hook_question = Text(
            "Where do simultaneous linear systems arise in the real world?",
            font_size=24,
            weight=BOLD,
            color=ACCENT_YELLOW
        ).shift(UP * 2.2)
        self.play(Write(hook_question), run_time=1.5)
        # Total elapsed: 14.0s

        # Three real-world application cards
        app1 = make_card(
            "1. Electrical Circuits",
            [
                "• Kirchhoff's Current Law",
                "• Kirchhoff's Voltage Law",
                "• Node voltage balance",
                "• Simultaneous linear loop equations"
            ],
            width=3.9,
            height=2.8,
            border_color=ACCENT_CYAN
        ).shift(LEFT * 4.2 + DOWN * 0.2)

        app2 = make_card(
            "2. Network & Traffic Flow",
            [
                "• Flow in = Flow out at nodes",
                "• Highway intersection equilibria",
                "• Packet routing optimization",
                "• Supply chain distribution"
            ],
            width=3.9,
            height=2.8,
            border_color=ACCENT_GREEN
        ).shift(DOWN * 0.2)

        app3 = make_card(
            "3. Graphics & Robotics",
            [
                "• Kinematic joint constraints",
                "• 3D coordinate transformations",
                "• Machine learning regression",
                "• Finite element structural analysis"
            ],
            width=3.9,
            height=2.8,
            border_color=ACCENT_PURPLE
        ).shift(RIGHT * 4.2 + DOWN * 0.2)

        self.play(FadeIn(app1, shift=UP * 0.3), FadeIn(app2, shift=UP * 0.3), FadeIn(app3, shift=UP * 0.3), run_time=1.5)
        self.wait(10.5)  # Let user explain these domains
        # Total elapsed: 26.0s

        # ----------------------------------------------------
        # Part 3: The Core Mathematical Challenge & Goal (0:28 - 0:45 | 19s)
        # ----------------------------------------------------
        self.play(FadeOut(app1), FadeOut(app2), FadeOut(app3), FadeOut(hook_question), run_time=1.0)
        # Total elapsed: 27.0s

        challenge_card = RoundedRectangle(
            corner_radius=0.2,
            width=11.2,
            height=3.6,
            fill_color=CARD_BG,
            fill_opacity=0.85,
            stroke_color=PRIMARY_BLUE,
            stroke_width=2
        ).shift(DOWN * 0.1)

        chal_title = Text("The Fundamental Challenge & Video Objective", font_size=22, weight=BOLD, color=ACCENT_CYAN).move_to(challenge_card.get_top() + DOWN * 0.4)
        div = Line(challenge_card.get_left() + RIGHT * 0.4, challenge_card.get_right() + LEFT * 0.4, color=CARD_BORDER).next_to(chal_title, DOWN, buff=0.15)

        p1 = Text("1. How do we represent dozens or thousands of simultaneous constraints concisely?", font_size=17, color=TEXT_WHITE)
        p2 = Text("2. What is the deep geometric difference between Row and Column perspectives?", font_size=17, color=TEXT_WHITE)
        p3 = Text("3. How does Gaussian Elimination systematically uncover the exact solution set?", font_size=17, color=TEXT_WHITE)

        p_group = VGroup(p1, p2, p3).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(div, DOWN, buff=0.35)
        goal_box = VGroup(challenge_card, chal_title, div, p_group)

        self.play(FadeIn(goal_box, shift=UP * 0.2), run_time=1.5)
        # Total elapsed: 28.5s
        self.wait(14.5)  # Voiceover window
        # Total elapsed: 43.0s
        self.play(FadeOut(goal_box), FadeOut(top_bar), run_time=2.0)
        # Total elapsed: 45.0s
