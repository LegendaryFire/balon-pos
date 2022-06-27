from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, HTML, Button
from django import forms
from django.forms import widgets
from sales.models import PurchaseOrder, SalesOrder
from django_select2 import forms as s2forms


class CustomerWidget(s2forms.ModelSelect2Widget):
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
        self.helper.include_media = False
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
                                data_bs_target="#customerModal"
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
                Column(PrependedText("asking_price", '$'), css_class='col-6 col-md-3'),
                Column("method", css_class='col-6 col-md-3'),
                Column("notes", css_class='col-6 col-md-3'),
                Column("purchase_date", css_class='col-6 col-md-3'),
            ),
            Row(
                Column("bill_of_sale", css_class='col-12, col-md-6'),
            ),
        )

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        localized_fields = '__all__'
        exclude = ('vehicle', 'sales_person', )
        widgets = {
            'purchase_date': widgets.DateInput(attrs={'type': 'date'}),
            'seller': CustomerWidget,
        }


class SaleForm(forms.ModelForm):
    total = forms.CharField(label="Total", required=False, disabled=True, initial=0.0)

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.layout = Layout(
            HTML("<h4 class=\"text-muted mt-3\">Purchaser Information</h4><hr/>"),
            Row(
                Column("purchaser", css_class='col-8 col-md-10'),
                Column(
                        Div(
                            HTML("<label for=\"id_add_customer\" class=\"form-label requiredField\">Customer</label>"),
                            Button(
                                "id_add_customer",
                                "Create",
                                css_class="btn btn-sm btn-outline-primary form-control",
                                css_id='id_add_customer',
                                data_bs_toggle="modal",
                                data_bs_target="#customerModal"
                            ),
                            css_class='mb-3'
                        ),
                        css_class='col-4 col-md-2',
                    ),
            ),
            HTML("<h4 class=\"text-muted mt-3\">Sale Pricing</h4><hr/>"),
            Row(
                Column(PrependedText("price", '$'), css_class='col-6 col-md-3'),
                Column(PrependedText("pst", '$'), css_class='col-6 col-md-3'),
                Column(PrependedText("gst", '$'), css_class='col-6 col-md-3'),
                Column(PrependedText("total", '$'), css_class='col-6 col-md-3'),
            ),
            Row(
                Column("sale_mileage", css_class='col-6 col-md-3'),
                Column("sale_date", css_class='col-6 col-md-3'),
                Column("paid_date", css_class='col-6 col-md-3'),
                Column("method", css_class='col-6 col-md-3'),
            ),
        )

    class Meta:
        model = SalesOrder
        fields = '__all__'
        localized_fields = '__all__'
        exclude = ('vehicle', 'sales_person', 'registration', )
        widgets = {
            'sale_date': widgets.DateInput(attrs={'type': 'date'}),
            'paid_date': widgets.DateInput(attrs={'type': 'date'}),
            'purchaser': CustomerWidget,
        }
