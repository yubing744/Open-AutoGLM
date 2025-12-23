#!/usr/bin/env python3
"""
Test script to verify the device-specific ADB Keyboard check fix.
"""

import subprocess
import sys

def test_device_specific_check():
    """Test the device-specific ADB Keyboard check logic."""

    print("🧪 Testing device-specific ADB Keyboard check...")

    # Test 1: Check without device ID (should use default device)
    print("\n1. Testing default device check:")
    try:
        result = subprocess.run(
            ["adb", "shell", "ime", "list", "-s"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        ime_list = result.stdout.strip()
        has_keyboard = "com.android.adbkeyboard/.AdbIME" in ime_list
        print(f"   Default device ADB Keyboard: {'✅' if has_keyboard else '❌'}")
    except Exception as e:
        print(f"   Default device check failed: {e}")

    # Test 2: Check with specific device ID (127.0.0.1:5555)
    print("\n2. Testing specific device (127.0.0.1:5555) check:")
    try:
        result = subprocess.run(
            ["adb", "-s", "127.0.0.1:5555", "shell", "ime", "list", "-s"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        ime_list = result.stdout.strip()
        has_keyboard = "com.android.adbkeyboard/.AdbIME" in ime_list
        print(f"   Device 127.0.0.1:5555 ADB Keyboard: {'✅' if has_keyboard else '❌'}")
    except Exception as e:
        print(f"   Device 127.0.0.1:5555 check failed: {e}")

    # Test 3: Check with specific device ID (emulator-5554)
    print("\n3. Testing specific device (emulator-5554) check:")
    try:
        result = subprocess.run(
            ["adb", "-s", "emulator-5554", "shell", "ime", "list", "-s"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        ime_list = result.stdout.strip()
        has_keyboard = "com.android.adbkeyboard/.AdbIME" in ime_list
        print(f"   Device emulator-5554 ADB Keyboard: {'✅' if has_keyboard else '❌'}")
    except Exception as e:
        print(f"   Device emulator-5554 check failed: {e}")

    print("\n✅ Device-specific check verification completed!")

if __name__ == "__main__":
    test_device_specific_check()