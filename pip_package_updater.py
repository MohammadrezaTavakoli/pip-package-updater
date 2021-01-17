import subprocess
import sys


command = "pip3 list --outdated | awk '{print $1}'"
sub_proccess = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
output = sub_proccess.stdout.decode('utf-8')

err_count = 0
install_count = 0

output_list = output.split('\n')

for pkg_name in output_list:
    if pkg_name == 'Package' or '-----' in pkg_name or  len(pkg_name) == 0:
        output_list.remove(pkg_name)

    else:
        try:
            shell_command = f'pip3 install --user --upgrade {pkg_name}'
            update_command = subprocess.run(shell_command, shell=True, 
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
            sys.stdout.write(update_command.stdout.decode('utf-8'))
            sys.stdout.flush()
            install_count += 1

        except subprocess.CalledProcessError as error:
            err_count += 1
            print(error.output)

if err_count == 0 and install_count == 0:
    print("All packages up to date.")
else:
    print(f"{install_count} packages installed.\n{err_count} errors occured.")
