AUTHOR = 'Oliver Byte'
SITENAME = 'Oliver Byte | Multimedia Artist'
SITEURL = "https://www.oliverbyte.de/"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

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
    #('Home', '/'),
    ('Laser',
        [
            ('goodtimes | laser crew', '/goodtimes-laser-crew.html'),
            ('osc2laser | laser software', 'https://github.com/goodtimes-code/osc2laser'),
            ('laserpong | laser game', 'https://github.com/goodtimes-code/laserpong'),
            ('msvg2ild | laser tool', 'https://github.com/goodtimes-code/msvg2ild'),
        ]
    ),
    ('Ansichten', [
        ('Tags', '/tags.html'),
        ('Kategorien', '/categories.html'),
        ('Chronologisch', '/archives.html'),
    ]),
    ('Kontakt', [
        ('E-Mail', 'mailto: info@oliverbyte.de'),
        ('Github', 'https://github.com/goodtimes-code'),
        ('Youtube', 'https://www.youtube.com/@goodtimes-laser'),
    ]),
]