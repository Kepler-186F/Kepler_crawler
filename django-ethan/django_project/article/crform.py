from django import forms

CHOICES = (
		('kansascity', 'kansascity'),
		('hudsonvalley', 'hudsonvalley'),
		('humboldt', 'humboldt'),
		('huntington', 'huntington'),
		('huntsville', 'huntsville'),
		('imperial', 'imperial'),
		('indianapolis', 'indianapolis'),
		('inlandempire', 'inlandempire'),
		('iowacity', 'iowacity'),
		('ithaca', 'ithaca'),
		('jxn', 'jxn'),
		('jackson', 'jackson'),
		('jacksontn', 'jacksontn'),
		('jacksonville', 'jacksonville'),
		('onslow', 'onslow'),
		('janesville', 'janesville'),
		('jerseyshore', 'jerseyshore'),
		('jonesboro', 'jonesboro'),
		('joplin', 'joplin'),
		('kalamazoo', 'kalamazoo'),
		('kalispell', 'kalispell'),
		('kenai', 'kenai'),
		('kpr', 'kpr'),
		('racine', 'racine'),
		('killeen', 'killeen'),
		('kirksville', 'kirksville'),
		('klamath', 'klamath'),
		('knoxville', 'knoxville'),
		('kokomo', 'kokomo'),
		('lacrosse', 'lacrosse'),
		('lasalle', 'lasalle'),
		('lafayette', 'lafayette'),
		('tippecanoe', 'tippecanoe'),
		('lakecharles', 'lakecharles'),
		('shreveport', 'shreveport'),
		('sierravista', 'sierravista'),
		('siouxcity', 'siouxcity'),
		('siouxfalls', 'siouxfalls'),
		('sfbay','san francisco bay area'),
		('seattle','seattle'),
		('tucson','tucson'),

)
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.IntegerField()
    city = forms.ChoiceField(required=False, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['type'] = 'email'


        self.fields['subject'].initial = 'bike'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['type'] = 'email'

        self.fields['message'].initial = 1
        self.fields['message'].widget.attrs['class'] = 'form-control'
