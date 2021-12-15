from baskets.models import Basket

def basket(request):
    basked_list = []
    if request.user.is_authenticated:
        basked_list = Basket.objects.filter(user=request.user)
    return {
        'baskets':basked_list
    }