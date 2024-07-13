# ADB Scrcpy Connector

This script connects an Android device via ADB over USB and then switches to a wireless connection. It then starts Scrcpy in fullscreen mode.

## Prerequisites

- Python 3.x
- ADB (Android Debug Bridge)
- Scrcpy

### Installation

#### macOS

1. **Install Homebrew** (if not already installed):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install ADB and Scrcpy:
   ```sh
    brew install android-platform-tools scrcpy

#### Windows
Download and Install ADB:

Go to Google's SDK Platform Tools and download the ZIP file.
Extract the ZIP file to a directory (e.g., C:\platform-tools).
Download and Install Scrcpy:

Go to Genymobile Scrcpy releases and download the latest release.
Extract the ZIP file to a directory (e.g., C:\scrcpy).

### Usage
Ensure your Android device has USB debugging enabled.

Go to Settings -> About phone -> Tap Build number seven times to unlock developer mode.
Go to Settings -> Developer options -> Enable USB debugging.
Connect your device via USB.

Update the adb_path in the script according to your OS:

- For macOS: /opt/homebrew/bin/adb
- For Windows: C:\\path\\to\\adb.exe (e.g., C:\\platform-tools\\adb.exe)
Enter the IP address of your Android device when prompted.

## Script Description

1. Set ADB to listen over TCP/IP on port 5555:
  ```py
  subprocess.run([adb_path, "tcpip", "5555"], check=True)
```
2. Connect to the device via USB to enable USB debugging:
  ```py
  connect_to_device_wired(adb_path)
```
3. Wait for a few seconds to ensure USB debugging is enabled:
```py
time.sleep(5)
```
4. Connect wirelessly using the provided IP address:
```py
connect_to_device_wireless(device_ip, adb_path)
```
5. Start Scrcpy in fullscreen mode:
```py
start_scrcpy_fullscreen()
```

#### Example Python Output:
```py
Connecting to device via USB...
Successfully connected to device via USB.
Enter the IP address of your Android device: 192.168.1.2
Connecting to device wirelessly...
Successfully connected to device wirelessly.
Starting Scrcpy...
Scrcpy started successfully in fullscreen mode.
```
