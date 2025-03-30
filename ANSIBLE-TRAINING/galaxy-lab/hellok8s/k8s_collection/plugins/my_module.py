# plugins/modules/my_module.py
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
        )
    )

    name = module.params['name']
    module.exit_json(changed=False, message=f'Hello, {name}!')

if __name__ == '__main__':
    run_module()

