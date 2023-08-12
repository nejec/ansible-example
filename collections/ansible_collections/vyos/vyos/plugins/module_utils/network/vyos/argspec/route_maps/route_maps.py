# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the vyos_route_maps module
"""


class Route_mapsArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_route_maps module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "route_map": {"type": "str"},
                "entries": {
                    "aliases": ["rules"],
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "sequence": {"type": "int"},
                        "call": {"type": "str"},
                        "description": {"type": "str"},
                        "action": {
                            "type": "str",
                            "choices": ["deny", "permit"],
                        },
                        "continue_sequence": {"type": "int"},
                        "set": {
                            "type": "dict",
                            "options": {
                                "aggregator": {
                                    "type": "dict",
                                    "options": {
                                        "ip": {"type": "str"},
                                        "as": {"type": "str"},
                                    },
                                },
                                "as_path_exclude": {"type": "str"},
                                "as_path_prepend": {"type": "str"},
                                "atomic_aggregate": {"type": "bool"},
                                "bgp_extcommunity_rt": {"type": "str"},
                                "comm_list": {
                                    "type": "dict",
                                    "options": {
                                        "comm_list": {"type": "str"},
                                        "delete": {"type": "bool"},
                                    },
                                },
                                "community": {
                                    "type": "dict",
                                    "options": {"value": {"type": "str"}},
                                },
                                "extcommunity_rt": {"type": "str"},
                                "extcommunity_soo": {"type": "str"},
                                "ip_next_hop": {"type": "str"},
                                "ipv6_next_hop": {
                                    "type": "dict",
                                    "options": {
                                        "ip_type": {
                                            "type": "str",
                                            "choices": ["global", "local"],
                                        },
                                        "value": {"type": "str"},
                                    },
                                },
                                "large_community": {"type": "str"},
                                "local_preference": {"type": "str"},
                                "metric": {"type": "str"},
                                "metric_type": {
                                    "type": "str",
                                    "choices": ["type-1", "type-2"],
                                },
                                "origin": {
                                    "type": "str",
                                    "choices": ["egp", "igp", "incomplete"],
                                },
                                "originator_id": {"type": "str"},
                                "src": {"type": "str"},
                                "tag": {"type": "str"},
                                "weight": {"type": "str"},
                            },
                        },
                        "match": {
                            "type": "dict",
                            "options": {
                                "as_path": {"type": "str"},
                                "community": {
                                    "type": "dict",
                                    "options": {
                                        "community_list": {"type": "str"},
                                        "exact_match": {"type": "bool"},
                                    },
                                },
                                "extcommunity": {"type": "str"},
                                "interface": {"type": "str"},
                                "ip": {
                                    "type": "dict",
                                    "options": {
                                        "address": {
                                            "type": "dict",
                                            "options": {
                                                "list_type": {
                                                    "type": "str",
                                                    "choices": [
                                                        "access-list",
                                                        "prefix-list",
                                                    ],
                                                },
                                                "value": {"type": "str"},
                                            },
                                        },
                                        "next_hop": {
                                            "type": "dict",
                                            "options": {
                                                "list_type": {
                                                    "type": "str",
                                                    "choices": [
                                                        "access-list",
                                                        "prefix-list",
                                                    ],
                                                },
                                                "value": {"type": "str"},
                                            },
                                        },
                                        "route_source": {
                                            "type": "dict",
                                            "options": {
                                                "list_type": {
                                                    "type": "str",
                                                    "choices": [
                                                        "access-list",
                                                        "prefix-list",
                                                    ],
                                                },
                                                "value": {"type": "str"},
                                            },
                                        },
                                    },
                                },
                                "ipv6": {
                                    "type": "dict",
                                    "options": {
                                        "address": {
                                            "type": "dict",
                                            "options": {
                                                "list_type": {
                                                    "type": "str",
                                                    "choices": [
                                                        "access-list",
                                                        "prefix-list",
                                                    ],
                                                },
                                                "value": {"type": "str"},
                                            },
                                        },
                                        "next_hop": {"type": "str"},
                                    },
                                },
                                "large_community_large_community_list": {"type": "str"},
                                "metric": {"type": "int"},
                                "origin": {
                                    "type": "str",
                                    "choices": ["ebgp", "ibgp", "incomplete"],
                                },
                                "peer": {"type": "str"},
                                "rpki": {
                                    "type": "str",
                                    "choices": [
                                        "notfound",
                                        "invalid",
                                        "valid",
                                    ],
                                },
                            },
                        },
                        "on_match": {
                            "type": "dict",
                            "options": {
                                "next": {"type": "bool"},
                                "goto": {"type": "int"},
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "overridden",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
