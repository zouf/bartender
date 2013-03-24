# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Drink.category'
        db.alter_column(u'bartender_drink', 'category', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

        # Changing field 'Drink.rating'
        db.alter_column(u'bartender_drink', 'rating', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

        # Changing field 'Drink.name'
        db.alter_column(u'bartender_drink', 'name', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Drink.url'
        db.alter_column(u'bartender_drink', 'url', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

        # Changing field 'Drink.glass'
        db.alter_column(u'bartender_drink', 'glass', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

        # Changing field 'Drink.mix_instructions'
        db.alter_column(u'bartender_drink', 'mix_instructions', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Drink.category'
        db.alter_column(u'bartender_drink', 'category', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Drink.rating'
        db.alter_column(u'bartender_drink', 'rating', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Drink.name'
        db.alter_column(u'bartender_drink', 'name', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Drink.url'
        db.alter_column(u'bartender_drink', 'url', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Drink.glass'
        db.alter_column(u'bartender_drink', 'glass', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Drink.mix_instructions'
        db.alter_column(u'bartender_drink', 'mix_instructions', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    models = {
        u'bartender.drink': {
            'Meta': {'object_name': 'Drink'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'glass': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bartender.Ingredient']", 'symmetrical': 'False'}),
            'mix_instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Drink'", 'max_length': '1000'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'bartender.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Ingredient'", 'max_length': '500'})
        }
    }

    complete_apps = ['bartender']