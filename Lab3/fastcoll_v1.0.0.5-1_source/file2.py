#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �w�7�<uu.:~i��iA���AgƂr�A����������\�'���U#�t�+��*���լ�����I�{ᫎTp6�/I���������#�%Vg	r���,Z�����[�[�8�"""
from hashlib import sha256
print sha256(blob).hexdigest()