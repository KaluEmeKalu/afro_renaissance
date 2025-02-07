# Generated manually

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifesto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Section',
            new_name='ManifestoSection',
        ),
    ]