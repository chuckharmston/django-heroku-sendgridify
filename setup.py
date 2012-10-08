from setuptools import setup, find_packages

setup(
    name='django-heroku-sendgridify',
    version='0.1',
    description=(
        'Automatic email configuration for the Django/Heroku/SendGrid stack'
    ),
    keywords='django heroku cloud email sendgrid sendgridify',
    author='Chuck Harmston',
    author_email='chuck@chuckharmston.com',
    url='https://github.com/chuckharmston/django-heroku-sendgridify',
    license='MIT',
    package_dir={
        'sendgridify': 'sendgridify',
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
    ],
)
