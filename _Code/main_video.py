"""
_Code/main_video.py
Unified Manim animation script orchestrating all 6 scenes:
Topic: Systems of Linear Equations (Ax = b)
Student: Himanshu | URN: E25B070781
Total Duration: 300.0 seconds (5 minutes exact)
"""

from manim import *
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from components import *
from scene1_hook import Scene1Hook
from scene2_concept import Scene2Concept
from scene3_intuition import Scene3Intuition
from scene4_worked_example import Scene4WorkedExample
from scene5_interpretation import Scene5Interpretation
from scene6_summary import Scene6Summary


class FullVideo(Scene):
    """
    Unified 5-Minute (300.0s) Animation Video:
    Scene 1: Hook & Context (45s)
    Scene 2: Concept Introduction (45s)
    Scene 3: Geometric Intuition: Row vs Column (60s)
    Scene 4: Worked Example: Gaussian Elimination (65s)
    Scene 5: Interpretation: Solution Set Taxonomy (50s)
    Scene 6: Key Takeaways & Credits (35s)
    """
    def construct(self):
        # Scene 1: Hook & Title
        Scene1Hook.construct(self)
        
        # Scene 2: Concept Introduction
        Scene2Concept.construct(self)
        
        # Scene 3: Geometric Intuition
        Scene3Intuition.construct(self)
        
        # Scene 4: Worked Example
        Scene4WorkedExample.construct(self)
        
        # Scene 5: Interpretation
        Scene5Interpretation.construct(self)
        
        # Scene 6: Summary & Credits
        Scene6Summary.construct(self)
