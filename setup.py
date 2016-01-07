from setuptools import find_packages, setup

setup(name="subnetcalc",
      description="subnet calculator tool",
      author="author email",
      auther_email="authoremail",
      packages=find_packages(),
      entry_points={
        'console_scripts':  [
            'subnetcalc = Subnetcalc:main',
            ],
        }
    )
