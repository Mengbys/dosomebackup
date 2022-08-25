import yaml
import os
import time

check = 0

config_file = './config.yaml'


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
backup_file = '{0}/backup-{1}.zip'.format(backup_dir, time.strftime('%Y%m%d%H%M%S'))

# compress command
command = 'zip -r {0} {1}'.format(backup_file, ' '.join(target))


if check:
    print('Check the command:')
    print(command)
    exit(0)


if os.system(command) == 0:
    print('backup.py: Info: Successful back up to', backup_dir)
else:
    print('backup.py: Error: Can not execute `zip` command.')


