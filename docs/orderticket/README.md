# order_ticket

### Available Operations

* [new_ticket_api_v1_ticket_post](#new_ticket_api_v1_ticket_post) - Add new order ticket
* [ticket_status_api_v1_ticket_ticket_id_comment_post](#ticket_status_api_v1_ticket_ticket_id_comment_post) - Add ticket comment

## new_ticket_api_v1_ticket_post

Add new order ticket

### Example Usage

```python
import lk
import dateutil.parser
from lk.models import operations, shared

s = lk.Lk()

req = shared.OrderTicket(
    decision='id',
    order_id=501324,
    solution_time=dateutil.parser.isoparse('2021-02-02T01:24:52.629Z'),
    status=shared.OrderTicketStatus.SEVENE9F1204_F46B_1410_FB9A_0050BA5D6C38,
    ticket_id='deserunt',
)

res = s.order_ticket.new_ticket_api_v1_ticket_post(req, operations.NewTicketAPIV1TicketPostSecurity(
    o_auth2_password_bearer="",
))

if res.response is not None:
    # handle response
```

## ticket_status_api_v1_ticket_ticket_id_comment_post

Add ticket comment

### Example Usage

```python
import lk
import dateutil.parser
from lk.models import operations, shared

s = lk.Lk()

req = operations.TicketStatusAPIV1TicketTicketIDCommentPostRequest(
    order_ticket=shared.OrderTicket(
        decision='nisi',
        order_id=423855,
        solution_time=dateutil.parser.isoparse('2021-10-15T07:59:26.631Z'),
        status=shared.OrderTicketStatus.THREEE7F420C_F46B_1410_FC9A_0050BA5D6C38,
        ticket_id='perferendis',
    ),
    ticket_id='nihil',
)

res = s.order_ticket.ticket_status_api_v1_ticket_ticket_id_comment_post(req, operations.TicketStatusAPIV1TicketTicketIDCommentPostSecurity(
    o_auth2_password_bearer="",
))

if res.response is not None:
    # handle response
```
