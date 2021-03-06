# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PersonFaceResult(Model):
    """PersonFace object.

    :param persisted_face_id: The persistedFaceId of the target face, which is
     persisted and will not expire. Different from faceId created by Face -
     Detect and will expire in 24 hours after the detection call.
    :type persisted_face_id: str
    :param user_data: User-provided data attached to the face.
    :type user_data: str
    """

    _validation = {
        'persisted_face_id': {'required': True},
    }

    _attribute_map = {
        'persisted_face_id': {'key': 'persistedFaceId', 'type': 'str'},
        'user_data': {'key': 'userData', 'type': 'str'},
    }

    def __init__(self, persisted_face_id, user_data=None):
        self.persisted_face_id = persisted_face_id
        self.user_data = user_data
