"""
_Code/components.py
Reusable visual and mathematical components for Manim animations
without relying on external LaTeX dependencies.
"""

from manim import *

# Color Palette
BG_COLOR = "#0b0f19"
PRIMARY_BLUE = "#3b82f6"
ACCENT_CYAN = "#06b6d4"
ACCENT_YELLOW = "#facc15"
ACCENT_GREEN = "#10b981"
ACCENT_PURPLE = "#a855f7"
ACCENT_ORANGE = "#f97316"
ACCENT_RED = "#ef4444"
TEXT_WHITE = "#f8fafc"
TEXT_MUTED = "#94a3b8"
CARD_BG = "#1e293b"
CARD_BORDER = "#334155"


def create_top_banner(scene_number, total_scenes, scene_title, timestamp_str=""):
    """Creates a sleek chapter progress banner at top of screen."""
    pill_bg = RoundedRectangle(
        corner_radius=0.15,
        width=13.0,
        height=0.6,
        fill_color=CARD_BG,
        fill_opacity=0.85,
        stroke_color=CARD_BORDER,
        stroke_width=1.5
    ).to_edge(UP, buff=0.25)

    badge = RoundedRectangle(
        corner_radius=0.1,
        width=1.8,
        height=0.4,
        fill_color=PRIMARY_BLUE,
        fill_opacity=0.9,
        stroke_width=0
    ).move_to(pill_bg.get_left() + RIGHT * 1.1)
    
    badge_text = Text(
        f"SCENE {scene_number}/{total_scenes}",
        font_size=15,
        weight=BOLD,
        color=TEXT_WHITE
    ).move_to(badge)

    title_text = Text(
        scene_title,
        font_size=17,
        weight=BOLD,
        color=ACCENT_CYAN
    ).next_to(badge, RIGHT, buff=0.4)

    return VGroup(pill_bg, badge, badge_text, title_text)


def create_bracket(mgroup, is_left=True, color=PRIMARY_BLUE, stroke_width=3, arm_length=0.18):
    """Creates a crisp square bracket for a matrix."""
    corner_top = mgroup.get_corner(UL if is_left else UR)
    corner_bot = mgroup.get_corner(DL if is_left else DR)
    
    dx = -0.15 if is_left else 0.15
    arm_dx = arm_length if is_left else -arm_length
    
    top_pt = corner_top + np.array([dx, 0.15, 0])
    bot_pt = corner_bot + np.array([dx, -0.15, 0])
    
    main_line = Line(top_pt, bot_pt, color=color, stroke_width=stroke_width)
    top_arm = Line(top_pt, top_pt + np.array([arm_dx, 0, 0]), color=color, stroke_width=stroke_width)
    bot_arm = Line(bot_pt, bot_pt + np.array([arm_dx, 0, 0]), color=color, stroke_width=stroke_width)
    
    return VGroup(main_line, top_arm, bot_arm)


def make_matrix_mobject(data, color_map=None, bracket_color=PRIMARY_BLUE, font_size=24, h_buff=0.7, v_buff=0.5):
    """Builds a matrix Mobject from 2D data list."""
    rows = []
    for r_idx, row in enumerate(data):
        row_mob = []
        for c_idx, val in enumerate(row):
            col = color_map.get((r_idx, c_idx), TEXT_WHITE) if color_map else TEXT_WHITE
            row_mob.append(Text(str(val), font_size=font_size, color=col))
        r_group = VGroup(*row_mob).arrange(RIGHT, buff=h_buff)
        rows.append(r_group)
    
    grid = VGroup(*rows).arrange(DOWN, buff=v_buff)
    
    # Align columns
    num_cols = len(data[0])
    num_rows = len(data)
    for c in range(num_cols):
        col_x = rows[0][c].get_x()
        for r in range(1, num_rows):
            rows[r][c].set_x(col_x)
            
    left_br = create_bracket(grid, is_left=True, color=bracket_color)
    right_br = create_bracket(grid, is_left=False, color=bracket_color)
    
    mat = VGroup(left_br, grid, right_br)
    mat.grid = grid
    mat.rows = rows
    return mat


def make_augmented_matrix_mobject(A_data, b_data, bracket_color=PRIMARY_BLUE, font_size=24, h_buff=0.7, v_buff=0.5):
    """Builds an augmented matrix [A | b] with a separator line."""
    A_mat = make_matrix_mobject(A_data, bracket_color=bracket_color, font_size=font_size, h_buff=h_buff, v_buff=v_buff)
    b_mat = make_matrix_mobject(b_data, bracket_color=bracket_color, font_size=font_size, h_buff=h_buff, v_buff=v_buff)
    
    # We strip individual brackets and join them
    A_grid = A_mat.grid
    b_grid = b_mat.grid
    
    b_grid.next_to(A_grid, RIGHT, buff=h_buff * 1.2)
    b_grid.align_to(A_grid, UP)
    
    # Dividing dashed or solid line
    sep_x = (A_grid.get_right()[0] + b_grid.get_left()[0]) / 2.0
    top_y = max(A_grid.get_top()[1], b_grid.get_top()[1]) + 0.15
    bot_y = min(A_grid.get_bottom()[1], b_grid.get_bottom()[1]) - 0.15
    
    sep_line = DashedLine(
        np.array([sep_x, top_y, 0]),
        np.array([sep_x, bot_y, 0]),
        color=TEXT_MUTED,
        dash_length=0.08,
        dashed_ratio=0.6,
        stroke_width=2
    )
    
    content = VGroup(A_grid, sep_line, b_grid)
    left_br = create_bracket(content, is_left=True, color=bracket_color)
    right_br = create_bracket(content, is_left=False, color=bracket_color)
    
    aug = VGroup(left_br, content, right_br)
    aug.A_grid = A_grid
    aug.b_grid = b_grid
    aug.sep_line = sep_line
    return aug


def make_card(title, lines, width=4.0, height=2.8, border_color=PRIMARY_BLUE, fill_color=CARD_BG):
    """Creates an info panel with title and bullet lines."""
    box = RoundedRectangle(
        corner_radius=0.15,
        width=width,
        height=height,
        fill_color=fill_color,
        fill_opacity=0.9,
        stroke_color=border_color,
        stroke_width=2
    )
    
    title_mob = Text(title, font_size=20, weight=BOLD, color=ACCENT_YELLOW).move_to(box.get_top() + DOWN * 0.35)
    line_div = Line(box.get_left() + RIGHT * 0.2, box.get_right() + LEFT * 0.2, stroke_color=CARD_BORDER, stroke_width=1).next_to(title_mob, DOWN, buff=0.15)
    
    text_mobs = []
    for line in lines:
        t = Text(line, font_size=15, color=TEXT_WHITE)
        text_mobs.append(t)
    
    body = VGroup(*text_mobs).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(line_div, DOWN, buff=0.25)
    
    card = VGroup(box, title_mob, line_div, body)
    return card
