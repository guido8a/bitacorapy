from django.db import connection

def ejecutaSql(txsql):
    with connection.cursor() as cursor:
        cursor.execute(txsql)
        row = cursor.fetchall()
    return row


def load_url_pattern_names(patterns):
    """Retrieve a list of urlpattern names"""
    URL_NAMES = []
    for pat in patterns:
        if pat.__class__.__name__ == 'RegexURLResolver':            # load patterns from this RegexURLResolver
            load_url_pattern_names(pat.url_patterns)
        elif pat.__class__.__name__ == 'RegexURLPattern':           # load name from this RegexURLPattern
            if pat.name is not None and pat.name not in URL_NAMES:
                URL_NAMES.append( pat.name)
    return URL_NAMES


def urls_lista(urls):
    for entry in urls:
        print("urls: {}".format(entry.name))
