import urllib.request as urllib2
import zipfile
import os
from importlib import import_module

def check_dir(path):
    if not os.path.isdir(path):
        print('path not exist, creating ', path, ' ... ')
        os.makedirs(path)
    print(path, ' exist')

def load_local_task_module(robot, module_name, class_name):
    task_module = import_module(module_name)
    task_class = getattr(task_module, class_name)
    task = task_class(robot)
    return task

def load_remote_task_module(robot, module_name, class_name, url):
    check_dir('tasks')
    check_dir('tmp')
    package = urllib2.urlopen(url)
    with open('tmp/package.zip','wb') as output:
        output.write(package.read())
    zip_ref = zipfile.ZipFile('tmp/package.zip', 'r')
    zip_ref.extractall('tasks')
    zip_ref.close()
    os.remove('tmp/package.zip')
    task = load_local_task_module(robot, module_name, class_name)
    return task
