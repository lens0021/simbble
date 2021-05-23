# A script to resolve dependencies of MediaWiki extension for Quibble test

from os import environ
# pf for https://raw.githubusercontent.com/wikimedia/integration-config/master/zuul/parameter_functions.py
from pf import dependencies, get_dependencies

# https://github.com/femiwiki/.github/issues/4
if 'MEDIAWIKI_VERSION' in environ and environ['MEDIAWIKI_VERSION'] == 'REL1_35':
  dependencies['EventLogging'].remove('EventBus')

# Add dependencies of target extension
if 'DEPENDENCIES' in environ:
  dependencies['ext'] = environ['DEPENDENCIES'].split(',')
else:
  dependencies['ext'] = open('dependencies').read().splitlines()

# Resolve
resolvedDependencies = []
for d in get_dependencies('ext', dependencies):
  d = 'mediawiki/extensions/' + d
  d = d.replace('/extensions/skins/', '/skins/')
  resolvedDependencies.append(d)
if 'EventLogging' in resolvedDependencies:
  resolvedDependencies.remove('EventLogging')
print(' '.join(resolvedDependencies))
