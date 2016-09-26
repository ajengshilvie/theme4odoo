{
    'name': 'Baby Pink Backend-Theme',
    'version': '1.0',
    'author': 'Ajeng Shilvie N',
    'description': '''
        A custom module to change default odoo menu color
    ''',
    'category': 'Themes/ASN',
    'depends': [
        'base',
    ],
    'data': [
        'views/custom_view.xml',
    ],
    'images':[
            'static/description/main_screenshot.jpg',
    ],
    'css': ['static/src/css/styles.css'],
    'auto_install': False,
    'installable': True,
}
