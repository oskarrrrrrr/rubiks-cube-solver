class Cube3by3:
    def __init__(self):
        self._init_faces()

    def _init_faces(self):
        self.top_face = Cube3by3._get_single_color_face('w')
        self.front_face = Cube3by3._get_single_color_face('r')
        self.left_face = Cube3by3._get_single_color_face('g')
        self.right_face = Cube3by3._get_single_color_face('b')
        self.back_face = Cube3by3._get_single_color_face('o')
        self.bottom_face = Cube3by3._get_single_color_face('y')

    @staticmethod
    def _get_single_color_face(color):
        return [[color] * 3,
                [color] * 3,
                [color] * 3]

    def __str__(self):
        s = '\n'.join([(' ' * 6) + ' '.join(r) for r in self.top_face]) + '\n'
        s += '\n'.join(
            [' '.join([' '.join(l), ' '.join(f), ' '.join(r), ' '.join(b)])
             for l, f, r, b in zip(self.left_face, self.front_face, self.right_face, self.back_face)]
        )
        s += '\n' + '\n'.join([(' ' * 6) + ' '.join(r) for r in self.bottom_face]) + '\n'
        return s

    def make_move(self, move):
        dbl_layer = move[0].islower()
        dbl_rot = '2' in move
        reverse = '\'' in move
        move = move.upper()
        move_letter = move[0]

        if move_letter == 'R':
            self._move_r(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'L':
            self._move_l(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'U':
            self._move_u(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'D':
            self._move_d(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'F':
            self._move_f(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'B':
            self._move_b(dbl_layer, dbl_rot, reverse)
        elif move_letter == 'M':
            self._move_m(dbl_rot, reverse)
        elif move_letter == 'E':
            self._move_e(dbl_rot, reverse)
        elif move_letter == 'S':
            self._move_x(dbl_rot, reverse)
        elif move_letter == 'X':
            self._move_m(dbl_rot, reverse)
        elif move_letter == 'Y':
            self._move_y(dbl_rot, reverse)
        elif move_letter == 'Z':
            self._move_z(dbl_rot, reverse)

    def _move_r(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_l(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_u(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_d(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_f(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_b(self, dbl_layer, dbl_rot, reverse):
        pass

    def _move_m(self, dbl_rot, reverse):
        pass

    def _move_e(self, dbl_rot, reverse):
        pass

    def _move_s(self, dbl_rot, reverse):
        pass

    def _move_x(self, dbl_rot, reverse):
        pass

    def _move_y(self, dbl_rot, reverse):
        pass

    def _move_z(self, dbl_rot, reverse):
        pass


if __name__ == '__main__':
    cube = Cube3by3()
    print(cube)
