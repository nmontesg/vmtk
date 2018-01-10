import pytest
import vmtk.vmtkimagesmoothing as imagesmoothing


def test_default_smoothing(aorta_image, image_to_sha):
    smoother = imagesmoothing.vmtkImageSmoothing()
    smoother.Image = aorta_image
    smoother.Execute()

    assert image_to_sha(smoother.Image) == '9885dd0ab5ecbc32f1c0b738a130af63fd559652'


def test_smoothing_high_standard_deviation(aorta_image, image_to_sha):
    smoother = imagesmoothing.vmtkImageSmoothing()
    smoother.Image = aorta_image
    smoother.StandardDeviation = 7.6
    smoother.Execute()

    assert image_to_sha(smoother.Image) == 'b5a71c71bd60e532a9228d21117367d7547669bb'


def test_lower_radius_factor(aorta_image, image_to_sha):
    smoother = imagesmoothing.vmtkImageSmoothing()
    smoother.Image = aorta_image
    smoother.RadiusFactor = 3.4
    smoother.Execute()

    assert image_to_sha(smoother.Image) == '9fbb09c29ab9ce44e74d412a0d6c668fc9c45be9'