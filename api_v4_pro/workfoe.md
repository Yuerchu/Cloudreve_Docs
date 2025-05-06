# workflow.ts API 文档

## 接口

### `ArchiveWorkflowService`
用于归档工作流的配置。

| 属性                | 类型       | 可选  | 描述                           |
|---------------------|------------|-------|--------------------------------|
| `src`               | `string[]` | 否    | 源文件/路径列表                |
| `dst`               | `string`   | 否    | 目标路径                       |
| `preferred_node_id` | `string`   | 是    | 优先使用的节点ID               |
| `encoding`          | `string`   | 是    | 编码方式                       |

---

### `TaskListResponse`
任务列表响应结构。

| 属性         | 类型                  | 描述               |
|--------------|-----------------------|--------------------|
| `tasks`      | `TaskResponse[]`      | 任务列表           |
| `pagination` | `PaginationResults`   | 分页信息           |

---

### `TaskResponse`
单个任务的详细信息。

| 属性               | 类型                   | 可选  | 描述                           |
|--------------------|------------------------|-------|--------------------------------|
| `created_at`       | `string`               | 否    | 任务创建时间                   |
| `updated_at`       | `string`               | 否    | 任务更新时间                   |
| `id`               | `string`               | 否    | 任务唯一ID                     |
| `status`           | `string`               | 否    | 任务状态（参考 `TaskStatus`）  |
| `type`             | `string`               | 否    | 任务类型（参考 `TaskType`）    |
| `node`             | `NodeSummary`          | 是    | 关联节点信息                   |
| `summary`          | `TaskSummary`          | 是    | 任务摘要                       |
| `error`            | `string`               | 是    | 错误信息                       |
| `error_history`    | `string[]`             | 是    | 历史错误记录                   |
| `duration`         | `number`               | 是    | 任务持续时长（秒）             |
| `resume_time`      | `number`               | 是    | 恢复时间戳                     |
| `retry_count`      | `number`               | 是    | 重试次数                       |

---

### `TaskSummary`
任务摘要信息。

| 属性      | 类型                     | 可选  | 描述                           |
|-----------|--------------------------|-------|--------------------------------|
| `phase`   | `string`                 | 是    | 任务阶段（如“传输中”）         |
| `props`   | `TaskSummaryProps`       | 否    | 任务属性                       |

#### `TaskSummaryProps`
| 属性               | 类型                     | 可选  | 描述                           |
|--------------------|--------------------------|-------|--------------------------------|
| `src`              | `string`                 | 是    | 源路径                         |
| `src_str`          | `string`                 | 是    | 源路径字符串                   |
| `dst`              | `string`                 | 是    | 目标路径                       |
| `src_multiple`     | `string[]`               | 是    | 多源路径列表                   |
| `dst_policy_id`    | `string`                 | 是    | 目标存储策略ID                 |
| `failed`           | `number`                 | 是    | 失败次数                       |
| `download`         | `DownloadTaskStatus`     | 是    | 下载任务状态                   |

---

### `DownloadTaskStatus`
下载任务状态详情。

| 属性               | 类型                   | 描述                           |
|--------------------|------------------------|--------------------------------|
| `name`             | `string`               | 任务名称                       |
| `state`            | `DownloadTaskState`    | 下载状态（参考枚举）           |
| `total`            | `number`               | 总大小（字节）                 |
| `downloaded`       | `number`               | 已下载大小（字节）             |
| `download_speed`   | `number`               | 下载速度（字节/秒）            |
| `upload_speed`     | `number`               | 上传速度（字节/秒）            |
| `uploaded`         | `number`               | 已上传大小（字节）             |
| `files`            | `DownloadTaskFile[]`   | 文件列表                       |
| `hash`             | `string`               | 文件哈希值                     |
| `pieces`           | `string`               | 分片信息                       |
| `num_pieces`       | `number`               | 总分片数                       |

---

### `DownloadTaskFile`
下载任务中的文件信息。

| 属性         | 类型      | 描述                           |
|--------------|-----------|--------------------------------|
| `index`      | `number`  | 文件索引                       |
| `name`       | `string`  | 文件名                         |
| `size`       | `number`  | 文件大小（字节）               |
| `progress`   | `number`  | 下载进度百分比                 |
| `selected`   | `boolean` | 是否被选中下载                 |

---

### `NodeSummary`
节点摘要信息。

| 属性           | 类型          | 描述                           |
|----------------|---------------|--------------------------------|
| `id`           | `string`      | 节点ID                         |
| `name`         | `string`      | 节点名称                       |
| `type`         | `NodeTypes`   | 节点类型（参考枚举）           |
| `capabilities` | `string`      | 节点支持的能力（位掩码）       |

---

### `RelocateWorkflowService`
文件迁移工作流配置。

| 属性             | 类型       | 描述                 |
|------------------|------------|----------------------|
| `src`            | `string[]` | 源路径列表           |
| `dst_policy_id`  | `string`   | 目标存储策略ID       |

---

### `DownloadWorkflowService`
下载工作流配置。

| 属性                | 类型       | 可选  | 描述                           |
|---------------------|------------|-------|--------------------------------|
| `src`               | `string[]` | 是    | 源路径列表                     |
| `src_file`          | `string`   | 是    | 源文件路径（单文件）           |
| `dst`               | `string`   | 否    | 目标路径                       |
| `preferred_node_id` | `string`   | 是    | 优先使用的节点ID               |

---

### `ListTaskService`
任务列表查询参数。

| 属性               | 类型                 | 可选  | 描述                           |
|--------------------|----------------------|-------|--------------------------------|
| `page_size`        | `number`             | 否    | 每页任务数量                   |
| `category`         | `ListTaskCategory`   | 否    | 任务分类（参考枚举）           |
| `next_page_token`  | `string`             | 是    | 下一页的令牌                   |

---

### `SetFileToDownloadArgs`
设置下载文件的参数。

| 属性         | 类型      | 描述                           |
|--------------|-----------|--------------------------------|
| `index`      | `number`  | 文件索引                       |
| `download`   | `boolean` | 是否下载该文件                 |

---

### `SetDownloadFilesService`
批量设置下载文件。

| 属性      | 类型                     | 描述                   |
|-----------|--------------------------|------------------------|
| `files`   | `SetFileToDownloadArgs[]`| 文件配置列表           |

---

### `TaskProgress`
任务进度信息。

| 属性           | 类型       | 描述                           |
|----------------|------------|--------------------------------|
| `total`        | `number`   | 总任务数                       |
| `current`      | `number`   | 当前完成数                     |
| `identifier`   | `string`   | 任务唯一标识符                 |

---

### `TaskProgresses`
任务进度集合（键值对）。

```typescript
{
  [key: string]: TaskProgress;
}
```

---

## 枚举

### `DownloadTaskState`
下载任务状态枚举。

| 值             | 描述               |
|----------------|--------------------|
| `seeding`      | 做种中             |
| `downloading`  | 下载中             |
| `error`        | 错误               |
| `completed`    | 完成               |
| `unknown`      | 未知状态           |

---

### `NodeTypes`
节点类型枚举。

| 值        | 描述       |
|-----------|------------|
| `master`  | 主节点     |
| `slave`   | 从节点     |

---

### `ListTaskCategory`
任务分类枚举。

| 值              | 描述               |
|-----------------|--------------------|
| `general`       | 通用任务           |
| `downloading`   | 下载中任务         |
| `downloaded`    | 已下载任务         |

---

### `TaskType`
任务类型枚举。

| 值                          | 描述                   |
|-----------------------------|------------------------|
| `create_archive`            | 创建压缩包             |
| `extract_archive`           | 解压压缩包             |
| `relocate`                  | 文件迁移               |
| `remote_download`           | 远程下载               |
| `media_metadata`            | 媒体元数据处理         |
| `entity_recycle_routine`    | 实体回收例行任务       |
| `explicit_entity_recycle`   | 显式实体回收           |
| `upload_sentinel_check`     | 上传哨兵检查           |

---

### `TaskStatus`
任务状态枚举。

| 值             | 描述               |
|----------------|--------------------|
| `queued`       | 排队中             |
| `processing`   | 处理中             |
| `suspending`   | 暂停中             |
| `error`        | 错误               |
| `canceled`     | 已取消             |
| `completed`    | 已完成             |

---

## 常量

### `NodeCapability`
节点能力位掩码常量。

| 常量                  | 值  | 描述               |
|-----------------------|-----|--------------------|
| `none`                | 0   | 无能力             |
| `create_archive`      | 1   | 支持创建压缩包     |
| `extract_archive`     | 2   | 支持解压压缩包     |
| `remote_download`     | 3   | 支持远程下载       |

---

**说明**  
- 所有接口均使用 TypeScript 定义，具体实现需参考业务逻辑。  
- 可选字段（`?`）可能在部分场景下为空。  
- 枚举值与实际业务状态需严格对应。