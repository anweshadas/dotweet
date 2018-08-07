from setuptools import setup

setup(
    name="dotweet",
    version='0.1',
    description="Twitter from commandline",
    long_description="A project to tweet, directmessage and see timeline form the command line.",
    author="Anwesha Das.",
    author_email="anwesha@das.community",
    url="https://github.com/anweshadas/dotweet",
    license="GPLv3+",
    py_modules=['dotweet'],
    install_requires=['Click','python-twitter'],
    entry_points='''
        [console_scripts]
        dotweet=dotweet:main
    ''',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6'
        )
    )
