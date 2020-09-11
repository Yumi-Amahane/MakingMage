import setuptools

setuptools.setup(
    name="MakingMage",
    version="0.1.8",
    author="Yumi-Amahane",
    description="Making Mage Program",
    url="https://github.com/Yumi-Amahane/MakingMage",
    entry_points={
        'console_scripts':[
            'MakingMage=MakingMage.MakingMage:main'
        ]
    }
    packages=["MakingMage"]
)
