# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_invoice_pdf_generated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='pdf_generated',
        ),
        migrations.AddField(
            model_name='invoice',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=b'invoices/'),
        ),
    ]
