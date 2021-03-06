from setuptools import find_packages
from setuptools import setup


setup(
    name='ll.theme',
    version='0.7',
    description="LL site theme.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/ll.theme',
    license='None-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['ll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sll.basetheme',
        'sll.carousel',
        'sll.templates'],
    extras_require={'test': ['hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
