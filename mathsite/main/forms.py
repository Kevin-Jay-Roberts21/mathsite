from django import forms 

class SearchAllPages(forms.Form):
	searchPages = forms.CharField(label="searchPages", required=True, widget=forms.Textarea(attrs={"placeholder": "Searching...", "rows": 1, "cols":20}))