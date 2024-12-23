# WifiCrack
This Python script scans for available Wi-Fi networks, generates potential passwords, and attempts to connect to them using a brute-force method. 

Features
--------

*   **Wi-Fi Scanning**: Identifies available Wi-Fi networks using the pywifi library, removing duplicate SSIDs.
    
*   **Password Management**: Loads existing passwords, generates new ones based on user input and common patterns, and saves them to a file.
    
*   **Brute-Force Connection Attempt**: Tries to connect to networks using stored passwords and logs attempts.
    
*   **Logging and Feedback**: Displays progress and discovered passwords clearly in the console.
    

Installation
------------

1.  git clone https://github.com/yourusername/wifi-cracker.gitcd wifi-cracker
    
2.  pip install pywifi
    
3.  Ensure you have a compatible wireless adapter capable of monitoring and connecting to networks.
    

Usage
-----

1.  python wifi\_cracker.py
    
2.  Follow the prompts:
    
    *   Review the list of available networks.
        
    *   Provide keywords and numbers to generate potential passwords.
        
    *   Wait as the script attempts to connect to the networks.
        
3.  Check the results:
    
    *   Discovered passwords are displayed in the console.
        
    *   All passwords (new and existing) are saved in password\_list.txt.
        

File Structure
--------------

Plain 
`.  ├── wifi_cracker.py       # Main script file
    ├── password_list.txt     # File containing password list (auto-generated)
    └── README.md             # Documentation file   `

Example Output
--------------

`   Wi-Fi Interface Name: wlan0  Scanning for available networks...  Available Networks:   - Network1   - Network2  For network 'Network1':  Enter possible keywords (comma-separated): admin, password  Enter possible numbers (comma-separated): 1234, 5678  New passwords added to 'password_list.txt'.  Attempting to crack password-protected networks...  Trying password 'admin1234' for network 'Network1'...  Trying password '1234admin' for network 'Network1'...  Password found! Wi-Fi network 'Network1' has the password: admin1234  ********** Discovered Passwords **********  WIFI NETWORK      PASSWORD  Network1          admin1234   `

Notes
-----

*   **Disclaimer**: This script is for educational purposes only. Ensure you have the owner's consent before attempting to access a Wi-Fi network.
    
*   **Compatibility**: Tested on Python 3.8+ with the pywifi library.
    
*   **Improvements**: Contributions are welcome! Feel free to fork the repository and submit a pull request.
    

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
