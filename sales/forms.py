from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, HTML, Button
from django import forms
from django.forms import widgets
from sales.models import PurchaseOrder
from django_select2 import forms as s2forms


class SellerWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "last_name__icontains",
        "phone_number__icontains",
    ]


class PurchaseForm(forms.ModelForm):
    total = forms.CharField(label="Total", required=False, disabled=True, initial=0.0)

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            HTML("<h4 class=\"text-muted mt-3\">Seller Information</h4><hr/>"),
            Row(
                Column("seller", css_class='col-8 col-md-10'),
                Column(
                        Div(
                            HTML("<label for=\"id_add_customer\" class=\"form-label requiredField\">Customer</label>"),
                            Button(
                                "id_add_customer",
                                "Create",
                                css_class="btn btn-sm btn-outline-primary form-control",
                                css_id='id_add_customer',
                                data_bs_toggle="modal",
                                data_bs_target="#modalCustomer"
                            ),
                            css_class='mb-3'
                        ),
                        css_class='col-4 col-md-2',
                    ),
            ),
            HTML("<h4 class=\"text-muted mt-3\">Purchase Pricing</h4><hr/>"),
            Row(
                Column(PrependedText("price", '$'), css_class='col-6 col-md-3'),
                Column(PrependedText("pst", '$'), css_class='col-6 col-md-3'),
                Column(PrependedText("gst", '$'),  css_class="col-6 col-md-3"),
                Column(PrependedText("total", '$'), css_class='col-6 col-md-3'),
            ),
            Row(
                Column("method", css_class='col-6 col-md-3'),
                Column("purchase_date", css_class='col-6 col-md-3'),
                Column(PrependedText("asking_price", '$'), css_class='col-6, col-md-3'),
                Column("bill_of_sale", css_class='col-6, col-md-3'),
            ),
        )

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        localized_fields = '__all__'
        exclude = ('sales_person', )
        widgets = {
            'purchase_date': widgets.DateInput(attrs={'type': 'date'}),
            'seller': SellerWidget,
        }
