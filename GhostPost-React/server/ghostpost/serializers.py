from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
          "pk",
          "is_boast",
          "contents",
          "up_votes",
          "down_votes",
          "submission_time"
        ]