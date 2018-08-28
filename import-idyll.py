import shutil

src_path = "../idyll-embed/dist/idyll-embed.min.js"
dest_path = "static/js/idyll-embed.min.js"

shutil.copyfile(src_path,dest_path)