# order_status

### Available Operations

* [status_request_validated_api_v1_orders_order_id_status_request_post](#status_request_validated_api_v1_orders_order_id_status_request_post) - Send order status request
* [status_schema_api_v1_orders_status_schema_get](#status_schema_api_v1_orders_status_schema_get) - Get JSON schema for order status
* [status_validated_api_v1_orders_order_id_status_post](#status_validated_api_v1_orders_order_id_status_post) - Set order status

## status_request_validated_api_v1_orders_order_id_status_request_post

Send order status request

### Example Usage

```python
import lk
from lk.models import operations, shared

s = lk.Lk()

req = operations.StatusRequestValidatedAPIV1OrdersOrderIDStatusRequestPostRequest(
    order_status=shared.OrderStatus(
        order_id=313218,
        status=shared.OrderStatuses.ONE,
    ),
    order_id=965417,
)

res = s.order_status.status_request_validated_api_v1_orders_order_id_status_request_post(req, operations.StatusRequestValidatedAPIV1OrdersOrderIDStatusRequestPostSecurity(
    o_auth2_password_bearer="",
))

if res.response is not None:
    # handle response
```

## status_schema_api_v1_orders_status_schema_get

Get JSON schema for order status

### Example Usage

```python
import lk


s = lk.Lk()


res = s.order_status.status_schema_api_v1_orders_status_schema_get()

if res.response is not None:
    # handle response
```

## status_validated_api_v1_orders_order_id_status_post

Set order status

### Example Usage

```python
import lk
from lk.models import operations, shared

s = lk.Lk()

req = operations.StatusValidatedAPIV1OrdersOrderIDStatusPostRequest(
    order_status=shared.OrderStatus(
        order_id=692532,
        status=shared.OrderStatuses.ONE,
    ),
    order_id=725255,
)

res = s.order_status.status_validated_api_v1_orders_order_id_status_post(req, operations.StatusValidatedAPIV1OrdersOrderIDStatusPostSecurity(
    o_auth2_password_bearer="",
))

if res.response is not None:
    # handle response
```
