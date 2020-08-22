from setuptools import setup

setup(
    name='Kickbase_Analysis',
    version='0.0.1',
    packages=['kickbase_analysis'],
    url='https://github.com/kevinskyba/kickbase-analysis',
    license='MIT',
    author='kevinskyba',
    author_email='kevinskyba@live.de',
    description='Analysis framework for kickbase',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=(
        'requests',
        'kickbase_api'
    )
)
