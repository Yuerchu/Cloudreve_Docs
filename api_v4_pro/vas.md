#本篇为pro前端源码文件 vas.ts API 文档

本文档描述了 `vas.ts` 文件中定义的所有接口、枚举和类型。

---

## 接口列表

### 1. PaymentSetting
支付全局配置信息。
| 属性           | 类型                | 说明               |
|----------------|---------------------|--------------------|
| currency_code  | `string`            | 货币代码（如 USD） |
| currency_mark  | `string`            | 货币符号（如 $）   |
| currency_unit  | `number`            | 货币单位基数       |
| providers      | `PaymentProvider[]` | 支持的支付提供商列表 |

---

### 2. PaymentProvider
支付提供商配置。
| 属性                 | 类型     | 说明                         | 是否可选 |
|----------------------|----------|------------------------------|----------|
| id                   | `string` | 提供商唯一标识               | 必填     |
| name                 | `string` | 提供商名称                   | 必填     |
| type                 | `string` | 提供商类型                   | 必填     |
| secret_key           | `string` | 密钥（如 Stripe 密钥）       | 可选     |
| app_id               | `string` | 应用 ID（如微信支付 AppID）  | 可选     |
| public_key           | `string` | 公钥（如支付宝公钥）         | 可选     |
| merchant_id          | `string` | 商户 ID                      | 可选     |
| certificate_serial   | `string` | 证书序列号                   | 可选     |
| api_private_key      | `string` | API 私钥                     | 可选     |
| endpoint             | `string` | 支付端点 URL                 | 可选     |

---

### 3. ProductParameter
产品参数配置。
| 属性           | 类型          | 说明                         | 是否可选 |
|----------------|---------------|------------------------------|----------|
| type           | `ProductType` | 产品类型（枚举值）           | 必填     |
| share_link_id  | `string`      | 分享链接 ID（类型为 1 时使用）| 可选     |
| sku_id         | `string`      | SKU ID（类型为 2/3/4 时使用）| 可选     |

---

### 4. CreatePaymentArgs
创建支付请求参数。
| 属性         | 类型              | 说明               | 是否可选 |
|--------------|-------------------|--------------------|----------|
| product      | `ProductParameter`| 产品参数           | 必填     |
| quantity     | `number`          | 购买数量           | 必填     |
| provider_id  | `string`          | 支付提供商 ID      | 可选     |
| email        | `string`          | 用户邮箱           | 可选     |

---

### 5. Payment
支付记录信息。
| 属性             | 类型            | 说明                           | 是否可选 |
|------------------|-----------------|--------------------------------|----------|
| id               | `string`        | 支付记录唯一 ID                | 必填     |
| trade_no         | `string`        | 交易号                         | 必填     |
| name             | `string`        | 支付名称                       | 必填     |
| status           | `PaymentStatus` | 支付状态（枚举值）             | 可选     |
| qyt              | `number`        | 购买数量（可能为 `quantity` 的拼写错误） | 必填     |
| price_unit       | `number`        | 单价（单位货币）               | 可选     |
| price_id         | `string`        | 价格 ID                        | 可选     |
| price_one_unit   | `number`        | 单件价格                       | 可选     |
| created_at       | `string`        | 创建时间                       | 必填     |
| updated_at       | `string`        | 更新时间                       | 必填     |
| product_type     | `number`        | 产品类型（对应 `ProductType` 枚举值） | 必填     |
| ticket           | `string`        | 支付凭证                       | 可选     |
| price_mark       | `string`        | 价格标记（如带货币符号的价格） | 可选     |

---

### 6. PaymentRequest
支付请求配置。
| 属性               | 类型      | 说明                     | 是否可选 |
|--------------------|-----------|--------------------------|----------|
| payment_needed     | `boolean` | 是否需要支付             | 必填     |
| url                | `string`  | 支付跳转 URL             | 可选     |
| qr_code_preferred  | `boolean` | 是否优先使用二维码支付   | 可选     |

---

### 7. CreatePaymentResponse
创建支付响应数据。
| 属性      | 类型            | 说明           |
|-----------|-----------------|----------------|
| payment   | `Payment`       | 支付记录信息   |
| request   | `PaymentRequest`| 支付请求配置   |

---

### 8. StorageProduct
存储产品配置。
| 属性     | 类型     | 说明           | 是否可选 |
|----------|----------|----------------|----------|
| id       | `string` | 产品 ID        | 必填     |
| name     | `string` | 产品名称       | 必填     |
| size     | `number` | 存储空间大小   | 必填     |
| time     | `number` | 有效期（天）   | 必填     |
| price    | `number` | 价格           | 必填     |
| chip     | `string` | 促销标签       | 可选     |
| points   | `number` | 积分奖励       | 可选     |

---

### 9. GroupSku
用户组 SKU 配置。
| 属性     | 类型       | 说明           |
|----------|------------|----------------|
| id       | `string`   | SKU ID         |
| name     | `string`   | SKU 名称       |
| price    | `number`   | 价格           |
| points   | `number`   | 积分奖励       |
| time     | `number`   | 有效期（天）   |
| chip     | `string`   | 促销标签       |
| des      | `string[]` | 描述列表       |

---

### 10. GiftCodeSummary
礼品码概要信息。
| 属性       | 类型     | 说明           | 是否可选 |
|------------|----------|----------------|----------|
| name       | `string` | 礼品码名称     | 必填     |
| qyt        | `number` | 数量           | 必填     |
| duration   | `number` | 有效期（天）   | 可选     |

---

### 11. GenerateRedeemsService
生成兑换码服务参数。
| 属性     | 类型              | 说明         |
|----------|-------------------|--------------|
| num      | `number`          | 生成数量     |
| product  | `ProductParameter`| 产品参数     |
| qyt      | `number`          | 单码包含数量 |

---

### 12. DeleteGiftCodeService
删除礼品码服务参数。
| 属性 | 类型     | 说明       |
|------|----------|------------|
| id   | `number` | 礼品码 ID  |

---

### 13. GiftCode
礼品码详细信息。
| 属性           | 类型              | 说明                     | 是否可选 |
|----------------|-------------------|--------------------------|----------|
| id             | `number`          | 礼品码 ID                | 必填     |
| created_at     | `string`          | 创建时间                 | 必填     |
| updated_at     | `string`          | 更新时间                 | 必填     |
| code           | `string`          | 礼品码字符串             | 必填     |
| used           | `boolean`         | 是否已使用               | 必填     |
| qyt            | `number`          | 数量                     | 必填     |
| used_by        | `number`          | 使用者 ID                | 必填     |
| product_props  | `ProductParameter`| 关联的产品参数           | 必填     |
| edges          | `{ user?: User }` | 关联的用户信息（可选）   | 可选     |

---

## 枚举列表

### 1. ProductType
产品类型枚举。
| 值           | 数值 | 说明               |
|--------------|------|--------------------|
| do_not_use   | 0    | 保留值，不可用     |
| share_link   | 1    | 分享链接类产品     |
| group        | 2    | 用户组类产品       |
| storage      | 3    | 存储空间类产品     |
| points       | 4    | 积分类产品         |

---

### 2. PaymentStatus
支付状态枚举。
| 值             | 说明               |
|----------------|--------------------|
| created        | 支付已创建         |
| paid           | 支付已完成         |
| fulfilled      | 支付已履约（如发放商品） |
| fulfill_failed | 履约失败           |
| canceled       | 支付已取消         |

---

### 3. PaymentProviderType
支付提供商类型枚举。
| 值       | 说明               |
|----------|--------------------|
| stripe   | Stripe 支付        |
| weixin   | 微信支付           |
| alipay   | 支付宝支付         |
| points   | 积分支付           |
| custom   | 自定义支付方式     |

```
```markdown

---

## 接口列表

### 4. CreatePaymentArgs
创建支付请求参数。（添加示例）
```typescript
// 创建存储空间购买请求示例
const exampleArgs: CreatePaymentArgs = {
  product: {
    type: ProductType.storage, // 3
    sku_id: "storage_500gb_30d"
  },
  quantity: 1,
  email: "user@example.com"
};

// 创建用户组购买请求示例
const groupPurchaseArgs: CreatePaymentArgs = {
  product: {
    type: ProductType.group, // 2
    sku_id: "vip_group_annual"
  },
  quantity: 1,
  provider_id: "alipay_001"
};
```

---

### 11. GenerateRedeemsService
生成兑换码服务参数。（添加示例）
```typescript
// 生成分享链接兑换码示例
const redeemExample: GenerateRedeemsService = {
  num: 10,
  product: {
    type: ProductType.share_link, // 1
    share_link_id: "link_8a2b3c"
  },
  qyt: 5 // 每个兑换码可兑换5次
};

// 生成积分兑换码示例
const pointsRedeem: GenerateRedeemsService = {
  num: 50,
  product: {
    type: ProductType.points, // 4
    sku_id: "points_1000"
  },
  qyt: 1
};
```

---

### 12. DeleteGiftCodeService
删除礼品码服务参数。（添加示例）
```typescript
// 删除操作请求示例
const deleteRequest: DeleteGiftCodeService = {
  id: 12345 // 要删除的礼品码ID
};
```

---

### 5. Payment
支付记录信息。（添加响应示例）
```json
// 支付成功响应示例
{
  "id": "pay_9s8d7f6g5h",
  "trade_no": "20230821123456",
  "name": "VIP用户组年费订阅",
  "status": "paid",
  "qyt": 1,
  "price_unit": 29900,
  "created_at": "2023-08-21T10:00:00Z",
  "updated_at": "2023-08-21T10:05:00Z",
  "product_type": 2,
  "price_mark": "¥299.00"
}
```

---

### 7. CreatePaymentResponse
创建支付响应数据。（添加完整示例）
```typescript
// 完整支付流程响应示例
const paymentResponse: CreatePaymentResponse = {
  payment: {
    id: "pay_a1b2c3d4",
    trade_no: "TRADE20230821001",
    name: "500GB存储空间",
    status: PaymentStatus.created,
    qyt: 1,
    price_unit: 9900,
    created_at: "2023-08-21T09:30:00Z",
    updated_at: "2023-08-21T09:30:00Z",
    product_type: 3,
    price_mark: "$99.00"
  },
  request: {
    payment_needed: true,
    url: "https://pay.example.com/checkout/a1b2c3d4",
    qr_code_preferred: true
  }
};
```

---

### 13. GiftCode
礼品码详细信息。（添加数据示例）
```json
// 已使用的礼品码示例
{
  "id": 8848,
  "created_at": "2023-08-01T00:00:00Z",
  "updated_at": "2023-08-15T14:30:00Z",
  "code": "GIFT-ABCD-EFGH",
  "used": true,
  "qyt": 5,
  "used_by": 1024,
  "product_props": {
    "type": 1,
    "share_link_id": "link_x9y8z7"
  },
  "edges": {
    "user": {
      "id": 1024,
      "name": "张三"
    }
  }
}
```

```
