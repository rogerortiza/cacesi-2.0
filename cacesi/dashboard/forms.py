#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class LoginClientForm(forms.Form):
	username = forms.CharField( max_length = 20)
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )

	def __init__(self, *args, **kwargs):
		super(LoginClientForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'id': 'username_login', 'class': '' } )
		self.fields['password'].widget.attrs.update( {'id': 'password_login', 'class': '' } )
