from django.shortcuts import render, get_object_or_404
from .models import Criatura, Habitat

# Create your views here.
def inicio(request):
    criaturas = Criatura.objects.select_related('habitat').filter(visible=True)

    habitat_id = request.GET.get('habitat',"")
    q = request.GET.get('q',"").strip()

    if habitat_id.isdigit():
        criaturas = criaturas.filter(habitat_id=int(habitat_id))
    if q:
        criaturas = criaturas.filter(nombre__icontains=q)

    contexto = {
        'criaturas': criaturas,
        'habitats': Habitat.objects.all(),
        'habitat_sel': habitat_id,
        'q': q,
    }
    return render(request, 'bestiario/inicio.html', contexto)

def detalle(request, id):
    criatura = get_object_or_404(
        Criatura.objects.select_related('habitat'),
        id=id,
        visible=True,
    )
    return render(request, 'bestiario/detalle.html', {'criatura': criatura}) 