# LK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/tarik-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import lk
from lk.models import shared

s = lk.Lk()

req = shared.BodyLoginAPIV1TokenPost(
    client_id='corrupti',
    client_secret='provident',
    grant_type='distinctio',
    password='quibusdam',
    scope='unde',
    username='Ryan.Little62',
)

res = s.authentication.login_api_v1_token_post(req)

if res.login_api_v1_token_post_200_application_json_any is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [authentication](docs/authentication/README.md)

* [login_api_v1_token_post](docs/authentication/README.md#login_api_v1_token_post) - Login

### [order](docs/order/README.md)

* [order_schema_api_v1_orders_schema_get](docs/order/README.md#order_schema_api_v1_orders_schema_get) - Get JSON schema for order
* [order_validated_api_v1_orders_post](docs/order/README.md#order_validated_api_v1_orders_post) - Add new order

### [order_status](docs/orderstatus/README.md)

* [status_request_validated_api_v1_orders_order_id_status_request_post](docs/orderstatus/README.md#status_request_validated_api_v1_orders_order_id_status_request_post) - Send order status request
* [status_schema_api_v1_orders_status_schema_get](docs/orderstatus/README.md#status_schema_api_v1_orders_status_schema_get) - Get JSON schema for order status
* [status_validated_api_v1_orders_order_id_status_post](docs/orderstatus/README.md#status_validated_api_v1_orders_order_id_status_post) - Set order status

### [order_ticket](docs/orderticket/README.md)

* [new_ticket_api_v1_ticket_post](docs/orderticket/README.md#new_ticket_api_v1_ticket_post) - Add new order ticket
* [ticket_status_api_v1_ticket_ticket_id_comment_post](docs/orderticket/README.md#ticket_status_api_v1_ticket_ticket_id_comment_post) - Add ticket comment
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
