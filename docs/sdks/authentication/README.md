# authentication

### Available Operations

* [login_api_v1_token_post](#login_api_v1_token_post) - Login

## login_api_v1_token_post

Login

### Example Usage

```python
import lk
from lk.models import shared

s = lk.Lk()

req = shared.BodyLoginAPIV1TokenPost(
    client_id='deserunt',
    client_secret='suscipit',
    grant_type='iure',
    password='magnam',
    scope='debitis',
    username='Anahi38',
)

res = s.authentication.login_api_v1_token_post(req)

if res.login_api_v1_token_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.BodyLoginAPIV1TokenPost](../../models/shared/bodyloginapiv1tokenpost.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.LoginAPIV1TokenPostResponse](../../models/operations/loginapiv1tokenpostresponse.md)**

