from setuptools import setup, find_packages


def get_long_description():
    with open('README.md') as f:
        return f.read()


setup(
    name="quickpomdps",
    version="0.0.1",
    description="Describing and Solving POMDPs in Python",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/JuliaPOMDP/quickpomdps",
    author="rejuvyesh",
    author_email="mail@rejuvyesh.com",
    license='MIT',
    packages=find_packages(),
    install_requires=["julia>=0.2"],
    test_requires=["pytest"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
