from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


class Command(BaseCommand):
    help = 'Cria grupos e associa permissões no sistema'

    def handle(self, *args, **kwargs):
        # Criando o grupo 'Usuário de Nível 1'
        group, created = Group.objects.get_or_create(name='Usuário de Nível 1')
        self.stdout.write(self.style.SUCCESS(f'Grupo "Usuário de Nível 1" {"criado" if created else "já existente"}'))

        # Definindo os apps e modelos para os quais as permissões serão associadas
        apps_and_models = {
            'employees': ['Employee'],  # Modelo Employee no app employees
            'bond': ['AdmissionInfo'],  # Modelo AdmissionInfo no app bond
            'file_manager': ['File', 'NameFile']
        }

        # Ações que correspondem às permissões padrão
        actions = ['add', 'change', 'delete', 'view']

        for app_name, models in apps_and_models.items():
            for model_name in models:
                try:
                    # Pegando o modelo usando o app_name e model_name
                    model = apps.get_model(app_name, model_name)

                    # Obtendo o ContentType do modelo
                    content_type = ContentType.objects.get_for_model(model)

                    for action in actions:
                        # Obtendo a permissão existente
                        permission_codename = f'{action}_{model_name.lower()}'
                        permission = Permission.objects.filter(
                            codename=permission_codename,
                            content_type=content_type
                        ).first()

                        if permission:
                            # Adicionando a permissão ao grupo
                            group.permissions.add(permission)
                            self.stdout.write(self.style.SUCCESS(f'Permissão {permission_codename} associada ao grupo {group.name}.'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Permissão {permission_codename} não encontrada para {model_name} no app {app_name}.'))

                    self.stdout.write(self.style.SUCCESS(f'Permissões para {model_name} no app {app_name} associadas ao grupo {group.name}.'))
                except LookupError:
                    self.stdout.write(self.style.ERROR(f'Modelo {model_name} não encontrado no app {app_name}.'))
                    continue
