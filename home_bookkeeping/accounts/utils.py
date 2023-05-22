import base64
from io import BytesIO

import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7, 3))
    plt.barh(x, y)
    plt.xticks(rotation=25)
    plt.xlabel('Сумма')
    plt.tight_layout()
    graph = get_graph()
    return graph
