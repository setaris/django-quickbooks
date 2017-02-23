from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.encrypted


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickbooksToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', django_extensions.db.fields.encrypted.EncryptedCharField(max_length=255)),
                ('access_token_secret', django_extensions.db.fields.encrypted.EncryptedCharField(max_length=255)),
                ('realm_id', models.CharField(max_length=64)),
                ('data_source', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
