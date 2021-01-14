from django.template.defaulttags import register

@register.filter(name='lookupMIN')
def lookupMIN(value, arg):
    return value.get(arg)[0]


@register.filter(name='lookupMAX')
def lookupMAX(value, arg):
    return value.get(arg)[1]