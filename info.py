#!/usr/bin/env python3
# IP Information Lookup Tool

import os
import requests

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display the large LORD header"""
    print("\033[1;36m")  # Cyan color
    print("   _                  ")
    print("  | |                 ")
    print("  | | ___  _ __   ___ ")
    print("  | |/ _ \| '_ \ / _ \\")
    print("  | | (_) | | | |  __/")
    print("  |_|\___/|_| |_|\___|")
    print("\033[0m")  # Reset color

def get_ip_info(ip_address):
    """Fetch IP information from API"""
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mError fetching information: {e}\033[0m")
        return None

def display_ip_info(ip_data):
    """Display the IP information"""
    if not ip_data:
        return
        
    print("\n\033[1;32mIP Information:\033[0m")
    print(f"IP Address: {ip_data.get('ip', 'N/A')}")
    print(f"Hostname: {ip_data.get('hostname', 'N/A')}")
    print(f"City: {ip_data.get('city', 'N/A')}")
    print(f"Region: {ip_data.get('region', 'N/A')}")
    print(f"Country: {ip_data.get('country', 'N/A')}")
    print(f"Location: {ip_data.get('loc', 'N/A')}")
    print(f"Organization: {ip_data.get('org', 'N/A')}")
    print(f"Postal Code: {ip_data.get('postal', 'N/A')}")
    print(f"Timezone: {ip_data.get('timezone', 'N/A')}")

def main():
    clear_screen()
    display_header()
    
    # Get IP address from user
    print("\033[1;33m")  # Yellow color
    ip_address = input("Please enter an IP address: ")
    print("\033[0m")  # Reset color
    
    if not ip_address:
        print("\033[1;31mNo IP address entered!\033[0m")
        return
    
    print(f"\n\033[1;32mFetching information for {ip_address}...\033[0m\n")
    
    ip_data = get_ip_info(ip_address)
    display_ip_info(ip_data)

if __name__ == "__main__":
    main()
