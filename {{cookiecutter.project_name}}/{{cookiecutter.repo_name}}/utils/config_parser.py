import tomli
from pathlib import Path

def parse_config_file(path:Path) -> dict: 

    with open(path, 'rb') as tl:
        settings =  tomli.load(tl)

    # find the environment that is the target
    target = settings['target_environment']    

    for env in settings['enviroment']:
        name = env.get('name')
        if name == target:
            settings_target = env
            break
    
    return(settings_target)