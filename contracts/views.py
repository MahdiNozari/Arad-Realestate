from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Contract
from django.contrib import messages
@login_required
def my_contracts(request):
    contracts_as_owner = request.user.seller_contracts.all()
    contracts_as_buyer = request.user.buyer_contracts.all()

    return render(request, 'contracts/my_contracts.html', {
        'contracts_as_owner': contracts_as_owner,
        'contracts_as_buyer': contracts_as_buyer,
    })

@login_required
def contract_detail(request, contract_id):
    contract = get_object_or_404(Contract, serial=contract_id)

    # اطمینان حاصل کنیم که کاربر حق دیدن قرارداد را دارد
    if contract.seller_customer != request.user and contract.buyer_customer != request.user:
        messages.error(request, "شما مجاز به مشاهده این قرارداد نیستید.")
        return redirect('contracts:my_contracts')

    return render(request, 'contracts/contract_detail.html', {'contract': contract})


from django.shortcuts import render
from .models import Contract

def agent_contracts(request):
    # قراردادهای مرتبط با ایجنت فعلی
    contracts = Contract.objects.filter(agent=request.user)
    return render(request, 'contracts/agent_contracts.html', {'contracts': contracts})
def contract_detail(request, serial):
    # جزئیات یک قرارداد خاص
    contract = get_object_or_404(Contract, serial=serial)
    return render(request, 'contracts/contract_details.html', {'contract': contract})
