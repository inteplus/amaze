#!/usr/bin/python3

from mt import np
from mt.base import logger

av_board = np.array([
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
    [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
    [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
])

av_piece01 = np.array([
    [1,1,1,1],
    [0,0,1,1],
])

av_piece02 = np.array([
    [1,1,1],
    [1,0,1],
])

av_piece03 = np.array([
    [1,1,1],
    [1,0,0],
    [1,0,0],
])

av_piece04 = np.array([
    [0,1,1,1],
    [1,1,0,0],
])

av_piece05 = np.array([
    [1,1,1,1],
    [1,0,0,0],
])

av_piece06 = np.array([
    [1,1],
    [1,0],
])

av_piece07 = np.array([
    [0,1,1],
    [1,1,0],
])

av_piece08 = np.array([
    [1,1,1],
    [0,1,1],
])

av_piece09 = np.array([
    [1,0,0],
    [1,1,1],
])

av_piece10 = np.array([
    [0,1,1],
    [1,1,0],
    [1,0,0],
])

av_piece11 = np.array([
    [1,1,1],
    [0,1,0],
])

av_piece12 = np.array([
    [1,1,1,1],
])

lm_pieces = [av_piece01, av_piece02, av_piece03, av_piece04, av_piece05, av_piece06, av_piece07,
             av_piece08, av_piece09, av_piece10, av_piece11] # exclude av_piece12

def rotate_ccw(mat: np.ndarray) -> np.ndarray:
    return mat[:,::-1].T


def make_patterns(lm_pieces: list) -> list:
    l_patterns = []
    for i, m_piece in enumerate(lm_pieces):
        piece = m_piece
        for j in range(4):
            skip = False
            for i2, piece2 in l_patterns:
                if np.array_equal(piece, piece2):
                    skip = True
                    break

            if not skip:
                l_patterns.append((i+1, piece))

            piece = rotate_ccw(piece)

    return l_patterns


def main():
    logger.info("Starting with {} pieces.".format(len(lm_pieces)))
    l_patterns = make_patterns(lm_pieces)
    logger.info("Generated {} patterns.".format(len(l_patterns)))


if __name__ == '__main__':
    main()
