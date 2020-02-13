import os

MODULES = "modules"

name_dir_project = str(input("Nome do seu projeto: "))
git = str(input("git init (Y/N): "))

a = "C:\\Users\\lbgoncalves\\Documents\\meus_tests\\"
dir_project = os.path.join(f'{a}{name_dir_project}')

def tree_project():
    folders = ['dev', 'uat', 'prod']
    sub_folders = ['backend','compute','networking']
    tfs = ["main","variables","outputs"]
    mainfilesdir = ['main.tf','variables.tf','outputs.tf','README.md','.gitignore']
    if not os.path.exists(dir_project):
        os.mkdir(dir_project)   # Cria diretório do projeto
        os.chdir(dir_project)   # Dentro da pasta criada
        os.mkdir(MODULES)       # Cria dir modules
        os.chdir(MODULES)
        for folder in folders:  # Cria diretórios dev,uat,prod
            os.mkdir(folder) 
        os.chdir(folders[0])    # Dentro de dev
        for sub1 in sub_folders: # Cria diretórios back,compute,network
            os.mkdir(sub1)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0]) # Files in backend
            for tfsback in tfs:
                f = open(f'{tfsback}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1]) # Files in compute
            for tfscompute in tfs:
                f = open(f'{tfscompute}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2]) # files in network
            for tfsnetwork in tfs:
                f = open(f'{tfsnetwork}.tf', 'w')
            os.chdir('..')
        os.chdir('..')
        os.chdir(folders[1]) # Dentro de uat
        for sub2 in sub_folders:
            os.mkdir(sub2)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0])
            for tfsback2 in tfs:
                f = open(f'{tfsback2}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1])
            for tfscompute2 in tfs:
                f = open(f'{tfscompute2}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2])
            for tfsnetwork2 in tfs:
                f = open(f'{tfsnetwork2}.tf', 'w')
            os.chdir('..')
        os.chdir('..')
        os.chdir(folders[2])
        for sub3 in sub_folders:
            os.mkdir(sub3)
        if os.path.isdir(sub_folders[0]):
            os.chdir(sub_folders[0])
            for tfsback3 in tfs:
                f = open(f'{tfsback3}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[1])
            for tfscompute3 in tfs:
                f = open(f'{tfscompute3}.tf', 'w')
            os.chdir('..')
            os.chdir(sub_folders[2])
            for tfsnetwork3 in tfs:
                f = open(f'{tfsnetwork3}.tf', 'w')
            os.chdir('..')
            os.chdir('..')
        os.chdir('..')
        for mainfiles in mainfilesdir:
            f = open(f'{mainfiles}', 'w')
        if git == "y":
            os.system('git init')
            os.system('cls')
        elif git == "n":
            pass
        os.system('cls')
        print(f'Your project was created in {os.getcwd()}')


tree_project()

