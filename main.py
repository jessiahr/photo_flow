import subprocess
import os
from pathlib import Path
resize_settings = """
{
"enabled": true,
"width": 1920,
"height": 1281,
"method": "lanczos3",
"fitMethod": "stretch",
"premultiply": true,
"linearRGB": true
}
""".replace("\n", "")
export_settings = """
{
"quality": 75,
"target_size": 0,
"target_PSNR": 0,
"method": 4,
"sns_strength": 50,
"filter_strength": 60,
"filter_sharpness": 0,
"filter_type": 1,
"partitions": 0,
"segments": 4,
"pass": 1,
"show_compressed": 0,
"preprocessing": 0,
"autofilter": 0,
"partition_limit": 0,
"alpha_compression": 1,
"alpha_filtering": 1,
"alpha_quality": 100,
"lossless": 0,
"exact": 0,
"image_hint": 0,
"emulate_jpeg_size": 0,
"thread_level": 0,
"low_memory": 0,
"near_lossless": 100,
"use_delta_palette": 0,
"use_sharp_yuv": 0
}
""".replace("\n", "")
export_mode = "--webp"
input_path = "./input"
output_path = "./output"
def setup():
    Path(input_path).mkdir(exist_ok=True)
    Path(output_path).mkdir(exist_ok=True)

def run():
    for file in os.listdir(input_path):
        path = input_path + "/" + file
        try: 
            if file == ".DS_Store":
                print(f"Skipping [{path}]")
                continue
            print(f"Exporting [{path}]")
            export_asset(input_path,file)
        except (RuntimeError, TypeError, NameError) as e:
            print(f"Error exporting {path}: {e} --- Skipped")
            continue


def export_asset(path, file):
    cmd = f"squoosh-cli --resize '{resize_settings}' {export_mode} '{export_settings}' -d {output_path} {path}/{file}"
    subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    output_file = os.path.splitext(file)[0] + "." + export_mode.removeprefix("--")
    size_before = os.path.getsize(Path(path, file))
    size_after = os.path.getsize(Path(output_path, output_file))
    delta = size_before - size_after
    print(f"Removed {'{:,}'.format(delta)} bytes ({'{:.1%}'.format( delta / size_before)} %)\n")
    
setup()
run()