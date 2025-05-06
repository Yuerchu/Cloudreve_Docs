```markdown
# setting.ts API 文档

## 类型导入
```typescript
import { PaginationResults } from "./explorer.ts";
```

---

## 接口说明

### 1. ListDavAccountsService
分页查询 Dav 账户的请求参数

**属性：**
| 属性名称          | 类型     | 必填 | 说明                |
|--------------------|----------|------|---------------------|
| `page_size`        | number   | 是   | 每页条目数量        |
| `next_page_token`  | string   | 否   | 下一页的令牌（可选）|

---

### 2. DavAccount
Dav 账户的实体定义

**属性：**
| 属性名称      | 类型     | 必填 | 说明                |
|---------------|----------|------|---------------------|
| `id`          | string   | 是   | 账户唯一 ID         |
| `created_at`  | string   | 是   | 创建时间            |
| `name`        | string   | 是   | 账户名称            |
| `uri`         | string   | 是   | Dav 服务地址        |
| `password`    | string   | 是   | 账户密码            |
| `options`     | string   | 否   | 附加选项（可选）    |

---

### 3. ListDavAccountsResponse
分页查询 Dav 账户的响应结果

**属性：**
| 属性名称       | 类型                          | 必填 | 说明                |
|----------------|-------------------------------|------|---------------------|
| `accounts`     | DavAccount[]                  | 是   | Dav 账户列表        |
| `pagination`   | PaginationResults             | 否   | 分页信息（可选）    |

---

### 4. CreateDavAccountService
创建 Dav 账户的请求参数

**属性：**
| 属性名称      | 类型     | 必填 | 说明                |
|---------------|----------|------|---------------------|
| `name`        | string   | 是   | 账户名称            |
| `uri`         | string   | 是   | Dav 服务地址        |
| `readonly`    | boolean  | 否   | 是否只读（可选）    |
| `proxy`       | boolean  | 否   | 是否启用代理（可选）|

---

## 常量说明

### DavAccountOption
Dav 账户选项的枚举值

**定义：**
```typescript
export const DavAccountOption = {
  readonly: 0,
  proxy: 1,
};
```

**可选值：**
- `readonly`: `0`（只读模式）
- `proxy`: `1`（代理模式）
```