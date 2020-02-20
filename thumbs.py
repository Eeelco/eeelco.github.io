import glob, os

maxs = 300

for f in glob.glob('figures/*.jpg'):
    name = f[8:]
    thumbname = 'thumbnails/' + name
    if os.path.isfile(thumbname):
        continue
    mindim = int(os.popen('identify -format "%[fx:min(w,h)]" {}'.format(f)).read())

    os.system('convert {} -gravity center -crop {}x{}+0+0 +repage {}'.format(f,mindim,mindim,thumbname))
    if mindim > maxs:
        os.system('convert {} -resize {}x{} {}'.format(thumbname, maxs,maxs,thumbname))
