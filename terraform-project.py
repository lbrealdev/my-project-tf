import os
from pathlib import Path

PROJECT = "projects"
MODULES = "modules"
HOMEPATH = str(Path.home())
ENTRYPOINT = "\\Documents\\"

name_dir_project = str(input("Nome do seu projeto: "))
git = str(input("git init (Y/N): "))

a = ("{}{}{}".format(HOMEPATH, ENTRYPOINT, PROJECT))
dir_project = os.path.join(f'{a}{name_dir_project}')

def tree_project():
    folders = ['dev', 'uat', 'prod']
    sub_folders = ['backend','compute','networking']
    tfs = ["main","variables","outputs"]
    mainfilesdir = ['main.tf','variables.tf','outputs.tf','README.md','.gitignore']
    if not os.path.exists(a):
        os.chdir(f'{HOMEPATH}{ENTRYPOINT}')
        os.mkdir(PROJECT)
        os.chdir(PROJECT)
    else:
        os.chdir(a)
    if not os.path.exists(dir_project):
        os.mkdir(name_dir_project)
        os.chdir(name_dir_project)
        os.mkdir(MODULES)
        os.chdir(MODULES)
        for folder in folders:
            os.mkdir(folder) 
        os.chdir(folders[0])
        for sub1 in sub_folders:
            os.mkdir(sub1)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0])
            for tfsback in tfs:
                open(f'{tfsback}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1])
            for tfscompute in tfs:
                open(f'{tfscompute}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2])
            for tfsnetwork in tfs:
                open(f'{tfsnetwork}.tf', 'w')
            os.chdir('..')
        os.chdir('..')
        os.chdir(folders[1])
        for sub2 in sub_folders:
            os.mkdir(sub2)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0])
            for tfsback2 in tfs:
                open(f'{tfsback2}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1])
            for tfscompute2 in tfs:
                open(f'{tfscompute2}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2])
            for tfsnetwork2 in tfs:
                open(f'{tfsnetwork2}.tf', 'w')
            os.chdir('..')
        os.chdir('..')
        os.chdir(folders[2])
        for sub3 in sub_folders:
            os.mkdir(sub3)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0])
            for tfsback3 in tfs:
                open(f'{tfsback3}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1])
            for tfscompute3 in tfs:
                open(f'{tfscompute3}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2])
            for tfsnetwork3 in tfs:
                open(f'{tfsnetwork3}.tf', 'w')
            os.chdir('..')
            os.chdir('..')
        os.chdir('..')
        for mainfiles in mainfilesdir:
            open(f'{mainfiles}', 'w')
        if git == "y":
            os.system('git init')
            os.system('cls')
        elif git == "n":
            pass
        os.system('cls')
        print(f'Your project was created in {os.getcwd()}')


tree_project()

