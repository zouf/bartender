# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ingredient.drink'
        db.delete_column(u'bartender_ingredient', 'drink_id')

        # Adding field 'Ingredient.name'
        db.add_column(u'bartender_ingredient', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Unnamed Ingredient', max_length=500),
                      keep_default=False)

        # Adding M2M table for field ingredients on 'Drink'
        db.create_table(u'bartender_drink_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drink', models.ForeignKey(orm[u'bartender.drink'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'bartender.ingredient'], null=False))
        ))
        db.create_unique(u'bartender_drink_ingredients', ['drink_id', 'ingredient_id'])


    def backwards(self, orm):
        # Adding field 'Ingredient.drink'
        db.add_column(u'bartender_ingredient', 'drink',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bartender.Drink'], null=True),
                      keep_default=False)

        # Deleting field 'Ingredient.name'
        db.delete_column(u'bartender_ingredient', 'name')

        # Removing M2M table for field ingredients on 'Drink'
        db.delete_table('bartender_drink_ingredients')


    models = {
        u'bartender.drink': {
            'Meta': {'object_name': 'Drink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bartender.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Drink'", 'max_length': '500'})
        },
        u'bartender.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Ingredient'", 'max_length': '500'})
        }
    }

    complete_apps = ['bartender']