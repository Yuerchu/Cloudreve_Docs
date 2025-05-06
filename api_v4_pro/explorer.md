# 本篇描述了 Cloudreve Pro Explorer API 中使用的关键接口定义、枚举类型和核心服务接口。

## 接口定义

### PaginationArgs
分页参数
**属性：**
- `page?: number` - 页码，默认为 1。
- `page_size?: number` - 每页数量，默认为服务器配置。
- `order_by?: string` - 排序字段。
- `order_direction?: string` - 排序方向，可选值为 `asc`（升序）或 `desc`（降序）。
- `next_page_token?: string` - 分页游标，用于下一页数据。

### ListFileService
文件列表服务参数 (继承自 `PaginationArgs`)
**扩展属性：**
- `uri: string` - 目标路径 URI，例如 `/` 表示根目录。

### FileResponse
文件/文件夹响应对象
**属性：**
- `type: number` - 类型，`0` 表示文件，`1` 表示文件夹。
- `id: string` - 唯一标识符。
- `name: string` - 名称。
- `size: number` - 文件大小，单位为字节。
- `path: string` - 完整路径。
- `metadata?: { [key: string]: string }` - 元数据键值对。
- `shared?: boolean` - 是否已共享。
- `folder_summary?: FolderSummary` - 文件夹摘要信息（仅当 `type` 为 `1` 时存在）。
- `extended_info?: ExtendedInfo` - 扩展信息。

### FolderSummary
文件夹摘要信息
**属性：**
- `size: number` - 总大小（包含子文件和子文件夹），单位为字节。
- `files: number` - 文件数量。
- `folders: number` - 子文件夹数量。
- `completed: boolean` - 是否已完成统计。
- `calculated_at: string` - 统计时间。

### StoragePolicy
存储策略配置
**属性：**
- `id: string` - 策略 ID。
- `name: string` - 策略名称。
- `type: PolicyType` - 存储类型。
- `max_size: number` - 最大文件大小限制，单位为字节。

### ListResponse
文件列表响应
**属性：**
- `files: FileResponse[]` - 文件列表数组。
- `pagination: PaginationResults` - 分页信息对象。
- `props: NavigatorProps` - 导航器属性。
- `parent?: FileResponse` - 父目录信息（如果不在根目录）。

## 枚举

### PolicyType
存储策略类型
```ts
enum PolicyType {
  local = "local",
  remote = "remote",
  oss = "oss",
  qiniu = "qiniu",
  onedrive = "onedrive",
  cos = "cos",
  upyun = "upyun",
  s3 = "s3",
  obs = "obs",
}
```

### FileType
文件类型标识
```ts
export const FileType = {
  file: 0,    // 文件
  folder: 1,  // 文件夹
};
```

## 常量对象

### Metadata
元数据键定义
```ts
export const Metadata = {
  share_redirect: "sys:shared_redirect", // 共享重定向标识
  restore_uri: "sys:restore_uri",      // 恢复路径
  gps_lng: "exif:longitude",          // GPS经度
  music_title: "music:title",          // 音乐标题
  // 其他键详见源码
};
```

### NavigatorCapability
导航器功能权限
```ts
export const NavigatorCapability = {
  create_file: 0,   // 创建文件
  rename_file: 1,   // 重命名文件
  delete_file: 14,  // 删除文件
  // 其他权限详见源码
};
```

## 核心服务接口

### DeleteFileService
删除文件服务参数
**属性：**
- `uris: string[]` - 要删除的文件或文件夹 URI 列表。
- `unlink?: boolean` - 是否解除与存储策略的关联（仅适用于文件）。
- `skip_soft_delete?: boolean` - 是否跳过软删除，直接物理删除。

**请求示例 (假设使用 JSON 格式发送请求):**
```json
{
  "uris": ["/path/to/file.txt", "/path/to/folder"],
  "unlink": false,
  "skip_soft_delete": false
}
```

### ShareCreateService
创建共享服务参数
**属性：**
- `uri: string` - 要共享的目标 URI。
- `permissions: PermissionSettingReq` - 共享权限设置。
- `expire?: number` - 共享过期时间，单位为秒。不设置或为 `0` 表示永不过期。

**请求示例 (假设使用 JSON 格式发送请求):**
```json
{
  "uri": "/path/to/shared_folder",
  "permissions": {
    "group_explicit": {
      "group_id_1": "read",
      "group_id_2": "readwrite"
    },
    "user_explicit": {
      "user_id_3": "download"
    }
  },
  "expire": 3600 // 1小时后过期
}
```

### UploadCredential
上传凭证
**属性：**
- `session_id: string` - 上传会话 ID。
- `upload_urls: string[]` - 分块上传地址列表。
- `callback: string` - 上传完成后的回调地址。
- `storage_policy?: StoragePolicy` - 关联的存储策略信息。

## 其他关键类型

### PermissionSettingReq
权限配置请求
**属性：**
- `group_explicit?: { [key: string]: string }` - 用户组显式权限设置，键为用户组 ID，值为权限字符串 (例如: "read", "write", "readwrite", "download")。
- `user_explicit?: { [key: string]: string }` - 用户显式权限设置，键为用户 ID，值为权限字符串。

### FileActivity
文件活动日志
**属性：**
- `content: LogEntry` - 日志内容对象。
- `user?: User` - 执行操作的用户信息。
- `version_id?: string` - 文件版本 ID（如果适用）。

### Viewer
文件查看器配置
**属性：**
- `id: string` - 查看器 ID。
- `type: string` - 查看器类型，例如 `builtin`、`wopi` 或 `custom`。
- `exts: string[]` - 支持的文件扩展名列表。
- `wopi_actions?: { [key: string]: object }` - WOPI 操作配置（如果 `type` 为 `wopi`）。