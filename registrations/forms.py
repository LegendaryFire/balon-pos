from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Column
from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from registrations.models import Registration


class RegistrationRequestForm(forms.Form):
    def __init__(self, customer_id, *args, **kwargs):
        super(RegistrationRequestForm, self).__init__(*args, **kwargs)

        selected_queryset = Registration.objects.filter(
            sales_order__purchaser_id__exact=customer_id,
            date_requested__isnull=True,
            date_received__isnull=True,
        )

        queryset = Registration.objects.filter(
            sales_order__purchaser_id__exact=customer_id,
            date_received__isnull=True,
        )

        self.fields[f'select_request_{customer_id}'] = forms.ModelMultipleChoiceField(
            queryset=queryset,
            initial=selected_queryset,
            widget=ModelSelect2MultipleWidget(
                model=Registration,
                search_fields=[
                    'sales_order__vehicle__vin__icontains',
                    'sales_order__vehicle__year__icontains',
                    'sales_order__vehicle__make__icontains',
                    'sales_order__vehicle__model__icontains',
                    'sales_order__vehicle__trim__icontains',
                ],
                attrs={
                    'style': 'width:100%',
                }
            )
        )

        self.fields[f'select_request_{customer_id}'].label = "Selection"

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.layout = Layout(
            Row(
                Column(f'select_request_{customer_id}', css_class='col-12'),
            ),
            HTML(f'<input type="hidden" value="request" name="action">'),
        )


class RegistrationReceiveForm(forms.Form):
    def __init__(self, customer_id, *args, **kwargs):
        super(RegistrationReceiveForm, self).__init__(*args, **kwargs)

        selected_queryset = Registration.objects.filter(
            sales_order__purchaser_id__exact=customer_id,
            date_requested__isnull=False,
            date_received__isnull=True,
        )

        queryset = Registration.objects.filter(
            sales_order__purchaser_id__exact=customer_id,
            date_received__isnull=True,
        )

        self.fields[f'select_receive_{customer_id}'] = forms.ModelMultipleChoiceField(
            queryset=queryset,
            initial=selected_queryset,
            widget=ModelSelect2MultipleWidget(
                model=Registration,
                search_fields=[
                    'sales_order__vehicle__vin__icontains',
                    'sales_order__vehicle__year__icontains',
                    'sales_order__vehicle__make__icontains',
                    'sales_order__vehicle__model__icontains',
                    'sales_order__vehicle__trim__icontains',
                ],
                attrs={
                    'style': 'width:100%',
                }
            )
        )

        self.fields[f'select_receive_{customer_id}'].label = "Selection"

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.layout = Layout(
            Row(
                Column(f'select_receive_{customer_id}', css_class='col-12'),
            ),
            HTML(f'<input type="hidden" value="receive" name="action">'),
        )