from setuptools import setup, find_packages


setup(

    name = "QuickBooks",

    version = '0.2.2',

    packages = find_packages(),

    install_requires = ['requests', 'requests-oauthlib', 'python-keyczar==0.71c', 'django-extensions'],
    include_package_data = True,

    # metadata for upload to PyPI
    author = "Hans Kuder",
    author_email = "hans@hiidef.com",
    maintainer = "Brent Hagany",
    maintainer_email = "brent@hiidef.com",
    description = "Django Quickbooks App",
    license = "MIT License",
    keywords = "django quickbooks intuit",
    url = "http://github.com/hiidef/django-quickbooks",

)
