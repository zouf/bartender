# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ingredient.is_available'
        db.add_column(u'bartender_ingredient', 'is_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ingredient.is_available'
        db.delete_column(u'bartender_ingredient', 'is_available')


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
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Ingredient'", 'max_length': '500'})
        }
    }

    complete_apps = ['bartender']