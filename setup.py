from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('emailreader'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('emailreader')+1:] # Strip "emailreader/" or "emailreader\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-emailpreview',
    version='1.0',
    description='django-emailpreview lets you preview HTML emails in the admin interface, ' +
        'which is especially useful for debugging during development',
    author='Arthur Debert',
    author_email='arthur@stimuli.com.br',
    url='https://github.com/arthur-debert/Django-Email-Preview',
    packages=packages,
    package_data={'emailreader': data_files},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)

