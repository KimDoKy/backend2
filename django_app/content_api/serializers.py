from rest_framework import serializers

from .models import Content


class ContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'content', 'ticket_url', 'phone', 'thumbnail',
                  'place_url', 'place_addr', 'gps_x', 'gps_y')


class ContentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'thumbnail',)
