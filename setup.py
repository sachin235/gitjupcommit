import setuptools

setuptools.setup(
    name="gitjupcommit",
    version='0.1.0',
    url="https://github.com/sachin235/gitjupcommit",
    author="Sachin",
    description="Jupyter extension to enable user push notebooks to a git repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'gitjupcommit': ['static/*']},
)
