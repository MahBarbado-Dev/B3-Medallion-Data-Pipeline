import pandas as pd

def ler_cotahist(caminho, nrows=None):
    layout = {
        "tipo_registro": (0, 2),
        "data": (2, 10),
        "codigo_acao": (12, 24),
        "nome_empresa": (27, 39),
        "preco_abertura": (56, 69),
        "preco_fechamento": (108, 121),
        "volume": (170, 188)
    }

    df = pd.read_fwf(
        caminho,
        colspecs=list(layout.values()),
        names=list(layout.keys()),
        dtype={"tipo_registro": str},
        nrows=nrows
    )

    return df