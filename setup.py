import setuptools

with open('README.md','r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_yash',
	version = '0.0.1',
	author = 'Yash Mudgal',
	author_email = 'yashmudgalyash@gmail.com',
	description = 'This is a preprocessing package',
	Long_description = long_description,
	Long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)