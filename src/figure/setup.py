from setuptools import setup

setup(
	name='figure',
	version='1.0.0',
	author='Jakob Gillich',
	author_email='jakob@gillich.me',
	description='Markdown extension for MkDocs to wrap images in figures',
	py_modules=['figure'],
	install_requires = ['markdown>=2.5'],
	license='MIT License',
)
