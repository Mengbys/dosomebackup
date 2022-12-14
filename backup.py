import yaml
import os
import time

check = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
config_file = dir_path + '/' + 'config.yaml'


print('backup.py: Info: Current time: {0}.'.format(time.strftime('%Y-%m-%d %H:%M:%S'))) 
print('backup.py: Info: Start backup operation.') 


try:
    with open(config_file) as y:
        data = yaml.safe_load(y)
except FileNotFoundError:  # what is the different between IOError and FileNotFoundError
    print('backup.py: Error: config.yaml not found.') 
    exit(1)
except yaml.YAMLError as exc:
    print('backup.py: Error: YAML file parse error.')
    exit(1)


target = data['target']
backup_dir = data['backup_dir']

if not os.path.exists(backup_dir):
    print('backup.py: Error: Backup directory does not exist.')
    exit(1)


# output file
filename = 'backup-{0}.zip'.format(time.strftime('%Y%m%d%H%M%S'))
filename_full = backup_dir + '/' + filename

# compress command
command = 'zip -r {0} {1}'.format(filename_full, ' '.join(target))


if check:
    print('Check the command:')
    print(command)
    exit(0)


if os.system(command) == 0:
    print('backup.py: Info: Successful back up to {0}.'.format(backup_dir))

    # delete the old backup files
    for file in os.listdir(backup_dir):
        if file != filename:
            os.remove(backup_dir + '/' + file)

else:
    print('backup.py: Error: Can not execute `zip` command.')


