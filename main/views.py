from django.shortcuts import render

# Create your views here.
def mainpage(request):
    context = {
        "generation": 2,
        "info": {'variable': '변수', 'tag': '태그', 'filter': '필터'},
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    features = [
        "입천장이 까맣다",
        "고구마를 너무 너무 좋아해서 5키로가 넘은 적이 있음",
        "산책을 싫어해서 절대 걷지 않고 안겨서 감",
        "혼자 있으면 화장실도 잘 안 감",
        "최근에 털을 빡빡 깎았음",
    ]
    return render(request, 'main/secondpage.html', {'features': features})
