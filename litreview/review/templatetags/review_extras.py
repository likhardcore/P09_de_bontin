from django import template
from datetime import datetime, timezone

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'moi'
    return user.username


@register.filter
def datetime_display(value):
    now = datetime.now(timezone.utc)
    time = value.time_created
    delta = (now-time).total_seconds()
    if delta < 60:
        return 'Il y a quelques secondes.'
    if delta < 3600:
        return "Il y a " + str(int(delta/60)) + " minutes."
    elif delta < 86400:
        return "Il y a " + str(int(delta/3600)) + " heures."
    else:
        return "A " + str(time.strftime("%H heure le %m/%d/%Y")) + "."
