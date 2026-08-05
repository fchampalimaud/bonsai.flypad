from pathlib import Path

import harp

# from analysis.utils import COLUMN_NAMES

OUTPUT_PATH = Path("../output")


def main() -> None:
    for dir in OUTPUT_PATH.iterdir():
        if dir.is_dir():
            reader = harp.create_reader(dir)

            data = reader.CapacitanceValues.read(dir / "FlyPAD_33.bin")
            # data = data.rename(columns=dict(zip(data.columns.tolist(), COLUMN_NAMES)))
            data_arr = data.values >> 4
            data_arr.reshape(-1).astype("ushort").tofile(dir / "FlyPAD_33_12bits.bin")
