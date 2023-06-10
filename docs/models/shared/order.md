# Order

Represents full info about order


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Format YYYY-MM-DD[T]HH:MM                                            |
| `customer`                                                           | [Customer](../../models/shared/customer.md)                          | :heavy_check_mark:                                                   | Represents info about order customer                                 |
| `items`                                                              | list[[Item](../../models/shared/item.md)]                            | :heavy_check_mark:                                                   | N/A                                                                  |
| `merchant_id`                                                        | *int*                                                                | :heavy_check_mark:                                                   | This field could be numeric string                                   |
| `order_id`                                                           | *int*                                                                | :heavy_check_mark:                                                   | This field could be numeric string                                   |
| `payment`                                                            | [Payment](../../models/shared/payment.md)                            | :heavy_check_mark:                                                   | Represents info about order payment                                  |
| `shipping`                                                           | [Shipping](../../models/shared/shipping.md)                          | :heavy_check_mark:                                                   | Represents info about shipping order                                 |