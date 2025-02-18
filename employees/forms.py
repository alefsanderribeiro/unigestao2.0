from django import forms


class EmployeeFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['telephone'].widget.attrs['class'] = 'mask-telephone'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
        self.fields['contact'].widget.attrs['placeholder'] = 'Nome do contato'
