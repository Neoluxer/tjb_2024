from django.shortcuts import render
from pathlib import Path

# Create your views here.
def u_c_f_private(request):
    customers_names_list = [w for w in
                            Path("media/files/customers.txt").read_text(encoding="utf-8").replace("\n", ";").split(";")]
    return render(request, 'make_contract_base/u_c_f_private.html',{'customers_names_list':customers_names_list} )


def u_c_f_firm(request):
    return render(request, 'u_c_f_firm.html', )

def result_contract(request):
    return render(request, 'make_contract_base/result_contract.html' )



if __name__ == '__main__':
    words = [w for w in Path("customers.txt").read_text(encoding="utf-8").replace("\n", ";").split(";")]
    print(words)

