from User.models import User
from django import forms
from django.forms.widgets import Widget
from django.forms.utils import flatatt
from django.utils.html import format_html

class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		manage_owned_comments = False
		if not self.current_user.is_superuser and len(self.current_user.groups.filter(name="Manage Owned Comments")):
			manage_owned_comments = True
		if self.instance.pk and manage_owned_comments and self.instance.created_by != self.current_user:
			self.fields['comment'].widget = ReadOnlyComment()
			self.can_delete = False 

class ReadOnlyComment(Widget):
	def render(self, name, value, attrs=None):
		if value is None:
			value = ''
		final_attrs = self.build_attrs(attrs)
		return format_html('<textarea {} name="{}" rows="10" cols="40" class="vLargeTextField" readonly="">{}</textarea>',flatatt(final_attrs), name, value)

