#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �w�7�<uu.:~i��iA���AgƂr�A����������\�'���U#�t�+��*���լ�����I�{ᫎTp6�/I���������#�%Vg	r���,Z�����[�[�8�"""
sha_file1="e3d2c68a81f21404f3ee2af30dec01d8e8965cd2dac1f2b011f888708d794f24"
sha_file2="0abb22d3e4de6a870e22cab4a09b34a5ae7ddca708c48dc032c5c85af6ed291d"
from hashlib import sha256
found=sha256(blob).hexdigest()
if(sha_file1==found):
  print 'I come in peace.'
if(sha_file2==found):
  print 'Prepare to be destroyed!'