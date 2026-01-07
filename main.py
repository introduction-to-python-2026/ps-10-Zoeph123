import numpy as np
from PIL import Image
from image_utils import load_image, edge_detection

def main():
    input_path = 'lena.jpg'
    output_path = 'lena_edges.jpg'
    
    try:
        print(f"Loading image: {input_path}...")
        original_image_array = load_image(input_path)
        
        print("Performing edge detection...")
        edges_array = edge_detection(original_image_array)
        
        edges_image = Image.fromarray(edges_array)
        
        edges_image.save(output_path)
        print(f"Success! Edge-detected image saved as: {output_path}")
        

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found. Please make sure it's in the project folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
