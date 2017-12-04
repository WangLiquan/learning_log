#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-30 17:11:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import forms

from .models import Topic , Entry

class TopicForm(forms.ModelForm):
    class Meta:
    	model = Topic
    	fields = ['text']
    	labels = {'text': ''}
    	
    		
class EntryForm(forms.ModelForm):
    class Meta:
    	model = Entry
    	fields = ['text']
    	labels = {'text':''}
    	widgets = {'text':forms.Textarea(attrs={'cols':80})}