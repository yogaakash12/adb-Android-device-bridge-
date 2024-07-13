import subprocess
import sys
import time

def connect_to_device_wired(adb_path):
    print("Connecting to device via USB...")
    try:
        subprocess.call([adb_path, "usb"])
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to device via USB: {e}")
        sys.exit(1)

def connect_to_device_wireless(device_ip, adb_path):
    print("Connecting to device wirelessly...")
    try:
        subprocess.call([adb_path, "connect", device_ip])
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to device wirelessly: {e}")
        sys.exit(1)

def start_scrcpy_fullscreen():
    print("Starting Scrcpy...")
    try:
        subprocess.call(["scrcpy", "--fullscreen"])
    except subprocess.CalledProcessError as e:
        print(f"Error starting Scrcpy: {e}")
        sys.exit(1)

if __name__ == "__main__":
    adb_path = "/opt/homebrew/bin/adb"  # Replace with the actual path to adb on your system

    # Set ADB to listen over TCP/IP on port 5555
    subprocess.call([adb_path, "tcpip", "5555"])

    # Connect via USB first to enable USB debugging
    connect_to_device_wired(adb_path)

    # Wait for a few seconds to ensure USB debugging is enabled
    time.sleep(5)

    # Then, connect wirelessly
    device_ip = input("Enter the IP address of your Android device: ")
    connect_to_device_wireless(device_ip, adb_path)
    start_scrcpy_fullscreen()
