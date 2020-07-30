import os

CONSTANTS = {
    'PORT': os.environ.get('PORT', 3001),
    'COSMOS': {
        'COLLECTION': 'ListItems'
    },
    'HTTP_STATUS': {
        '404_NOT_FOUND': 404,
        '201_CREATED': 201,
        '500_INTERNAL_SERVER_ERROR': 500
    },
    'ENDPOINT': {
        'MASTER_DETAIL': '/api/masterdetail',
        'LIST': '/api/list',
        'GRID': '/api/grid',
    }
}