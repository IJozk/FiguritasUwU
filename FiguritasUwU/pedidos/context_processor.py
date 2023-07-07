def total_carro(request):
    total=0
    if request.user.is_authenticated:
        if 'carro' in request.session: 
            for key, value in request.session["carro"].items():
                total=total+(int(value["precio"])*value["cantidad"])
    return {"total_carro":total}