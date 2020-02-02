

from  rest_framework import  serializers
from .models import Entry




class EntrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'



