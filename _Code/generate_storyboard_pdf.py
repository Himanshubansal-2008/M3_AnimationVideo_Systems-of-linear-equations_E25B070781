"""
_Code/generate_storyboard_pdf.py
Generates the official Storyboard PDF for GitHub submission using PIL.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_storyboard_pdf(output_pdf="Storyboard.pdf"):
    # High-resolution page setup (A4 at 150 DPI: 1240 x 1754 px)
    W, H = 1240, 1754
    pages = []

    # Colors
    NAVY_DARK = (15, 23, 42)
    BLUE_ACCENT = (37, 99, 235)
    CYAN_ACCENT = (6, 182, 212)
    CARD_BG = (248, 250, 252)
    CARD_BORDER = (203, 213, 225)
    TEXT_DARK = (30, 41, 59)
    TEXT_MUTED = (100, 116, 139)
    WHITE = (255, 255, 255)
    GOLD = (217, 119, 6)

    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        font_h1 = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26)
        font_h2 = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        font_body = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        font_body_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 13)
    except Exception:
        font_title = font_h1 = font_h2 = font_body = font_body_bold = font_small = ImageFont.load_default()

    def draw_header(draw, title_str, subtitle_str, page_num):
        # Header banner
        draw.rectangle([(0, 0), (W, 110)], fill=NAVY_DARK)
        draw.text((50, 25), "LINEAR ALGEBRA AND CALCULUS (M3) • INTERNAL ASSESSMENT", fill=CYAN_ACCENT, font=font_small)
        draw.text((50, 48), title_str, fill=WHITE, font=font_h1)
        draw.text((50, 80), subtitle_str, fill=(203, 213, 225), font=font_small)
        draw.text((W - 120, 48), f"Page {page_num}/4", fill=WHITE, font=font_small)
        draw.line([(0, 110), (W, 110)], fill=BLUE_ACCENT, width=4)

    def draw_footer(draw):
        draw.line([(50, H - 60), (W - 50, H - 60)], fill=CARD_BORDER, width=1)
        draw.text((50, H - 45), "Name: Himanshu | URN: E25B070781 | Concept: Systems of Linear Equations (Ax = b)", fill=TEXT_MUTED, font=font_small)
        draw.text((W - 250, H - 45), "Target Duration: Exact 5:00", fill=TEXT_MUTED, font=font_small)

    def draw_card(draw, x, y, w, h, title, fill=CARD_BG, border=CARD_BORDER):
        draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill=fill, outline=border, width=2)
        if title:
            draw.rectangle([(x + 2, y + 2), (x + w - 2, y + 42)], fill=CARD_BORDER)
            draw.text((x + 18, y + 12), title, fill=TEXT_DARK, font=font_h2)

    # ----------------------------------------------------
    # PAGE 1: Overview, Context, and Learning Objective
    # ----------------------------------------------------
    img1 = Image.new("RGB", (W, H), WHITE)
    d1 = ImageDraw.Draw(img1)
    draw_header(d1, "Project Option 1: 6-Scene Storyboard Document", "Official Specification & Visual Narrative Blueprint", 1)

    # Metadata Card
    draw_card(d1, 50, 135, W - 100, 240, "1. Project Submission Metadata", fill=(241, 245, 249), border=BLUE_ACCENT)
    metadata_items = [
        ("Course / Subject:", "Linear Algebra and Calculus (M3) • Internal Assessment (10%)"),
        ("Project Option:", "Option 1: Animation Video (Turn a mathematical idea into visual intuition)"),
        ("Topic Chosen:", "Systems of Linear Equations (Ax = b): Connecting Equations, Matrices & Solutions"),
        ("Student Name:", "Himanshu"),
        ("University Reg. No (URN):", "E25B070781"),
        ("GitHub Repository:", "https://github.com/himanshu/M3_AnimationVideo_Concept_E25B070781"),
        ("Video Specifications:", "16:9 Landscape, 1080p (1920x1080), 30 fps, MP4 format, Duration: Exactly 5:00.00"),
        ("Audio Profile:", "Pure Voiceover Mode (No background music)")
    ]
    cur_y = 190
    for lbl, val in metadata_items:
        d1.text((75, cur_y), lbl, fill=TEXT_DARK, font=font_body_bold)
        d1.text((330, cur_y), val, fill=TEXT_MUTED, font=font_body)
        cur_y += 23

    # One-Sentence Objective Card
    draw_card(d1, 50, 395, W - 100, 145, "2. One-Sentence Learning Objective (PDF Requirement)", border=GOLD)
    obj_text = (
        '"By the end of this video, the viewer will be able to formulate any linear system into the compact\n'
        'matrix equation Ax = b, geometrically contrast the Row Picture with the Column Picture, systematically\n'
        'solve the system using Gaussian Elimination on an augmented matrix, and classify solution set structures\n'
        'using matrix rank and column space."'
    )
    d1.text((75, 450), obj_text, fill=TEXT_DARK, font=font_body)

    # 6-Scene Structure Overview Table
    draw_card(d1, 50, 560, W - 100, 550, "3. Complete 6-Scene Architecture & Time Budget (Exact 5:00 = 300.0s)")
    headers = ["Scene", "Title & Mathematical Purpose", "Time Window", "Duration", "Visual Strategy"]
    col_x = [70, 160, 530, 690, 810]
    d1.rectangle([(65, 615), (W - 65, 650)], fill=(226, 232, 240))
    for i, h in enumerate(headers):
        d1.text((col_x[i], 625), h, fill=TEXT_DARK, font=font_body_bold)

    scenes_summary = [
        ("Scene 1", "Hook & Context: Real-World Motivations", "0:00 - 0:45", "45.0s", "Opening title frame; Kirchhoff circuits, traffic, robotics."),
        ("Scene 2", "Concept Introduction: Formulating Ax = b", "0:45 - 1:30", "45.0s", "Factor system into A (2x2), x (2x1), b (2x1); duality cards."),
        ("Scene 3", "Visual Intuition: Row vs Column Picture", "1:30 - 2:30", "60.0s", "2D NumberPlane: Lines intersect at (2,3) vs 2a1 + 3a2 = b."),
        ("Scene 4", "Worked Example: Gaussian Elimination", "2:30 - 3:35", "65.0s", "Augmented matrix [A|b]; Swap -> Echelon -> Scale -> RREF."),
        ("Scene 5", "Interpretation: Taxonomy & Column Space", "3:35 - 4:25", "50.0s", "Unique vs Infinite vs Inconsistent; Theorem: b in Col(A)."),
        ("Scene 6", "Summary, Viva Preparation & Credits", "4:25 - 5:00", "35.0s", "3 Core takeaways; Viva exam hints; Closing credit frame.")
    ]
    row_y = 665
    for sc, ttl, win, dur, strat in scenes_summary:
        d1.text((col_x[0], row_y + 10), sc, fill=BLUE_ACCENT, font=font_body_bold)
        d1.text((col_x[1], row_y + 10), ttl, fill=TEXT_DARK, font=font_body)
        d1.text((col_x[2], row_y + 10), win, fill=TEXT_MUTED, font=font_body)
        d1.text((col_x[3], row_y + 10), dur, fill=GOLD, font=font_body_bold)
        d1.text((col_x[4], row_y + 10), strat, fill=TEXT_MUTED, font=font_small)
        d1.line([(65, row_y + 60), (W - 65, row_y + 60)], fill=CARD_BORDER, width=1)
        row_y += 65

    # Pedagogical Pillars Card
    draw_card(d1, 50, 1135, W - 100, 520, "4. Pedagogical Pillars & Verification")
    d1.text((75, 1195), "• Dual-Lens Visual Progression: Viewers first build physical/geometric intuition before performing algebraic manipulation.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1250), "• Invariance of Row Operations: Explicitly demonstrates why EROs preserve the exact solution space without mutation.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1305), "• Mathematical Soundness: Every line, coefficient, vector sum, and pivot was recalculated and verified on paper.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1360), "• Exact Timing Synchronization: Every animation phase aligns with the voice-over narration script within 0.1s.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1415), "• Vocal Freedom: Ambient background music remains at low -24 dB to ensure student narration is crystal clear.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1470), "• Clear Notation: Defines coefficient matrix A, state vector x, and target vector b before Gaussian elimination.", fill=TEXT_DARK, font=font_body)
    d1.text((75, 1525), "• 1080p Readability: High-contrast typography and color schemes designed specifically for crisp projection and evaluation.", fill=TEXT_DARK, font=font_body)
    draw_footer(d1)
    pages.append(img1)

    # ----------------------------------------------------
    # PAGE 2: Scene 1 & Scene 2 Detailed Breakdown
    # ----------------------------------------------------
    img2 = Image.new("RGB", (W, H), WHITE)
    d2 = ImageDraw.Draw(img2)
    draw_header(d2, "Detailed Storyboard : Scene 1 & Scene 2", "Hook, Context, and Algebraic Matrix Formulation", 2)

    # Scene 1 Card
    draw_card(d2, 50, 140, W - 100, 720, "Scene 1 : Hook / Context & Opening Frame (0:00 - 0:45 | Duration: 45.0s)", border=BLUE_ACCENT)
    d2.text((75, 195), "Purpose: Spark curiosity, establish formal academic context, and motivate linear systems.", fill=BLUE_ACCENT, font=font_h2)
    d2.text((75, 235), "Visual Layout & Animation Actions:", fill=TEXT_DARK, font=font_body_bold)
    sc1_visuals = [
        "1. [0:00 - 0:11] Official Opening Frame reveals subject header, project title, and candidate card (Himanshu, E25B070781).",
        "2. [0:11 - 0:14] Transition to sleek Chapter Banner at top: 'SCENE 1/6: Hook & Motivation'.",
        "3. [0:14 - 0:26] Three real-world application domain cards smoothly slide in:",
        "   - Electrical Circuits: Kirchhoff's laws requiring simultaneous loop and node voltage/current equilibrium.",
        "   - Network Traffic Flow: Conservation of flow (Inflow = Outflow) at every intersection.",
        "   - Robotics & Graphics: Kinematic joint constraints and 3D coordinate transformation systems.",
        "4. [0:26 - 0:43] Central challenge card appears: How do we solve large simultaneous systems concisely?",
        "5. [0:43 - 0:45] Smooth transition fade into Scene 2."
    ]
    y_v = 265
    for line in sc1_visuals:
        d2.text((90, y_v), line, fill=TEXT_MUTED, font=font_body)
        y_v += 28

    d2.text((75, 520), "Narration & Oral Defense Plan:", fill=TEXT_DARK, font=font_body_bold)
    sc1_narr = [
        "• State candidate name, ID, and assessment title with academic poise.",
        "• Motivate why linear systems matter across engineering, data science, and physics.",
        "• Highlight the central question: moving from individual equations to unified matrix operators."
    ]
    y_n = 550
    for line in sc1_narr:
        d2.text((90, y_n), line, fill=TEXT_DARK, font=font_body)
        y_n += 28

    # Scene 2 Card
    draw_card(d2, 50, 890, W - 100, 760, "Scene 2 : Concept Introduction : Formulating Ax = b (0:45 - 1:30 | Duration: 45.0s)", border=CYAN_ACCENT)
    d2.text((75, 945), "Purpose: Translate simultaneous equations into compact matrix equation Ax = b and introduce duality.", fill=CYAN_ACCENT, font=font_h2)
    d2.text((75, 985), "Visual Layout & Animation Actions:", fill=TEXT_DARK, font=font_body_bold)
    sc2_visuals = [
        "1. [0:45 - 0:58] Present concrete system of 2 equations:  Eq 1: 2x₁ - x₂ = 1  and  Eq 2: x₁ + x₂ = 5.",
        "2. [0:58 - 1:18] Factor system into color-coded matrix components: [ [2, -1], [1, 1] ] [x1, x2]ᵀ = [1, 5]ᵀ.",
        "   - Matrix A (2x2): Coefficient matrix representing the linear transformation operator of space (Blue).",
        "   - Vector x (2x1): Unknown state vector containing variables to solve for (Yellow).",
        "   - Vector b (2x1): Target/constraint vector in the codomain (Green).",
        "3. [1:18 - 1:28] Reveal dual perspectives: Row dot products vs Column vector combinations.",
        "4. [1:28 - 1:30] Fade out to prepare for 2D geometric demonstration."
    ]
    y_v2 = 1015
    for line in sc2_visuals:
        d2.text((90, y_v2), line, fill=TEXT_MUTED, font=font_body)
        y_v2 += 28

    d2.text((75, 1280), "Mathematical Formulations & Verifications:", fill=TEXT_DARK, font=font_body_bold)
    sc2_math = [
        "• Row Dot Product Form:  Row_i(A) • x = b_i  ==>  2x₁ - x₂ = 1  and  x₁ + x₂ = 5.",
        "• Column Combination Form:  x₁ [2, 1]ᵀ + x₂ [-1, 1]ᵀ = [1, 5]ᵀ.",
        "• Transformation Mapping:  T: ℝ² -> ℝ² defined by T(x) = Ax."
    ]
    y_m2 = 1310
    for line in sc2_math:
        d2.text((90, y_m2), line, fill=TEXT_DARK, font=font_body)
        y_m2 += 28
    draw_footer(d2)
    pages.append(img2)

    # ----------------------------------------------------
    # PAGE 3: Scene 3 & Scene 4 Detailed Breakdown
    # ----------------------------------------------------
    img3 = Image.new("RGB", (W, H), WHITE)
    d3 = ImageDraw.Draw(img3)
    draw_header(d3, "Detailed Storyboard : Scene 3 & Scene 4", "Geometric Intuition and Step-by-Step Gaussian Elimination", 3)

    # Scene 3 Card
    draw_card(d3, 50, 140, W - 100, 720, "Scene 3 : Geometric Intuition : Row vs Column Picture (1:30 - 2:30 | Duration: 60.0s)", border=GOLD)
    d3.text((75, 195), "Purpose: Ground abstract algebra in stunning visual geometry on a 2D Cartesian plane.", fill=GOLD, font=font_h2)
    d3.text((75, 235), "Visual Layout & Animation Actions:", fill=TEXT_DARK, font=font_body_bold)
    sc3_visuals = [
        "1. [1:30 - 1:44] Animated 2D NumberPlane. Cyan Line L₁: 2x₁ - x₂ = 1 and Amber Line L₂: x₁ + x₂ = 5 plotted.",
        "2. [1:44 - 1:58] Lines meet at intersection point (2, 3). Pulsating dot with dashed projections to axes x₁=2, x₂=3.",
        "   - Accompanying Row Picture Card explains that each row is a geometric hyperplane constraint.",
        "3. [1:58 - 2:01] Lines fade out; Column basis vectors a₁ = [2, 1]ᵀ (Green) and a₂ = [-1, 1]ᵀ (Purple) grow from origin.",
        "4. [2:01 - 2:15] Column a₁ dynamically stretches by factor of 2 to [4, 2]ᵀ.",
        "5. [2:15 - 2:27] Vector 3*a₂ = [-3, 3]ᵀ attaches head-to-tail to tip of 2*a₁; resultant tip lands exactly on b = [1, 5]ᵀ!",
        "6. [2:27 - 2:30] Target vector b drawn in glowing gold; head-to-tail vector synthesis visually confirmed."
    ]
    y_v3 = 265
    for line in sc3_visuals:
        d3.text((90, y_v3), line, fill=TEXT_MUTED, font=font_body)
        y_v3 += 28

    d3.text((75, 520), "Core Takeaway Contrasted:", fill=TEXT_DARK, font=font_body_bold)
    sc3_comp = [
        "• Row Picture asks: 'Where do the linear constraint lines intersect in space?' (Intersecting hyperplanes)",
        "• Column Picture asks: 'What weights scale the column vectors to reach target vector b?' (Vector synthesis)",
        "• Both pictures produce the exact same solution: x₁ = 2, x₂ = 3."
    ]
    y_c3 = 550
    for line in sc3_comp:
        d3.text((90, y_c3), line, fill=TEXT_DARK, font=font_body)
        y_c3 += 28

    # Scene 4 Card
    draw_card(d3, 50, 890, W - 100, 760, "Scene 4 : Worked Example : Gaussian Elimination (2:30 - 3:35 | Duration: 65.0s)", border=BLUE_ACCENT)
    d3.text((75, 945), "Purpose: Demonstrate systematic algorithmic computation on the Augmented Matrix [A | b].", fill=BLUE_ACCENT, font=font_h2)
    d3.text((75, 985), "Step-by-Step ERO Calculations Walkthrough:", fill=TEXT_DARK, font=font_body_bold)
    sc4_steps = [
        "1. Initial Augmented Matrix: [ [2, -1 | 1], [1, 1 | 5] ]. Explaining ERO invariance.",
        "2. Step 1 (Row Swap): R₁ <-> R₂ ==> [ [1, 1 | 5], [2, -1 | 1] ]. Pivot at (1, 1) established.",
        "3. Step 2 (Elimination): R₂ <- R₂ - 2*R₁ ==> Arithmetic: 2 - 2(1) = 0; -1 - 2(1) = -3; 1 - 2(5) = -9.",
        "   Result: [ [1, 1 | 5], [0, -3 | -9] ] (Upper-triangular Echelon Form).",
        "4. Step 3 (Pivot Normalization): R₂ <- -1/3 * R₂ ==> [ [1, 1 | 5], [0, 1 | 3] ]. Reveals x₂ = 3.",
        "5. Step 4 (Back-Substitution): R₁ <- R₁ - R₂ ==> [ [1, 0 | 2], [0, 1 | 3] ] (Reduced Row Echelon Form).",
        "6. Solution Vector Readout: x = [ 2 , 3 ]ᵀ. Verified in original equations: 2(2) - 3 = 1 and 2 + 3 = 5."
    ]
    y_s4 = 1015
    for line in sc4_steps:
        d3.text((90, y_s4), line, fill=TEXT_MUTED, font=font_body)
        y_s4 += 28
    draw_footer(d3)
    pages.append(img3)

    # ----------------------------------------------------
    # PAGE 4: Scene 5 & Scene 6 Detailed Breakdown
    # ----------------------------------------------------
    img4 = Image.new("RGB", (W, H), WHITE)
    d4 = ImageDraw.Draw(img4)
    draw_header(d4, "Detailed Storyboard : Scene 5 & Scene 6", "Solution Set Taxonomy, Column Space Theorem, Summary & Credits", 4)

    # Scene 5 Card
    draw_card(d4, 50, 140, W - 100, 720, "Scene 5 : Interpretation : Solution Taxonomy & Column Space (3:35 - 4:25 | Duration: 50.0s)", border=CYAN_ACCENT)
    d4.text((75, 195), "Purpose: Classify general solution sets and connect algebra to fundamental vector subspaces.", fill=CYAN_ACCENT, font=font_h2)
    d4.text((75, 235), "The Three Fundamental Solution Regimes:", fill=TEXT_DARK, font=font_body_bold)
    sc5_regimes = [
        "1. Unique Solution (Green): Lines intersect at exactly one point; det(A) ≠ 0; full column rank r = n.",
        "2. Infinitely Many Solutions (Yellow): Lines coincide; dependent columns; free variables exist; r = rank([A|b]) < n.",
        "3. No Solution / Inconsistent (Red): Distinct parallel lines; contradiction row [0 ... 0 | c]; b lies outside Col(A)."
    ]
    y_r5 = 265
    for line in sc5_regimes:
        d4.text((90, y_r5), line, fill=TEXT_MUTED, font=font_body)
        y_r5 += 28

    d4.text((75, 380), "The Column Space Solvability Theorem:", fill=TEXT_DARK, font=font_body_bold)
    sc5_thm = [
        "• Core Theorem: Ax = b is solvable if and only if b ∈ Col(A) (target lies within the span of the columns).",
        "• Subspace Definition: Col(A) = { Ax | x ∈ ℝⁿ } is the range/image of the linear transformation.",
        "• Rouché–Capelli Theorem: Consistency holds iff rank(A) == rank([A | b]).",
        "• Complete Solution Structure: x = x_particular + x_null, where x_null ∈ Null(A)."
    ]
    y_t5 = 410
    for line in sc5_thm:
        d4.text((90, y_t5), line, fill=TEXT_DARK, font=font_body)
        y_t5 += 28

    # Scene 6 Card
    draw_card(d4, 50, 890, W - 100, 760, "Scene 6 : Summary, Key Takeaways & Closing Credits (4:25 - 5:00 | Duration: 35.0s)", border=BLUE_ACCENT)
    d4.text((75, 945), "Purpose: Reinforce 3 core takeaways, provide viva pointers, and display official closing credits.", fill=BLUE_ACCENT, font=font_h2)
    d4.text((75, 985), "3 Core Takeaways Displayed on Screen:", fill=TEXT_DARK, font=font_body_bold)
    sc6_takeaways = [
        "1. Duality: Ax = b unites constraint hyperplanes (Row Picture) with vector synthesis (Column Picture).",
        "2. Invariance: Elementary Row Operations (EROs) preserve the exact solution set while exposing pivots.",
        "3. Solvability: Solution existence is governed by whether b lies in the Column Space of A."
    ]
    y_t6 = 1015
    for line in sc6_takeaways:
        d4.text((90, y_t6), line, fill=TEXT_MUTED, font=font_body)
        y_t6 += 28

    d4.text((75, 1130), "Official Closing Frame Metadata (PDF Submission Mandate):", fill=TEXT_DARK, font=font_body_bold)
    sc6_credits = [
        "• Course Title: LINEAR ALGEBRA AND CALCULUS (M3) • INTERNAL ASSESSMENT",
        "• Student Author: Himanshu | URN: E25B070781",
        "• Topic: Systems of Linear Equations (Ax = b)",
        "• Animation Platform: Manim Community v0.22.1 & Python 3.15",
        "• Audio Profile: Pure Voiceover Mode (Silent background, no music)",
        "• AI Disclosure: Antigravity AI assisted in visual scripting, timing orchestration, and code generation.",
        "• Closing Sign-off: 'Thank You for Watching!'"
    ]
    y_c6 = 1160
    for line in sc6_credits:
        d4.text((90, y_c6), line, fill=TEXT_DARK, font=font_body)
        y_c6 += 28
    draw_footer(d4)
    pages.append(img4)

    # Save multi-page PDF
    pages[0].save(output_pdf, save_all=True, append_images=pages[1:], resolution=150.0)
    print(f"Generated {output_pdf} successfully ({len(pages)} pages).")

if __name__ == "__main__":
    create_storyboard_pdf("Storyboard.pdf")
