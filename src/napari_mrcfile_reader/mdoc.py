from pathlib import Path


class MDOC:
    def __init__(self, path: str):
        self.path = Path(path)
        self.montage = False
        self.piece_coords = []
        self.aligned_piece_coords = []

        if self.path.is_file():
            with open(self.path) as file:
                for line in file:
                    if line.startswith('Montage = '):
                        self.montage = bool(line.split()[-1])
                    elif line.startswith('PieceCoordinates = '):
                        self.piece_coords.append(tuple(map(int, line.split()[-3:])))
                    elif line.startswith('AlignedPieceCoords = '):
                        self.aligned_piece_coords.append(tuple(map(int, line.split()[-3:])))
