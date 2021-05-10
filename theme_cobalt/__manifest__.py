{
    'name': 'Cobalt Theme',
    'description': 'Clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['website'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/cobalt_poster.jpg',
        'static/description/cobalt_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-cobalt.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_cobalt/static/src/js/tour.js',
        ],
    }
}
