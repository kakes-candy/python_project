import logging
from pathlib import Path
import datetime
import tomllib as tomli

def logfileNamer(path:Path, basename) -> Path:

    # log bestandsnaam
    datum = datetime.datetime.now().strftime("%Y%m%d")

    # Loop om bestanden te nummeren als op dezelde dag hetzelfde script gedraaid wordt
    i = 0
    while True:

        numberpart = '' if i < 1 else f'_{i}' 
        logfile_path = Path(f'{path}/{datum}_{basename}{numberpart}.log')
        # Check of bestand al bestaat op log locatie
        if logfile_path.exists():
            i += 1
            continue
        else:
            return logfile_path



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


def create_logger(configfile:Path) -> logging.Logger:

    settings = parse_config_file(configfile)
    logroot = settings.get('logroot')
    loglevel = settings.get('loglevel', 'DEBUG')

    filename = logfileNamer(path=logroot, basename="{{cookiecutter.repo_name}}")


    log_config = {
        "version": 1,
        "root": {"handlers": ["console", "file"], "level": loglevel},
        "handlers": {
            "console": {
                "formatter": "std_out",
                "class": "logging.StreamHandler",
                "level": loglevel,
            },
            "file": {
                "formatter": "std_out",
                "class": "logging.FileHandler",
                "level": loglevel,
                "filename": filename,
            },
        },
        "formatters": {
            "std_out": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - Module: %(module)s - Function: %(funcName)s - Regel: %(lineno)d \nLog : %(message)s",
                "datefmt":   "%Y-%m-%d %H:%M:%S",
            }
        },
    }

    logging.config.dictConfig(log_config)

    return logging.getLogger()