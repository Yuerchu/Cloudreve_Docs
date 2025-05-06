```markdown
# Dashboard API 文档

## 目录
- [系统信息](#系统信息)
- [用户管理](#用户管理)
- [组管理](#组管理)
- [存储策略](#存储策略)
- [节点管理](#节点管理)
- [任务管理](#任务管理)
- [文件与实体](#文件与实体)
- [日志与审计](#日志与审计)
- [支付与订单](#支付与订单)
- [其他类型](#其他类型)

---

## 系统信息

### `HomepageSummary`
首页概要信息

```typescript
interface HomepageSummary {
  metrics_summary?: MetricsSummary; // 系统指标摘要
  site_urls: string[];             // 站点URL列表
  license: License;                // 许可证信息
  version: Version;                // 版本信息
}
```

### `MetricsSummary`
系统指标统计

```typescript
interface MetricsSummary {
  dates: string[];         // 日期序列
  files: number[];         // 每日文件数
  users: number[];         // 每日用户数
  shares: number[];        // 每日分享数
  file_total: number;      // 总文件数
  user_total: number;      // 总用户数
  share_total: number;     // 总分享数
  entities_total: number;  // 总实体数
  generated_at: string;    // 生成时间
}
```

### `License`
许可证信息

```typescript
interface License {
  expired_at: string;   // 过期时间
  signed_at: string;    // 签发时间
  root_domains: string[]; // 根域名列表
  domains: string[];      // 域名列表
  vol_domains: string[]; // 容量域名列表
}
```

## 用户管理

### `User`
用户实体

```typescript
interface User extends CommonMixin {
  email: string;                // 用户邮箱
  nick: string;                 // 昵称
  password?: string;            // 密码（仅创建时）
  settings?: UserSetting;       // 用户设置
  status?: UserStatus;          // 用户状态
  storage?: number;             // 存储空间
  edges: {
    group?: GroupEnt;           // 所属用户组
    storage_policy?: StoragePolicy; // 存储策略
  };
  // ...其他字段
}
```

### `UserStatus`
用户状态枚举

```typescript
enum UserStatus {
  active = "active",          // 活跃
  inactive = "inactive",      // 未激活
  manual_banned = "manual_banned", // 手动封禁
  sys_banned = "sys_banned"   // 系统封禁
}
```

### `ListUserResponse`
用户列表响应

```typescript
interface ListUserResponse {
  users: User[];                // 用户列表
  pagination: PaginationResults; // 分页信息
}
```

## 组管理

### `GroupEnt`
用户组实体

```typescript
interface GroupEnt extends CommonMixin {
  name: string;                 // 组名称
  max_storage?: number;         // 最大存储限制
  speed_limit?: number;         // 速度限制
  permissions?: string;         // 权限字符串
  edges: {
    storage_policies: StoragePolicy[]; // 关联存储策略
  };
  // ...其他字段
}
```

### `AdminListGroupResponse`
组列表响应

```typescript
interface AdminListGroupResponse {
  groups: GroupEnt[];           // 组列表
  pagination: PaginationResults; // 分页信息
}
```

## 存储策略

### `StoragePolicy`
存储策略实体

```typescript
interface StoragePolicy extends CommonMixin {
  name: string;                 // 策略名称
  type: PolicyType;             // 策略类型
  server?: string;              // 存储服务器地址
  bucket_name?: string;         // 存储桶名称
  secret_key?: string;          // 密钥
  edges: {
    users?: User[];             // 关联用户
    groups?: GroupEnt[];        // 关联用户组
  };
}
```

### `ListStoragePolicyResponse`
存储策略列表响应

```typescript
interface ListStoragePolicyResponse {
  policies: StoragePolicy[];    // 策略列表
  pagination: PaginationResults; // 分页信息
}
```

## 节点管理

### `Node`
节点实体

```typescript
interface Node extends CommonMixin {
  name?: string;                // 节点名称
  type?: NodeType;              // 节点类型（master/slave）
  server?: string;              // 节点服务器地址
  settings?: NodeSetting;       // 节点配置
}
```

### `NodeType`
节点类型枚举

```typescript
enum NodeType {
  master = "master",   // 主节点
  slave = "slave"      // 从节点
}
```

## 任务管理

### `Task`
后台任务实体

```typescript
interface Task extends CommonMixin {
  type?: string;                // 任务类型
  status?: TaskStatus;          // 任务状态
  edges: {
    user?: User;                // 关联用户
  };
}
```

### `TaskStatus`
任务状态枚举（来自 `workflow.ts`）

```typescript
enum TaskStatus {
  Pending = "pending",
  Running = "running",
  Completed = "completed",
  Failed = "failed"
}
```

## 文件与实体

### `File`
文件实体

```typescript
interface File extends CommonMixin {
  name?: string;                // 文件名
  size?: number;                // 文件大小
  edges: {
    owner?: User;               // 所有者
    entities?: Entity[];        // 关联实体
  };
}
```

### `Entity`
存储实体

```typescript
interface Entity extends CommonMixin {
  source?: string;              // 实体源地址
  size?: number;                // 实体大小
  edges: {
    storage_policy?: StoragePolicy; // 关联存储策略
  };
}
```

## 日志与审计

### `AuditLog`
审计日志

```typescript
interface AuditLog extends CommonMixin {
  ip?: string;                  // 操作者IP
  content?: LogEntry;           // 日志内容详情
  edges: {
    user?: User;                // 关联用户
    file?: File;                // 关联文件
  };
}
```

## 支付与订单

### `Payment`
支付订单

```typescript
interface Payment extends CommonMixin {
  trade_no?: string;            // 交易号
  status?: PaymentStatus;       // 支付状态
  edges: {
    user?: User;                // 关联用户
  };
}
```

## 其他类型

### `CommonMixin`
通用字段混合

```typescript
interface CommonMixin {
  id: number;                   // 唯一ID
  created_at?: string;          // 创建时间
  updated_at?: string;          // 更新时间
  deleted_at?: string;          // 删除时间（软删除）
}
```

### `PaginationResults`
分页结果

```typescript
interface PaginationResults {
  total: number;                // 总记录数
  page: number;                 // 当前页码
  page_size: number;            // 每页数量
}
```