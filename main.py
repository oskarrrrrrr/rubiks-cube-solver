from abc import ABC, abstractmethod
from enum import Enum, auto


class FaceColor(Enum):
    WHITE = auto()
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    ORANGE = auto()
    YELLOW = auto()


color2letter = {
    FaceColor.WHITE: 'w',
    FaceColor.RED: 'r',
    FaceColor.GREEN: 'g',
    FaceColor.BLUE: 'b',
    FaceColor.ORANGE: 'o',
    FaceColor.YELLOW: 'y',
}


class ClassicCubeEngine(ABC):
    @abstractmethod
    def get_face(self, face_name):
        pass

    @abstractmethod
    def move_R(self, double, reverse):
        pass

    def move_r(self, double, reverse):
        self.move_R(double, reverse)
        self.move_M(double, not reverse)

    @abstractmethod
    def move_L(self, double, reverse):
        pass

    def move_l(self, double, reverse):
        self.move_L(double, reverse)
        self.move_M(double, reverse)

    @abstractmethod
    def move_U(self, double, reverse):
        pass

    def move_u(self, double, reverse):
        self.move_U(double, reverse)
        self.move_E(double, not reverse)

    @abstractmethod
    def move_D(self, double, reverse):
        pass

    def move_d(self, double, reverse):
        self.move_D(double, reverse)
        self.move_E(double, reverse)

    @abstractmethod
    def move_F(self, double, reverse):
        pass

    def move_f(self, double, reverse):
        self.move_F(double, reverse)
        self.move_S(double, reverse)

    @abstractmethod
    def move_B(self, double, reverse):
        pass

    def move_b(self, double, reverse):
        self.move_B(double, reverse)
        self.move_S(double, not reverse)

    @abstractmethod
    def move_M(self, double, reverse):
        pass

    @abstractmethod
    def move_E(self, double, reverse):
        pass

    @abstractmethod
    def move_S(self, double, reverse):
        pass

    @abstractmethod
    def move_X(self, double, reverse):
        pass

    @abstractmethod
    def move_Y(self, double, reverse):
        pass

    @abstractmethod
    def move_Z(self, double, reverse):
        pass

    def make_move(self, move):
        double = '2' in move
        reverse = "'" in move
        move_letter = move[0]

        if move_letter == 'R':
            self.move_R(double, reverse)
        elif move_letter == 'r':
            self.move_r(double, reverse)

        elif move_letter == 'L':
            self.move_L(double, reverse)
        elif move_letter == 'l':
            self.move_l(double, reverse)

        elif move_letter == 'U':
            self.move_U(double, reverse)
        elif move_letter == 'u':
            self.move_u(double, reverse)

        elif move_letter == 'D':
            self.move_D(double, reverse)
        elif move_letter == 'd':
            self.move_d(double, reverse)

        elif move_letter == 'F':
            self.move_F(double, reverse)
        elif move_letter == 'f':
            self.move_f(double, reverse)

        elif move_letter == 'B':
            self.move_B(double, reverse)
        elif move_letter == 'b':
            self.move_b(double, reverse)

        elif move_letter == 'M':
            self.move_M(double, reverse)
        elif move_letter == 'E':
            self.move_E(double, reverse)
        elif move_letter == 'S':
            self.move_S(double, reverse)

        elif move_letter == 'X':
            self.move_X(double, reverse)
        elif move_letter == 'Y':
            self.move_Y(double, reverse)
        elif move_letter == 'Z':
            self.move_Z(double, reverse)


class CubeSimple(ClassicCubeEngine):
    def __init__(self):
        self._init_faces()

    def _init_faces(self):
        self.top_face = CubeSimple._get_single_color_face(FaceColor.WHITE)
        self.front_face = CubeSimple._get_single_color_face(FaceColor.RED)
        self.left_face = CubeSimple._get_single_color_face(FaceColor.GREEN)
        self.right_face = CubeSimple._get_single_color_face(FaceColor.BLUE)
        self.back_face = CubeSimple._get_single_color_face(FaceColor.ORANGE)
        self.bottom_face = CubeSimple._get_single_color_face(FaceColor.YELLOW)

    @staticmethod
    def _get_single_color_face(color):
        return [[color] * 3,
                [color] * 3,
                [color] * 3]

    def get_face(self, face_name):
        if face_name == 'top':
            return self.top_face
        if face_name == 'front':
            return self.front_face
        if face_name == 'left':
            return self.left_face
        if face_name == 'right':
            return self.right_face
        if face_name == 'back':
            return self.back_face
        if face_name == 'bottom':
            return self.bottom_face

    def move_R(self, double, reverse):
        self.right_face = CubeSimple._rotate_face(self.right_face, not reverse, double)
        if double:
            CubeSimple._swap_columns(self.front_face, 2, self.back_face, 0, True)
            CubeSimple._swap_columns(self.top_face, 2, self.bottom_face, 2, False)
        else:
            if reverse:
                CubeSimple._swap_columns(self.front_face, 2, self.bottom_face, 2)
                CubeSimple._swap_columns(self.front_face, 2, self.back_face, 0, True)
                CubeSimple._swap_columns(self.front_face, 2, self.top_face, 2)
            else:
                CubeSimple._swap_columns(self.front_face, 2, self.top_face, 2)
                CubeSimple._swap_columns(self.front_face, 2, self.back_face, 0, True)
                CubeSimple._swap_columns(self.front_face, 2, self.bottom_face, 2)

    def move_L(self, double, reverse):
        pass

    def move_U(self, double, reverse):
        pass

    def move_D(self, double, reverse):
        pass

    def move_F(self, double, reverse):
        pass

    def move_B(self, double, reverse):
        pass

    def move_M(self, double, reverse):
        pass

    def move_E(self, double, reverse):
        pass

    def move_S(self, double, reverse):
        pass

    def move_X(self, double, reverse):
        pass

    def move_Y(self, double, reverse):
        pass

    def move_Z(self, double, reverse):
        pass

    @staticmethod
    def _rotate_face(face, clockwise, double):
        if double:
            # corners
            face[0][0], face[2][2] = face[2][2], face[0][0]
            face[0][2], face[2][0] = face[2][0], face[0][2]
            # sides
            face[0][1], face[2][1] = face[2][1], face[0][1]
            face[1][0], face[1][2] = face[1][2], face[1][0]
        else:
            if clockwise:
                # corners
                face[0][0], face[0][2] = face[0][2], face[0][0]
                face[0][0], face[2][2] = face[2][2], face[0][0]
                face[0][0], face[2][0] = face[2][0], face[0][0]
                # sides
                face[0][1], face[1][2] = face[1][2], face[0][1]
                face[0][1], face[2][1] = face[2][1], face[0][1]
                face[0][1], face[1][0] = face[1][0], face[0][1]
            else:
                # corners
                face[0][0], face[2][0] = face[2][0], face[0][0]
                face[0][0], face[2][2] = face[2][2], face[0][0]
                face[0][0], face[0][2] = face[0][2], face[0][0]
                # sides
                face[0][1], face[1][0] = face[1][0], face[0][1]
                face[0][1], face[2][1] = face[2][1], face[0][1]
                face[0][1], face[1][2] = face[1][2], face[0][1]
        return face

    @staticmethod
    def _swap_columns(face1, col1, face2, col2, reverse=False):
        if reverse:
            for i in range(3):
                face1[2-i][col1], face2[i][col2] = face2[i][col2], face1[2-i][col1]
        else:
            for i in range(3):
                face1[i][col1], face2[i][col2] = face2[i][col2], face1[i][col1]

    def __str__(self):
        s = '\n'.join([(' ' * 6) + ' '.join(map(color2letter.get, r)) for r in self.get_face('top')]) + '\n'
        s += '\n'.join(
            [' '.join([' '.join(map(color2letter.get, l)), ' '.join(map(color2letter.get, f)),
                       ' '.join(map(color2letter.get, r)), ' '.join(map(color2letter.get, b))])
             for l, f, r, b in
             zip(self.get_face('left'), self.get_face('front'), self.get_face('right'), self.get_face('back'))]
        )
        s += '\n' + '\n'.join([(' ' * 6) + ' '.join(map(color2letter.get, r)) for r in self.get_face('bottom')]) + '\n'
        return s


def get_test_cube_1():
    cube = CubeSimple()
    cube.right_face = [
        [FaceColor.WHITE, FaceColor.RED, FaceColor.BLUE],
        [FaceColor.BLUE, FaceColor.RED, FaceColor.WHITE],
        [FaceColor.YELLOW, FaceColor.YELLOW, FaceColor.ORANGE]
    ]
    cube.top_face[0][2] = FaceColor.GREEN
    cube.top_face[1][2] = FaceColor.YELLOW
    cube.front_face[0][2] = FaceColor.BLUE
    cube.front_face[1][2] = FaceColor.ORANGE
    return cube


if __name__ == '__main__':
    cube = get_test_cube_1()
    print(cube)
    cube.move_R(True, False)
    print(cube)
