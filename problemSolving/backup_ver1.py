import os
import time

# Directory containing the files to be backed up
source = ['/Users/david.coy/Desktop/Ruby/learning-ruby/README.md']

# The backup is stored in a backup Directory
target_dir = '/Users/david.coy/Desktop/Ruby/backup/'

# Files are backed up into a zip
# The name of the zip file is the current date/time
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create a target directory if it not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# Use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Run the backup!
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
