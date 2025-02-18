from django import forms


class EmployeeFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeFormAdmin, self).__init__(*args, **kwargs)
        # Classes
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['telephone'].widget.attrs['class'] = 'mask-telephone'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

        # Placeholder
        # self.fields['full_name'].widget.attrs['placeholder'] = 'Nome Completo do Funcionário'
        # self.fields['mother_name'].widget.attrs['placeholder'] = 'Nome Completo da Mãe'
        # self.fields['father_name'].widget.attrs['placeholder'] = 'Nome Completo do Pai'
        # self.fields['contact'].widget.attrs['placeholder'] = 'Nome do Contato'
        # self.fields['telephone'].widget.attrs['placeholder'] = 'Telefone Para Contato'
