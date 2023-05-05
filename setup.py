from setuptools import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
	name='titanic',
	version='0.1',
	description='Data Analysis of the Titanic Dataset',
	long_description=readme(),
	classifiers=[
		'Programming Language :: Python :: 3.10',
	],
	url='https://github.com/DawdlingDaedalus/titanic',
	author='Peter McMaster',
	author_email='petermcmaster9@gmail.com',
	license='MIT',
	packages=['titanic'],
	install_requires=[
		'pandadoc>=0.1.0'
	]
)
