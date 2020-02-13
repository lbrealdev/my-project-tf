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



# real_path = os.path.realpath(dir_project)



# os.makedirs("{modules}\\{dev}\\{uat}\\{prod}".format())





""" def first_action():
    if not os.path.exists(n_path):
        os.makedirs(n_path)
        os.chdir(n_path)
        os.system('{a} {main} && {b} {variables} && {c} {outputs} && {d} {read} && {e} {ignore}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, read=readme, e=touch, ignore=ignore))
        os.system('cls')
        if not os.path.exists(f2):
            os.makedirs(f2)
            if os.path.exists(f2):
                os.chdir(f2)
                dir_envs()
                os.system('{a} {main} && {b} {variables} && {c} {outputs}  && {d} {ignore}'.format(a=touch, main=main_f, b=touch, variables=vars_f, c=touch, outputs=out_f, d=touch, ignore=ignore))
                os.system('cls')



first_action()
 """
























#path = input("Onde vai ser criado: ")


# n_path = (r"C:\Users\lbgoncalves\Documents\structure")
# n_path = ("{C:\\Users\\lbgoncalves\\Documents}\\{}".format(f_root))

#work_path = ("{}\\{}".format(path, f_root))


""" f1 = "{}\\{}".format(real_path, ENVS)
f2 = "{}\\{}".format(real_path, MODULES) """

""" new = 'novo'

dirs = ['dev', 'uat', 'prod']

def git_init():
    os.system('git init')
    os.system('cls')

def tree():
    if os.path.exists(real_path):
        os.chdir(real_path)
        print("yes")
tree() """