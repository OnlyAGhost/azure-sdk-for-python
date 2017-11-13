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

from .response import Response


class SearchResponse(Response):
    """Defines the top-level object that the response includes when the request
    succeeds.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar contractual_rules: A list of rules that you must adhere to if you
     display the item.
    :vartype contractual_rules:
     list[~azure.cognitiveservices.search.entitysearch.models.ContractualRulesContractualRule]
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar query_context: An object that contains the query string that Bing
     used for the request. This object contains the query string as entered by
     the user. It may also contain an altered query string that Bing used for
     the query if the query string contained a spelling mistake.
    :vartype query_context:
     ~azure.cognitiveservices.search.entitysearch.models.QueryContext
    :ivar entities: A list of entities that are relevant to the search query.
    :vartype entities:
     ~azure.cognitiveservices.search.entitysearch.models.Entities
    :ivar places: A list of local entities such as restaurants or hotels that
     are relevant to the query.
    :vartype places:
     ~azure.cognitiveservices.search.entitysearch.models.Places
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'contractual_rules': {'readonly': True},
        'web_search_url': {'readonly': True},
        'query_context': {'readonly': True},
        'entities': {'readonly': True},
        'places': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'contractual_rules': {'key': 'contractualRules', 'type': '[ContractualRulesContractualRule]'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'entities': {'key': 'entities', 'type': 'Entities'},
        'places': {'key': 'places', 'type': 'Places'},
    }

    def __init__(self):
        super(SearchResponse, self).__init__()
        self.query_context = None
        self.entities = None
        self.places = None
        self._type = 'SearchResponse'