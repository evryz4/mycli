import os, json

save = {
    'inputstyle': '> ',
    'autoclear': False,
    'defpath': os.getcwd()
}

path = 'C:\\MyCLI'
savepath = 'save.json'

def savef():
    with open(os.path.join(path, savepath), 'w') as file:
        file.write(json.dumps(save, indent = 4))

if not os.path.exists(path):
    # Create save if not exists #
    os.mkdir(path=path)
    savef()

# Load save #
with open(os.path.join(path, savepath)) as file:
    save = json.loads(file.read())
