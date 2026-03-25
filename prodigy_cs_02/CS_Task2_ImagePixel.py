from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        # Open image
        original_image = Image.open(image_path)

        # Convert to array
        image_array = np.array(original_image)

        # XOR encryption (lossless)
        encrypted_array = image_array ^ key

        # Save encrypted image
        encrypted_image = Image.fromarray(np.uint8(encrypted_array))
        encrypted_image.save("encrypted_image.png")

        print(" Image encrypted successfully!")
        print("Saved as: encrypted_image.png")

    except Exception as e:
        print("Error:", e)


def decrypt_image(image_path, key):
    try:
        # Open encrypted image
        encrypted_image = Image.open(image_path)

        # Convert to array
        encrypted_array = np.array(encrypted_image)

        # XOR decryption (same operation)
        decrypted_array = encrypted_array ^ key

        # Save decrypted image
        decrypted_image = Image.fromarray(np.uint8(decrypted_array))
        decrypted_image.save("decrypted_image.png")

        print(" Image decrypted successfully!")
        print("Saved as: decrypted_image.png")

    except Exception as e:
        print("Error:", e)


def encrypt_choice():
    try:
        key = int(input("Enter encryption key (number): "))
        image_path = input("Enter image path: ")
        encrypt_image(image_path, key)
    except ValueError:
        print(" Please enter a valid number for key!")
        encrypt_choice()


def decrypt_choice():
    try:
        key = int(input("Enter decryption key (same as encryption key): "))
        image_path = input("Enter encrypted image path: ")
        decrypt_image(image_path, key)
    except ValueError:
        print(" Please enter a valid number for key!")
        decrypt_choice()


def main():
    while True:
        print("\nSelect an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")

        choice = input("Your choice: ").lower()

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()