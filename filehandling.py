new_content = input("Enter your content : ")
try:
    with open("devo.txt","w") as file:
        file.write(f"{new_content}\n")
        append_content = input("Enter your content : ")
    with open("devo.txt","a") as file1:
        file1.write(f"{append_content}\n")
    with open("images.jpeg", "rb") as img:
        with open("image.jpeg", "wb") as img1:
            for i in img:
                img1.write(i)    
            else:
                with open("images.jpeg", "rb") as img:
                    binary_data = img.read()  # Read the binary content
                    print("Image copied successfully to 'image.jpeg'.")

except PermissionError as per:
    input(f"Permission error Occured : {per}")
except FileNotFoundError as fn:
    input(f"File not found error occured : {fn}")
    
    