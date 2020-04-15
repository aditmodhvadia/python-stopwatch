from setuptools import setup, find_packages

setup(name="fenwaysavings",
      version="0.0.1",
      packages=find_packages(exclude=['test', 'test.*']),
      # install_requires=[],
      # test_suite="test",
      entry_points={'console_scripts': [
          'fenwaysavings = fenwaysavings.__main__:main'
      ]
      })

print("Project Setup file")
