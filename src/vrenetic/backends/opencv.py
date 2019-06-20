import cv2 as cv


def details():
    details = cv.getBuildInformation()
    details_list = details.splitlines()
    details_summary = details_list[1:28]
    print("\n".join(details_summary))