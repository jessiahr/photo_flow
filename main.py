import subprocess
import os
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


def run():
    for file in os.listdir(input_path):
        path = input_path + "/" + file
        print(f"Exporting [{path}]")
        export_asset(path)

        
def export_asset(path):
    cmd = f"squoosh-cli --resize '{resize_settings}' {export_mode} '{export_settings}' -d {output_path} {input_path}"
    print(cmd)
    subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
run()