from setuptools import find_packages, setup

setup(name="subnetcalc",
      description="subnet calculator tool",
      author="Nathan Sutherland",
      author_email="authoremail",
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'subnetcalc = Subnetcalc:main',
          ],
      }
      )
