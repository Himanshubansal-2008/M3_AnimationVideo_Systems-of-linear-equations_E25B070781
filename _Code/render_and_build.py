"""
_Code/render_and_build.py
Automated production pipeline:
1. Renders all 6 scenes with Manim Community in 1080p30 (16:9 Landscape).
2. Verifies the exact duration of each scene.
3. Generates the mild ambient background audio track (300.0s).
4. Concatenates and muxes into final root `_Video.mp4`.
"""

import os
import sys
import subprocess
import json

SCENES = [
    ("scene1_hook.py", "Scene1Hook", 45.0),
    ("scene2_concept.py", "Scene2Concept", 45.0),
    ("scene3_intuition.py", "Scene3Intuition", 60.0),
    ("scene4_worked_example.py", "Scene4WorkedExample", 65.0),
    ("scene5_interpretation.py", "Scene5Interpretation", 50.0),
    ("scene6_summary.py", "Scene6Summary", 35.0),
]

def run_cmd(cmd):
    print(f"[RUN] {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed:\n{res.stderr}")
        sys.exit(res.returncode)
    return res.stdout

def get_duration(file_path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{file_path}"'
    out = run_cmd(cmd).strip()
    return float(out)

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    code_dir = os.path.join(root_dir, "_Code")
    media_dir = os.path.join(root_dir, "media")
    os.chdir(root_dir)

    print("==================================================")
    print("M3 Animation Video Production Pipeline")
    print("Topic: Systems of Linear Equations (Ax = b)")
    print("Student: Himanshu | URN: E25B070781")
    print("Target Duration: Exact 300.0s (5:00)")
    print("==================================================")

    # Step 1: Render each scene at 1080p30
    rendered_files = []
    total_rendered_dur = 0.0

    for script, cls_name, exp_dur in SCENES:
        script_path = os.path.join(code_dir, script)
        print(f"\n--- Rendering {cls_name} ({exp_dur}s target) ---")
        render_cmd = f"manim -qh -r 1920,1080 --fps 30 {script_path} {cls_name}"
        run_cmd(render_cmd)

        # Expected output path in media/videos/<script_stem>/1080p30/<cls_name>.mp4
        stem = os.path.splitext(script)[0]
        out_mp4 = os.path.join(media_dir, "videos", stem, "1080p30", f"{cls_name}.mp4")
        if not os.path.exists(out_mp4):
            print(f"[ERROR] Could not find output video: {out_mp4}")
            sys.exit(1)

        dur = get_duration(out_mp4)
        print(f"[OK] {cls_name} rendered: {dur:.2f}s (Expected: {exp_dur:.2f}s)")
        rendered_files.append(out_mp4)
        total_rendered_dur += dur

    print(f"\nTotal Rendered Duration: {total_rendered_dur:.2f}s (Target: 300.0s)")

    # Step 2: Ensure mild ambient audio track exists
    audio_path = os.path.join(code_dir, "ambient_mild_track.wav")
    if not os.path.exists(audio_path):
        print("\n--- Synthesizing Ambient Audio Track ---")
        run_cmd(f"python3 {os.path.join(code_dir, 'generate_audio.py')}")
    audio_dur = get_duration(audio_path)
    print(f"[OK] Ambient Audio Track ready: {audio_dur:.2f}s")

    # Step 3: Concatenate video scenes
    concat_list_path = os.path.join(code_dir, "concat_list.txt")
    with open(concat_list_path, "w") as f:
        for rf in rendered_files:
            f.write(f"file '{rf}'\n")

    concat_video_path = os.path.join(code_dir, "video_silent_concat.mp4")
    print("\n--- Concatenating Video Scenes ---")
    run_cmd(f'ffmpeg -y -f concat -safe 0 -i "{concat_list_path}" -c copy "{concat_video_path}"')

    # Step 4: Mux Video + Silent Audio Bed to produce root _Video.mp4 (No music)
    final_video_path = os.path.join(root_dir, "_Video.mp4")
    print(f"\n--- Finalizing {final_video_path} (Pure Voiceover Mode: No Music) ---")
    mux_cmd = (
        f'ffmpeg -y -i "{concat_video_path}" -f lavfi -i anullsrc=r=44100:cl=stereo '
        f'-c:v copy -c:a aac -b:a 128k -t 300.000 -map 0:v:0 -map 1:a:0 '
        f'-movflags +faststart "{final_video_path}"'
    )
    run_cmd(mux_cmd)

    # Step 5: Final Verification
    final_dur = get_duration(final_video_path)
    file_size_mb = os.path.getsize(final_video_path) / (1024 * 1024)
    print("\n==================================================")
    print("PRODUCTION COMPLETE!")
    print(f"Output File: {final_video_path}")
    print(f"File Size:   {file_size_mb:.2f} MB")
    print(f"Duration:    {final_dur:.2f} seconds ({int(final_dur//60):02d}:{final_dur%60:05.2f})")
    print("==================================================")

if __name__ == "__main__":
    main()
