from setuptools import setup


setup(
    name='boxes',
    version='0.3',
    description='Automate your boxes',
    packages=['boxes', 'boxes.scripts'],
    install_requires=['fabric'],
    package_data = {
        'boxes': ['pdu-requirements.txt']
    },
    entry_points = {
        'console_scripts': [
            'install_xcp_xapi = boxes.scripts.install_xcp_xapi:main',
            'create_start_deblike = boxes.scripts.create_start_deblike:main',
            'install_openstack_plugins = boxes.scripts.install_openstack_plugins:main',
            'get_devstack_domu_ip = boxes.scripts.get_devstack_domu_ip:main',
            'start_devstack = boxes.scripts.start_devstack:main',
            'run_tempest_tests = boxes.scripts.run_tempest_tests:main',
            'hard_reset = boxes.scripts.hard_reset:main',
            'install_pxeboot_config = boxes.scripts.pxeboot_config:install_main',
            'remove_pxeboot_config = boxes.scripts.pxeboot_config:remove_main',
            'install_pdu_requirements = boxes.scripts.install_pdu_requirements:main',
            'wait_for_ssh = boxes.scripts.wait_for_ssh:main',
            'prepare_xs_for_devstack_ci = boxes.scripts.prepare_host:prepare_xs',
            'prepare_generic_host = boxes.scripts.prepare_host:setup_ssh',
            'run_exercise = boxes.scripts.run_exercise:main',
            'restart_devstack_service = boxes.scripts.restart_devstack_service:main',
            'set_extra_config = boxes.scripts.set_extra_config:main'
        ]
    }
)
