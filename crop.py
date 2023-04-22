import cv2
import numpy as np

file = ['vid/bicubic_city.png']
# file = ['udm/bicubic_0014.png']
# file = ['vimeo/bicubic_im4.png']
# file = ['udm/gbrsn.png', 'udm/fgbrsn.png']
pt1 = (480,160)  # 长方形框左上角坐标
pt2 = (560,210)  # 长方形框右下角坐标

# pt1 = (460,430)  # 长方形框左上角坐标
# pt2 = (515,470)  # 长方形框右下角坐标

# pt1 = (110,150)  # 长方形框左上角坐标
# pt2 = (220,210)  # 长方形框右下角坐标


for i in file:
    image = cv2.imread(i)
    patch = image[pt1[1]:pt2[1], pt1[0]:pt2[0], :]
    patch = cv2.resize(patch, (160, 100))
    cv2.imwrite('crop/'+i, patch)
    # if i=='udm/gt.png':
    #     cv2.rectangle(image, pt1, pt2, (0, 0, 255), 2)
    #     cv2.imwrite('crop/'+'udm/gtx.png', image)
