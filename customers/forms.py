from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, HTML
from django_select2.forms import *

from customers.models import Customer


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class='col-6 col-md-3'),
                Column("last_name", css_class='col-6 col-md-3'),
                Column("province", css_class='col-6 col-md-3'),
                Column("city", css_class='col-6 col-md-3'),
            ),
            Row(
                Column("address", css_class='col-6 col-md-9'),
                Column("postal_code", css_class='col-6 col-md-3'),
            ),
            Row(
                Column("phone_number", css_class='col-12 col-md-6'),
                Column("email_address", css_class='col-12 col-md-6'),
            ),
            Row(
                Column("gst_number", css_class='col-6 col-md-6'),
                Column("notes", css_class='col-6 col-md-6'),
            ),
        )

    class Meta:
        model = Customer
        fields = '__all__'
