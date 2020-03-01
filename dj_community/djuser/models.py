from django.db import models

# Create your models here.

class Djuser(models.Model):
	objects = models.Manager()
	username = models.CharField(max_length = 64, verbose_name = "아이디")
	useremail = models.EmailField(max_length = 128, verbose_name = "이메일")
	password = models.CharField(max_length = 64, verbose_name = "비밀번호")
	registerd_dttm = models.DateTimeField(auto_now_add = True, verbose_name = "등록일시")

	def __str__(self):
		return self.username
	
	class Meta:
		db_table = "djuser"
		verbose_name = "사용자관리"
		verbose_name_plural = "사용자관리"

# EOF
