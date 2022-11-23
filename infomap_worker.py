from infomap import Infomap

def infomap_worker(filename, outname, seed=123, states=False, **kwargs):
    im = Infomap(seed=seed, **kwargs)
    im.read_file(filename)
    im.run()
    im.write(outname, states=states)

    return {
        "codelength": im.codelength,
        "num_levels": im.num_levels,
        "num_modules": im.num_top_modules,
        "outname": outname,
    }
