from enum import IntEnum


class InpaintingPreProcessTypes(IntEnum):
    """
    Enum class for inpainting pre-processing types.

    1- None: No pre-processing.
    2- Resize: Resize the image and mask to the specified height and width.
    3- Crop and Resize: Calculate the bounding box of the mask, adjust bounding box
    to match the aspect ratio of the given height and width. Then, crop the image
    and mask according to the bounding box.
    """

    NONE = 1
    RESIZE = 2
    CROP_AND_RESIZE = 3


class InpaintingPostProcessTypes(IntEnum):
    """
    Enum class for inpainting post-processing types.

    1- None: No post-processing.
    2- Direct Replace: Directly replace the inpainted region with the original image.
    3- Blend: Blend the inpainted region with the original image.
    """

    NONE = 1
    DIRECT_REPLACE = 2
    BLEND = 3


class InpaintingBlendingTypes(IntEnum):
    """
    Enum class for inpainting blending types.

    1- None: No blending.
    2- Poisson Blending: Use Poisson blending to blend the inpainted region with the
    original image.
    3- Gaussian Blending: Use Gaussian blending to blend the inpainted region with the
    original image.
    4- Linear Blending: Use linear blending to blend the inpainted region with the
    original image.
    5- Smooth Blending: Use smooth blending to blend the inpainted region with the
    original image.
    6- Smoother Blending: Use smoother blending to blend the inpainted region with the
    original image.
    """

    NONE = 1
    POISSON_BLENDING = 2
    GAUSSIAN_BLENDING = 3
    LINEAR_BLENDING = 4
    SMOOTH_BLENDING = 5
    SMOOTHER_BLENDING = 6
