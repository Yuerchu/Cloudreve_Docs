# Share API 文档

此文档描述 `share.ts` 文件中定义的接口及其用途。

---

## 接口列表

### 1. `ShareInfo`
**描述**：表示分享资源的详细信息。  
**属性**：

| 属性名             | 类型      | 可选  | 说明                                                                 |
|---------------------|-----------|-------|---------------------------------------------------------------------|
| `id`               | `string`  | 否    | 分享的唯一标识符                                                     |
| `name`             | `string`  | 是    | 分享名称                                                             |
| `source_type`      | `number`  | 是    | 资源类型                                                             |
| `remain_downloads` | `number`  | 是    | 剩余可下载次数                                                       |
| `visited`          | `number`  | 是    | 访问次数                                                             |
| `downloaded`       | `number`  | 是    | 下载次数                                                             |
| `permission`       | `string`  | 是    | 权限标识（如：`view`、`download`）                                   |
| `price`            | `number`  | 是    | 访问价格（可能需要付费解锁）                                         |
| `expires`          | `string`  | 是    | 过期时间（日期字符串）                                               |
| `created_at`       | `string`  | 是    | 创建时间（日期字符串）                                               |
| `unlocked`         | `boolean` | 否    | 是否已解锁（付费后为 `true`）                                        |
| `owner`            | `User`    | 否    | 分享所有者，类型来自 `./user.ts`                                      |
| `expired`          | `boolean` | 是    | 是否已过期                                                           |

---

### 2. `ListShareService`
**描述**：用于分页和排序分享列表的请求参数。  
**属性**：

| 属性名               | 类型      | 可选  | 说明                                                                 |
|-----------------------|-----------|-------|---------------------------------------------------------------------|
| `page_size`          | `number`  | 否    | 每页返回的分享数量                                                   |
| `order_by`           | `string`  | 是    | 排序字段（如：`created_at`）                                         |
| `order_direction`    | `string`  | 是    | 排序方向（如：`asc` 或 `desc`）                                      |
| `next_page_token`    | `string`  | 是    | 分页令牌，用于获取下一页数据                                         |

---

### 3. `ListShareResponse`
**描述**：分页查询分享列表的响应结果。  
**属性**：

| 属性名         | 类型                  | 可选  | 说明                                                                 |
|-----------------|-----------------------|-------|---------------------------------------------------------------------|
| `shares`       | `Share[]`            | 否    | 分享列表，`Share` 类型来自 `./explorer.ts`                           |
| `pagination`   | `PaginationResults`  | 否    | 分页信息，`PaginationResults` 类型来自 `./explorer.ts`               |

---

## 依赖类型说明
- `User`: 来自 `./user.ts`，表示用户信息。
- `Share`: 来自 `./explorer.ts`，表示基础分享信息。
- `PaginationResults`: 来自 `./explorer.ts`，包含分页结果的总数和分页状态。
