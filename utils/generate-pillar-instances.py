#!/usr/bin/env python2

#   -------------------------------------------------------------
#   Salt configuration for Woods Cloud servers
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Woods Cloud
#   Created:        2018-11-30
#   -------------------------------------------------------------


from __future__ import print_function
from datetime import date
import salt.config
import salt.loader
import yaml


def prepare_salt_master():
    __opts__ = salt.config.client_config("/etc/salt/master")
    __opts__['grains'] = salt.loader.grains(__opts__)
    __utils__ = salt.loader.utils(__opts__)

    return salt.loader.minion_mods(__opts__, utils=__utils__)


def get_instance(instance, __salt__):
    return __salt__['cloud.get_instance'](instance)


def get_instances(__salt__, pillar_title):
    instances = {name: get_instance(name, __salt__) for name in get_instances_names()}

    return {pillar_title: instances}


def get_instances_names():
    pillar = yaml.load(open("pillar/nodes/nodes.sls", "r"))
    return pillar['nodes'].keys()


def print_header():
    print("#   -------------------------------------------------------------")
    print("#   Salt configuration for Woods Cloud servers")
    print("#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("#   Project:        Woods Cloud")
    print("#   Data source:    salt-cloud")
    print("#   Generated:     ", date.today().isoformat())
    print("#   -------------------------------------------------------------")
    print("#")
    print("#   <auto-generated>")
    print("#       This file is generated by utils/generate-pillar-instances.py.")
    print("#")
    print("#       Changes to this file may cause incorrect behavior")
    print("#       and will be lost if the script is redeployed.")
    print("#")
    print("#       To refresh all generated files, you can use 'make clean all'.")
    print("#       To refresh only this file, delete it, then run 'make'.")
    print("#   </auto-generated>")
    print()


def unicode_repr(self, data):
    """Avoids !!python/unicode annotations in Python 2."""

    return self.represent_str(data.encode('utf-8'))


def run():
    __salt__ = prepare_salt_master()
    instances = get_instances(__salt__, "cloud_instances")

    print_header()

    yaml.representer.Representer.add_representer(unicode, unicode_repr)
    print(yaml.dump(instances, default_flow_style=False))


if __name__ == "__main__":
    run()
