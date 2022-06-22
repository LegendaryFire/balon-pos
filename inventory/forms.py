from inventory.models import Vehicle
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from django import forms


class VehicleForm(forms.ModelForm):
    stock = forms.IntegerField(help_text="The stock number of the vehicle.", disabled=True, required=False)

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = True
        self.helper.layout = Layout(
            HTML('<h4 class="text-muted mt-3">Description</h4><hr/>'),
            Row(
                Column("stock", css_class='col-md-3'),
                Column("vin", css_class='col-md-9'),
            ),
            Row(
                Column("year", css_class='col-6 col-md-3'),
                Column("make", css_class='col-6 col-md-3'),
                Column("model", css_class='col-6 col-md-3'),
                Column("trim", css_class='col-6 col-md-3'),
            ),
            Row(
                Column("mileage", css_class='col-6 col-md-3'),
                Column("mileage_units", css_class='col-6 col-md-3'),
                Column("condition", css_class='col-6 col-md-3'),
                Column("color", css_class='col-6 col-md-3'),
            ),
            Row(
                Column("branch", css_class='col-6 col-md-3'),
            ),
            HTML('<h4 class="text-muted">Additional Fields</h4><hr/>'),
            Row(
                Column("body_style", css_class='col-6 col-md-4'),
                Column("body_type", css_class='col-6 col-md-4'),
                Column("engine_type", css_class='col-6 col-md-4'),
            ),
            Row(
                Column('pickup_location', css_class='col-12, col-md-6'),
                Column('disclosures', css_class='col-12 col-md-6'),
            ),
        )

    class Meta:
        model = Vehicle
        fields = '__all__'
        localized_fields = ('mileage', )
