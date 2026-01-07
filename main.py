import numpy as np
from PIL import Image
# ייבוא הפונקציות שכתבת ב-image_utils
from image_utils import load_image, edge_detection

def main():
    # 1. נתיב לתמונה המקורית (וודאי שהקובץ lena.jpg נמצא באותה תיקייה)
    input_path = 'lena.jpg'
    output_path = 'lena_edges.jpg'
    
    try:
        # 2. טעינת התמונה באמצעות הפונקציה שמימשת
        print(f"Loading image: {input_path}...")
        original_image_array = load_image(input_path)
        
        # 3. ביצוע זיהוי קצוות
        print("Performing edge detection...")
        edges_array = edge_detection(original_image_array)
        
        # 4. המרת המערך חזרה לאובייקט תמונה של PIL כדי שנוכל לשמור/להציג
        edges_image = Image.fromarray(edges_array)
        
        # 5. שמירת התמונה התוצאה
        edges_image.save(output_path)
        print(f"Success! Edge-detected image saved as: {output_path}")
        
        # הצגת התמונה (אופציונלי - יפתח את מציג התמונות במחשב)
        # edges_image.show()

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found. Please make sure it's in the project folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
