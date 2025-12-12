from pathlib import Path

import dlib
import numpy as np
from PIL import Image


def test_import():
    """Basic import and version check."""
    print("dlib version:", dlib.__version__)
    assert hasattr(dlib, "__version__")


def test_frontal_face_detector_exists():
    detector = dlib.get_frontal_face_detector()
    assert detector is not None, "Failed to get frontal face detector"


def test_frontal_face_detector_runs_on_blank_image():
    detector = dlib.get_frontal_face_detector()

    # A simple 128x128 blank image (3-channel)
    img = np.zeros((128, 128, 3), dtype=np.uint8)

    # Should return an empty rectangle list, but must run without crashing
    detections = detector(img)
    print("Detector output:", detections)

    assert detections is not None
    assert len(detections) == 0  # blank image → zero faces expected


def test_frontal_face_detector_on_real_face():
    """Run the frontal face detector on a real image with a simple face-like pattern."""
    detector = dlib.get_frontal_face_detector()

    test_image_path = Path(__file__).parent / "data" / "lena.jpg"
    img_pil = Image.open(test_image_path).convert("L")  # convert to grayscale
    img = np.array(img_pil)

    detections = detector(img)
    assert len(detections) == 1
    print("Detections:", detections)

def test_dlib_array_operations():
    # Confirm that array → dlib conversion works
    arr = np.zeros((50, 50), dtype=np.uint8)
    dlib_arr = dlib.as_grayscale(arr)

    assert dlib_arr.shape == arr.shape
    assert dlib_arr[0][0] == 0

def test_numpy_to_dlib_matrix_operations():
    """Test conversion of numpy arrays to dlib matrices and basic arithmetic."""
    arr = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    mat = dlib.as_grayscale(arr)

    # Matrix arithmetic
    mat2 = mat + 10
    mat3 = mat2 - 5

    assert mat3.shape == arr.shape
    assert int(mat3[0][0]) >= 0
    assert int(mat3[0][0]) <= 255


def test_image_resize_and_copy():
    """Test resizing a dlib image and copying it."""
    arr = np.zeros((100, 100), dtype=np.uint8)
    img = dlib.as_grayscale(arr)

    # Resize to 50x50
    resized = dlib.resize_image(img, 50, 50)
    assert resized.shape == (50, 50)

    # Copy
    copied = resized.copy()
    assert np.array_equal(resized, copied)
