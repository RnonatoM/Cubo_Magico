import random


class Cube:
  """
  Representa um cubo mágico.

  Attributes:
    _faces: Uma lista de listas de strings, representando as faces do cubo.
  """

  def __init__(self):
    self._faces = [['W', 'W', 'W'], ['Y', 'Y', 'Y'], ['R', 'R', 'R'],
                    ['O', 'O', 'O'], ['B', 'B', 'B'], ['G', 'G', 'G']]

  def __str__(self):
    """
    Represente o cubo como uma string.

    Returns:
      Uma string representando o cubo.
    """
    output = ''
    for face in self._faces:
      output += '|'.join(face) + '\n'
    return output

  def rotate(self, face, direction):
    """
    Gira uma face do cubo.

    Args:
      face: O número da face a girar.
      direction: A direção da rotação.
    """
    if direction == 'CW':
      self._faces[face] = self._faces[face][::-1]
    elif direction == 'CCW':
      self._faces[face] = self._faces[face][::-1][::-1]

  def scramble(self):
    """
    Embaralha o cubo.
    """
    moves = []
    for _ in range(100):
      face = random.randint(0, 5)
      direction = random.choice(['CW', 'CCW'])
      moves.append((face, direction))

    for face, direction in moves:
      self.rotate(face, direction)

    self._scramble_colors()

  def _scramble_colors(self):
    """
    Embaralha as cores das faces do cubo.
    """
    for face in range(6):
      for i in range(3):
        face_index = random.randint(0, 2)
        self._faces[face][i], self._faces[face][face_index] = self._faces[face][face_index], self._faces[face][i]


def main():
  cube = Cube()
  cube.scramble()
  print(cube)


if __name__ == '__main__':
  main()
