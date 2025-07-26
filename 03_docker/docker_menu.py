import os 
while True:
    print(
    """
    ---------------------------------------------------------------------------------
                           DOCKER MENU BASED PROGRAM
    ---------------------------------------------------------------------------------
    
    1 . Launch new container  5 . List images            09 .  rename image 
    2 . Stop the container    6 . List all Containers    10 . create a image
    3 . Remove the container  7 . remove image           11 .
    4 . start the container   8 . rename container name  12 . exit
    """
    )
    choice = input("Enter the choice : ")
    if choice == "1":
        name = input("Enter name of container : ")
        os.system(f"docker images ")
        image = input ("Enter the name of image : ")
        os.system(f"docker run -dit --name={name} {image}")
    elif choice == "2" :
        os.system(f"docker ps -a ")
        name = input("Enter name of the container  : ")
        os.system(f"docker stop {name}")
    elif choice == "3" :
        os.system(f"docker ps -a ")
        name = input("Enter name of the container : ")
        os.system(f"docker rm -f {name}")
    elif choice == "4" :
        name = input("Enter name of the container : ")
        os.system(f"docker start {name}")
    elif choice == "5" :
        os.system(f"docker images ")
    elif choice == "6":
        os.system(f"docker ps -a ")
    elif choice == "7":
        os.system(f"docker images ")
        image = input ("Enter the name of image : ")
        os.system(f"docker rmi {image} ")
    elif choice == "8":
        os.system(f"docker ps -a ")
        old = input ("Enter the old name of the container : ")
        new =input ("Enter the new name of the container : ")
        os.system(f"docker rename {old} {new} ")
    elif choice == "9":
        os.system(f"docker images ")
        old = input ("Enter the old image name : ")
        new =input ("Enter the new name of image : ")
        os.system(f"docker tag {old} {new} ")
    elif choice == "10":
        os.system(f"docker images ")
        os.system(f"docker ps -a ")
        name = input("Enter name of container : ")
        new =input ("Enter the new name of image : ")
        os.system(f"docker commit {name} {new} ")
    # elif choice == "11":
    #     name = input("Enter name of tool or software : ")
    #     os.system(f"apt install {name}-y ")
    elif choice == "12":
        break
    else:
        print("Enter the proper option")
