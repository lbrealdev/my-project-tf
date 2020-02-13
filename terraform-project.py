import os

ENVS = "environments"
MODULES = "modules"

# Terraform files directories
DEV = "dev"
PRE = "uat"
PROD = "prod"

# Terraform modules directories
BACK = "backend"
CM = "compute"
NET = "networking"

# Files .tf

readme = "README.md"
main_f = "main.tf"
vars_f = "variables.tf"
out_f = "outputs.tf"
ignore = ".gitignore"
# cmd

touch = "copy nul"

name_dir_project = str(input("Nome do seu projeto: "))
""" git = str(input("git init (Y/N): ")) """

a = "C:\\Users\\lbgoncalves\\Documents\\meus_tests\\"


dir_project = os.path.join(f'{a} {name_dir_project}')

def tree_project():
    folders = ['dev', 'uat', 'prod']
    sub_folders = ['backend','compute','networking']
    tfs = ['main.tf','variables.tf','outputs.tf']
    if not os.path.exists(dir_project):
        os.mkdir(dir_project)   # Cria diretório do projeto
        os.chdir(dir_project)   # Dentro da pasta criada
        os.mkdir(MODULES)       # Cria dir modules
        p1 = os.path.join(os.getcwd(), MODULES)
        os.chdir(p1)
        for folder in folders:  # Cria diretórios dev,uat,prod
            os.mkdir(folder)  
        pwd_dev = os.path.join(os.getcwd(), folders[0]) 
        os.chdir(pwd_dev)            # Dentro de dev
        for sub1 in sub_folders: # Cria diretórios back,compute,network
            os.mkdir(sub1)
        os.chdir('..')
        pwd_uat = (f'{os.getcwd()}\\{folders[1]}')
        os.chdir(pwd_uat)
        for sub2 in sub_folders:
            os.mkdir(sub2)
        os.chdir('..')
        pwd_pro = (f'{os.getcwd()}\\{folders[2]}')
        os.chdir(pwd_pro)
        for sub3 in sub_folders:
            os.mkdir(sub3)
        os.chdir('..')


tree_project()

