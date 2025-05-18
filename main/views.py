from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# функции представления/контроллеры
def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'МО-ШОП — Главная',
        'content': 'Добро пожаловать!',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'МО-ШОП — О нас',
        'content': 'О нас',
        'text_on_page': 'Здравствуйте, покупатель!\n\nМы, студенты МатМеха УрФУ, решили создать эту площадку, чтобы вы могли в любой момент порадовать себя новой классной покупкой, не выходя из дома.\n\nПриятных покупок!'
    }

    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'МО-ШОП — Контакты',
        'content': 'Контакты',
        'text_on_page': 'Уважаемый покупатель!\n\nВы можете связаться с нами, написав письмо на почту с пометкой "МО-ШОП":\n',
        'email_text': 'example@mail.ru',
        'email_href': 'mailto:example@mail.ru'
    }

    return render(request, 'main/contacts.html', context)


def delivery_and_payments(request):
    context = {
        'title': 'МО-ШОП — Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Уважаемый покупатель!\n\nДоставка осуществляется по территории России в фирменные пункты выдачи "МО-ШОП".\nОплата производится онлайн по номеру банковской карты или СБП.\n\nПриятных покупок!'
    }

    return render(request, 'main/delivery_and_payments.html', context)
