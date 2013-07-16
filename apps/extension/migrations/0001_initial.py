# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Extension'
        db.create_table('extension_extension', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classroom', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['classroom.Classroom'], unique=True)),
            ('banner_filename', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('crn_list', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('meeting_time', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('meeting_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('textbook', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['extension.Textbook'], null=True, blank=True)),
            ('chapters', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('topic_list_main', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('topic_list_also', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('outcomes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('outline', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('extension', ['Extension'])

        # Adding model 'Textbook'
        db.create_table('extension_textbook', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('edition', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('extension', ['Textbook'])

        # Adding model 'WebpageComponent'
        db.create_table('extension_webpagecomponent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classroom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classroom.Classroom'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('access_index', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('extension', ['WebpageComponent'])


    def backwards(self, orm):
        # Deleting model 'Extension'
        db.delete_table('extension_extension')

        # Deleting model 'Textbook'
        db.delete_table('extension_textbook')

        # Deleting model 'WebpageComponent'
        db.delete_table('extension_webpagecomponent')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'classroom.classroom': {
            'Meta': {'ordering': "[u'-first_day']", 'object_name': 'Classroom'},
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classroom.Department']"}),
            'first_day': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classroom.Instructor']", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scratchpad': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'classroom.department': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Department'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'classroom.instructor': {
            'Meta': {'ordering': "[u'user__last_name', u'user__first_name']", 'object_name': 'Instructor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_hours': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'office_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'extension.extension': {
            'Meta': {'object_name': 'Extension'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'banner_filename': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'chapters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'classroom': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['classroom.Classroom']", 'unique': 'True'}),
            'crn_list': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meeting_time': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'outcomes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'outline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'textbook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['extension.Textbook']", 'null': 'True', 'blank': 'True'}),
            'topic_list_also': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'topic_list_main': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'extension.textbook': {
            'Meta': {'ordering': "[u'author', u'title', u'-edition']", 'object_name': 'Textbook'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'edition': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'extension.webpagecomponent': {
            'Meta': {'object_name': 'WebpageComponent'},
            'access_index': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'classroom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classroom.Classroom']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['extension']