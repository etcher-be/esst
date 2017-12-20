# coding=utf-8
"""
Validates config object
"""

from esst import __version__

MANDATORY_CONFIG_OPTIONS = [
    'saved_games_dir',
    'discord_token',
    'discord_channel',
    'discord_bot_name',
    'dcs_server_password',
    'dcs_server_name',
    'dcs_path',
]


def validate_config(config_instance):
    """
    Validates config object
    """
    print('ESST version', __version__)
    print('Validating config')
    missing_values = []
    for attrib_name in dir(config_instance):
        if not attrib_name.startswith('_'):
            attrib = getattr(config_instance, attrib_name)
            if not callable(attrib):
                if attrib_name in MANDATORY_CONFIG_OPTIONS and not attrib:
                    missing_values.append(attrib_name)

    if missing_values:
        missing_values = '\t' + '\n\t'.join(missing_values)
        print(
            f"""
The following values are missing from your configuration:

{missing_values}

There is a "esst.yml.example" file provided with this repository to serve as a base to create your own config.
Refer to https://github.com/132nd-vWing/ESST/blob/master/README.md for more information about setting ESST up.""")
        exit(1)