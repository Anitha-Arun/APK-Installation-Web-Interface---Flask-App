Description:
This project is a Flask-based web application designed to facilitate the installation and uninstallation of APK files on Android devices connected to a server. The application allows users to select APK files from predefined directories, choose Android devices to install the APKs on, and view the installation process in a user-friendly interface.
Key Features:
Web Interface:

Provides an easy-to-use web interface where users can view available APKs and select which ones to install or uninstall on multiple Android devices.
Multiple Device Support:

Users can specify multiple Android devices, and the app will install the selected APKs on each device using the ADB (Android Debug Bridge) commands.
Automated APK Management:

The app automatically manages APK installations by connecting to devices over the network, uninstalling existing APKs if necessary, and then installing the selected ones.
Dynamic APK Directory Management:

APK files are organized in directories for different categories such as teams, admin, and cp. The app allows users to install APKs from any of these categories based on their requirements.
ADB Integration:

Uses ADB commands to connect to Android devices, uninstall existing apps, and install new ones directly from the server. It handles the installation process efficiently and silently, with detailed logs of each operation.
Result Logs:

After the installation process, the app generates logs of the installation process for each device, which includes connection status, installation success, or failure for each APK.
Error Handling:

If an APK is not found or the connection fails, the app gracefully handles errors and logs the issue, providing feedback to the user.
How It Works:
User Interaction:
The user opens the web interface and selects the APK files they want to install or uninstall for each device.
Device Selection:
Multiple devices can be specified, and the app will attempt to connect to each one over the network using ADB.
APK Installation:
The app checks if the APK exists in the respective folder. It uninstalls any previously installed APKs (if necessary) and installs the selected APKs on each device.
Logging and Feedback:
Detailed logs are generated for each device to track the installation status and any errors encountered during the process.
rom the interface, select the APKs you want to install or uninstall, input the IP addresses of the devices, and initiate the installation process.

The result page will show the status of each device, including any errors or successful installations.

Technologies Used:
Flask: A Python web framework for creating the web application.
ADB (Android Debug Bridge): A command-line tool to interact with Android devices for installing/uninstalling APKs.
Python: The backend code is written in Python, handling logic for APK installation, uninstallation, and interaction with the web interface.
Use Cases:
Automated App Deployment: Ideal for situations where multiple Android devices need to have the same set of apps installed across a fleet of devices, such as in enterprise environments or testing labs.
App Testing: Great for app developers who need to install and uninstall APKs on test devices quickly.
Device Management: Manage and deploy apps on a large number of Android devices efficiently.
