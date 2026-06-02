import socket
import os
import sys
import time
import threading
from datetime import datetime, timedelta
from flask import Flask, render_template

app = Flask(__name__)

# Global state for profiles and session
class SessionProfile:
    def __init__(self, name, commands, duration_minutes=60):
        self.name = name
        self.commands = commands
        self.duration_minutes = duration_minutes
        self.start_time = None
        self.end_time = None
        self.is_active = False
        self.completed_commands = []
        self.remaining_commands = list(commands)
    
    def start(self):
        """Start the profile timer"""
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=self.duration_minutes)
        self.is_active = True
    
    def get_time_remaining(self):
        """Get remaining time in format HH:MM:SS"""
        if not self.is_active or not self.end_time:
            return "00:00:00"
        remaining = self.end_time - datetime.now()
        if remaining.total_seconds() <= 0:
            self.is_active = False
            return "00:00:00"
        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def execute_command(self, command):
        """Execute a command and move it to completed"""
        if command in self.remaining_commands:
            self.remaining_commands.remove(command)
            self.completed_commands.append(command)
            return True
        return False
    
    def get_status(self):
        """Get current profile status"""
        return {
            'name': self.name,
            'is_active': self.is_active,
            'time_remaining': self.get_time_remaining(),
            'completed': len(self.completed_commands),
            'remaining': len(self.remaining_commands),
            'total': len(self.commands)
        }

# Pre-defined profiles
PROFILES = {
    'network_scan': SessionProfile(
        'Network Scanner',
        [
            'nmap -p- -sV target.com',
            'netstat -an | grep ESTABLISHED',
            'arp -a',
            'tracert target.com',
            'ipconfig /all'
        ],
        duration_minutes=30
    ),
    'osint_passive': SessionProfile(
        'Passive OSINT',
        [
            'whois lookup',
            'DNS enumeration',
            'SSL certificate analysis',
            'Subdomain discovery',
            'Email finder'
        ],
        duration_minutes=45
    ),
    'security_audit': SessionProfile(
        'Security Audit',
        [
            'Port scanning',
            'Vulnerability assessment',
            'Configuration review',
            'Access control check',
            'Log analysis'
        ],
        duration_minutes=60
    )
}

current_profile = None

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the TRACK ME NOW banner"""
    banner = "\033[92m" + "="*65 + "\033[0m\n"
    banner += """
  _____ ___    _    ____ _  __  __ _____    __  __  ___  __    __
 |_   _| _ \  / \  / ___| |/ / |  \/  | ____|  |  \/  |/ _ \ \  / /
   | | | |_) |/ _ \| |   | ' /  | |\/| |  _|    | |\/| | | | \ \/ / 
   | | |  _ < / ___ \ |___| . \  | |  | | |___   | |  | | |_| | /  \ 
   |_| |_| \_\_/   \_\____|_|\_\ |_|  |_|_____|  |_|  |_|\___//_/\_\
    """
    banner += "\033[92m" + "="*65 + "\033[0m\n"
    banner += " \033[96m[*] Personal OSINT & IP Network Engine v1.0.5 [*]\033[0m\n"
    banner += "\033[92m" + "="*65 + "\033[0m\n"
    return banner

def print_timer_display(profile):
    """Display the timer and active session info at the top"""
    status = profile.get_status()
    
    timer_display = "\n" + "\033[95m" + "┌" + "─"*58 + "┐\033[0m\n"
    timer_display += "\033[95m│\033[0m " + "\033[93m⏱️  ACTIVE SESSION TIMER\033[0m".center(56) + " \033[95m│\033[0m\n"
    timer_display += "\033[95m├" + "─"*58 + "┤\033[0m\n"
    timer_display += f"\033[95m│\033[0m  Profile: \033[96m{status['name']}\033[0m" + " "*(38-len(status['name'])) + " \033[95m│\033[0m\n"
    timer_display += f"\033[95m│\033[0m  Time Remaining: \033[91m{status['time_remaining']}\033[0m" + " "*(34-len(status['time_remaining'])) + " \033[95m│\033[0m\n"
    timer_display += f"\033[95m│\033[0m  Progress: \033[92m{status['completed']}/{status['total']}\033[0m completed" + " "*(34) + " \033[95m│\033[0m\n"
    timer_display += "\033[95m└" + "─"*58 + "┘\033[0m\n"
    
    return timer_display

def print_remaining_commands(profile):
    """Display remaining commands"""
    if not profile.remaining_commands:
        commands_display = "\n\033[92m✓ All commands completed!\033[0m\n"
        return commands_display
    
    commands_display = "\n" + "\033[94m" + "┌" + "─"*58 + "┐\033[0m\n"
    commands_display += "\033[94m│\033[0m " + "\033[96m📋 REMAINING COMMANDS\033[0m".center(56) + " \033[94m│\033[0m\n"
    commands_display += "\033[94m├" + "─"*58 + "┤\033[0m\n"
    
    for idx, cmd in enumerate(profile.remaining_commands, 1):
        cmd_display = f"  {idx}. {cmd}"
        commands_display += f"\033[94m│\033[0m {cmd_display:<56} \033[94m│\033[0m\n"
    
    commands_display += "\033[94m└" + "─"*58 + "┘\033[0m\n"
    return commands_display

def print_completed_commands(profile):
    """Display completed commands"""
    if not profile.completed_commands:
        return ""
    
    commands_display = "\n" + "\033[92m" + "┌" + "─"*58 + "┐\033[0m\n"
    commands_display += "\033[92m│\033[0m " + "\033[92m✓ COMPLETED COMMANDS\033[0m".center(56) + " \033[92m│\033[0m\n"
    commands_display += "\033[92m├" + "─"*58 + "┤\033[0m\n"
    
    for idx, cmd in enumerate(profile.completed_commands, 1):
        cmd_display = f"  {idx}. {cmd}"
        commands_display += f"\033[92m│\033[0m \033[92m✓\033[0m {cmd_display:<54} \033[92m│\033[0m\n"
    
    commands_display += "\033[92m└" + "─"*58 + "┘\033[0m\n"
    return commands_display

def print_local_ip_info():
    """Print local IP information"""
    my_ip = get_local_ip()
    
    ip_display = "\n" + "\033[93m" + "┌" + "─"*58 + "┐\033[0m\n"
    ip_display += "\033[93m│\033[0m " + "\033[93m🌐 YOUR DEVICE IP INFO\033[0m".center(56) + " \033[93m│\033[0m\n"
    ip_display += "\033[93m├" + "─"*58 + "┤\033[0m\n"
    ip_display += f"\033[93m│\033[0m  Local IP:  \033[96mhttp://{my_ip}:5000\033[0m" + " "*(25-len(my_ip)) + " \033[93m│\033[0m\n"
    ip_display += f"\033[93m│\033[0m  Loopback:  \033[96mhttp://127.0.0.1:5000\033[0m" + " "*18 + " \033[93m│\033[0m\n"
    ip_display += "\033[93m└" + "─"*58 + "┘\033[0m\n"
    
    return ip_display

def get_local_ip():
    """Function to find the actual local IP address of the device"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def update_display():
    """Update the display with timer and commands at the top"""
    global current_profile
    
    if not current_profile or not current_profile.is_active:
        return
    
    # Clear screen and show updated info
    clear_screen()
    sys.stdout.write(print_banner())
    sys.stdout.write(print_timer_display(current_profile))
    sys.stdout.write(print_remaining_commands(current_profile))
    sys.stdout.write(print_completed_commands(current_profile))
    sys.stdout.write(print_local_ip_info())
    sys.stdout.flush()

def timer_thread():
    """Background thread to update timer every second"""
    while True:
        if current_profile and current_profile.is_active:
            update_display()
            time.sleep(1)
        else:
            time.sleep(0.5)

@app.route('/')
def index():
    """Local dashboard for IP monitoring"""
    return "<h1>TRACK ME NOW - OSINT Core is Running Locally! Check Termux Console.</h1>"

if __name__ == '__main__':
    # Clear the terminal screen before displaying the banner
    clear_screen()
    
    print(print_banner())
    
    # Retrieve local IP
    my_ip = get_local_ip()
    
    print("\033[94m[*] Scanning Local Network Interfaces...")
    print("[+] Status: ONLINE and Connected\033[0m")
    print(print_local_ip_info())
    
    print("\n\033[96m[*] TRACK ME NOW - Available Profiles:\033[0m")
    for profile_key, profile in PROFILES.items():
        print(f"    • {profile.name} ({len(profile.commands)} commands, {profile.duration_minutes} min)")
    
    print("\n\033[93m[*] Running secure local server. Press Ctrl+C to stop.\n\033[0m")
    
    # Start background timer thread
    timer = threading.Thread(target=timer_thread, daemon=True)
    timer.start()
    
    # Run the server locally
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )
