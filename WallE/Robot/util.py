from importlib import import_module

def get_impl(mode, info):
    if mode == 'local':
        return get_local_impl(info['file_path'], info['class_name'])
    return None

def get_local_impl(file_path, class_name):
    robot_module = import_module(file_path)
    robot_impl = getattr(robot_module, class_name)
    return robot_impl
