from flask import Flask, request, jsonify, render_template
import os
import subprocess

app = Flask(__name__)

# Define the paths to the APK directories
APK_DIRECTORIES = {
    'teams': '/app/apks/teams',
    'admin': '/app/apks/admin',
    'cp': '/app/apks/cp'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_apks', methods=['GET'])
def get_apks():
    folder = request.args.get('folder')
    if folder not in APK_DIRECTORIES:
        return jsonify([])

    folder_path = APK_DIRECTORIES[folder]
    apk_files = [f for f in os.listdir(folder_path) if f.endswith('.apk')]
    return jsonify(apk_files)

def run_adb_command(ip, command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

def uninstall_apks(ip, package_name):
    # Adjusted to run silently without returning output
    command = f"adb -s {ip} shell pm uninstall {package_name}"
    subprocess.run(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ''

def install_apks(ip, folder, apks):
    result_output = ''
    for apk in apks:
        apk_path = os.path.join(APK_DIRECTORIES[folder], apk)
        if os.path.exists(apk_path):
            command = f"adb -s {ip} install {apk_path}"
            result_output += f"Installing {apk}...\n"
            result_output += run_adb_command(ip, command.split())
        else:
            result_output += f"APK not found: {apk_path}\n"
    return result_output

def handle_team_apks(ip, apks):
    # No need to print uninstallation message
    result_output = uninstall_apks(ip, 'com.microsoft.skype.teams.ipphone')
    result_output += install_apks(ip, 'teams', apks)
    return result_output

def handle_admin_apks(ip, apks):
    # No need to print uninstallation message
    result_output = uninstall_apks(ip, 'com.microsoft.teams.ipphone.admin.agent')
    result_output += install_apks(ip, 'admin', apks)
    return result_output

def handle_cp_apks(ip, apks):
    # No need to print uninstallation message
    result_output = uninstall_apks(ip, 'com.microsoft.windowsintune.companyportal')
    result_output += install_apks(ip, 'cp', apks)
    return result_output

@app.route('/install', methods=['POST'])
def install():
    device_count = int(request.form.get('device_count'))
    device_ips = [request.form.get(f'device_ip_{i+1}') for i in range(device_count)]

    selected_apks = {
        'teams': request.form.getlist('apk_file_teams'),
        'admin': request.form.getlist('apk_file_admin'),
        'cp': request.form.getlist('apk_file_cp')
    }

    results = []
    for ip in device_ips:
        result = {'ip': ip, 'output': ''}

        # Try to connect to the device
        result['output'] += f"Connecting to {ip}...\n"
        result['output'] += run_adb_command(ip, ['adb', 'connect', ip]) + '\n'

        # If connection is successful, proceed with APK installation
        if selected_apks['teams']:
            result['output'] += handle_team_apks(ip, selected_apks['teams'])
        if selected_apks['admin']:
            result['output'] += handle_admin_apks(ip, selected_apks['admin'])
        if selected_apks['cp']:
            result['output'] += handle_cp_apks(ip, selected_apks['cp'])
        results.append(result)
    
    return render_template('install_result.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
