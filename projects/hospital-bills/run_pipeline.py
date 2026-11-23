"""Master automated execution script for Stickman Systems: Episode #03
Run from projects/hospital-bills/ or pass project path.
"""
import os, sys, subprocess, argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.expanduser(r"~\.claude\skills")
STICK_SKILL = os.path.join(SKILLS_DIR, "stickman-hybrid")
VOX_SKILL = os.path.join(SKILLS_DIR, "vox-doc-sound")

def run(cmd, env=None):
    print(f"--> Running: {cmd}")
    cur_env = os.environ.copy()
    cur_env["USE_TF"] = "0"
    winget_links = r"C:\Users\Lenovo\AppData\Local\Microsoft\WinGet\Links"
    if winget_links not in cur_env.get("PATH", ""):
        cur_env["PATH"] = winget_links + ";" + cur_env.get("PATH", "")
    if env:
        cur_env.update(env)
    res = subprocess.run(cmd, shell=True, cwd=BASE_DIR, env=cur_env)
    if res.returncode != 0:
        print(f"Command failed with exit code {res.returncode}")
        return False
    return True

def generate_voice_kokoro(voice="am_michael", speed=1.0):
    print(f"\n[1/3] Generating voice takes with Kokoro ({voice})...")
    kokoro_script = os.path.join(VOX_SKILL, "scripts", "kokoro_vo.py")
    if not run(f'python "{kokoro_script}" LINES.tsv --lang a --voice {voice} --speed {speed} --out takes'):
        return False
    
    print("\n[2/3] Joining voice takes into VO.wav with vo_join.py...")
    join_script = os.path.join(VOX_SKILL, "scripts", "vo_join.py")
    if not run(f'python "{join_script}" takes LINES.tsv --out VO --preset foreign'):
        return False
    
    print("\n[3/3] Aligning speech to words with faster-whisper (align.py)...")
    align_script = os.path.join(VOX_SKILL, "scripts", "align.py")
    if not run(f'python "{align_script}" --vo VO.wav --lines VO.tsv --out WORDS.tsv --lang en --model tiny'):
        return False
    
    print("\n[SUCCESS] Voice generation & word alignment complete: VO.wav, VO.tsv, WORDS.tsv ready.")
    return True

def mix_audio():
    mix_script = os.path.join(VOX_SKILL, "scripts", "mix.py")
    print("\nMixing VO, music bed, and SFX with mix.py...")
    return run(f'python "{mix_script}" cues.tsv --vo VO.wav --lines VO.tsv --words WORDS.tsv --out mix.wav')

def submit_flow(test_only=False):
    pictures_script = os.path.join(STICK_SKILL, "scripts", "pictures.py")
    if test_only:
        print("\nSubmitting 2 test shots to Google Flow (Nano Banana 2)...")
        return run(f'python "{pictures_script}" submit 1 4')
    else:
        print("\nSubmitting all shots in SHOTS.tsv to Google Flow...")
        return run(f'python "{pictures_script}" submit')

def submit_elements():
    pictures_script = os.path.join(STICK_SKILL, "scripts", "pictures.py")
    print("\nSubmitting sticker elements to Google Flow...")
    return run(f'python "{pictures_script}" elements')

def render_video():
    render_script = os.path.join(STICK_SKILL, "scripts", "render.py")
    print("\nChecking pacing and rendering video...")
    run(f'python "{render_script}" --pacing')
    return run(f'python "{render_script}" --out hospital-bills.mp4')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stickman Systems Episode #03 Automation Runner")
    parser.add_argument("--voice", choices=["kokoro", "kaggle"], default=None, help="Generate voice track")
    parser.add_argument("--mix", action="store_true", help="Mix audio bed and SFX")
    parser.add_argument("--flow-test", action="store_true", help="Submit 2 test shots to Google Flow")
    parser.add_argument("--flow-all", action="store_true", help="Submit all shots to Google Flow")
    parser.add_argument("--elements", action="store_true", help="Generate sticker elements")
    parser.add_argument("--render", action="store_true", help="Render final video")
    args = parser.parse_args()

    if args.voice == "kokoro":
        generate_voice_kokoro()
    elif args.mix:
        mix_audio()
    elif args.flow_test:
        submit_flow(test_only=True)
    elif args.flow_all:
        submit_flow(test_only=False)
    elif args.elements:
        submit_elements()
    elif args.render:
        render_video()
    else:
        print("Usage:")
        print("  python run_pipeline.py --voice kokoro   # Generate English voiceover + WORDS.tsv")
        print("  python run_pipeline.py --mix            # Mix VO.wav + cues.tsv into mix.wav")
        print("  python run_pipeline.py --flow-test      # Submit 2 test shots to Google Flow")
        print("  python run_pipeline.py --flow-all       # Submit full batch to Google Flow")
        print("  python run_pipeline.py --elements       # Generate cutout sticker elements")
        print("  python run_pipeline.py --render         # Render pacing check and final MP4")
