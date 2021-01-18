from django.template.defaulttags import register

@register.filter(name='lookupMIN')
def lookupMIN(value, arg):
    return value.get(arg)[0]

@register.filter(name='lookupMAX')
def lookupMAX(value, arg):
    return value.get(arg)[1]

@register.filter(name='access')
def lookupMAX(value, arg):
    return value[arg]

@register.filter(name='access2')
def lookupMAX(value, arg):
    return value[arg][0]