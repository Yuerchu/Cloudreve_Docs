```markdown
# Share API 文档（补充请求示例）

---

## 接口请求示例

### 1. 获取单个分享详情（`ShareInfo`）
**请求**  
```http
GET /api/shares/{share_id}
```

**成功响应示例**  
```json
{
  "id": "sh_123456",
  "name": "年度报告.pdf",
  "source_type": 1,
  "remain_downloads": 5,
  "visited": 20,
  "downloaded": 15,
  "permission": "download",
  "price": 0,
  "expires": "2024-12-31T23:59:59Z",
  "created_at": "2023-01-01T10:00:00Z",
  "unlocked": true,
  "owner": {
    "id": "u_987654",
    "name": "张三",
    "email": "zhangsan@example.com"
  },
  "expired": false
}
```

---

### 2. 分页获取分享列表（`ListShareService`）
**请求**  
```http
GET /api/shares?page_size=10&order_by=created_at&order_direction=desc&next_page_token=abc123
```

**请求参数说明**  
- `page_size`: 每页数量（必填）
- `order_by`: 排序字段（可选，如 `created_at`）
- `order_direction`: 排序方向（可选，`asc` 或 `desc`）
- `next_page_token`: 分页令牌（可选，用于下一页）

**成功响应示例**  
```json
{
  "shares": [
    {
      "id": "sh_123456",
      "name": "项目文档.zip",
      "created_at": "2023-05-01T12:00:00Z",
      "expired": false,
      "permission": "view"
    },
    {
      "id": "sh_789012",
      "name": "设计稿.psd",
      "created_at": "2023-04-30T09:30:00Z",
      "expired": true,
      "permission": "download"
    }
  ],
  "pagination": {
    "total": 50,
    "page_size": 10,
    "next_page_token": "def456",
    "has_more": true
  }
}
```

---

### 3. 创建分享
**请求**  
```http
POST /api/shares
```

**请求体示例**  
```json
{
  "name": "会议记录.docx",
  "source_type": 2,
  "expires": "2024-06-30T23:59:59Z",
  "permission": "view",
  "price": 10
}
```

**成功响应示例**  
```json
{
  "id": "sh_345678",
  "created_at": "2023-10-01T15:00:00Z",
  "expired": false,
  "unlocked": false
}
```

---

## 说明
1. **字段一致性**：响应字段与 `ShareInfo` 和 `ListShareResponse` 定义严格匹配。
2. **依赖类型**：
   - `User` 类型假设包含 `id`、`name`、`email` 字段。
   - `PaginationResults` 包含分页元数据（如 `total`、`has_more`）。
3. **时间格式**：日期字段使用 ISO 8601 格式（如 `2023-01-01T10:00:00Z`）。
```