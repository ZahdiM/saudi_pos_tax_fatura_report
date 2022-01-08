{
    'name': 'Saudia Tax Invoice for POS فاتورة ضريبية مبسطة',
    'version': '15.0.0.0',
    'category': 'Sales/Point of Sale',
    'sequence': 40,
    'summary': 'This Module will help in printing the Simplified Tax Report for POS فاتورة ضريبية مبسطة',
    'description': """ Simplified Tax Report for POS
    Point of Sale tax report for saudi arabia
    Simplified VAT Report
    Saudi Arabia VAT Invoice
    VAT E-Invoice Standard
    E-Invoicing
    B2C VAT Invoice
    Fatora 
    فاتورة ضريبیة
    فاتورة ضريبية مبسطة
    """,
    'license': 'OPL-1',

    # Author
    'author': 'Mediod Consulting Pvt. Ltd.',
    'website': 'http://www.mediodconsulting.com/',
    'maintainer': 'Mediod Consulting Pvt. Ltd.',
    'depends': ['point_of_sale'],
    'data': [
        'views/assets.xml',
    ],
        'assets': {
        'point_of_sale.assets': [
            'pos_reports/static/src/js/qrcode.js',
            'pos_reports/static/src/js/pos.js',
        ],
        'web.assets_qweb': [
            'pos_reports/static/src/xml/OrderReceipt.xml',
        ],
    },
    'data': [
    ],
    "images": ['static/description/Banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 15.00,
    'currency': 'USD',
}
