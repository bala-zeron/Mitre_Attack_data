"""
Serializer for serializing the Attack() object data.(Currently not in use)
"""
from rest_framework import serializers


class YourSerializer(serializers.Serializer):
    # tech = serializers.DictField(
    # child = serializers.CharField())
    # technique = serializers.DictField(
    # child = serializers.CharField())
    technique_name = serializers.DictField(child = serializers.CharField())
    created = serializers.DictField(child = serializers.CharField())
    modified = serializers.DictField(child = serializers.CharField())
    type = serializers.DictField(child = serializers.CharField())
    actor_name = serializers.DictField(child = serializers.CharField())
    actor_aliases = serializers.DictField(child = serializers.CharField())
    malware_name = serializers.DictField(child = serializers.CharField())
    mitigation = serializers.DictField(child = serializers.CharField())

#    name = serializers.JSONField(binary=True)
#    created = serializers.JSONField(binary=True)
#    modified = serializers.JSONField(binary=True)
#    type = serializers.JSONField(binary=True)
#    actor_name = serializers.JSONField(binary=True)
#    actor_aliases = serializers.JSONField(binary=True)
#    malware_name = serializers.JSONField(binary=True)
#    mitigation = serializers.JSONField(binary=True)
