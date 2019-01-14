class Code:
    SUCCESS = 200
    NOT_ENOUGH_PARAM = 500
    NO_DATA = 501
    NO_AUTH = 502
    MYSQL_ERROR = 503
    DUPLICATE_DATA = 504
    NO_DATA_CHANGE = 505

    msg = {
        SUCCESS: 'success',
        NOT_ENOUGH_PARAM: 'not enough params',
        NO_DATA: 'no data',
        NO_AUTH: 'you have no authorization',
        MYSQL_ERROR: 'mysql error',
        DUPLICATE_DATA: 'duplicate data',
        NO_DATA_CHANGE: 'data not change'
    }
