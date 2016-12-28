#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=X0_a6U6PkCA
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *


def lomo(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    s_curve = (0, 0, 96, 64, 128, 128, 160, 192, 255, 255)
    inverted_s_curve = (0, 0, 64, 96, 128, 128, 192, 160, 255, 255)
    num_points = 10
    pdb.gimp_curves_spline(drawable, HISTOGRAM_RED, num_points, s_curve)
    pdb.gimp_curves_spline(drawable, HISTOGRAM_GREEN, num_points, s_curve)
    pdb.gimp_curves_spline(drawable, HISTOGRAM_BLUE, num_points,
                           inverted_s_curve)
    #add new layer & Set to 'overlay'
    opacity_100 = 100
    layer = pdb.gimp_layer_new(image, image.width, image.height, RGB_IMAGE,
                               "Overlay", opacity_100, OVERLAY_MODE)
    layer_position = 0
    pdb.gimp_image_insert_layer(image, layer, None, layer_position)

    # blend arguments and call to function
    blend_mode = 0
    paint_mode = 0
    gradient_type = 0
    offset = 0
    repeat = 0
    reverse = False
    supersample = False
    max_depth = 1
    threshold = 0
    dither = True
    x1 = layer.width # top-right
    y1 = 0
    x2 = layer.width / 2 # centre
    y2 = layer.height / 2
    pdb.gimp_edit_blend(layer, blend_mode, paint_mode, gradient_type,
                        opacity_100, offset, repeat, reverse, supersample,
                        max_depth, threshold,  dither, x1, y1, x2, y2)
    #merge all layers
    layer = pdb.gimp_image_merge_visible_layers(image, 0)
    #pdb.gimp_displays_flush()
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-lomo",
    "Lomo effect",
    "Creates a lomo effect on a given image",
    "Jackson Bates", "Jackson Bates", "2015",
    "Lomo",
    "RGB", # type of image it works on (*, RGB, RGB*, RGBA etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    lomo, menu="<Image>/Filters")  # second item is menu location

main()
