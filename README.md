# Linear Algebra and Calculus (M3) • Internal Assessment
## Project Option 1: Animation Video — Systems of Linear Equations ($Ax = b$)

**Official Submission Repository for Public Evaluation**

---

### Student & Project Metadata
- **Student Name:** Himanshu
- **University Registration Number (URN):** `E25B070781`
- **Course Title:** Linear Algebra and Calculus (M3)
- **Assessment Component:** Internal Assessment (Option 1: Animation Video, 10% Weightage)
- **Topic Chosen:** **Systems of Linear Equations ($Ax = b$)**
- **Repository Name:** `M3_AnimationVideo_Concept_E25B070781`
- **Video Output:** `_Video.mp4` (1080p Landscape 16:9, H.264 / AAC)
- **Video Duration:** **Exact 5 Minutes 00 Seconds (`300.000000` s)**
- **Audio Profile:** Complete Synchronized Voiceover Narration (Stereo 48 kHz AAC, Mastered at -25 dB RMS / -2.9 dB True Peak)

---

## 1. One-Sentence Learning Objective
> *"By the end of this video, the viewer will be able to formulate any linear system into the compact matrix equation $Ax = b$, geometrically contrast the Row Picture (intersecting hyperplanes) with the Column Picture (vector synthesis), systematically compute the exact solution using Gaussian Elimination on an augmented matrix, and classify the solution set using matrix rank and column space."*

---

## 2. Deliverables Checklist

| Deliverable | File Path | Status | Verification Details |
|---|---|---|---|
| **Final Video** | [`_Video.mp4`](file:///_Video.mp4) | **Complete** | 1080p (1920×1080), 30 fps, H.264/AAC, **Duration: 05:00.00 (300.0s)**, Size: 17.0 MB. Features Opening Frame and Closing Credits Frame. |
| **Animation Source Code** | [`_Code/`](file:///_Code) | **Complete** | Modular Python scripts using Manim Community v0.22.1 (`main_video.py`, `scene1_hook.py` through `scene6_summary.py`, `components.py`, `render_and_build.py`). |
| **Storyboard Document (PDF)** | [`Storyboard.pdf`](file:///Storyboard.pdf) | **Complete** | 4-page official submission PDF detailing all 6 scenes, timecodes, mathematical plans, and visual actions. |
| **Storyboard Source (MD)** | [`Storyboard.md`](file:///Storyboard.md) | **Complete** | Complete GitHub Flavored Markdown storyboard matrix with Mermaid diagrams and pedagogy. |
| **Narration Voiceover Script** | [`Narration_Script.md`](file:///Narration_Script.md) | **Complete** | Word-for-word timestamped voiceover narration script for Himanshu to record or present live. |
| **Viva / Q&A Prep Guide** | [`Viva_Preparation_Guide.md`](file:///Viva_Preparation_Guide.md) | **Complete** | Comprehensive oral defense preparation covering derivations, rank-nullity, column space, and code walk-through. |

---

## 3. The 6-Scene Narrative Structure

```mermaid
flowchart LR
    S1["Scene 1 (0:00 - 0:45)\nHook & Motivation\nReal-World Systems"] --> S2["Scene 2 (0:45 - 1:30)\nMatrix Formulation\nAx = b Decomposition"]
    S2 --> S3["Scene 3 (1:30 - 2:30)\nGeometric Intuition\nRow vs Column Picture"]
    S3 --> S4["Scene 4 (2:30 - 3:35)\nWorked Example\nGaussian Elimination"]
    S4 --> S5["Scene 5 (3:35 - 4:25)\nInterpretation\nTaxonomy & Col(A)"]
    S5 --> S6["Scene 6 (4:25 - 5:00)\nTakeaways & Credits\nOpening/Closing Frames"]
```

### Detailed Breakdown

#### **Scene 1: Hook / Context & Opening Frame (0:00 - 0:45 | 45.0s)**
- **Opening Title Frame (0:00 - 0:11):** Official course identification, project option, student identity (Himanshu, URN: E25B070781), and topic title.
- **Real-World Motivation (0:11 - 0:26):** Simultaneous linear balance in electrical circuits (Kirchhoff's Laws), traffic network flow conservation, and 3D robotics kinematics.
- **The Core Challenge (0:26 - 0:45):** Why individual equations fail to scale, and how matrix algebra provides a unified geometric language.

#### **Scene 2: Concept Introduction : Formulating $Ax = b$ (0:45 - 1:30 | 45.0s)**
- **System of Equations:**
  $$\begin{cases} 2x_1 - x_2 = 1 \\ x_1 + x_2 = 5 \end{cases}$$
- **Modular Factorization:**
  $$\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \end{bmatrix}$$
  - $A \in \mathbb{R}^{2 \times 2}$: Coefficient Matrix (Linear transformation operator).
  - $\mathbf{x} \in \mathbb{R}^{2 \times 1}$: Vector of unknown state variables.
  - $\mathbf{b} \in \mathbb{R}^{2 \times 1}$: Target constraint vector in the codomain.
- **Duality Foundations:** Row Dot Product view ($\mathbf{r}_i \cdot \mathbf{x} = b_i$) vs Column Combination view ($\sum x_j \mathbf{a}_j = \mathbf{b}$).

#### **Scene 3: Geometric Intuition : The Row Picture vs The Column Picture (1:30 - 2:30 | 60.0s)**
- **Part A (The Row Picture):**
  - Line $L_1$: $x_2 = 2x_1 - 1$ (Cyan).
  - Line $L_2$: $x_2 = 5 - x_1$ (Amber).
  - The solution is the geometric **point of intersection**: $(x_1=2, x_2=3)$.
- **Part B (The Column Picture):**
  - Column 1: $\mathbf{a}_1 = [2, 1]^T$ (Green); Column 2: $\mathbf{a}_2 = [-1, 1]^T$ (Purple).
  - Scaling: $2\mathbf{a}_1 = [4, 2]^T$.
  - Head-to-tail addition: $[4, 2]^T + 3[-1, 1]^T = [4-3, 2+3]^T = [1, 5]^T = \mathbf{b}$.
  - Target vector $\mathbf{b}$ (Gold) is reached via linear combination of basis columns.

#### **Scene 4: Worked Example : Step-by-Step Gaussian Elimination (2:30 - 3:35 | 65.0s)**
- **Augmented Matrix $[A \mid b]$ Setup:**
  $$\left[\begin{array}{cc|c} 2 & -1 & 1 \\ 1 & 1 & 5 \end{array}\right]$$
- **Step 1 (Row Swap $R_1 \leftrightarrow R_2$):** Select leading pivot 1.
  $$\left[\begin{array}{cc|c} 1 & 1 & 5 \\ 2 & -1 & 1 \end{array}\right]$$
- **Step 2 (Elimination $R_2 \leftarrow R_2 - 2R_1$):**
  - $2 - 2(1) = 0$
  - $-1 - 2(1) = -3$
  - $1 - 2(5) = -9$
  $$\left[\begin{array}{cc|c} 1 & 1 & 5 \\ 0 & -3 & -9 \end{array}\right] \quad \text{(Row Echelon Form)}$$
- **Step 3 (Normalization $R_2 \leftarrow -\frac{1}{3}R_2$):**
  $$\left[\begin{array}{cc|c} 1 & 1 & 5 \\ 0 & 1 & 3 \end{array}\right] \implies x_2 = 3$$
- **Step 4 (Back-Substitution $R_1 \leftarrow R_1 - R_2$):**
  $$\left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 3 \end{array}\right] \implies \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
- **Verification:** Both original equations and vector additions verified with 100% precision.

#### **Scene 5: Interpretation : Solution Set Taxonomy & Column Space (3:35 - 4:25 | 50.0s)**
- **The Three Solution Regimes:**
  1. **Unique Solution:** Lines intersect at 1 point; $\det(A) \neq 0$; $\text{rank}(A) = \text{rank}([A \mid b]) = n$.
  2. **Infinitely Many Solutions:** Lines coincide; free variables exist; $\text{rank}(A) = \text{rank}([A \mid b]) < n$.
  3. **No Solution (Inconsistent):** Parallel distinct lines; contradiction $[0 \dots 0 \mid c]$; $\text{rank}(A) < \text{rank}([A \mid b])$.
- **The Fundamental Solvability Principle:**
  $$A\mathbf{x} = \mathbf{b} \text{ is consistent } \iff \mathbf{b} \in \text{Col}(A)$$

#### **Scene 6: Summary, Takeaways, Viva Prep & Closing Credits (4:25 - 5:00 | 35.0s)**
- **3 Core Takeaways:** Duality, Invariance of EROs, and Column Space Solvability.
- **Viva Preparation Tips:** Pivots, rank-nullity, and homogeneous null space.
- **Official Closing Frame:** Course details, student credentials (Himanshu, E25B070781), tool credits, and AI disclosure.

---

## 4. Repository Structure

```
M3_AnimationVideo_Concept_E25B070781/
├── _Video.mp4                      # Final 1080p MP4 animation video (Exact 5:00.00)
├── Storyboard.pdf                  # 4-Page official submission Storyboard PDF
├── Storyboard.md                   # Full Markdown Storyboard document
├── Narration_Script.md             # Complete word-for-word voiceover script with timestamps
├── Viva_Preparation_Guide.md       # Comprehensive Q&A and viva oral examination guide
├── README.md                       # Repository overview & project documentation
└── _Code/
    ├── components.py               # Reusable mathematical UI components (Matrices, Brackets, Cards)
    ├── scene1_hook.py              # Scene 1: Hook, Context & Opening Title (45.0s)
    ├── scene2_concept.py           # Scene 2: Concept Introduction (Ax = b) (45.0s)
    ├── scene3_intuition.py         # Scene 3: Row Picture vs Column Picture (60.0s)
    ├── scene4_worked_example.py    # Scene 4: Step-by-Step Gaussian Elimination (65.0s)
    ├── scene5_interpretation.py    # Scene 5: Solution Taxonomy & Column Space (50.0s)
    ├── scene6_summary.py           # Scene 6: Key Takeaways & Closing Credits (35.0s)
    ├── main_video.py               # Unified script sequencing all 6 scenes
    ├── generate_audio.py           # Ambient soundtrack synthesis script (-24 dB)
    ├── generate_storyboard_pdf.py  # Storyboard PDF compilation script
    └── render_and_build.py         # Complete automated rendering & ffmpeg pipeline
```

---

## 5. How to Reproduce & Build from Source

### Prerequisites
- macOS or Linux with **Python 3.10+**
- **Manim Community Edition** (`pip install manim` or `brew install manim`)
- **FFmpeg** (`brew install ffmpeg` or `sudo apt install ffmpeg`)
- Python packages: `numpy`, `scipy`, `pillow`

### One-Command Full Build
To re-render all 6 scenes, verify timings, synthesize the audio, and produce `_Video.mp4`:
```bash
python3 _Code/render_and_build.py
```

### Running Individual Scenes (Fast Preview)
```bash
# Render Scene 3 in 480p preview:
manim -ql _Code/scene3_intuition.py Scene3Intuition

# Render Scene 4 in 1080p30:
manim -qh -r 1920,1080 --fps 30 _Code/scene4_worked_example.py Scene4WorkedExample
```

### Regenerating Storyboard PDF
```bash
python3 _Code/generate_storyboard_pdf.py
```

---

## 6. Mathematical Verification & Proof of Soundness

1. **System Solvability:**
   $$\det\begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} = (2)(1) - (-1)(1) = 2 + 1 = 3 \neq 0$$
   Since $\det(A) = 3 \neq 0$, the matrix $A$ is invertible, guaranteeing a unique solution.
2. **Matrix Inverse:**
   $$A^{-1} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix}$$
   $$\mathbf{x} = A^{-1} \mathbf{b} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 5 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 1(1) + 1(5) \\ -1(1) + 2(5) \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 6 \\ 9 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$$
3. **Column Space Inclusion:**
   $$2 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 3 \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix} + \begin{pmatrix} -3 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix} = \mathbf{b} \in \text{Col}(A)$$

---

## 7. AI & Tool Disclosures
In accordance with course guidelines:
- **Animation Framework:** [Manim Community v0.22.1](https://www.manim.community/)
- **Audio Engineering:** Custom synthesized ambient audio using Python (`numpy`, `wave`, `struct`)
- **Video Encoding:** [FFmpeg](https://ffmpeg.org/) (H.264 video stream, AAC stereo audio stream)
- **AI Tool Disclosure:** Antigravity AI was utilized to assist in scene timing calculations, visual composition scripting, and generating documentation. All mathematical formulas, derivations, and solutions were independently verified.

---

*Submitted by Himanshu (URN: E25B070781) for the M3 Linear Algebra Internal Assessment.*
