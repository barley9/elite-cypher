"""
661. Image Smoother

An image smoother is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells. If one or more of the surrounding cells of a cell is not present, we do not consider it in the average. Given an `m x n` integer matrix `img` representing the grayscale of an image, return the image after applying the smoother on each cell of it.
"""

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smoothed = [[0 for col in row] for row in img]

        for i in range(len(img)):
            for j in range(len(img[i])):
                indices = [
                    (i - 1, j - 1),
                    (i - 1, j    ),
                    (i - 1, j + 1),
                    (i    , j - 1),
                    (i    , j    ),
                    (i    , j + 1),
                    (i + 1, j - 1),
                    (i + 1, j    ),
                    (i + 1, j + 1),
                ]
                s = 0  # sum of cell values
                n = 0  # number of valid cells
                for row, col in indices:
                    if (0 <= row < len(img)) and (0 <= col < len(img[row])):
                        s += img[row][col]
                        n += 1
                smoothed[i][j] = s // n
        
        return smoothed