# idyll-flask

This is a simple quickstart to create multiple templated pages delivered via Python and Flask.

To run:

1. Clone this repo with

   ```
   git clone https://github.com/cmakler/idyll-flask.git
   ```
2. Install dependencies in the project's lib directory.

   ```
   pip install -r requirements.txt -t lib
   ```
3. Run this project locally from the command line:

   ```
   flask run
   ```

4. Visit the application [http://localhost:5000](http://localhost:5000)


## Importing idyll-embed

Idyll-embed is a standalone version of idyll that can be embedded in an HTML page. This repo has a possibly outdated version of that file. Also, you might want to regenerate that file using your own custom components.

To do this, clone the idyll-embed repo from https://github.com/idyll-lang/idyll-embed. You may then run

   ```
   python import-idyll.py
   ```
   
which is a simple script to copy the minified JS from that directory to this. The source path assumes that repo is in a sibling directory to this one.
