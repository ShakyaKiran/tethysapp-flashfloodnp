# from setuptools import setup, find_namespace_packages
# from tethys_apps.app_installation import find_all_resource_files
# from tethys_apps.base.app_base import TethysAppBase
#
# # -- Apps Definition -- #
# app_package = 'flashfloodnp'
# release_package = f'{TethysAppBase.package_namespace}-{app_package}'
#
# # -- Python Dependencies -- #
# dependencies = []
#
# # -- Get Resource File -- #
# resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)
#
#
# setup(
#     name=release_package,
#     version='0.0.1',
#     description='',
#     long_description='',
#     keywords='',
#     author='',
#     author_email='',
#     url='',
#     license='',
#     packages=find_namespace_packages(),
#     package_data={'': resource_files},
#     include_package_data=True,
#     zip_safe=False,
#     install_requires=dependencies,
# )

import os
from setuptools import setup, find_namespace_packages

# -- Apps Definition -- #
app_package = 'flashfloodnp'
package_namespace = 'tethysapp'
release_package = f'{package_namespace}-{app_package}'

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File (Pure Python Replacer) -- #
def find_all_resource_files(directory, package):
    paths = []
    # Walk through public, templates, and work spaces inside tethysapp/flashfloodnp
    base_path = os.path.join(package, directory)
    for (path, directories, filenames) in os.walk(base_path):
        for filename in filenames:
            paths.append(os.path.relpath(os.path.join(path, filename), base_path))
    return paths

resource_files = find_all_resource_files(app_package, package_namespace)

setup(
    name=release_package,
    version='0.0.1',
    description='',
    long_description='',
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={f'{package_namespace}.{app_package}': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)