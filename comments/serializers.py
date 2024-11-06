from rest_framework import serializers

from comments.models import Comentario

"""
Serializer para enviar los objetos como JSON
"""
class ComentarioSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    responseComment = serializers.PrimaryKeyRelatedField(
        queryset=Comentario.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Comentario
        fields = ['id', 'content', 'responseComment','replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return ComentarioSerializer(obj.replies.all(), many=True).data
        
        return []