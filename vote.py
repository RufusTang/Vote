# -*- coding: utf-8 -*-


import urllib
import urllib2
import cookielib
import lxml.html


LOGIN_EMAIL = '15825279415'
LOGIN_PASSWORD = ''
LOGIN_URL = 'http://mail.10086.cn/'


def login_cookies():
    """working login
    """
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    html = opener.open(LOGIN_URL).read()
    data = parse_form(html)
    data['UserName'] = LOGIN_EMAIL
    data['Password'] = LOGIN_PASSWORD
    encoded_data = urllib.urlencode(data)
    request = urllib2.Request(LOGIN_URL, encoded_data)
    response = opener.open(request)
    print response.geturl()
    return opener


def parse_form(html):
    """extract all input properties from the form
    """
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data


def main():
    login_cookies()


if __name__ == '__main__':
    main()
