"""
_Code/scene6_summary.py
Scene 6: Summary, Key Takeaways, Viva Prep & Closing Credits
Duration: 35.0 seconds (4:25 - 5:00)
"""

from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *

class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # ----------------------------------------------------
        # Top Chapter Banner (1.0s)
        # ----------------------------------------------------
        top_bar = create_top_banner(6, 6, "Summary, Key Takeaways & Closing Credits", "4:25 - 5:00")
        self.play(FadeIn(top_bar, shift=DOWN * 0.2), run_time=1.0)
        # Total: 1.0s

        # ----------------------------------------------------
        # Part 1: 3 Core Takeaways for Viva & Exam (19.0s)
        # ----------------------------------------------------
        takeaways_card = RoundedRectangle(
            corner_radius=0.2,
            width=12.2,
            height=4.8,
            fill_color=CARD_BG,
            fill_opacity=0.9,
            stroke_color=PRIMARY_BLUE,
            stroke_width=2.5
        ).shift(DOWN * 0.3)

        card_title = Text("3 Core Takeaways to Master for Systems of Linear Equations", font_size=20, weight=BOLD, color=ACCENT_YELLOW).move_to(takeaways_card.get_top() + DOWN * 0.45)
        div = Line(takeaways_card.get_left() + RIGHT * 0.4, takeaways_card.get_right() + LEFT * 0.4, color=CARD_BORDER).next_to(card_title, DOWN, buff=0.15)

        t1_num = Text("1. Duality:", font_size=17, weight=BOLD, color=ACCENT_CYAN)
        t1_txt = Text(" Row Picture (intersecting hyperplanes) vs Column Picture (vector synthesis x₁a₁ + x₂a₂ = b).", font_size=15, color=TEXT_WHITE)
        t1_group = VGroup(t1_num, t1_txt).arrange(RIGHT, buff=0.15)

        t2_num = Text("2. Invariance:", font_size=17, weight=BOLD, color=ACCENT_GREEN)
        t2_txt = Text(" Elementary Row Operations (EROs) preserve the exact solution set while exposing RREF pivots.", font_size=15, color=TEXT_WHITE)
        t2_group = VGroup(t2_num, t2_txt).arrange(RIGHT, buff=0.15)

        t3_num = Text("3. Solvability:", font_size=17, weight=BOLD, color=ACCENT_PURPLE)
        t3_txt = Text(" Ax = b has solutions if and only if b ∈ Col(A), verified by rank(A) == rank([A | b]).", font_size=15, color=TEXT_WHITE)
        t3_group = VGroup(t3_num, t3_txt).arrange(RIGHT, buff=0.15)

        viva_note = Text("Viva Tip: Be ready to explain pivots, free variables, and the homogeneous system Ax = 0 null space!", font_size=14, weight=BOLD, color=ACCENT_YELLOW)

        takeaways_list = VGroup(t1_group, t2_group, t3_group, viva_note).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(div, DOWN, buff=0.35)

        takeaways_box = VGroup(takeaways_card, card_title, div, takeaways_list)

        self.play(FadeIn(takeaways_box, shift=UP * 0.2), run_time=1.5)
        # Total: 2.5s
        self.wait(16.5)  # Voiceover reviews takeaways
        # Total: 19.0s

        self.play(FadeOut(takeaways_box), FadeOut(top_bar), run_time=1.0)
        # Total: 20.0s

        # ----------------------------------------------------
        # Part 2: Official Closing Frame & Credits (15.0s)
        # ----------------------------------------------------
        close_box = RoundedRectangle(
            corner_radius=0.25,
            width=12.2,
            height=5.6,
            fill_color="#0f172a",
            fill_opacity=0.95,
            stroke_color=ACCENT_CYAN,
            stroke_width=2.5
        ).shift(ORIGIN)

        c_course = Text("LINEAR ALGEBRA AND CALCULUS (M3) • INTERNAL ASSESSMENT", font_size=17, weight=BOLD, color=ACCENT_CYAN).move_to(close_box.get_top() + DOWN * 0.5)
        c_proj = Text("PROJECT OPTION 1 : ANIMATION VIDEO", font_size=14, color=TEXT_MUTED).next_to(c_course, DOWN, buff=0.15)
        c_div1 = Line(close_box.get_left() + RIGHT * 0.5, close_box.get_right() + LEFT * 0.5, color=CARD_BORDER).next_to(c_proj, DOWN, buff=0.2)

        c_author_box = RoundedRectangle(corner_radius=0.12, width=9.0, height=0.7, fill_color="#1e293b", fill_opacity=0.9, stroke_color=PRIMARY_BLUE, stroke_width=1.5).next_to(c_div1, DOWN, buff=0.25)
        c_author = Text("Name: Himanshu   |   URN: E25B070781", font_size=19, weight=BOLD, color=TEXT_WHITE).move_to(c_author_box)

        c_topic = Text("Topic: Systems of Linear Equations (A x = b)", font_size=18, weight=BOLD, color=ACCENT_YELLOW).next_to(c_author_box, DOWN, buff=0.25)

        c_meta1 = Text("Animation Engine: Manim Community v0.22.1 (Python 3.15)", font_size=14, color=TEXT_MUTED)
        c_meta2 = Text("Audio Profile: Pure Voiceover Mode (No Background Music)", font_size=14, color=TEXT_MUTED)
        c_meta3 = Text("AI Disclosure: Visual scripting, timing layout & code crafted with Antigravity AI assistance", font_size=14, color=TEXT_MUTED)
        c_meta_group = VGroup(c_meta1, c_meta2, c_meta3).arrange(DOWN, buff=0.15).next_to(c_topic, DOWN, buff=0.25)

        c_thanks = Text("Thank You for Watching!", font_size=18, weight=BOLD, color=ACCENT_GREEN).next_to(c_meta_group, DOWN, buff=0.25)

        closing_group = VGroup(close_box, c_course, c_proj, c_div1, c_author_box, c_author, c_topic, c_meta_group, c_thanks)

        self.play(FadeIn(closing_group, shift=UP * 0.2), run_time=1.5)
        # Total: 21.5s
        self.wait(11.5)  # Closing frame display
        # Total: 33.0s
        self.play(FadeOut(closing_group), run_time=2.0)
        # Total: 35.0s
