from pathlib import Path

LOGCONFIGFILE_TEMP_NAME = 'config.toml.temp' 
LOGCONFIGFILE_DEF_NAME = 'config.toml'

temppath = Path(LOGCONFIGFILE_TEMP_NAME)
defpath = Path(LOGCONFIGFILE_DEF_NAME)

print(temppath)
print(defpath)

if temppath.exists():
    print('file found')
    temppath.rename(defpath)
