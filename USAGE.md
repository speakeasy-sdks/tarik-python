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