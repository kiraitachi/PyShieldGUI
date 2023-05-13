import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Function to execute terminal command and show output in a dialog
def run_command(command):
    output = subprocess.check_output(command.split())
    dialog = Gtk.MessageDialog(parent=None, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Output")
    dialog.format_secondary_text(output.decode("utf-8"))
    dialog.run()
    dialog.destroy()

# Function to show virtual locations and prompt to connect
def show_locations():
    vpn_status_output = subprocess.check_output("hotspotshield status".split())
    vpn_status = vpn_status_output.decode("utf-8")
    if "Connected" in vpn_status:
        # VPN is running, prompt to stop it first
        dialog = Gtk.MessageDialog(parent=None, flags=0, message_type=Gtk.MessageType.WARNING, buttons=Gtk.ButtonsType.OK_CANCEL)
        dialog.set_title("VPN is currently running")
        dialog.set_markup("Do you want to stop the VPN before connecting to a new location?")
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            return  # User canceled, do not continue
        run_command("hotspotshield stop")
    locations_output = subprocess.check_output("hotspotshield locations".split())
    locations = locations_output.decode("utf-8").splitlines()
    dialog = Gtk.Dialog(title="Connect to Virtual Location", parent=None, flags=0)
    dialog.add_buttons("Connect", Gtk.ResponseType.OK, "Cancel", Gtk.ResponseType.CANCEL)
    dialog.set_default_size(200, 100)
    dialog.set_border_width(10)
    vbox = dialog.get_content_area()
    label = Gtk.Label(label="Select a Virtual Location to connect to:")
    vbox.add(label)
    location_combobox = Gtk.ComboBoxText()
    for location in locations:
        location_combobox.append_text(location)
    location_combobox.set_active(0)
    vbox.pack_start(location_combobox, True, True, 0)
    dialog.show_all()
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        location = location_combobox.get_active_text()
        run_command(f"hotspotshield connect {location}")
    dialog.destroy()

# Function to check public IP
def check_public_ip():
    run_command("curl ipinfo.io")

# Create main window
win = Gtk.Window(title="Hotspot Shield")
win.set_default_size(300, 250)

# Create buttons
account_status_button = Gtk.Button(label="Account Status")
account_status_button.connect("clicked", lambda button: run_command("hotspotshield account status"))

vpn_status_button = Gtk.Button(label="VPN Status")
vpn_status_button.connect("clicked", lambda button: run_command("hotspotshield status"))

check_public_ip_button = Gtk.Button(label="Check PublicIP")
check_public_ip_button.connect("clicked", lambda button: check_public_ip())

start_button = Gtk.Button(label="Start VPN")
start_button.connect("clicked", lambda button: run_command("hotspotshield start"))

stop_button = Gtk.Button(label="Stop VPN")
stop_button.connect("clicked", lambda button: run_command("hotspotshield stop"))

connect_button = Gtk.Button(label="Connect to Locations")
connect_button.connect("clicked", lambda button: show_locations())

# Create buttons
account_status_button = Gtk.Button(label="Account Status")
account_status_button.connect("clicked", lambda button: run_command("hotspotshield account status"))

vpn_status_button = Gtk.Button(label="VPN Status")
vpn_status_button.connect("clicked", lambda button: run_command("hotspotshield status"))

check_public_ip_button = Gtk.Button(label="Check PublicIP")
check_public_ip_button.connect("clicked", lambda button: run_command("curl ipinfo.io"))

start_button = Gtk.Button(label="Start VPN")
start_button.connect("clicked", lambda button: run_command("hotspotshield start"))

stop_button = Gtk.Button(label="Stop VPN")
stop_button.connect("clicked", lambda button: run_command("hotspotshield stop"))

connect_button = Gtk.Button(label="Connect to Locations")
connect_button.connect("clicked", lambda button: show_locations())

# Create box to hold buttons
box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
box.pack_start(account_status_button, True, True, 0)
box.pack_start(vpn_status_button, True, True, 0)
box.pack_start(check_public_ip_button, True, True, 0)
box.pack_start(start_button, True, True, 0)
box.pack_start(stop_button, True, True, 0)
box.pack_start(connect_button, True, True, 0)

# Add box to window
win.add(box)

# Show window
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
