from django import forms
from django.utils.translation import gettext as _


# first step of iquiry form


class cs_FormInitial(forms.Form):
    name = forms.CharField(label=_('Vaše jméno'), required=True)
    email = forms.EmailField(label=_('Váš email'), required=True)
    gdpr = forms.BooleanField(
        label=_('Tímto souhlasím se zpracováním mých osobních údajů na základě GDPR.'))
