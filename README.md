# OpenVPN Auto Connect with OTP

This project provides a macOS shortcut application that automates the process of connecting to OpenVPN using an OTP (One-Time Password) generated from a secret key stored in the macOS Keychain.

## Installation and Setup

### 1. Install OpenVPN Connect

First, install the OpenVPN Connect client on your macOS using Homebrew:

```bash
brew install openvpn-connect
```

### 2. Open OpenVPN and Import VPN Profile

- Launch the OpenVPN Connect application.
- Import your VPN profile into OpenVPN Connect.

### 3. Configure Keychain for VPN Profile

If your VPN profile is user-locked and requires a password, you need to set up the macOS Keychain to store your VPN credentials:

1. Store your secret key in the Keychain:

   ```bash
   security add-generic-password -a "username" -s "vpn_secret" -w "your-secret-key"
   ```

2. Store your PIN in the Keychain:

   ```bash
   security add-generic-password -a "username" -s "vpn_pin" -w "your-pin"
   ```

Make sure to replace `"username"`, `"vpn_secret"`, `"vpn_pin"`, `"your-secret-key"`, and `"your-pin"` with your actual values.

### 4. Customize the Scripts

You need to customize the Python and AppleScript files for your environment:

1. **gen_otp.py**:
   - Update the following variables with your own values:
     - `username`
     - `vpn_secret`
     - `vpn_pin`

2. **connect_vpn.applescript**:
   - Update the paths to point to the correct location of your Python installation and the `gen_otp.py` script:
     ```applescript
     set otpCode to do shell script "path/to/python /path/to/gen_otp.py"
     ```

### 5. Create a Shortcut in the Menu Bar and Pin to Dock

1. Open the Shortcuts app on your Mac.
2. Select the "Menu Bar" section.
3. Create a new shortcut.
4. Add the "Run AppleScript" action.
5. Copy the contents of `connect_vpn.applescript` into the script area, making sure you've already customized the paths.
6. Save the shortcut, and optionally change its icon and name as desired.
7. To pin the shortcut to the Dock for quick access, drag the saved shortcut to the Dock.

### 6. Grant Accessibility Permissions

For the AppleScript to control the OpenVPN Connect application, you need to grant Accessibility permissions:

1. Go to **System Settings** > **Privacy & Security** > **Accessibility**.
2. Click the lock to make changes and authenticate with your password.
3. Find the Shortcuts app and ensure it's enabled.

## Usage

1. Click the shortcut in the menu bar or from the Dock.
2. The shortcut will automatically generate the OTP, launch OpenVPN Connect, and connect to your VPN using the generated OTP.

## Notes

- Ensure that the OpenVPN profile is already configured in OpenVPN Connect.
- The script assumes that OpenVPN Connect is already installed and configured on your system.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Say Thank You

If you find this project useful and would like to support its development, consider buying me a coffee: [Ko-fi - Oh Teik](https://ko-fi.com/ohteik).

[<img style="float:left" src="https://user-images.githubusercontent.com/14358394/115450238-f39e8100-a21b-11eb-89d0-fa4b82cdbce8.png" width="200">](https://ko-fi.com/ohteik)
