from setuptools import setup, find_packages

setup(
    name='suaidoc',
    version='0.1',
    py_modules=['suaidoc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
	[console_scripts]
	suaidoc=suaidoc:suaidoc
 	'''
)
