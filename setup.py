import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mikes_toolbox',
    packages=['mikes_toolbox'],
    version='0.0.3',
    license='MIT',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mike Huls',
    author_email='mike_huls@hotmail.com',
    url='https://github.com/Muls/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    install_requires=['requests'],

    download_url="https://github.com/mike-huls/toolbox_public/archive/refs/tags/0.0.3.tar.gz",
    keywords=["pypi", "mikes_toolbox", "tutorial"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Tutorial',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: "Python :: 3',
        'Programming Language :: "Python :: 3.7',
        'Programming Language :: "Python :: 3.8',
        'Programming Language :: "Python :: 3.9',
    ]
)

