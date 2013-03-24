# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Drink.category'
        db.add_column(u'bartender_drink', 'category',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Drink.rating'
        db.add_column(u'bartender_drink', 'rating',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Drink.url'
        db.add_column(u'bartender_drink', 'url',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Drink.mix_instructions'
        db.add_column(u'bartender_drink', 'mix_instructions',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Drink.glass'
        db.add_column(u'bartender_drink', 'glass',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Drink.category'
        db.delete_column(u'bartender_drink', 'category')

        # Deleting field 'Drink.rating'
        db.delete_column(u'bartender_drink', 'rating')

        # Deleting field 'Drink.url'
        db.delete_column(u'bartender_drink', 'url')

        # Deleting field 'Drink.mix_instructions'
        db.delete_column(u'bartender_drink', 'mix_instructions')

        # Deleting field 'Drink.glass'
        db.delete_column(u'bartender_drink', 'glass')


    models = {
        u'bartender.drink': {
            'Meta': {'object_name': 'Drink'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'glass': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bartender.Ingredient']", 'symmetrical': 'False'}),
            'mix_instructions': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Drink'", 'max_length': '500'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'})
        },
        u'bartender.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Ingredient'", 'max_length': '500'})
        }
    }

    complete_apps = ['bartender']