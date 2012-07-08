# -*- coding: utf-8 -*-
"""
    Shake.templates
    --------------------------

    Template globals, filters and tests

"""
from xml.sax.saxutils import quoteattr

from jinja2 import Markup

from .helpers import local, to_unicode


__all__ = (
    'plural', 'link_to',
)


def plural(num, plural='s', singular=''):
    """A dumb simple pluralize function.
    """
    return plural if num != 1 else singular


def html_attrs(classes=None, **kwargs):
    """Generate HTML attributes from the provided keyword arguments.

    The output value is sorted by the passed keys, to provide consistent
    output.  Because of the frequent use of the normally reserved keyword
    `class`, `classes` is used instead. Also, all underscores are translated
    to regular dashes.

    Set any property with a `True` value.

    >>> _get_html_attrs({'id': 'text1', 'classes': 'myclass',
        'data_id': 1, 'checked': True})
    u'class="myclass" data-id="1" id="text1" checked'

    """
    attrs = []
    props = []

    classes = classes.strip()
    if classes:
        classes = to_unicode(quoteattr(classes))
        attrs.append('class=%s' % classes)

    for key, value in kwargs.iteritems():
        key = key.replace('_', '-')
        key = to_unicode(key)
        if isinstance(value, bool):
            if value is True:
                props.append(key)
        else:
            value = quoteattr(to_unicode(value))
            attrs.append(u'%s=%s' % (key, value))

    attrs.sort()
    props.sort()
    attrs.extend(props)
    return u' '.join(attrs)


def link_to(text='', url='', classes='', **kwargs):
    """Build an HTML anchor element for the provided URL.
    If the url match the beginning of that in the current request, an `active`
    class is added.  This is intended to be use to build navigation links.

    Other HTML attributes are generated from the keyword argument
    (see the `html_attrs` function).
    Example:

        >>> link_to('Hello', '/hello/', title='click me')
        u'<a href="/hello/" title="click me">Hello</a>'

        >>> from werkzeug.test import EnvironBuilder
        >>> builder = EnvironBuilder(method='GET', path='/foo/')
        >>> env = builder.get_environ()
        >>> from shake import Request
        >>> local.request = Request(env)
        >>> link_to('Bar', '/foo/')
        u'<a href="/foo/" class="active">Bar</a>'

    """
    request = local.request
    if request.path.startswith(url):
        classes += ' active'
    data = {
        'url': url,
        'text': text,
        'attrs': html_attrs(classes, **kwargs),
    }
    data['attrs'] = ' ' + data['attrs'] if data['attrs'] else ''
    html = u'<a href="%(url)s"%(attrs)s>%(text)s</a>' % data
    return Markup(html)
