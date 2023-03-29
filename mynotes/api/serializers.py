from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        # If you want to serialize particular fields, you can give them in a list.
        # like this => ['body', 'updated',]
        # for all fields you can just simply type __all__
        fields = '__all__'