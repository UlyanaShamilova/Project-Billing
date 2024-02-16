from django.shortcuts import render
from .models import Lessee, Complex, Lessor
# Create your views here.
def new_lessee(request):
    context = {}

    if request.method == 'POST':

        complex = request.POST.get('complexes1')
        num_contract = request.POST.get('num_conct')
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')
        data3 = request.POST.get('data3')
        lessee = request.POST.get('side1')
        lessor = request.POST.get('side2')
        lessor_r_s = request.POST.get('side3')
        type_contract = request.POST.get('others1')
        comment = request.POST.get('others5')
        num_document_in_count = request.POST.get('others6')
        main_contract = request.POST.get('others7')
        main_lot = request.POST.get('others8')

        if lessee:
            Lessee.objects.create(
                lessee =lessee,
                comment = comment
            )
            if complex:
                Complex.objects.create(
                    complex = complex
                )

            if lessor:
                Lessor.objects.create(
                    num_contract  =num_contract, 
                    data1 =data1,
                    data2 =data2,
                    data3  =data3, 
                    lessor  =lessor, 
                    lessor_r_s =lessor_r_s,
                    type_contract =type_contract,
                    num_document_in_count =num_document_in_count,
                    main_contract =main_contract,
                    main_lot = main_lot
                )

    return render(request, 'new_lesse/new_lessee.html', context)