AUTHOR = 'Oliver Byte'
SITENAME = 'Oliver Byte | Multimedia Artist'
SITEURL = "https://www.oliverbyte.de"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = "content"
MARKUP = ('md', 'html')

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
#   ("Instagram", "https://www.instagram.com/goodtimes_laser/"),
#   ("Youtube", "https://www.youtube.com/@goodtimes-laser"),
# )

# DEFAULT_PAGINATION = True

THEME = 'themes/pelican-chameleon'

MENUITEMS = [
    ('Kategorien', '/categories.html'),
    ('Kontakt', [
        ('E-Mail', 'mailto: info@oliverbyte.de'),
        ('Github', 'https://github.com/goodtimes-code'),
        ('Youtube', 'https://www.youtube.com/@oliverbyte'),
    ]),
]