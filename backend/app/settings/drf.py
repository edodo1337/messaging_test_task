import django 

DATE_INPUT_FORMATS = ['%d.%m.%Y', '%d-%m-%Y']
SHORT_DATE_FORMAT = '%d.%m.%Y'
DATE_FORMAT = '%d.%m.%Y'

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 9,
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'SHORT_DATE_FORMAT': SHORT_DATE_FORMAT,
    'DATE_FORMAT': DATE_FORMAT,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    ),

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
        'api.throttling.messaging.MessagingRateThrottle'
    ],

    'DEFAULT_THROTTLE_RATES': {
        'messaging': '10/minute',
    }
}

# SWAGGER_SETTINGS = {
#     'Authorization': {
#       'USE_SESSION_AUTH': False,
#       'LOGIN_URL': "/admin/login/",
#       'LOGOUT_URL': "/admin/logout/",

#     },
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#         }
#     },
# }


SWAGGER_SETTINGS = {
     # default inspector classes, see advanced documentation
     'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
     'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.ReferencingSerializerInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
     ],
     'DEFAULT_FILTER_INSPECTORS': [
        'drf_yasg.inspectors.CoreAPICompatInspector',
     ],
     'DEFAULT_PAGINATOR_INSPECTORS': [
        'drf_yasg.inspectors.DjangoRestResponsePagination',
        'drf_yasg.inspectors.CoreAPICompatInspector',
     ],

    # 'USE_SESSION_AUTH': True,  # add Django Login and Django Logout buttons, CSRF token to swagger UI page
    'LOGIN_URL': getattr(django.conf.settings, 'LOGIN_URL', None),  # URL for the login button
    'LOGOUT_URL': getattr(django.conf.settings, 'LOGOUT_URL', None),  # URL for the logout button

    # url to an external Swagger validation service; defaults to 'http://online.swagger.io/validator/'
    # set to None to disable the schema validation badge in the UI
    'VALIDATOR_URL': '',

    # swagger-ui configuration settings, see https://github.com/swagger-api/swagger-ui/blob/112bca906553a937ac67adc2e500bdeed96d067b/docs/usage/configuration.md#parameters
    'OPERATIONS_SORTER': None,
    'TAGS_SORTER': None,
    'DOC_EXPANSION': 'list',
    'DEEP_LINKING': False,
    'SHOW_EXTENSIONS': True,
    'DEFAULT_MODEL_RENDERING': 'model',
    'DEFAULT_MODEL_DEPTH': 3,

    'Authorization': {
      'USE_SESSION_AUTH': False,
      'LOGIN_URL': "/admin/login/",
      'LOGOUT_URL': "/admin/logout/",
    },

    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },

    'USE_SESSION_AUTH': False
}

REDOC_SETTINGS = {
    # ReDoc UI configuration settings, see https://github.com/Rebilly/ReDoc#redoc-tag-attributes
    'LAZY_RENDERING': True,
    'HIDE_HOSTNAME': False,
    'EXPAND_RESPONSES': 'all',
    'PATH_IN_MIDDLE': False,
}