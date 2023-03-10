{
    "name": "AS Reload Form",

    'author': 'Artemenko Stas',
    'website': 'https://github.com/artstas/',

    'category': 'Other',
    'license': 'OPL-1',
    'version': '15.0.1.0.1',

    "depends": [
        'base',
        'web',
    ],

    "installable": True,
    "application": False,

    'assets': {
        'web.assets_backend': [
            'as_reload_form/static/src/css/reload.css',
        ],
        'web.assets_qweb': [
            'as_reload_form/static/src/xml/base.xml',
        ],
    },

}
