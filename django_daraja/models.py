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


# class Hero(models.Model):
# 	phoneNumber = models.CharField(max_length=60)
# 	servicecode = models.CharField(max_length=60)
# 	sessionid = models.CharField(max_length=60)
# 	text = models.CharField(max_length=4)

	

# 	def __str__(self):
# 		return self.phoneNumber

class Hro(models.Model):
	phoneNumber = models.CharField(max_length=60)
	serviceCode = models.CharField(max_length=60)
	sessionID = models.CharField(max_length=60)
	text = models.CharField(max_length=4, null=True)

	

	def __str__(self):
		return self.phoneNumber