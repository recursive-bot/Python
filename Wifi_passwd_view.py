import subprocess

# Get saved Wi-Fi profiles
profiles = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']
).decode('utf-8').splitlines()

names = [
    line.split(':', 1)[1].strip()
    for line in profiles
    if "All User Profile" in line
]

while True:

    print("\nSaved Wi-Fi Profiles:")
    
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    print("0. Exit")

    try:
        ch = int(input("\nEnter the number of the Wi-Fi profile: "))

        if ch == 0:
            print("Exiting...")
            break

        if ch < 1 or ch > len(names):
            print("Invalid selection. Try again.")
            continue

        wifi = names[ch - 1]

        result = subprocess.check_output(
            f'netsh wlan show profile "{wifi}" key=clear',
            shell=True
        ).decode('utf-8').splitlines()

        for line in result:
            if "Key Content" in line:
                password = line.split(":", 1)[1].strip()
                print(f"\nWi-Fi: {wifi}")
                print(f"Password: {password}")
                break
        else:
            print(f"\nWi-Fi: {wifi}")
            print("Password not found.")

    except ValueError:
        print("Please enter a number.")

    except subprocess.CalledProcessError:
        print("Could not retrieve the Wi-Fi profile.")