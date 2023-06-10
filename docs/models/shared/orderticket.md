# OrderTicket


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `decision`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Decision                                                             |
| `order_id`                                                           | *int*                                                                | :heavy_check_mark:                                                   | Marketplace Order ID                                                 |
| `solution_time`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Format YYYY-MM-DD[T]HH:MM                                            |
| `status`                                                             | [OrderTicketStatus](../../models/shared/orderticketstatus.md)        | :heavy_check_mark:                                                   | Status                                                               |
| `ticket_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | BPM ticket ID                                                        |