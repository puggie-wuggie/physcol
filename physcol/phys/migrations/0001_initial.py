# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('audience', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=2048)),
                ('local_contact0', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('local_contact1', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('notes', models.CharField(max_length=2048)),
                ('createdby_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(to='phys.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('affiliation', models.CharField(max_length=1028)),
                ('details', models.CharField(max_length=2048)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=524)),
                ('affiliation', models.CharField(max_length=2048)),
                ('research', models.CharField(max_length=2048)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('vote_count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='speaker_id',
            field=models.ForeignKey(to='phys.Speaker'),
        ),
        migrations.AddField(
            model_name='event',
            name='speaker',
            field=models.ForeignKey(to='phys.Speaker'),
        ),
    ]
