# Не оптимизировать импорты и не менять их порядок

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_ac.settings")
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()

import logging
import datetime
from asgiref.sync import sync_to_async
from lids.models import Lids
from make_contract_base.models import ContractBase, Organization, PrivateContract
from addprofit.models import AddProfits, Customer_category
from invoice.models import Invoice
from app_telegram.models import TGUser
from customer.models import Private_person

logger = logging.getLogger(__name__)


@sync_to_async
def add_invoice(invoice_file,
                name,
                published,
                sum,
                invoice_number,
                invoice_file_invoice,
                ):
    print("def add_invoice")
    try:
        new_invoice = Invoice(invoice_file=invoice_file,
                              name=name,
                              published=published,
                              sum=int(sum),
                              invoice_number=invoice_number,
                              invoice_file_invoice=invoice_file_invoice,
                              )
        new_invoice.save()
        return new_invoice
    except Exception as e:
        print("Can not create class instance")
        print(e)


@sync_to_async
def add_private_person(
        customername,
        mail,
        passportnumber,
        issued,
        whenissued,
        placeofregistration,
        telephonenum

):
    print("add_private_person")
    try:

        new_person = Private_person(customername=customername,
                                    mail=mail,
                                    passportnumber=passportnumber,
                                    issued=issued,
                                    whenissued=whenissued,
                                    placeofregistration=placeofregistration,
                                    telephonenum=telephonenum,
                                    )
        new_person.save()

        return new_person
    except Exception as e:

        nowd = datetime.datetime.now()
        whenissued_error = f'{nowd.year}-{nowd.month}-{nowd.day}'
        new_person = Private_person(customername=customername,
                                    mail=mail,
                                    passportnumber=passportnumber,
                                    issued=issued,
                                    whenissued=whenissued_error,
                                    placeofregistration=placeofregistration,
                                    telephonenum=telephonenum,
                                    )
        new_person.save()
        print("Can not create Private_person class instance")

        print(e)


@sync_to_async()
def add_lid(name: str = "no name", email: str = "email@mail.ru", town: str = "Краснодар",
            telephone: str = "+79780740854", area: int = 100, description: str = "No description",
            source: str = "Unknown", what_service: str = "Unknown", our_price: int = 0, new: int = 0,
            result: str = "no result"):
    try:
        new_lid = Lids(
            name=str(name),
            email=str(email),
            town=str(town),
            telephone=str(telephone),
            area=int(area),
            description=str(description),
            source=str(source),
            what_service=str(what_service),
            our_price=int(our_price),
            new=int(new),
            result=str(result)
        )
        new_lid.save()
    except Exception as e:
        print(f'{e}')
        print(f'name: {name}')
        print(f'email: {email}  {type(email) == str}')
        print(f'town: {town}  {type(town) == str}')
        print(f'telephone: {telephone}  {type(telephone) == str}')
        print(f'area: {area}  {type(area) == int}')
        print(f'description: {description}  {type(description) == str}')
        print(f'source: {source}  {type(source) == str}')
        print(f'what_service: {what_service}  {type(what_service) == str}')
        print(f'our_price: {our_price}  {type(our_price) == int}')
        print(f'new:{new}  {type(new) == int}')
        print(f'result:{result}  {type(result) == str}')


@sync_to_async()
def add_contract(customername, quantity, price, adressofobject, mail, total_cost, townobject,
                 telephonenum, customer_firm, organization_full_name, organization_adress,
                 customer_legal_basis, organization_inn, organization_kpp, ogrn, okpo,
                 organization_rs, bank_name, bank_bik, bank_ks, contract_file):
    print("* @sync_to_async() def add_contract")
    try:
        print("try (new_contract = ContractBase()")
        new_contract = ContractBase(customer_delegate=customername,
                                    quantity=quantity,
                                    contract_file=contract_file,
                                    price=price,
                                    adressofobject=adressofobject,
                                    mail=mail,
                                    total_cost=total_cost,
                                    townobject=townobject,
                                    telephonenum=telephonenum,
                                    customer_firm=customer_firm,
                                    organization_full_name=organization_full_name,
                                    organization_adress=organization_adress,
                                    customer_legal_basis=customer_legal_basis,
                                    organization_inn=organization_inn,
                                    organization_kpp=organization_kpp,
                                    ogrn=ogrn,
                                    okpo=okpo,
                                    organization_rs=organization_rs,
                                    bank_name=bank_name,
                                    bank_bik=bank_bik,
                                    bank_ks=bank_ks)

        print("try new_contract.save()")
        new_contract.save()
        return new_contract



    except Exception as e:
        print("Can not create class instance")
        print(e)


@sync_to_async()
def add_private_contract(customername, quantity, price, address_of_object, town_object, private_contract_file, source,
                         square, published, ):
    try:
        new_customer = Customer_category(name=customername)
        new_customer.save()
        print("Такого заказчика нет")
    except:
        print("Такой заказчик есть")
        new_customer = Customer_category.objects.get(name=customername)
        print("Добавляем")
    print("* add_private_contract")


    try:
        print("try (new_contract = ContractBase()")
        new_contract = PrivateContract(customername=new_customer,
                                       quantity=quantity,
                                       price=price,
                                       address_of_object=address_of_object,
                                       town_object=town_object,
                                       private_contract_file=private_contract_file,
                                       source=source,
                                       square=square,
                                       published=published,
                                       )
        print("-----------------------------------------------------------------------------------")
        print(f'private_contract_file=private_contract_file  {new_contract.private_contract_file}')
        print("-----------------------------------------------------------------------------------")
        print("try new_contract.save()")
        new_contract.save()
        return new_contract

    except Exception as e:
        print("Can not create class instance")
        print(e)
        return None


@sync_to_async()
def add_organization(name, mail, telephonenum, organization_full_name, organization_adress,
                     organization_inn, organization_kpp, ogrn, okpo,
                     organization_rs, bank_name, bank_bik, bank_ks):
    new_org = Organization(name=name,
                           mail=mail,
                           telephonenum=telephonenum,
                           organization_full_name=organization_full_name,
                           organization_adress=organization_adress,
                           organization_inn=organization_inn,
                           organization_kpp=organization_kpp,
                           ogrn=ogrn,
                           okpo=okpo,
                           organization_rs=organization_rs,
                           bank_name=bank_name,
                           bank_bik=bank_bik,
                           bank_ks=bank_ks)
    new_org.save()
    print("In add organisation")


@sync_to_async
def add_or_create_user(user_id: int) -> TGUser:
    user, created = TGUser.objects.get_or_create(tg_id=user_id)
    if created:
        logger.info(f"user {user.tg_id} was added to DB")
    else:
        logger.info(f"User {user.tg_id} is already exist")
    return user


@sync_to_async
def add_profit(customer, price, description, category):
    print("in # def add_profit")
    try:
        new_customer = Customer_category(name=customer)
        new_customer.save()
        print("Такого заказчика нет")
    except:
        print("Такой заказчик есть")
        new_customer = Customer_category.objects.get(name=customer)
        print("Добавляем")
    try:
        new_profit = AddProfits(customer=new_customer,
                                price=float(price),
                                description=str(description),
                                category=int(category))
        new_profit.save()
        print("Запись прошла успешно")
    except Exception as e:
        # todo Нужна проверка наличия в Customer_category с добавлением
        print("Запись не успешна")
        print(e)


if __name__ == '__main__':
    pass
