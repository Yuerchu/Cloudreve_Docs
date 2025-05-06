# workflow.ts API 文档（补充请求示例）

---

## 接口请求示例

### `ArchiveWorkflowService`
**场景**：创建归档任务  
```typescript
const archiveRequest: ArchiveWorkflowService = {
  src: ["/user/docs/report.pdf", "/user/images/"],
  dst: "/backup/2023-archive/",
  preferred_node_id: "node-123",
  encoding: "zip",
};
```

---

### `RelocateWorkflowService`
**场景**：迁移文件到指定存储策略  
```typescript
const relocateRequest: RelocateWorkflowService = {
  src: ["/data/logs/2023-10.log", "/data/temp/"],
  dst_policy_id: "policy-storage-aws",
};
```

---

### `DownloadWorkflowService`
**场景1**：从多个源路径下载文件  
```typescript
const downloadMultiSource: DownloadWorkflowService = {
  src: ["/cloud/files/doc1.txt", "/cloud/files/doc2.txt"],
  dst: "/local/downloads/",
  preferred_node_id: "node-download-456",
};

// 场景2：从单个文件下载
const downloadSingleFile: DownloadWorkflowService = {
  src_file: "/cloud/videos/sample.mp4",
  dst: "/local/videos/",
};
```

---

### `ListTaskService`
**场景**：分页查询“下载中”任务  
```typescript
const listTasksRequest: ListTaskService = {
  page_size: 20,
  category: ListTaskCategory.downloading,
  next_page_token: "eyJwYWdlIjozfQ==", // 可选，用于翻页
};
```

---

### `SetDownloadFilesService`
**场景**：批量设置下载文件的选择状态  
```typescript
const setFilesRequest: SetDownloadFilesService = {
  files: [
    { index: 0, download: true },  // 下载第一个文件
    { index: 1, download: false }, // 跳过第二个文件
    { index: 2, download: true },
  ],
};
```

---

### `TaskResponse` 示例
**场景**：获取任务详情的响应  
```typescript
const taskResponse: TaskResponse = {
  created_at: "2023-10-05T08:30:00Z",
  updated_at: "2023-10-05T08:45:00Z",
  id: "task-789",
  status: TaskStatus.processing,
  type: TaskType.remote_download,
  node: {
    id: "node-123",
    name: "EU-West-Node",
    type: NodeTypes.slave,
    capabilities: "3", // 支持远程下载和创建压缩包（1 + 2）
  },
  summary: {
    phase: "downloading",
    props: {
      src: "/cloud/files/large-video.mp4",
      download: {
        name: "large-video.mp4",
        state: DownloadTaskState.downloading,
        total: 1024 * 1024 * 1024, // 1GB
        downloaded: 512 * 1024 * 1024, // 512MB
        download_speed: 10 * 1024 * 1024, // 10MB/s
        upload_speed: 0,
        uploaded: 0,
        files: [
          {
            index: 0,
            name: "large-video.mp4",
            size: 1024 * 1024 * 1024,
            progress: 50,
            selected: true,
          },
        ],
      },
    },
  },
  duration: 900, // 15分钟
  retry_count: 0,
};
```

---

### `TaskProgresses` 示例
**场景**：批量查询任务进度  
```typescript
const progresses: TaskProgresses = {
  "task-123": {
    total: 100,
    current: 75,
    identifier: "task-123",
  },
  "task-456": {
    total: 200,
    current: 200,
    identifier: "task-456",
  },
};
```

---

## 枚举使用示例

### `TaskType` 使用
```typescript
const createArchiveTask: TaskResponse = {
  // ...其他字段
  type: TaskType.create_archive,
};

const remoteDownloadTask: TaskResponse = {
  // ...其他字段
  type: TaskType.remote_download,
};
```

---

### `TaskStatus` 使用
```typescript
const completedTask: TaskResponse = {
  // ...其他字段
  status: TaskStatus.completed,
};

const errorTask: TaskResponse = {
  // ...其他字段
  status: TaskStatus.error,
  error: "Connection timeout",
};
```

---

## 说明
- 所有示例基于 TypeScript 接口定义，实际请求需转换为 JSON 格式（如通过 `JSON.stringify()`）。
- 可选字段可根据业务场景省略（如未指定 `preferred_node_id` 时由系统自动分配节点）。
- 枚举值需严格使用定义的常量（如 `TaskStatus.processing` 而非字符串 `"processing"`）。