from django.db import models

class Board(models.Model):
	objects = models.Manager()
	title = models.CharField(max_length = 128, verbose_name = "제목")
	contents = models.TextField(verbose_name = "내용")
	writer = models.ForeignKey('djuser.Djuser', on_delete = models.CASCADE, verbose_name = "작성자")
	registerd_dttm = models.DateTimeField(auto_now_add = True, verbose_name = "등록시간")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "board"
		verbose_name = "게시글"
		verbose_name_plural = "게시글"

# EOF
