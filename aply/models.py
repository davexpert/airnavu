from django.db import models


class ProcessingApplicationsUav(models.Model):
    organization_name = models.CharField(max_length=255, verbose_name='Полное наименование организации')
    fullname_position_head = models.CharField(max_length=255, verbose_name='ФИО и Должность руководителя')
    legal_bank_address = models.CharField(max_length=255, verbose_name='Юридический адрес и Банковские реквизиты')
    letter_from_the_MinistryOfDefense = models.FileField(
        verbose_name='Копия письма от Министерства обороны Кыргызской Республики.')
    '''
    Тут еще будут какие-то файлы, которые нужно прикреплять при заявки
    '''
    name_surname_applicant = models.CharField(max_length=255, verbose_name='ФИО заявителя')
    manage_position_applicant = models.CharField(max_length=255, verbose_name='Должность заявителя')
    email = models.EmailField(verbose_name='Электронная почта')
    contact_number = models.CharField(verbose_name='Контактные телефоны')
    created_date = models.DateField(verbose_name='Дата подачи заявки')
    confirm = models.BooleanField(default=False, verbose_name='Подтверждаю')


class AplicateANO(models.Model):
    organization_name = models.CharField(max_length=255, verbose_name='Полное наименование организации')
    fullname_position_head = models.CharField(max_length=255, verbose_name='ФИО и Должность руководителя')
    legal_address = models.CharField(max_length=255, verbose_name='Юридический адрес')
    regulations = models.FileField(verbose_name='Устав', upload_to='files/regulations/')
    air_operator_certificate = models.FileField(verbose_name='Сертификат эксплуатанта', upload_to='files/air-operator/')
    operational_permit = models.FileField(verbose_name='Эксплуатационное разрешение', upload_to='files/operational/')
    fullname_position_applicant = models.CharField(max_length=255, verbose_name='ФИО заявителя и Должность заявителя')
    email = models.EmailField(verbose_name='Электронная почта')
    contact_number = models.CharField(verbose_name='Контактные телефоны')
    created_date = models.DateField(verbose_name='Дата подачи заявки')
    confirm = models.BooleanField(default=False, verbose_name='Подтверждаю')
