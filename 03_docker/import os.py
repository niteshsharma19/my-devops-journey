import os 

while True:
    print(
        """
        -------------------------------------
          DOCKER MENU BASED PROGRAM
        -------------------------------------
        
        1 . Launch new container 
        2 . Stop the container 
        3 . Remove the container 
        4 . Start the container 
        5 . List image 
        6 . List all Containers
        7 . Exit
        """
    )
    choice = input("Enter the choice : ")

    if choice == "1":
        name = input("Enter the container name: ")
        image = input("Enter the name of image: ")
        os.system(f"docker run -dit --name {name} {image}")

    elif choice == "2":
        name = input("Enter the container name: ")
        os.system(f"docker stop {name}")

    elif choice == "3":
        name = input("Enter the container name: ")
        os.system(f"docker rm {name}")

    elif choice == "4":
        name = input("Enter the container name: ")
        os.system(f"docker start {name}")

    elif choice == "5":
        os.system("docker image ls")

    elif choice == "6":
        os.system("docker ps -a")

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("❌ Enter the proper option.")
