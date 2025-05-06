# site.ts API 文档

## 枚举

### `CaptchaType`

验证码类型枚举。

| 值          | 说明                  |
|------------|-----------------------|
| `NORMAL`   | 普通验证码             |
| `RECAPTCHA`| Google reCAPTCHA      |
| `TCAPTCHA` | 腾讯验证码（已弃用）     |
| `TURNSTILE`| Cloudflare Turnstile   |

---

## 接口

### `SiteConfig`

站点配置接口，所有属性均为可选。

| 属性                        | 类型                                      | 说明                                                                 |
|-----------------------------|-------------------------------------------|----------------------------------------------------------------------|
| `instance_id?`              | `string`                                  | 实例唯一标识                                                         |
| `title?`                    | `string`                                  | 站点标题                                                             |
| `login_captcha?`            | `boolean`                                 | 登录时是否需要验证码                                                  |
| `reg_captcha?`              | `boolean`                                 | 注册时是否需要验证码                                                  |
| `forget_captcha?`           | `boolean`                                 | 忘记密码时是否需要验证码                                              |
| `themes?`                   | `string`                                  | 可用主题列表                                                         |
| `default_theme?`            | `string`                                  | 默认主题                                                             |
| `authn?`                    | `boolean`                                 | 是否启用 WebAuthn 认证                                               |
| `user?`                     | `User`                                    | 当前用户信息（从 `user.ts` 导入）                                     |
| `captcha_ReCaptchaKey?`     | `string`                                  | reCAPTCHA 密钥                                                       |
| `site_notice?`              | `string`                                  | 站点公告内容                                                         |
| `captcha_type?`             | `CaptchaType`                             | 验证码类型                                                           |
| `turnstile_site_id?`        | `string`                                  | Turnstile 站点 ID                                                    |
| `register_enabled?`         | `boolean`                                 | 是否允许用户注册                                                     |
| `qq_enabled?`               | `boolean`                                 | 是否启用 QQ 登录                                                     |
| `sso_enabled?`              | `boolean`                                 | 是否启用单点登录（SSO）                                              |
| `sso_display_name?`         | `string`                                  | SSO 显示名称                                                         |
| `logo?`                     | `string`                                  | 站点 Logo（暗色模式）                                                |
| `logo_light?`               | `string`                                  | 站点 Logo（亮色模式）                                                |
| `tos_url?`                  | `string`                                  | 服务条款 URL                                                        |
| `privacy_policy_url?`       | `string`                                  | 隐私政策 URL                                                        |
| `icons?`                    | `string`                                  | 自定义图标配置                                                       |
| `emoji_preset?`             | `string`                                  | 预设表情符号配置                                                     |
| `point_enabled?`            | `boolean`                                 | 是否启用积分系统                                                     |
| `share_point_gain_rate?`    | `number`                                  | 分享文件获得的积分比率                                               |
| `map_provider?`             | `string`                                  | 地图服务提供商                                                       |
| `google_map_tile_type?`     | `string`                                  | Google 地图瓦片类型                                                  |
| `file_viewers?`             | `ViewerGroup[]`                           | 文件预览器配置（从 `explorer.ts` 导入）                               |
| `max_batch_size?`           | `number`                                  | 最大批量操作文件数量                                                 |
| `app_promotion?`            | `boolean`                                 | 是否显示应用推广信息                                                 |
| `app_feedback?`             | `string`                                  | 应用反馈链接                                                        |
| `app_forum?`                | `string`                                  | 应用论坛链接                                                        |
| `payment?`                  | `PaymentSetting`                          | 支付配置（从 `vas.ts` 导入）                                         |
| `anonymous_purchase?`       | `boolean`                                 | 是否允许匿名购买                                                     |
| `point_price?`              | `number`                                  | 积分兑换比例（1 元 = X 积分）                                        |
| `shop_nav_enabled?`         | `boolean`                                 | 是否显示商店导航                                                     |
| `storage_products?`         | `StorageProduct[]`                        | 存储空间商品列表（从 `vas.ts` 导入）                                 |
| `group_skus?`               | `GroupSku[]`                              | 用户组商品列表（从 `vas.ts` 导入）                                   |
| `thumbnail_width?`          | `number`                                  | 缩略图宽度（像素）                                                   |
| `thumbnail_height?`         | `number`                                  | 缩略图高度（像素）                                                   |

---

### `CaptchaResponse`

验证码响应接口。

| 属性      | 类型       | 说明                   |
|-----------|------------|------------------------|
| `ticket`  | `string`   | 验证码验证票据         |
| `image`   | `string`   | 验证码图片（Base64 或 URL） |