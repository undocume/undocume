# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'home_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'home', ['Language'])

        # Adding model 'Category'
        db.create_table(u'home_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['Category'])

        # Adding model 'CategoryTranslate'
        db.create_table(u'home_categorytranslate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Language'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['CategoryTranslate'])

        # Adding model 'TypeOrganization'
        db.create_table(u'home_typeorganization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'home', ['TypeOrganization'])

        # Adding model 'Service'
        db.create_table(u'home_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Category'])),
            ('Type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.TypeOrganization'])),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contactemail', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('contactnumber', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('fee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ss', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['Service'])

        # Adding model 'ServiceTranslate'
        db.create_table(u'home_servicetranslate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Language'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Service'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['ServiceTranslate'])

        # Adding model 'InformationType'
        db.create_table(u'home_informationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['InformationType'])

        # Adding model 'Information'
        db.create_table(u'home_information', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('informationtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.InformationType'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['Information'])

        # Adding model 'InformationTranslate'
        db.create_table(u'home_informationtranslate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Language'])),
            ('information', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Information'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['InformationTranslate'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'home_language')

        # Deleting model 'Category'
        db.delete_table(u'home_category')

        # Deleting model 'CategoryTranslate'
        db.delete_table(u'home_categorytranslate')

        # Deleting model 'TypeOrganization'
        db.delete_table(u'home_typeorganization')

        # Deleting model 'Service'
        db.delete_table(u'home_service')

        # Deleting model 'ServiceTranslate'
        db.delete_table(u'home_servicetranslate')

        # Deleting model 'InformationType'
        db.delete_table(u'home_informationtype')

        # Deleting model 'Information'
        db.delete_table(u'home_information')

        # Deleting model 'InformationTranslate'
        db.delete_table(u'home_informationtranslate')


    models = {
        u'home.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'home.categorytranslate': {
            'Meta': {'object_name': 'CategoryTranslate'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.information': {
            'Meta': {'ordering': "['name']", 'object_name': 'Information'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informationtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.InformationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'home.informationtranslate': {
            'Meta': {'object_name': 'InformationTranslate'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Information']"}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.informationtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'InformationType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'home.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'home.service': {
            'Meta': {'ordering': "['name']", 'object_name': 'Service'},
            'Type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.TypeOrganization']"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Category']"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contactemail': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contactnumber': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ss': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'home.servicetranslate': {
            'Meta': {'object_name': 'ServiceTranslate'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Service']"})
        },
        u'home.typeorganization': {
            'Meta': {'object_name': 'TypeOrganization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['home']