from django.db import models


class Venda(models.Model):
    data = models.DateField()
    produto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    faturamento = models.DecimalField(max_digits=12, decimal_places=2)
    data_importacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-data']

    def __str__(self):
        return f"{self.produto} - {self.data}"


class ArquivoImportado(models.Model):
    nome_arquivo = models.CharField(max_length=255)
    data_upload = models.DateTimeField(auto_now_add=True)
    total_linhas = models.IntegerField()

    class Meta:
        verbose_name = "Arquivo Importado"
        verbose_name_plural = "Arquivos Importados"
        ordering = ['-data_upload']

    def __str__(self):
        return f"{self.nome_arquivo} - {self.total_linhas} linhas"
