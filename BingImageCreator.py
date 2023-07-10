import argparse
import os
from BingImageCreator import ImageGen

def main():
    parser = argparse.ArgumentParser()    
    # default to specify the number of images to download
    parser.add_argument("--download-count", help="Number of images to download", type=int, default=2)
    args = parser.parse_args()

    # Prompt 
    prompt = "Timmy dodging a tricky monkey while playing soccer."

    # Create a BingImageCreator instance for image generation
    auth_cookie = "YOUR_AUTH_COOKIE"
    image_generator = ImageGen(auth_cookie)

    try:
        # Get image link
        image_links = image_generator.get_images(prompt)

        # Create image storage directory
        output_dir = "YOUR_DIRECTORY_ADDRESS"

        # Download and save images
        image_generator.save_images(
            links=image_links,
            output_dir=output_dir,
            download_count=args.download_count
        )

        print(f"{args.download_count} images downloaded and saved in {output_dir}")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
