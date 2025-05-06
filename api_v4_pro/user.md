# TypeScript 接口与类型文档

此文档描述了 `user.ts` 文件中定义的所有接口、枚举、类型及相关API。

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

## 核心用户模型

### `User`
用户数据结构。
```typescript
interface User {
  id: string;                   // 用户ID
  email?: string;               // 邮箱（可选）
  nickname: string;             // 昵称
  status?: any;                 // 用户状态（类型未明确）
  avatar?: string;              // 头像URL（可选）
  created_at: any;              // 创建时间（类型未明确）
  preferred_theme?: string;     // 偏好主题（可选）
  credit?: number;              // 用户积分（整数）
  anonymous?: boolean;          // 是否匿名用户（可选）
  group?: Group;                // 所属用户组（可选）
  pined?: PinedFile[];          // 置顶文件列表（可选）
  language?: string;            // 语言偏好（可选）
}
```

---

## 登录与认证

### `UserLoginService`
用户登录请求参数。
```typescript
interface UserLoginService {
  email: string;      // 邮箱
  password: string;   // 密码
  otp?: string;       // 两步验证码（可选）
}
```

### `LoginResponse`
登录成功响应。
```typescript
interface LoginResponse {
  user: User;         // 用户信息
  token: Token;       // 令牌信息
}

interface Token {
  access_token: string;     // 访问令牌
  refresh_token: string;    // 刷新令牌
  access_expires: string;   // 访问令牌过期时间
  refresh_expires: string;  // 刷新令牌过期时间
}
```

### `TwoFALoginRequest`
两步验证登录请求。
```typescript
interface TwoFALoginRequest {
  otp: string;        // 两步验证码
  session_id: string; // 会话ID
}
```

---

## 用户权限与组

### `Group`
用户组信息。
```typescript
interface Group {
  id: string;                     // 组ID
  name: string;                   // 组名称
  permission?: string;            // 权限标识（可选）
  direct_link_batch_size?: number;// 直链批量操作限制（可选）
  trash_retention?: number;       // 回收站保留天数（可选）
}
```

### `GroupPermission`
用户组权限常量（数值映射）。
```typescript
const GroupPermission = {
  is_admin: 0,                    // 管理员权限
  is_anonymous: 1,                // 匿名用户权限
  share: 2,                       // 分享权限
  webdav: 3,                      // WebDAV权限
  // 其他权限略（详见源码）
};
```

---

## 用户设置与安全

### `UserSettings`
用户设置信息。
```typescript
interface UserSettings {
  group_expires?: string;          // 用户组过期时间（可选）
  open_id?: OpenID[];              // 绑定的第三方登录（可选）
  version_retention_enabled: boolean; // 是否启用文件版本保留
  passwordless: boolean;           // 是否启用无密码登录
  two_fa_enabled: boolean;         // 是否启用两步验证
  // 其他字段略（详见源码）
}
```

### `Passkey`
无密码登录密钥信息。
```typescript
interface Passkey {
  id: string;         // 密钥ID
  name: string;       // 密钥名称
  created_at: string; // 创建时间
  used_at: string;    // 最后使用时间
}
```

---

## 存储与支付

### `Capacity`
存储容量信息。
```typescript
interface Capacity {
  total: number;              // 总容量（单位未明确）
  used: number;               // 已使用容量
  storage_pack_total: number; // 存储包总容量
}
```

### `ListPaymentResponse`
支付记录响应。
```typescript
interface ListPaymentResponse {
  payments: Payment[];         // 支付记录列表
  pagination: PaginationResults; // 分页信息
}
```

---

## 辅助类型

### `PinedFile`
用户置顶文件。
```typescript
interface PinedFile {
  uri: string;    // 文件URI
  name?: string;  // 文件名（可选）
}
```

### `CreditChangeLog`
积分变动记录。
```typescript
interface CreditChangeLog {
  changed_at: string; // 变动时间
  diff: number;       // 变动数值
  reason: string;     // 原因描述
}
```

---

## 枚举

### `OpenIDProvider`
第三方登录提供方。
```typescript
enum OpenIDProvider {
  logto = 0,  // Logto 提供方
  qq = 1,     // QQ 提供方
}
```

---

> **说明**  
> - 部分字段类型标记为 `any`（如 `status`、`created_at`），实际类型需参考后端定义。  
> - 接口命名中带 `Service` 的多为请求参数模型（如 `SignUpService`）。  
> - 完整代码请参考原文件 `user.ts`。