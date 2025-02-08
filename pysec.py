import subprocess
import socket

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def check_file_attributes():
    """Check for file attributes using attrib command."""
    drive = input("Enter the drive to check (e.g., C, D, E): ").upper()
    if len(drive) == 1 and drive.isalpha():
        drive += ":\\"
        print(f"Checking file attributes on the {drive} drive using attrib command...")
        run_command(f'cd {drive}')
        attrib_output = run_command(f'attrib -r -a -s -h {drive}*')
        print("\n Please inspect and authenticate the following files")
        print(attrib_output)
    else:
        print("Invalid drive specified. Please enter a valid drive letter.")

def show_network_connections():
    """Show current network connections using netstat."""
    print("Displaying current network connections using netstat...")
    netstat_output = run_command('netstat -b')

    if netstat_output:
        print(netstat_output)
    else:
        print("No active network connections found or insufficient permissions to execute netstat -b.")

def show_packet_statistics():
    """Show packet statistics using netstat."""
    print("Displaying packet statistics using netstat...")
    netstat_output = run_command('netstat -e')

    if netstat_output:
        print(netstat_output)
    else:
        print("Could not retrieve packet statistics or insufficient permissions to execute netstat -e.")

def list_running_processes():
    """List all running processes using tasklist command."""
    print("Listing all running processes using tasklist...")
    tasklist_output = run_command('tasklist')
    print(tasklist_output)


def list_running_processes():
    """List all running processes using tasklist command."""
    print("Listing all running processes using tasklist...")
    tasklist_output = run_command('tasklist')
    print(tasklist_output)

def show_system_info():
    """Display system information using systeminfo command."""
    print("Displaying system information using systeminfo...")
    systeminfo_output = run_command('systeminfo')
    print(systeminfo_output)

def print_menu():
    """Prints the menu options."""
    print("\n--------------------------")
    print("\nPlease select an option:\n")
    print("1. Check file attributes")
    print("2. Show network connections")
    print("3. Show packet statistics")
    print("4. List running processes")
    print("5. Show system information")
    print("6. Exit")
    print("\n--------------------------")

def main():
    ascii_art= r""" 
    
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄        ▄▄▄▄     
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌      ▐░░░░░░░░░▌     ▄█░░░░▌    
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░█░█▀▀▀▀▀█░▌   ▐░░▌▐░░▌    
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌               ▐░▌▐░▌    ▐░▌    ▀▀ ▐░░▌    
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌               ▐░▌ ▐░▌   ▐░▌       ▐░░▌    
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               ▐░▌  ▐░▌  ▐░▌       ▐░░▌    
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌               ▐░▌   ▐░▌ ▐░▌       ▐░░▌    
▐░▌               ▐░▌               ▐░▌▐░▌          ▐░▌               ▐░▌    ▐░▌▐░▌       ▐░░▌    
▐░▌               ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄█░█░▌▄  ▄▄▄▄█░░█▄▄▄ 
▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌      ▐░░░░░░░░░▌▐░▌▐░░░░░░░░░░░▌
 ▀                 ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀  ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                  
    """
    print(ascii_art)
    print("PYSEC 0.1\n")
    print("**RUN SHELL AS ADMIN**\n")
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ")
        if choice == '1':
            check_file_attributes()
        elif choice == '2':
            show_network_connections()
        elif choice =="3":
            show_packet_statistics()
        elif choice == '4':
            list_running_processes()
        elif choice == '5':
            show_system_info()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
