import json
from pathlib import Path
path=Path("Taller_2_nombre_apellido.ipynb")
nb=json.loads(path.read_text(encoding="utf-8"))
cell=nb['cells'][27]
lines=cell['source']
for i,line in enumerate(list(lines)):
    if line == 'print("\n\n":)\n':
        pass
