# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Drink'
        db.create_table(u'bartender_drink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'bartender', ['Drink'])

        # Adding model 'Ingredient'
        db.create_table(u'bartender_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drink', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bartender.Drink'], null=True)),
        ))
        db.send_create_signal(u'bartender', ['Ingredient'])


    def backwards(self, orm):
        # Deleting model 'Drink'
        db.delete_table(u'bartender_drink')

        # Deleting model 'Ingredient'
        db.delete_table(u'bartender_ingredient')


    models = {
        u'bartender.drink': {
            'Meta': {'object_name': 'Drink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'bartender.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'drink': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bartender.Drink']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bartender']