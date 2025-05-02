{
    'name': 'Hello World',
    'version': '16.0.1.0.0',
    'summary': 'Basit bir Merhaba Dünya modülü',
    'description': 'Odoo için basit bir örnek uygulama.',
    'author': 'Senin Adın',
    'website': 'https://github.com/kullanici_adin',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hello_view.xml',
    ],
    'installable': True,
    'application': True,
}
