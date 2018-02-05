from importlib import import_module

def get_impl(mode, info):
    if mode == 'local':
        return get_local_impl(info['module_name'], info['class_name'])
    return None

def get_local_impl(module_name, class_name):
    robot_module = import_module(module_name)
    robot_impl = getattr(robot_module, class_name)
    return robot_impl
