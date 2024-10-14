import os
import subprocess
import shutil
import re

def main():
    # Stop OPALStudyList.exe process
    subprocess.call(['taskkill', '/F', '/IM', 'OPALStudyList.exe'])
    
    # Stop Opal services
    services = [
        'Opal Agent',
        'Opal Backup',
        'OpalRad Dicom Print',
        'OpalRad DICOM Receive',
        'OpalRad Listener',
        'OpalRad Router',
        'OpalRad ImageServer'
    ]
    for service in services:
        subprocess.call(['net', 'stop', service])
    
    # Change directory to C:\opal\cfg
    os.chdir(r'C:\opal\cfg')
    
    # Create Backup directory if it doesn't exist
    if not os.path.exists('Backup'):
        os.mkdir('Backup')
    
    # Copy configuration files to Backup
    shutil.copy2('opalconfiguration.xml', r'C:\opal\cfg\Backup')
    shutil.copy2('OpalStudyListConfig.xml', r'C:\opal\cfg\Backup')
    
    # Change 'sa' password
    subprocess.call(['sqlcmd', '-Q', "ALTER LOGIN [sa] WITH PASSWORD=N'1q2w3e4r5t'"])
    
    # Delete from USERS_SESSION_INFO table
    subprocess.call(['sqlcmd', '-d', 'opalrad', '-Q', "DELETE FROM USERS_SESSION_INFO;"])
    
    # Enable SQL Server network protocols
    subprocess.call([
        'WMIC',
        '/NAMESPACE:\\root\Microsoft\SqlServer\ComputerManagement12',
        'PATH', 'ServerNetworkProtocol',
        'WHERE', "ProtocolName='Tcp'",
        'CALL', 'SetEnable'
    ])
    subprocess.call([
        'WMIC',
        '/NAMESPACE:\\root\Microsoft\SqlServer\ComputerManagement12',
        'PATH', 'ServerNetworkProtocol',
        'WHERE', "ProtocolName='Np'",
        'CALL', 'SetEnable'
    ])
    
    # Add firewall rule
    subprocess.call([
        'netsh', 'advfirewall', 'firewall', 'add', 'rule',
        'name=Opal', 'dir=in', 'action=allow',
        'protocol=TCP', 'localport=104,1433,33333-33338,80'
    ])
    
    # Stop IIS
    subprocess.call(['iisreset', '/stop'])
    
    # Delete contents of C:\Windows\Temp
    temp_dir = r'C:\Windows\Temp'
    if os.path.exists(temp_dir):
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f'Failed to delete file: {os.path.join(root, file)} Error: {str(e)}')
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                except Exception as e:
                    print(f'Failed to delete directory: {os.path.join(root, dir)} Error: {str(e)}')
        # Remove the temp directory
        try:
            shutil.rmtree(temp_dir)
        except Exception as e:
            print(f'Failed to remove directory: {temp_dir} Error: {str(e)}')
    
    # Delete contents of C:\Windows\Logs\CBS
    logs_dir = r'C:\Windows\Logs\CBS'
    if os.path.exists(logs_dir):
        for root, dirs, files in os.walk(logs_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f'Failed to delete file: {os.path.join(root, file)} Error: {str(e)}')
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                except Exception as e:
                    print(f'Failed to delete directory: {os.path.join(root, dir)} Error: {str(e)}')
        # Remove the logs directory
        try:
            shutil.rmtree(logs_dir)
        except Exception as e:
            print(f'Failed to remove directory: {logs_dir} Error: {str(e)}')
    
    # Delete contents of C:\inetpub\wwwroot\OpalWeb\OpalImages
    opal_images_dir = r'C:\inetpub\wwwroot\OpalWeb\OpalImages'
    if os.path.exists(opal_images_dir):
        shutil.rmtree(opal_images_dir, ignore_errors=True)
    
    # Delete contents of C:\inetpub\wwwroot\OpalWeb.Services\cache
    cache_dir = r'C:\inetpub\wwwroot\OpalWeb.Services\cache'
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir, ignore_errors=True)
    
    # Set permissions using 'cacls'
    wwwroot = r'c:\inetpub\wwwroot'
    users = [
        'Administrators',
        '2020tech',
        'opal',
        'Users',
        'Everyone',
        'Network Service',
        'Local Service'
    ]
    for user in users:
        subprocess.call(['cacls', wwwroot, '/t', '/e', '/g', f'{user}:f'])
    
    # Start IIS
    subprocess.call(['iisreset', '/start'])
    
    # Disable hibernation
    subprocess.call(['powercfg', '/hibernate', 'OFF'])
    subprocess.call([
        'REG', 'ADD',
        r'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power',
        '/V', 'HiberbootEnabled', '/T', 'REG_DWORD', '/D', '0', '/F'
    ])
    
    # Add environment variables
    subprocess.call([
        'REG', 'ADD', r'HKCU\Environment',
        '/V', 'SEE_MASK_NOZONECHECKS', '/T', 'REG_SZ', '/D', '1', '/F'
    ])
    subprocess.call([
        'REG', 'ADD', r'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
        '/V', 'SEE_MASK_NOZONECHECKS', '/T', 'REG_SZ', '/D', '1', '/F'
    ])
    subprocess.call([
        'REG', 'ADD',
        r'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Associations',
        '/v', 'LowRiskFileTypes', '/f', '/d', '.bat'
    ])
    
    # Disable User Account Control (UAC)
    subprocess.call([
        os.path.join(os.environ['windir'], 'System32', 'reg.exe'), 'ADD',
        r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',
        '/v', 'EnableLUA', '/t', 'REG_DWORD', '/d', '0', '/f'
    ])
    
    # Set power scheme to High Performance
    subprocess.call(['powercfg', '-s', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'])
    subprocess.call(['powercfg', '-change', '-disk-timeout-ac', '0'])
    
    # Get the current power scheme GUID
    result = subprocess.check_output(['powercfg', '-getactivescheme'], text=True)
    match = re.search(r'Power Scheme GUID: ([a-f0-9\-]+)', result)
    if match:
        guid = match.group(1)
        # Set power configuration values
        subprocess.call([
            'powercfg', '-setacvalueindex', guid,
            '2a737441-1930-4402-8d77-b2bebba308a3',
            '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '000'
        ])
        subprocess.call([
            'powercfg', '-setdcvalueindex', guid,
            '2a737441-1930-4402-8d77-b2bebba308a3',
            '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '000'
        ])
        subprocess.call([
            'powercfg', '-setacvalueindex', guid,
            '7516b95f-f776-4464-8c53-06167f40cc99',
            'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '000'
        ])
        subprocess.call([
            'powercfg', '-setdcvalueindex', guid,
            '7516b95f-f776-4464-8c53-06167f40cc99',
            'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '000'
        ])
    
    subprocess.call(['powercfg', '-change', '-disk-timeout-ac', '240'])
    
    # Re-register ASP.NET with IIS
    net_versions = ['v2.0.50727', 'v4.0.30319']
    for version in net_versions:
        net_path = os.path.join(os.environ['SYSTEMROOT'], 'Microsoft.NET', 'Framework', version)
        os.chdir(net_path)
        subprocess.call(['aspnet_regiis.exe', '-i'])
    
    # Set power configuration again
    subprocess.call(['powercfg', '-s', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'])
    result = subprocess.check_output(['powercfg', '-getactivescheme'], text=True)
    match = re.search(r'Power Scheme GUID: ([a-f0-9\-]+)', result)
    if match:
        guid = match.group(1)
        subprocess.call([
            'powercfg', '-setacvalueindex', guid,
            '2a737441-1930-4402-8d77-b2bebba308a3',
            '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '000'
        ])
        subprocess.call([
            'powercfg', '-setdcvalueindex', guid,
            '2a737441-1930-4402-8d77-b2bebba308a3',
            '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '000'
        ])
        subprocess.call([
            'powercfg', '-setacvalueindex', guid,
            '7516b95f-f776-4464-8c53-06167f40cc99',
            'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '000'
        ])
        subprocess.call([
            'powercfg', '-setdcvalueindex', guid,
            '7516b95f-f776-4464-8c53-06167f40cc99',
            'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '000'
        ])
    
    # Update registry settings
    subprocess.call([
        'reg.exe', 'Add',
        r'HKLM\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers',
        '/v', r'C:\opal\bin\OPALStudyList.exe', '/d', 'RUNASADMIN', '/f'
    ])
    
    # Add ASP.NET SQL Server session state
    net_v2_path = os.path.join(os.environ['SYSTEMROOT'], 'Microsoft.NET', 'Framework', 'v2.0.50727')
    os.chdir(net_v2_path)
    subprocess.call(['aspnet_regsql.exe', '-E', '-S', 'localhost', '-ssadd'])
    
    # Change 'sa' password again
    subprocess.call(['sqlcmd', '-Q', "ALTER LOGIN [sa] WITH PASSWORD=N'1q2w3e4r5t'"])
    
    # Modify web.config to remove 'UnhandledExceptionModule' entries
    subprocess.call(['net', 'stop', 'W3SVC'])
    os.chdir(r'C:\inetpub\wwwroot\OpalWeb')
    if os.path.exists('web.config'):
        with open('web.config', 'r') as file:
            lines = file.readlines()
        with open('web.config', 'w') as file:
            for line in lines:
                if 'UnhandledExceptionModule' not in line:
                    file.write(line)
    subprocess.call(['net', 'start', 'W3SVC'])
    
    # Restart services
    services_to_stop = [
        'Opal Agent',
        'Opal Backup',
        'OpalRad Dicom Print',
        'OpalRad DICOM Receive',
        'OpalRad Listener',
        'OpalRad Router',
        'OpalRad ImageServer',
        'SQL Server (MSSQLSERVER)'
    ]
    for service in services_to_stop:
        subprocess.call(['net', 'stop', service])
    
    # Reset IIS
    subprocess.call(['iisreset'])
    
    services_to_start = [
        'SQL Server (MSSQLSERVER)',
        'OpalRad ImageServer',
        'OpalRad Dicom Print',
        'OpalRad DICOM Receive',
        'OpalRad Listener',
        'OpalRad Router',
        'Opal Agent',
        'Opal Backup',
        'OpalRad Modality Worklist',
        'World Wide Web Publishing Service'
    ]
    for service in services_to_start:
        subprocess.call(['net', 'start', service])
    
    print('Script execution completed successfully.')

if __name__ == '__main__':
    main()