import setuptools


setuptools.setup(
  name="random-mac",
  version="0.3.0",
  description="Use machine learning to identify randomly-generated MAC addresses.",
  url="https://github.com/critical-path/random-mac",
  author="critical-path",
  author_email="n/a",
  license="MIT",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
  ],
  keywords="python machine-learning ml random media-access-control mac mac-address",
  packages=setuptools.find_packages(),
  install_requires=[
    "macaddress @ git+https://github.com/critical-path/macaddress.git",
    "numpy",
    "pandas",
    "scikit-learn"
  ]
)
