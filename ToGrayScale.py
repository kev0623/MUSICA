from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Open the image file
    with Image.open(input_image_path) as image:
        # Convert the image to grayscale
        grayscale_image = image.convert("L")
        # Save the grayscale image
        grayscale_image.save(output_image_path)
        print(f"Grayscale image saved as {output_image_path}")

# Example usage
input_image_path = "Input/" + "4.png"
output_image_path = "Input/" + "4_grayscale_image.jpg"
convert_to_grayscale(input_image_path, output_image_path)