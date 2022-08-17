import argparse
import dlib

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor("D:\ML LAB\datasets\labels_ibug_300W_test.xml", "D:\ML LAB\eye_predictor.dat")
print("[INFO] error: {}".format(error))
