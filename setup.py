from setuptools import setup, find_packages

setup(name="pythonstopwatch",
      version="0.0.1",
      author="Adit Modhvadia",
      author_email="dev.aditmodhvadia@gmail.com",
      license="LICENSE",
      url="https://github.com/aditmodhvadia/fenway-savings",
      description="A Python command line program for a Stop Watch.",
      packages=find_packages(exclude=['tests', 'tests.*'], include=['assets', 'assets.*']),
      data_files=[('images', ['assets/pause.png', 'assets/play.png', 'assets/reset_enabled.png'])],
      install_requires=['Pillow'],
      test_suite="tests",
      package_data={'': ['license.txt', 'MANIFEST.in']},
      include_package_data=True,
      entry_points={'console_scripts': [
          'pstopwatch = pythonstopwatch.__main__:main'
      ]
      })

print("Project Setup file")
