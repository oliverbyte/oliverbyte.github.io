# Generate local preview
1. `pelican -r -l`
2. Browse to http://127.0.0.1:8000
3. Commit to main

# Publish site
1. `ghp-import output -p -c www.oliverbyte.de` (pushes to remote branch 'gh-pages' which is deployed then via GitHub actions)