# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IngredientForDrink'
        db.create_table(u'bartender_ingredientfordrink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drink', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bartender.Drink'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bartender.Ingredient'])),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
        ))
        db.send_create_signal(u'bartender', ['IngredientForDrink'])

        # Removing M2M table for field ingredients on 'Drink'
        db.delete_table('bartender_drink_ingredients')


    def backwards(self, orm):
        # Deleting model 'IngredientForDrink'
        db.delete_table(u'bartender_ingredientfordrink')

        # Adding M2M table for field ingredients on 'Drink'
        db.create_table(u'bartender_drink_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drink', models.ForeignKey(orm[u'bartender.drink'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'bartender.ingredient'], null=False))
        ))
        db.create_unique(u'bartender_drink_ingredients', ['drink_id', 'ingredient_id'])


    models = {
        u'bartender.drink': {
            'Meta': {'ordering': "['name']", 'object_name': 'Drink'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'glass': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bartender.Ingredient']", 'through': u"orm['bartender.IngredientForDrink']", 'symmetrical': 'False'}),
            'mix_instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Drink'", 'max_length': '1000'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'bartender.ingredient': {
            'Meta': {'ordering': "['name']", 'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unnamed Ingredient'", 'max_length': '500'})
        },
        u'bartender.ingredientfordrink': {
            'Meta': {'object_name': 'IngredientForDrink'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'drink': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bartender.Drink']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bartender.Ingredient']"})
        }
    }

    complete_apps = ['bartender']