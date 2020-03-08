import setuptools

setuptools.setup(
    name="init-python",
    version="0.0.1",
    author="Arghajit",
    author_email="argha.bh@gmail.com",
    description="Bootstrapped Project Skeleton for Python3",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
            'console_scripts': [
                'app = init.bin.app:main'
            ],
        },
)
