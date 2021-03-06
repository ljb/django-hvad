from setuptools import setup, find_packages
import hvad

with open('README.rst', 'rb') as f:
    long_description = f.read().decode('utf-8')

setup(
    name = 'django-hvad',
    version = hvad.__version__,
    description = 'A content translation framework for django integrated automatically in the normal ORM. Removes the pain of having to think about translations in a django project.',
    long_description = long_description,
    author = 'Kristian Ollegaard',
    author_email = 'kristian.ollegaard@divio.ch',
    url = 'https://github.com/KristianOellegaard/django-hvad',
    packages = find_packages(
        exclude = [
            'testproject',
            'testproject.app',
            'hvad.tests',
        ],
    ),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.8',
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Text Processing :: Linguistic",
    ]
)
