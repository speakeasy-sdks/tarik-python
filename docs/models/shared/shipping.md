# Shipping

Represents info about shipping order


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `address`                                                          | [NPPackStation](../../models/shared/nppackstation.md)              | :heavy_check_mark:                                                 | Represents info about shipping via `Nova Posta PackStation` method |
| `method`                                                           | [ShippingMethod](../../models/shared/shippingmethod.md)            | :heavy_check_mark:                                                 | N/A                                                                |
| `price`                                                            | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | N/A                                                                |
| `recipient`                                                        | [Recipient](../../models/shared/recipient.md)                      | :heavy_check_mark:                                                 | Represents info about recipient                                    |