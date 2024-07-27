from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'RAGE is now officially on supported on Python.'
LONG_DESCRIPTION = 'A package to manage your cloud database operations through local storage approach.'

# Setting up
setup(
    name="rage_py",
    version=VERSION,
    author="Maghish",
    author_email="<mail4mithran@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'rage', 'rage-py', 'rage_py', 'ragepy', 'database'],
)