# site.ts API 请求示例文档

## 枚举

### `CaptchaType`

验证码类型枚举。

| 值          | 说明                  |
|------------|-----------------------|
| `NORMAL`   | 普通验证码             |
| `RECAPTCHA`| Google reCAPTCHA      |
| `TCAPTCHA` | 腾讯验证码（已弃用）     |
| `TURNSTILE`| Cloudflare Turnstile   |

**使用示例：**
```typescript
// 设置验证码类型为 Turnstile
const captchaType: CaptchaType = CaptchaType.TURNSTILE;
```

---

## 接口

### `SiteConfig`

站点配置接口，所有属性均为可选。

（属性表格保持不变...）

**请求示例：**
```typescript
// 构建站点配置对象
const siteConfig: SiteConfig = {
  title: "Cloudreve Pro",
  login_captcha: true,
  register_enabled: false,
  captcha_type: CaptchaType.TURNSTILE,
  turnstile_site_id: "0x4AAAAAAABcdefGhijKLmno",
  logo: "/assets/logo-dark.png",
  thumbnail_width: 256,
  storage_products: [
    {
      sku_id: "storage_50gb",
      name: "50GB 存储空间",
      price: 9.9
    }
  ]
};
```

---

### `CaptchaResponse`

验证码响应接口。

（属性表格保持不变...）

**响应示例：**
```json
{
  "ticket": "t026b4f7d3c4c4d7e8b0a1c2d3e4f5g6h",
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

---

### 其他类型使用示例

**PaymentSetting 示例：**
```typescript
// 从 vas.ts 导入的类型
const paymentSetting: PaymentSetting = {
  wechat_pay: true,
  alipay: false,
  stripe_key: "pk_test_51H7..."
};
```

**文件预览器配置示例：**
```typescript
// 从 explorer.ts 导入的 ViewerGroup
const imageViewer: ViewerGroup = {
  type: "image",
  viewers: ["preview", "download"]
};
```

> 注意：示例中的部分类型（如 `User`、`StorageProduct`）需要从对应模块导入完整的类型定义后使用。