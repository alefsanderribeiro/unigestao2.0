# ------------------------------------------------------------
# JAZZMIN CONFIGURATION
# ------------------------------------------------------------

JAZZMIN_SETTINGS = {
    'site_title': 'SGP',
    'site_header': 'Uni Gestão',
    'site_brand': 'Uni Gestão (SGP)',
    'site_logo': '/image/icons/gestao_site.png',
    'login_logo': '/image/icons/gestao_login.png',
    'welcome_sign': 'Bem-vindo(a) ao Uni Gestão (SGP)',
    'copyright': 'Coding Solutions LTDA',
    'search_model': ['employees.Funcionario',],
    'order_with_respect_to': [
        'auth',
        'employees',
        'bond',
        'file_manager',
        'payroll',
        'configurations',
        'configurations.bank',
        'configurations.accounttype',
        'configurations.paymenttype',
        'configurations.pixtype',
    ],
    'hide_models': ['bond.AdmissionInfo', 'payroll.Payment'],
    'custom_links': {
        'bond': [{
            'name': 'Gerenciar Vinculo',
            'url': 'admin:bond_admissioninfo_changelist',
            'icon': 'fas fa-briefcase',
        }],
        'payroll': [{
            'name': 'Gerenciar Pagamento',
            'url': 'admin:payroll_payment_changelist',
            'icon': 'fa-solid fa-cash-register',
        }]
    },
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',

        # App 'employees'
        'employees.Employee': 'fa-solid fa-address-book',

        # App 'geography'
        'geography.City': 'fa-solid fa-tree-city',
        'geography.State': 'fa-solid fa-map',
        'geography.Country': 'fa-solid fa-earth-americas',
        'geography.Region': 'fa-solid fa-compass',
        'geography.Capital': 'fa-solid fa-city',

        # App 'configurations'
        'configurations.AdmissionType': 'fa-solid fa-cogs',
        'configurations.HarmfulExposure': 'fa-solid fa-biohazard',
        'configurations.PaymentType': 'fa-solid fa-credit-card',
        'configurations.Bank': 'fa-solid fa-university',
        'configurations.AccountType': 'fa-solid fa-wallet',
        'configurations.PixType': 'fa-solid fa-qrcode',
        'configurations.MaritalStatus': 'fa-solid fa-hand-holding-heart',
        'configurations.Deficiency': 'fa-solid fa-wheelchair',
        'configurations.DegreeInstruction': 'fa-solid fa-file-contract',
        'configurations.Nationality': 'fa-solid fa-earth-americas',
        'configurations.Race': 'fa-solid fa-hands-holding-circle',
        'configurations.Gender': 'fa-solid fa-venus-mars',

        # App 'cbos'
        'cbos.CBO': 'fa-solid fa-file-shield',
        'cbos.Occupation': 'fa-solid fa-file-lines',

        # App 'file_manager
        'file_manager.File': 'fa-solid fa-upload',
        'file_manager.NameFile': 'fa-solid fa-file-signature',
    },
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': False,
    'accent': 'accent-primary',
    'navbar': 'navbar-white navbar-light',
    'no_navbar_border': False,
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': True,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,
    'theme': 'default',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success'
    },
    'actions_sticky_top': True,
}
