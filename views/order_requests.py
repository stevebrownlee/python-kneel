ORDERS = [
    {
      "id": 1,
      "metalId": 3,
      "sizeId": 2,
      "styleId": 3,
      "timestamp": 1614659931693
    },
    {
      "metalId": 1,
      "sizeId": 1,
      "styleId": 3,
      "timestamp": 1616333988188,
      "id": 2
    },
    {
      "metalId": 1,
      "sizeId": 1,
      "styleId": 1,
      "timestamp": 1616334884289,
      "id": 3
    },
    {
      "metalId": 5,
      "sizeId": 5,
      "styleId": 3,
      "timestamp": 1616334890694,
      "id": 4
    }
  ]

def get_all_orders():
    return ORDERS


def get_single_order(id):
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(req):
    return ORDERS


def update_order(req):
    return ORDERS


def delete_order(req):
    return ORDERS
