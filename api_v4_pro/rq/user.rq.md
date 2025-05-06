# TypeScript 接口与类型文档（请求示例）

此文档描述了 `user.ts` 文件中定义的所有接口、枚举、类型及相关API，并补充了典型HTTP请求示例。

---

## 目录
1. [核心用户模型](#核心用户模型)
2. [登录与认证](#登录与认证)
3. [用户权限与组](#用户权限与组)
4. [用户设置与安全](#用户设置与安全)
5. [存储与支付](#存储与支付)
6. [辅助类型](#辅助类型)
7. [枚举](#枚举)

---

## 登录与认证

### `UserLoginService` 示例
**接口用途**：用户登录  
**请求方法**：`POST /api/auth/login`  
**请求头**：`Content-Type: application/json`  
```json
{
  "email": "user@example.com",
  "password": "your_password_123",
  "otp": "654321"  // 可选，当启用两步验证时
}
```

---

### `TwoFALoginRequest` 示例
**接口用途**：两步验证登录  
**请求方法**：`POST /api/auth/2fa`  
```json
{
  "otp": "123456",
  "session_id": "abcd-efgh-1234-5678"
}
```

---

### `RefreshTokenRequest` 示例
**接口用途**：刷新访问令牌  
**请求方法**：`POST /api/auth/refresh`  
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 用户管理

### `SignUpService` 示例
**接口用途**：用户注册  
**请求方法**：`POST /api/auth/signup`  
```json
{
  "email": "newuser@example.com",
  "password": "secure_password_456",
  "language": "zh-CN"
}
```

---

### `SendResetEmailService` 示例
**接口用途**：发送密码重置邮件  
**请求方法**：`POST /api/auth/reset/request`  
```json
{
  "email": "user@example.com"
}
```

---

### `ResetPasswordService` 示例
**接口用途**：重置密码  
**请求方法**：`POST /api/auth/reset/confirm`  
```json
{
  "password": "new_password_789",
  "secret": "reset_token_from_email"
}
```

---

## 用户设置

### `PatchUserSetting` 示例
**接口用途**：更新用户设置  
**请求方法**：`PATCH /api/user/settings`  
```json
{
  "nick": "新昵称",
  "preferred_theme": "dark",
  "current_password": "old_password_123",  // 修改密码时需提供
  "new_password": "new_password_456"
}
```

---

## 支付与积分

### `ListPaymentService` 示例
**接口用途**：分页查询支付记录  
**请求方法**：`GET /api/payments?page_size=10&order_by=created_at`  
**响应示例**：  
```json
{
  "payments": [
    {
      "id": "pay_123",
      "amount": 99.99,
      "status": "completed"
    }
  ],
  "pagination": {
    "total": 5,
    "next_page_token": "page_2"
  }
}
```

---

### `GetCreditLogService` 示例
**接口用途**：查询积分变动记录  
**请求方法**：`GET /api/user/credit/logs?page_size=20`  
**响应示例**：  
```json
{
  "changes": [
    {
      "changed_at": "2023-10-01T12:00:00Z",
      "diff": 100,
      "reason": "活动奖励"
    }
  ],
  "pagination": {
    "total": 15,
    "next_page_token": "next_page_2"
  }
}
```

---

## 第三方登录

### `OpenIDSignInService` 示例
**接口用途**：绑定第三方登录  
**请求方法**：`POST /api/auth/openid/link`  
```json
{
  "provider": 0,  // OpenIDProvider.logto
  "hint": "user@logto.io"
}
```

---

### `OpenIDCallbackService` 示例
**接口用途**：第三方登录回调验证  
**请求方法**：`POST /api/auth/openid/callback`  
```json
{
  "provider_id": 1,  // OpenIDProvider.qq
  "code": "auth_code_from_qq",
  "session_id": "session_abcd1234"
}
```

---

> **说明**  
> 1. 示例中的端点（如 `/api/auth/login`）为假设路径，实际路径需根据后端实现调整。  
> 2. 部分字段（如 `Token` 中的 `access_token`）为示例值，实际值由服务端生成。  
> 3. 时间格式建议遵循 ISO 8601（如 `2023-10-01T12:00:00Z`）。
