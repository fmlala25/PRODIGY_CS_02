from PIL import Image

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()  # Access pixels of the image

    # Encrypt the image by modifying pixel values
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel
            # Encrypt each channel using XOR with the key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)  # Save the encrypted image
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    # Decrypt the image by reversing pixel value changes
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Decrypt by applying XOR with the same key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Example usage
encrypt_image('original_image.png', 'encrypted_image.png', key=123)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=123)
