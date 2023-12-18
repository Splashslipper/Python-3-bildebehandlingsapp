from PIL import Image, ImageOps
import pilgram
import os


file_path = input("Enter the path of your image file: ")


if not os.path.isfile(file_path):
    print("File not found. Exiting.")
    exit()


want_rotate = input("Do you want to rotate the image? Y/N: ")
if want_rotate.lower() == "y":
    direction = int(input("How much do you want to rotate the image?: "))
    image = Image.open(file_path).rotate(direction)
else:
    image = Image.open(file_path)


want_style = input("Do you want to style your image? Y/N: ")
if want_style.lower() == "y":
    print("Which of these styles do you want, _1977,", "aden,", "brannan,", "brooklyn,", "clarendon,", "earlybird,", "gingham,", "hudson,",
                 "inkwell,", "kelvin,", "lark,", "lofi,", "maven,", "mayfair,", "moon,", "nashville,",
                 "perpetua,", "reyes,", "rise,", "slumber,", "stinson,", "toaster,", "valencia,",
                 "walden,", "willow,", "xpro2,")
    style = input("What style do you want? ")

    if style in ["_1977", "aden", "brannan", "brooklyn", "clarendon", "earlybird", "gingham", "hudson",
                 "inkwell", "kelvin", "lark", "lofi", "maven", "mayfair", "moon", "nashville",
                 "perpetua", "reyes", "rise", "slumber", "stinson", "toaster", "valencia",
                 "walden", "willow", "xpro2"]:
        image = getattr(pilgram, style)(image)
    else:
        print("Invalid style, please choose from one of the above.")


want_width = input("Do you want to change the resolution of your image? Y/N: ")
if want_width.lower() == "y":
    width = int(input("Please input a width of the image that's above 1080: "))
    while width < 1080:
        print("Please input a value above 1080:")
        width = int(input("Please input a width of the image that's above 1080: "))
    height = int(input("Please input a height of the image: "))
    image = image.resize((width, height))


want_frame = input("Do you want to frame your image? Y/N: ")
if want_frame.lower() == "y":
    frame_color = input("What color do you want your border to be?: ")
    frame_size = int(input("How big do you want your border to be?: "))
    image = ImageOps.expand(image, border=frame_size, fill=frame_color)


want_save_folder = input("Do you want to save the final image to a folder? Y/N: ")
if want_save_folder.lower() == "y":
    folder_path = input("Enter the path of the folder where you want to save the image: ")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    imagename = input("Enter the name for your image (without extension): ")
    final_path = os.path.join(folder_path, imagename + ".jpg")
    image = image.convert('RGB')
    final_path = os.path.join(folder_path, imagename + ".jpg")
    image.save(final_path)

    image.save(final_path)
    print(f"Image saved to {final_path}")
else:
    print("No save folder specified. Exiting.")


