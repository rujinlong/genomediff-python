from distutils.core import setup

setup(
    name='genomediff2',
    version='0.3.3',
    packages=['genomediff'],
    url='https://github.com/biosustain/genomediff-python.git',
    license='MIT',
    author='Lars Schoening',
    author_email='lays@biosustain.dtu.dk',
    description='GenomeDiff (*.gd) file reader',
    long_description='GenomeDiff file reader',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ]
)
