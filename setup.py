from setuptools import setup, find_packages

setup(name="fenwaysavings",
      version="0.0.1",
      author="Adit Modhvadia",
      url="https://github.com/aditmodhvadia/fenway-savings",
      description="A Python command line program for a banking system.",
      packages=find_packages(exclude=['test', 'test.*']),
      install_requires=['pymongo'],
      # test_suite="test",
      entry_points={'console_scripts': [
          'fsavings = fenwaysavings.__main__:main'
      ]
      })

print("Project Setup file")
