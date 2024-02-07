import conveyor_of_contract_instance as coci


if __name__ == '__main__':
    d1 = '1.1.2025'  # начальная дата
    d2 = '1.1.2026'  # конечная дата
    co_dataset = coci.contract_dataset_generator(15, d1, d2)
    print()
    print(coci.calendar_dict_from_instance_list(co_dataset))