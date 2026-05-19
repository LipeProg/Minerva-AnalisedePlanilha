from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ArquivoImportado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_arquivo', models.CharField(max_length=255)),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('total_linhas', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Arquivo Importado',
                'verbose_name_plural': 'Arquivos Importados',
                'ordering': ['-data_upload'],
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('produto', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('faturamento', models.DecimalField(decimal_places=2, max_digits=12)),
                ('data_importacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
                'ordering': ['-data'],
            },
        ),
    ]
