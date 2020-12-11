from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Sankarsan",email="sankarsanpakhira@gmail.com",is_staff=True,is_superuser=True,
                            phone="7063220399",gender="Male")
        
        user.set_password("Sanu54321")
        user.save()

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]