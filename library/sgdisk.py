#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ansible.module_utils.basic import *
import commands

def newpartition(disk):
    cmd = 'sgdisk -n 0:0:0 {}'.format(disk)
    output = commands.getoutput(cmd)
    commands.getoutput('mkfs.xfs {}1 -f'.format(disk))
    return output
    
def main():
    changed = False
    module = AnsibleModule(
                argument_spec = dict(
                  disk = dict(type='str', required=True),
                  zap = dict(default='no', choices=['yes', 'no']),
                ),
    )
    disk = module.params['disk']
    zap = module.params['zap']
    if zap == 'no':
        status, check_output = commands.getstatusoutput('blkid -o value -s UUID {}1'.format(disk))
        if status != 0:
            output = newpartition(disk)
            result = dict(stdout=output, zap=zap, changed=True, rc=0)
        else:
            result = dict(msg=check_output, zap=zap, rc=status)
        module.exit_json(**result)
    elif zap == 'yes':
        zap_cmd = 'sgdisk -Z {}'.format(disk)
        zap_output = commands.getoutput(zap_cmd)
        output = newpartition(disk)
        result = dict(stdout=output, zap=zap, changed=True, rc=0)
        module.exit_json(**result)
    else:
        pass
        

if __name__ == '__main__':
    main()
