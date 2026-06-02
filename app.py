import socket
import os
from flask import Flask, render_template

app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == '__main__':

    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # TRACK ME NOW Banner
    print("╔" + "═" * 70 + "╗")
    print("║" + " " * 70 + "║")
    print("║  ████████╗██████╗  █████╗  ██████╗██╗  ██╗    ███╗   ███╗███████╗ ║")
    print("║  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔════╝ ║")
    print("║     ██║   ██████╔╝███████║██║     █████╔╝     ██╔████╔██║█████╗   ║")
    print("║     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗     ██║╚██╔╝██║██╔══╝   ║")
    print("║     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗    ██║ ╚═╝ ██║███████╗ ║")
    print("║     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝ ║")
    print("║" + " " * 70 + "║")
    print("║                    T R A C K   M E   N O W  v1.0.6                ║")
    print("║                     Personal Network Dashboard                   ║")
    print("║" + " " * 70 + "║")
    print("╚" + "═" * 70 + "╝")

    my_ip = get_local_ip()

    print("\n[+] Scanning Local Network Interfaces...")
    print("[+] Status: ONLINE and connected\n")

    print("═══════════════[ YOUR DEVICE IP INFO ]══════════════")
    print(f"  LOCAL IP      : http://{my_ip}:5000")
    print("  LOOPBACK IP   : http://127.0.0.1:5000")
    print("════════════════════════════════════════════════════\n")

    print("[+] Flask server is running...")
    print("[+] Press CTRL+C to stop.\n")

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
