from setuptools import setup, find_packages

setup(
    name='suaidoc',
    version='0.0.1',
    py_modules=['suaidoc'],
    install_requires=[
        'click',
        'pdfkit',
        'python_frontmatter',
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
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
