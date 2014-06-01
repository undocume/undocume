# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ServiceTranslate.description'
        db.alter_column(u'home_servicetranslate', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Category.description'
        db.alter_column(u'home_category', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'InformationType.description'
        db.alter_column(u'home_informationtype', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'CategoryTranslate.description'
        db.alter_column(u'home_categorytranslate', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Information.description'
        db.alter_column(u'home_information', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Service.description'
        db.alter_column(u'home_service', 'description', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):

        # Changing field 'ServiceTranslate.description'
        db.alter_column(u'home_servicetranslate', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Category.description'
        db.alter_column(u'home_category', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'InformationType.description'
        db.alter_column(u'home_informationtype', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'CategoryTranslate.description'
        db.alter_column(u'home_categorytranslate', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Information.description'
        db.alter_column(u'home_information', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Service.description'
        db.alter_column(u'home_service', 'description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    models = {
        u'home.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'home.categorytranslate': {
            'Meta': {'object_name': 'CategoryTranslate'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'home.information': {
            'Meta': {'ordering': "['name']", 'object_name': 'Information'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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