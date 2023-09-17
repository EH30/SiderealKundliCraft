from setuptools import setup
from setuptools import find_packages


long_description = ""
with open("README.md", "r") as opn:
    long_description = opn.read()

setup(
    # Project
    name='SiderealKundliCraft',
    version='1.2.0',
    
    # Sources
    packages=find_packages(),
    package_data={},
    
    # Dependencies
    install_requires=['pyswisseph==2.10.3.2'],
    
    # Metadata
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Python package for Astrology',
    url='https://github.com/EH30/SiderealKundliCraft',
    keywords=['Astrology', 'Sidereal Astrology', "Kundli"],
    license='UNLICENSE',
    
    # Authoring
    author='EH',
    author_email=None,
    
    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 
)
