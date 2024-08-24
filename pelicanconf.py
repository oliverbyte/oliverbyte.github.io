AUTHOR = 'Oliver Byte'
SITENAME = 'Oliver Byte | Multimedia Artist'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
# SOCIAL = (
#    ("Instagram", "https://www.instagram.com/goodtimes_laser/"),
#    ("Youtube", "https://www.youtube.com/@goodtimes-laser"),
#)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/pelican-chameleon'

MENUITEMS = [
    ('Home', '/home.html'),
    #('Laser', [
    #    ('Laser Art', '/category/laser-art.html'),
    #    ]),
    ('Archives', [
        ('Tags', '/tags.html'),
        ('Kategorien', '/categories.html'),
        ('Chronologisch', '/archives.html'),
        ]),
    ('Social', [
        ('E-Mail', 'mailto: info@oliverbyte.de'),
        ('Github', 'https://github.com/goodtimes-code'),
        ('Youtube', 'https://www.youtube.com/@goodtimes-laser'),
        ]),
    ]