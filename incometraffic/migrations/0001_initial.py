# Generated by Django 2.2.6 on 2019-11-04 22:25

import uuid

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
import django.utils.timezone
import djmoney.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyApiEndpoint",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, null=None)),
                ("endpoint", models.URLField(unique=True)),
                ("status", models.CharField(choices=[("live", "live"), ("down", "down")], max_length=200)),
                ("created_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("headers", django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectLimit",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("time_limit", models.DurationField()),
                (
                    "amount_currency",
                    djmoney.models.fields.CurrencyField(
                        choices=[
                            ("XUA", "ADB Unit of Account"),
                            ("AFN", "Afghani"),
                            ("DZD", "Algerian Dinar"),
                            ("ARS", "Argentine Peso"),
                            ("AMD", "Armenian Dram"),
                            ("AWG", "Aruban Guilder"),
                            ("AUD", "Australian Dollar"),
                            ("AZN", "Azerbaijanian Manat"),
                            ("BSD", "Bahamian Dollar"),
                            ("BHD", "Bahraini Dinar"),
                            ("THB", "Baht"),
                            ("PAB", "Balboa"),
                            ("BBD", "Barbados Dollar"),
                            ("BYN", "Belarussian Ruble"),
                            ("BYR", "Belarussian Ruble"),
                            ("BZD", "Belize Dollar"),
                            ("BMD", "Bermudian Dollar (customarily known as Bermuda Dollar)"),
                            ("BTN", "Bhutanese ngultrum"),
                            ("VEF", "Bolivar Fuerte"),
                            ("BOB", "Boliviano"),
                            ("XBA", "Bond Markets Units European Composite Unit (EURCO)"),
                            ("BRL", "Brazilian Real"),
                            ("BND", "Brunei Dollar"),
                            ("BGN", "Bulgarian Lev"),
                            ("BIF", "Burundi Franc"),
                            ("XOF", "CFA Franc BCEAO"),
                            ("XAF", "CFA franc BEAC"),
                            ("XPF", "CFP Franc"),
                            ("CAD", "Canadian Dollar"),
                            ("CVE", "Cape Verde Escudo"),
                            ("KYD", "Cayman Islands Dollar"),
                            ("CLP", "Chilean peso"),
                            ("XTS", "Codes specifically reserved for testing purposes"),
                            ("COP", "Colombian peso"),
                            ("KMF", "Comoro Franc"),
                            ("CDF", "Congolese franc"),
                            ("BAM", "Convertible Marks"),
                            ("NIO", "Cordoba Oro"),
                            ("CRC", "Costa Rican Colon"),
                            ("HRK", "Croatian Kuna"),
                            ("CUP", "Cuban Peso"),
                            ("CUC", "Cuban convertible peso"),
                            ("CZK", "Czech Koruna"),
                            ("GMD", "Dalasi"),
                            ("DKK", "Danish Krone"),
                            ("MKD", "Denar"),
                            ("DJF", "Djibouti Franc"),
                            ("STD", "Dobra"),
                            ("DOP", "Dominican Peso"),
                            ("VND", "Dong"),
                            ("XCD", "East Caribbean Dollar"),
                            ("EGP", "Egyptian Pound"),
                            ("SVC", "El Salvador Colon"),
                            ("ETB", "Ethiopian Birr"),
                            ("EUR", "Euro"),
                            ("XBB", "European Monetary Unit (E.M.U.-6)"),
                            ("XBD", "European Unit of Account 17(E.U.A.-17)"),
                            ("XBC", "European Unit of Account 9(E.U.A.-9)"),
                            ("FKP", "Falkland Islands Pound"),
                            ("FJD", "Fiji Dollar"),
                            ("HUF", "Forint"),
                            ("GHS", "Ghana Cedi"),
                            ("GIP", "Gibraltar Pound"),
                            ("XAU", "Gold"),
                            ("XFO", "Gold-Franc"),
                            ("PYG", "Guarani"),
                            ("GNF", "Guinea Franc"),
                            ("GYD", "Guyana Dollar"),
                            ("HTG", "Haitian gourde"),
                            ("HKD", "Hong Kong Dollar"),
                            ("UAH", "Hryvnia"),
                            ("ISK", "Iceland Krona"),
                            ("INR", "Indian Rupee"),
                            ("IRR", "Iranian Rial"),
                            ("IQD", "Iraqi Dinar"),
                            ("IMP", "Isle of Man Pound"),
                            ("JMD", "Jamaican Dollar"),
                            ("JOD", "Jordanian Dinar"),
                            ("KES", "Kenyan Shilling"),
                            ("PGK", "Kina"),
                            ("LAK", "Kip"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("AOA", "Kwanza"),
                            ("MMK", "Kyat"),
                            ("GEL", "Lari"),
                            ("LVL", "Latvian Lats"),
                            ("LBP", "Lebanese Pound"),
                            ("ALL", "Lek"),
                            ("HNL", "Lempira"),
                            ("SLL", "Leone"),
                            ("LSL", "Lesotho loti"),
                            ("LRD", "Liberian Dollar"),
                            ("LYD", "Libyan Dinar"),
                            ("SZL", "Lilangeni"),
                            ("LTL", "Lithuanian Litas"),
                            ("MGA", "Malagasy Ariary"),
                            ("MWK", "Malawian Kwacha"),
                            ("MYR", "Malaysian Ringgit"),
                            ("TMM", "Manat"),
                            ("MUR", "Mauritius Rupee"),
                            ("MZN", "Metical"),
                            ("MXV", "Mexican Unidad de Inversion (UDI)"),
                            ("MXN", "Mexican peso"),
                            ("MDL", "Moldovan Leu"),
                            ("MAD", "Moroccan Dirham"),
                            ("BOV", "Mvdol"),
                            ("NGN", "Naira"),
                            ("ERN", "Nakfa"),
                            ("NAD", "Namibian Dollar"),
                            ("NPR", "Nepalese Rupee"),
                            ("ANG", "Netherlands Antillian Guilder"),
                            ("ILS", "New Israeli Sheqel"),
                            ("RON", "New Leu"),
                            ("TWD", "New Taiwan Dollar"),
                            ("NZD", "New Zealand Dollar"),
                            ("KPW", "North Korean Won"),
                            ("NOK", "Norwegian Krone"),
                            ("PEN", "Nuevo Sol"),
                            ("MRO", "Ouguiya"),
                            ("TOP", "Paanga"),
                            ("PKR", "Pakistan Rupee"),
                            ("XPD", "Palladium"),
                            ("MOP", "Pataca"),
                            ("PHP", "Philippine Peso"),
                            ("XPT", "Platinum"),
                            ("GBP", "Pound Sterling"),
                            ("BWP", "Pula"),
                            ("QAR", "Qatari Rial"),
                            ("GTQ", "Quetzal"),
                            ("ZAR", "Rand"),
                            ("OMR", "Rial Omani"),
                            ("KHR", "Riel"),
                            ("MVR", "Rufiyaa"),
                            ("IDR", "Rupiah"),
                            ("RUB", "Russian Ruble"),
                            ("RWF", "Rwanda Franc"),
                            ("XDR", "SDR"),
                            ("SHP", "Saint Helena Pound"),
                            ("SAR", "Saudi Riyal"),
                            ("RSD", "Serbian Dinar"),
                            ("SCR", "Seychelles Rupee"),
                            ("XAG", "Silver"),
                            ("SGD", "Singapore Dollar"),
                            ("SBD", "Solomon Islands Dollar"),
                            ("KGS", "Som"),
                            ("SOS", "Somali Shilling"),
                            ("TJS", "Somoni"),
                            ("SSP", "South Sudanese Pound"),
                            ("LKR", "Sri Lanka Rupee"),
                            ("XSU", "Sucre"),
                            ("SDG", "Sudanese Pound"),
                            ("SRD", "Surinam Dollar"),
                            ("SEK", "Swedish Krona"),
                            ("CHF", "Swiss Franc"),
                            ("SYP", "Syrian Pound"),
                            ("BDT", "Taka"),
                            ("WST", "Tala"),
                            ("TZS", "Tanzanian Shilling"),
                            ("KZT", "Tenge"),
                            ("XXX", "The codes assigned for transactions where no currency is involved"),
                            ("TTD", "Trinidad and Tobago Dollar"),
                            ("MNT", "Tugrik"),
                            ("TND", "Tunisian Dinar"),
                            ("TRY", "Turkish Lira"),
                            ("TMT", "Turkmenistan New Manat"),
                            ("TVD", "Tuvalu dollar"),
                            ("AED", "UAE Dirham"),
                            ("XFU", "UIC-Franc"),
                            ("USD", "US Dollar"),
                            ("USN", "US Dollar (Next day)"),
                            ("UGX", "Uganda Shilling"),
                            ("CLF", "Unidad de Fomento"),
                            ("COU", "Unidad de Valor Real"),
                            ("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),
                            ("UYU", "Uruguayan peso"),
                            ("UZS", "Uzbekistan Sum"),
                            ("VUV", "Vatu"),
                            ("CHE", "WIR Euro"),
                            ("CHW", "WIR Franc"),
                            ("KRW", "Won"),
                            ("YER", "Yemeni Rial"),
                            ("JPY", "Yen"),
                            ("CNY", "Yuan Renminbi"),
                            ("ZMK", "Zambian Kwacha"),
                            ("ZMW", "Zambian Kwacha"),
                            ("ZWD", "Zimbabwe Dollar A/06"),
                            ("ZWN", "Zimbabwe dollar A/08"),
                            ("ZWL", "Zimbabwe dollar A/09"),
                            ("PLN", "Zloty"),
                        ],
                        default="UAH",
                        editable=False,
                        max_length=3,
                    ),
                ),
                ("amount", djmoney.models.fields.MoneyField(decimal_places=4, default_currency="UAH", max_digits=19)),
                ("created_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "endpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="incometraffic.ProxyApiEndpoint"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomingMessage",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[("processing", "processing"), ("delivered", "delivered")],
                        default="processing",
                        max_length=200,
                    ),
                ),
                ("delivered_time", models.DateTimeField(default=None)),
                ("response_message", django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ("request_data", django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                (
                    "amount_currency",
                    djmoney.models.fields.CurrencyField(
                        choices=[
                            ("XUA", "ADB Unit of Account"),
                            ("AFN", "Afghani"),
                            ("DZD", "Algerian Dinar"),
                            ("ARS", "Argentine Peso"),
                            ("AMD", "Armenian Dram"),
                            ("AWG", "Aruban Guilder"),
                            ("AUD", "Australian Dollar"),
                            ("AZN", "Azerbaijanian Manat"),
                            ("BSD", "Bahamian Dollar"),
                            ("BHD", "Bahraini Dinar"),
                            ("THB", "Baht"),
                            ("PAB", "Balboa"),
                            ("BBD", "Barbados Dollar"),
                            ("BYN", "Belarussian Ruble"),
                            ("BYR", "Belarussian Ruble"),
                            ("BZD", "Belize Dollar"),
                            ("BMD", "Bermudian Dollar (customarily known as Bermuda Dollar)"),
                            ("BTN", "Bhutanese ngultrum"),
                            ("VEF", "Bolivar Fuerte"),
                            ("BOB", "Boliviano"),
                            ("XBA", "Bond Markets Units European Composite Unit (EURCO)"),
                            ("BRL", "Brazilian Real"),
                            ("BND", "Brunei Dollar"),
                            ("BGN", "Bulgarian Lev"),
                            ("BIF", "Burundi Franc"),
                            ("XOF", "CFA Franc BCEAO"),
                            ("XAF", "CFA franc BEAC"),
                            ("XPF", "CFP Franc"),
                            ("CAD", "Canadian Dollar"),
                            ("CVE", "Cape Verde Escudo"),
                            ("KYD", "Cayman Islands Dollar"),
                            ("CLP", "Chilean peso"),
                            ("XTS", "Codes specifically reserved for testing purposes"),
                            ("COP", "Colombian peso"),
                            ("KMF", "Comoro Franc"),
                            ("CDF", "Congolese franc"),
                            ("BAM", "Convertible Marks"),
                            ("NIO", "Cordoba Oro"),
                            ("CRC", "Costa Rican Colon"),
                            ("HRK", "Croatian Kuna"),
                            ("CUP", "Cuban Peso"),
                            ("CUC", "Cuban convertible peso"),
                            ("CZK", "Czech Koruna"),
                            ("GMD", "Dalasi"),
                            ("DKK", "Danish Krone"),
                            ("MKD", "Denar"),
                            ("DJF", "Djibouti Franc"),
                            ("STD", "Dobra"),
                            ("DOP", "Dominican Peso"),
                            ("VND", "Dong"),
                            ("XCD", "East Caribbean Dollar"),
                            ("EGP", "Egyptian Pound"),
                            ("SVC", "El Salvador Colon"),
                            ("ETB", "Ethiopian Birr"),
                            ("EUR", "Euro"),
                            ("XBB", "European Monetary Unit (E.M.U.-6)"),
                            ("XBD", "European Unit of Account 17(E.U.A.-17)"),
                            ("XBC", "European Unit of Account 9(E.U.A.-9)"),
                            ("FKP", "Falkland Islands Pound"),
                            ("FJD", "Fiji Dollar"),
                            ("HUF", "Forint"),
                            ("GHS", "Ghana Cedi"),
                            ("GIP", "Gibraltar Pound"),
                            ("XAU", "Gold"),
                            ("XFO", "Gold-Franc"),
                            ("PYG", "Guarani"),
                            ("GNF", "Guinea Franc"),
                            ("GYD", "Guyana Dollar"),
                            ("HTG", "Haitian gourde"),
                            ("HKD", "Hong Kong Dollar"),
                            ("UAH", "Hryvnia"),
                            ("ISK", "Iceland Krona"),
                            ("INR", "Indian Rupee"),
                            ("IRR", "Iranian Rial"),
                            ("IQD", "Iraqi Dinar"),
                            ("IMP", "Isle of Man Pound"),
                            ("JMD", "Jamaican Dollar"),
                            ("JOD", "Jordanian Dinar"),
                            ("KES", "Kenyan Shilling"),
                            ("PGK", "Kina"),
                            ("LAK", "Kip"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("AOA", "Kwanza"),
                            ("MMK", "Kyat"),
                            ("GEL", "Lari"),
                            ("LVL", "Latvian Lats"),
                            ("LBP", "Lebanese Pound"),
                            ("ALL", "Lek"),
                            ("HNL", "Lempira"),
                            ("SLL", "Leone"),
                            ("LSL", "Lesotho loti"),
                            ("LRD", "Liberian Dollar"),
                            ("LYD", "Libyan Dinar"),
                            ("SZL", "Lilangeni"),
                            ("LTL", "Lithuanian Litas"),
                            ("MGA", "Malagasy Ariary"),
                            ("MWK", "Malawian Kwacha"),
                            ("MYR", "Malaysian Ringgit"),
                            ("TMM", "Manat"),
                            ("MUR", "Mauritius Rupee"),
                            ("MZN", "Metical"),
                            ("MXV", "Mexican Unidad de Inversion (UDI)"),
                            ("MXN", "Mexican peso"),
                            ("MDL", "Moldovan Leu"),
                            ("MAD", "Moroccan Dirham"),
                            ("BOV", "Mvdol"),
                            ("NGN", "Naira"),
                            ("ERN", "Nakfa"),
                            ("NAD", "Namibian Dollar"),
                            ("NPR", "Nepalese Rupee"),
                            ("ANG", "Netherlands Antillian Guilder"),
                            ("ILS", "New Israeli Sheqel"),
                            ("RON", "New Leu"),
                            ("TWD", "New Taiwan Dollar"),
                            ("NZD", "New Zealand Dollar"),
                            ("KPW", "North Korean Won"),
                            ("NOK", "Norwegian Krone"),
                            ("PEN", "Nuevo Sol"),
                            ("MRO", "Ouguiya"),
                            ("TOP", "Paanga"),
                            ("PKR", "Pakistan Rupee"),
                            ("XPD", "Palladium"),
                            ("MOP", "Pataca"),
                            ("PHP", "Philippine Peso"),
                            ("XPT", "Platinum"),
                            ("GBP", "Pound Sterling"),
                            ("BWP", "Pula"),
                            ("QAR", "Qatari Rial"),
                            ("GTQ", "Quetzal"),
                            ("ZAR", "Rand"),
                            ("OMR", "Rial Omani"),
                            ("KHR", "Riel"),
                            ("MVR", "Rufiyaa"),
                            ("IDR", "Rupiah"),
                            ("RUB", "Russian Ruble"),
                            ("RWF", "Rwanda Franc"),
                            ("XDR", "SDR"),
                            ("SHP", "Saint Helena Pound"),
                            ("SAR", "Saudi Riyal"),
                            ("RSD", "Serbian Dinar"),
                            ("SCR", "Seychelles Rupee"),
                            ("XAG", "Silver"),
                            ("SGD", "Singapore Dollar"),
                            ("SBD", "Solomon Islands Dollar"),
                            ("KGS", "Som"),
                            ("SOS", "Somali Shilling"),
                            ("TJS", "Somoni"),
                            ("SSP", "South Sudanese Pound"),
                            ("LKR", "Sri Lanka Rupee"),
                            ("XSU", "Sucre"),
                            ("SDG", "Sudanese Pound"),
                            ("SRD", "Surinam Dollar"),
                            ("SEK", "Swedish Krona"),
                            ("CHF", "Swiss Franc"),
                            ("SYP", "Syrian Pound"),
                            ("BDT", "Taka"),
                            ("WST", "Tala"),
                            ("TZS", "Tanzanian Shilling"),
                            ("KZT", "Tenge"),
                            ("XXX", "The codes assigned for transactions where no currency is involved"),
                            ("TTD", "Trinidad and Tobago Dollar"),
                            ("MNT", "Tugrik"),
                            ("TND", "Tunisian Dinar"),
                            ("TRY", "Turkish Lira"),
                            ("TMT", "Turkmenistan New Manat"),
                            ("TVD", "Tuvalu dollar"),
                            ("AED", "UAE Dirham"),
                            ("XFU", "UIC-Franc"),
                            ("USD", "US Dollar"),
                            ("USN", "US Dollar (Next day)"),
                            ("UGX", "Uganda Shilling"),
                            ("CLF", "Unidad de Fomento"),
                            ("COU", "Unidad de Valor Real"),
                            ("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),
                            ("UYU", "Uruguayan peso"),
                            ("UZS", "Uzbekistan Sum"),
                            ("VUV", "Vatu"),
                            ("CHE", "WIR Euro"),
                            ("CHW", "WIR Franc"),
                            ("KRW", "Won"),
                            ("YER", "Yemeni Rial"),
                            ("JPY", "Yen"),
                            ("CNY", "Yuan Renminbi"),
                            ("ZMK", "Zambian Kwacha"),
                            ("ZMW", "Zambian Kwacha"),
                            ("ZWD", "Zimbabwe Dollar A/06"),
                            ("ZWN", "Zimbabwe dollar A/08"),
                            ("ZWL", "Zimbabwe dollar A/09"),
                            ("PLN", "Zloty"),
                        ],
                        default="UAH",
                        editable=False,
                        max_length=3,
                    ),
                ),
                ("amount", djmoney.models.fields.MoneyField(decimal_places=4, default_currency="UAH", max_digits=19)),
                (
                    "proxy_project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="incometraffic.ProxyApiEndpoint"
                    ),
                ),
            ],
        ),
    ]