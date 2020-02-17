#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv

from cvoverlayimg import CvOverlayImage


def main():
    cv_background_image = cv.imread("image/bg_takeyabu.jpg")
    cv_overlay_image = cv.imread(
        "image/ninja_hashiru.png",
        cv.IMREAD_UNCHANGED)  # IMREAD_UNCHANGEDを指定しα込みで読み込む
    cv_overlay_image = cv.resize(cv_overlay_image, (100, 100))

    point = (550, 250)

    image = CvOverlayImage.overlay(cv_background_image, cv_overlay_image,
                                   point)

    cv.imshow("sample", image)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
