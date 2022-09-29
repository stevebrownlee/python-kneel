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


def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order



def update_order(req):
    return ORDERS


def delete_order(id):
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)
