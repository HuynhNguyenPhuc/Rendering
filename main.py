from PIL import Image

def convert(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            img.save(output_file)
        print(f"Image saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_files = ["results/single_light_source_output.ppm", "results/multiple_light_sources_output.ppm"]
    output_files = ["results/single_light_source_output.png", "results/multiple_light_sources_output.png"]
    
    for input_file, output_file in zip(input_files, output_files):
        convert(input_file, output_file)