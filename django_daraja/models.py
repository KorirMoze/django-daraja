# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AccessToken(models.Model):
	token = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		get_latest_by = 'created_at'

	def __str__(self):
		return self.token


class Hero(models.Model):
	phone_number = models.CharField(max_length=60)
	service_code = models.CharField(max_length=60,null=True)
	session_id = models.CharField(max_length=60)
	text = models.CharField(max_length=4,null=True)


	

	def __str__(self):
		return self.phone_number