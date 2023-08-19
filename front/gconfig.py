import json

## Load entrypoint config
file_read = open('config.json')
cfg = json.load(file_read)
del file_read

WEB = cfg["ENTRYPOINT_DIR"]
WEB_TEMPLATES = f'{WEB}/templates'
WEB_TEMPLATES_STATICS = f'{WEB_TEMPLATES}/static'
WEB_TEMPLATES_COMPONENTS = f'{WEB_TEMPLATES}/components'
WEB_TEMPLATES_COMPONENTS_REL = f'components/'
