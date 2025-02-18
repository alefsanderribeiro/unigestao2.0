import os

def delete_migration_files(directory):
    for root, dirs, files in os.walk(directory):
        if 'migrations' in dirs:
            migration_dir = os.path.join(root, 'migrations')
            for file in os.listdir(migration_dir):
                if file != '__init__.py' and file.endswith('.py'):
                    file_path = os.path.join(migration_dir, file)
                    os.remove(file_path)
                    print(f'Removido: {file_path}')

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    delete_migration_files(project_dir)
    print("Todas as migrações foram removidas, exceto __init__.py.")
