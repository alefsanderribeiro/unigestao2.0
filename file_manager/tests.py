from datetime import date
from django.test import TestCase
from .models import NameFile, File
from employees.models import Employee
from configurations.models import Gender, Race, MaritalStatus, DegreeInstruction, Nationality
from geography.models import Country, State, City

class NameFileModelTest(TestCase):
    def setUp(self):
        self.name_file = NameFile.objects.create(name="Test File")

    def test_name_file_creation(self):
        self.assertEqual(self.name_file.name, "Test File")
        self.assertTrue(isinstance(self.name_file, NameFile))
        self.assertEqual(str(self.name_file), "Test File")

class FileModelTest(TestCase):
    def setUp(self):
        # Criação dos objetos necessários para Employee
        self.gender = Gender.objects.create(description="Masculino")
        self.race = Race.objects.create(description="Branco")
        self.marital_status = MaritalStatus.objects.create(description="Solteiro")
        self.degree_instruction = DegreeInstruction.objects.create(description="Ensino Médio")
        self.nationality = Nationality.objects.create(description="Brasileiro")
        
        # Criação dos objetos para Geography
        country = Country.objects.create(name="Brasil")
        self.state = State.objects.create(name="São Paulo", abbreviation="SP", code="001", country=country)
        self.city = City.objects.create(name="São Paulo", state=self.state)
        
        # Criação do Employee com todos os campos obrigatórios
        self.employee = Employee.objects.create(
            full_name="John Doe",
            gender=self.gender,
            race=self.race,
            marital_status=self.marital_status,
            birth_date=date(1990, 1, 1),
            degree_instruction=self.degree_instruction,
            nationality=self.nationality,
            naturalness_uf=self.state,
            natural_city=self.city,
            cpf="00000000000",
            cep="12345678",
            address_uf="SP",
            city_address="São Paulo",
            neighborhood="Centro",
            number="123"
        )
        
        self.name_file = NameFile.objects.create(name="Test File")
        self.file = File.objects.create(
            name_file=self.name_file,
            employee=self.employee,
            file="test_file.txt"
        )

    def test_file_creation(self):
        self.assertEqual(self.file.name_file.name, "Test File")
        self.assertEqual(self.file.employee.full_name, "John Doe")
        self.assertEqual(self.file.file, "test_file.txt")
        self.assertTrue(isinstance(self.file, File))
        self.assertEqual(
            str(self.file),
            f"{self.name_file} - {self.employee.full_name} - {self.file.file.name}"
        )
