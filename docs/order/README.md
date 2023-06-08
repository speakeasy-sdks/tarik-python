# order

### Available Operations

* [order_schema_api_v1_orders_schema_get](#order_schema_api_v1_orders_schema_get) - Get JSON schema for order
* [order_validated_api_v1_orders_post](#order_validated_api_v1_orders_post) - Add new order

## order_schema_api_v1_orders_schema_get

Get JSON schema for order

### Example Usage

```python
import lk


s = lk.Lk()


res = s.order.order_schema_api_v1_orders_schema_get()

if res.response is not None:
    # handle response
```

## order_validated_api_v1_orders_post

Checks if JSON has valid schema and adds request to create new order. No multiple orders will be created for the same **order_id**, even if request is accepted. Only first order request for **order_id** is created.

### Example Usage

```python
import lk
import dateutil.parser
from lk.models import operations, shared

s = lk.Lk()

req = shared.Order(
    created_at=dateutil.parser.isoparse('2022-03-18T00:29:19.137Z'),
    customer=shared.Customer(
        email='Junior.Kshlerin@hotmail.com',
        erp_id=925597,
        first_name='Rocky',
        human_id=71036,
        id=337396,
        last_name='Bogisich',
        middle_name='deserunt',
        phone='489-818-8947',
    ),
    items=[
        shared.Item(
            name='Deanna Sauer MD',
            price=6399.21,
            quantity=582020,
            sku=143353,
        ),
        shared.Item(
            name='Irvin Rosenbaum III',
            price=4736,
            quantity=264555,
            sku=186332,
        ),
        shared.Item(
            name='Jonathon Klocko',
            price=1352.18,
            quantity=18789,
            sku=324141,
        ),
        shared.Item(
            name='Louis Moore',
            price=3864.89,
            quantity=943749,
            sku=902599,
        ),
    ],
    merchant_id=681820,
    order_id=449950,
    payment=shared.Payment(
        method=shared.PaymentMethod.ZERO,
        status=shared.PaymentStatus.ZERO,
    ),
    shipping=shared.Shipping(
        address=shared.NPPackStation(
            city='Kertzmannside',
            city_id='b10faaa2-352c-4595-9907-aff1a3a2fa94',
            comment='commodi',
            region='quam',
            region_id='739251aa-52c3-4f5a-9019-da1ffe78f097',
            settlement_description='cum',
            settlement_type='0074f154-71b5-4e6e-93b9-9d488e1e91e4',
            street=shared.Street(
                name='Elizabeth Orn',
            ),
            warehouse_id='abd44269-802d-4502-a94b-b4f63c969e9a',
            warehouse_number=223081,
        ),
        method=shared.ShippingMethod.NOVAPOSHTA_PACKSTATION,
        price=8915.55,
        recipient=shared.Recipient(
            first_name='Veda',
            last_name='Parisian',
            middle_name='in',
            phone='896.227.8436 x825',
        ),
    ),
)

res = s.order.order_validated_api_v1_orders_post(req, operations.OrderValidatedAPIV1OrdersPostSecurity(
    o_auth2_password_bearer="",
))

if res.response is not None:
    # handle response
```
