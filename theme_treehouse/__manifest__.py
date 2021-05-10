{
    'name': 'Treehouse Theme',
    'description': 'Treehouse Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Environment',
    'summary': 'Environment, Nature, Ecology, Sustainable Development, Non Profit, NGO, Travels',
    'sequence': 140,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_share.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_title.xml',

        ],
    'images': [
        'static/description/treehouse_cover.jpg',
        'static/description/treehouse_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-treehouse.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_treehouse/static/src/js/tour.js',
        ],
    }
}
