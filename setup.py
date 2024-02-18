from setuptools import setup, find_packages

setup(
    name='suaidoc',
    version='0.0.1',
    py_modules=['suaidoc'],
    install_requires=[
        'click >= 8.1.0',
        'pdfkit >= 1.0.0',
        'python_frontmatter >= 1.1.0',
        'setuptools >= 69.0.0',
    ],
    packages=find_packages(),
    package_data={
        'templates': [
            'template.tex',
            'template.html',
        ],
    },
    entry_points={
        'console_scripts': [
            'suaidoc=suaidoc:suaidoc',
        ],
    },
)
