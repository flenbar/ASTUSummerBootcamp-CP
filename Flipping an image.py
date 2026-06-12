class Solution(object):
    def flipAndInvertImage(self, image):
        inv_image = [0] * len(image)
        for i in range(len(image)):
            inv_image[i] = image[i][::-1]
        for i in range(len(image)):
            for j in range(len(image[i])):
                if inv_image[i][j] == 1:
                    inv_image[i][j] = 0
                else:
                    inv_image[i][j] = 1
        return inv_image