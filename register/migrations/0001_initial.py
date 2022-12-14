# Generated by Django 4.1 on 2022-08-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("surname", models.CharField(max_length=65)),
                ("birth_date", models.DateField()),
                ("rg", models.CharField(max_length=7)),
                ("cpf", models.CharField(max_length=11)),
                ("cnpj", models.CharField(blank=True, max_length=14, null=True)),
                ("mother_name", models.CharField(blank=True, max_length=95, null=True)),
                ("phone", models.CharField(max_length=15)),
                ("country", models.CharField(default="Brazil", max_length=25)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapa"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceara"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espirito Santo"),
                            ("GO", "Goias"),
                            ("MA", "Maranhao"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Para"),
                            ("PB", "Paraiba"),
                            ("PR", "Parana"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piaui"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondonia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "Sao Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        default="",
                        max_length=2,
                    ),
                ),
                ("city", models.CharField(max_length=30)),
                ("neighborhood", models.CharField(max_length=30)),
                ("street", models.CharField(max_length=30)),
                ("number", models.IntegerField()),
                ("note", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
