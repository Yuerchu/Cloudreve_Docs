# 概览

`api.ts` 文件定义了与后端交互的所有 API 接口，涉及管理员接口、用户接口、文件操作、分享、支付等功能。每个接口都封装为一个函数，使用 `send` 方法发送 HTTP 请求。下文将逐一列出每个接口的名称、请求方法和路径、请求参数、响应类型以及简要说明和请求示例。

## 接口列表

### `deleteStoragePolicy (DELETE /admin/policy/{id})`

* **请求方法**: `DELETE`
* **路径**: `/admin/policy/{id}`
* **请求参数**:
    * `id` (路径参数, `number`)
* **响应**: `void`
* **说明**: 删除指定 ID 的存储策略。
* **请求示例**:
  ```
  DELETE /admin/policy/123
  ```

### `sendSinUp (POST /user)`

* **请求方法**: `POST`
* **路径**: `/user`
* **请求参数**:
    * **请求体 (body)**: `req` (`SignUpService`, 用户注册请求数据)
* **响应**: `User` (用户对象)
* **说明**: 用户注册。
* **请求示例**:
  ```json
  POST /user
  Content-Type: application/json

  {
    "username": "newuser",
    "password": "securepassword",
    "email": "newuser@example.com"
  }
  ```

### `sendPreparePasskeyLogin (PUT /session/authn)`

* **请求方法**: `PUT`
* **路径**: `/session/authn`
* **请求参数**: 无
* **响应**: `PreparePasskeyLoginResponse` (准备登录的响应数据)
* **说明**: 获取准备进行密码钥匙（passkey）登录的初始化数据。
* **请求示例**:
  ```
  PUT /session/authn
  ```

### `getShares (GET /share)`

* **请求方法**: `GET`
* **路径**: `/share`
* **请求参数**:
    * **查询参数 (query)**: `req` (`ListShareService`, 分享列表请求参数)
* **响应**: `ListShareResponse` (分享列表响应)
* **说明**: 获取分享列表。
* **请求示例**:
  ```
  GET /share?page=1&pageSize=10&sortBy=createdAt&order=desc
  ```

### `get2FAInitSecret (GET /user/setting/2fa)`

* **请求方法**: `GET`
* **路径**: `/user/setting/2fa`
* **请求参数**: 无
* **响应**: `string` (2FA 初始化密钥)
* **说明**: 获取 2FA（双因子认证）的初始化密钥。
* **请求示例**:
  ```
  GET /user/setting/2fa
  ```

### `deleteVersion (DELETE /file/version)`

* **请求方法**: `DELETE`
* **路径**: `/file/version`
* **请求参数**:
    * **请求体 (body)**: `req` (`VersionControlService`, 版本控制删除请求)
* **响应**: `void`
* **说明**: 删除文件的指定版本（需要提供版本控制请求数据）。
* **请求示例**:
  ```json
  DELETE /file/version
  Content-Type: application/json

  {
    "uri": "/path/to/file",
    "versionId": "v1.0.1"
  }
  ```

### `getShareList (POST /admin/share)`

* **请求方法**: `POST`
* **路径**: `/admin/share`
* **请求参数**:
    * **请求体 (body)**: `args` (`AdminListService`, 分页查询参数)
* **响应**: `AdminListShareResponse` (管理员视角下分享列表响应)
* **说明**: 管理员获取分享列表（通过 POST 提交查询参数）。
* **请求示例**:
  ```json
  POST /admin/share
  Content-Type: application/json

  {
    "page": 1,
    "pageSize": 20,
    "filter": {
      "creatorId": 1
    }
  }
  ```

### `sendUpdateFile (PUT /file/content)`

* **请求方法**: `PUT`
* **路径**: `/file/content`
* **请求参数**:
    * **查询参数 (query)**: `req` (`FileUpdateService`, 更新文件的查询参数，可能包含文件 URI 等)
    * **请求体 (body)**: `data` (`any`, 文件内容数据)
* **响应**: `FileResponse` (文件响应数据)
* **说明**: 更新文件内容（上传新文件流）。该接口上传二进制流，`data` 是文件内容，`req` 中携带文件定位信息。
* **请求示例**:
  ```
  PUT /file/content?uri=/path/to/file
  Content-Type: application/octet-stream

  (文件二进制数据)
  ```

### `sendFinishPasskeyRegistration (POST /user/authn)`

* **请求方法**: `POST`
* **路径**: `/user/authn`
* **请求参数**:
    * **请求体 (body)**: `req` (`FinishPasskeyRegistrationService`, 完成密码钥匙注册所需数据)
* **响应**: `Passkey` (密码钥匙信息)
* **说明**: 完成密码钥匙注册，将客户端返回的数据提交到服务端。
* **请求示例**:
  ```json
  POST /user/authn
  Content-Type: application/json

  {
    "credential": {
      "id": "...",
      "rawId": "...",
      "response": {
        "attestationObject": "...",
        "clientDataJSON": "..."
      },
      "type": "public-key"
    }
  }
  ```

### `getFileEntityUrl (POST /file/url)`

* **请求方法**: `POST`
* **路径**: `/file/url`
* **请求参数**:
    * **请求体 (body)**: `req` (`FileURLService`, 文件 URL 请求参数，可能包含文件 URIs 列表)
* **响应**: `FileURLResponse` (包含文件直链或下载链接的响应)
* **说明**: 获取文件的实体 URL/下载链接。根据 `req.uris` 生成相应的 URL 列表。
* **请求示例**:
  ```json
  POST /file/url
  Content-Type: application/json

  {
    "uris": ["/path/to/file1", "/path/to/file2"]
  }
  ```

### `sendUploadAvatar (PUT /user/setting/avatar)`

* **请求方法**: `PUT`
* **路径**: `/user/setting/avatar`
* **请求参数**:
    * **请求体 (body)**: `avatar` (`Blob | undefined`, 用户头像二进制数据)
    * **可选请求头 (headers)**: `contentType` (`string`, 可选，图片的 Content-Type，例如 `image/jpeg`)
* **响应**: (未指定具体类型)
* **说明**: 上传或更新用户头像。`avatar` 是头像文件的二进制，`contentType` 指定文件类型。
* **请求示例**:
  ```
  PUT /user/setting/avatar
  Content-Type: image/jpeg

  (头像文件的二进制数据)
  ```

### `sendSetPermission (POST /file/permission)`

* **请求方法**: `POST`
* **路径**: `/file/permission`
* **请求参数**:
    * **请求体 (body)**: `req` (`SetPermissionService`, 设置文件权限的参数，包含文件 URI 列表和权限设定)
* **响应**: `void`
* **说明**: 设置文件的权限。根据 `req.uris` 列表对文件进行权限变更。
* **请求示例**:
  ```json
  POST /file/permission
  Content-Type: application/json

  {
    "uris": ["/path/to/file"],
    "permissions": [
      {
        "entityId": 2,
        "entityType": "user",
        "read": true,
        "write": false
      }
    ]
  }
  ```

### `upsertStoragePolicy (PUT /admin/policy[/{id}])`

* **请求方法**: `PUT`
* **路径**: `/admin/policy` 或 `/admin/policy/{id}`（如果 `args.policy.id` 存在，则带上 ID）
* **请求参数**:
    * **请求体 (body)**: `args` (`UpsertStoragePolicyService`, 存储策略创建/更新参数，包括 `policy` 对象)
* **响应**: `AdminStoragePolicy` (存储策略对象)
* **说明**: 新建或更新存储策略。如果 `args.policy.id` 存在则更新，否则创建新的策略。
* **创建示例**:
  ```json
  PUT /admin/policy
  Content-Type: application/json

  {
    "policy": {
      "name": "New Policy",
      "driver": "local",
      "config": {
        "basePath": "/data"
      }
    }
  }
  ```
* **更新示例**:
  ```json
  PUT /admin/policy/123
  Content-Type: application/json

  {
    "policy": {
      "id": 123,
      "name": "Updated Policy Name",
      "config": {
        "maxFileSize": 1024
      }
    }
  }
  ```

### `getSettings (POST /admin/settings)`

* **请求方法**: `POST`
* **路径**: `/admin/settings`
* **请求参数**:
    * **请求体 (body)**: `keys` (`GetSettingService`, 包含要获取的设置键列表)
* **响应**: `对象` (键值对形式，返回指定设置项及其值)
* **说明**: 获取指定的站点设置。返回一个对象，键为设置项名称，值为对应值。
* **请求示例**:
  ```json
  POST /admin/settings
  Content-Type: application/json

  {
    "keys": ["siteName", "allowUserSignup"]
  }
  ```

### `getQueueMetrics (GET /admin/queue/metrics)`

* **请求方法**: `GET`
* **路径**: `/admin/queue/metrics`
* **请求参数**: 无
* **响应**: `QueueMetric[]` (队列指标列表)
* **说明**: 获取系统队列的指标信息。
* **请求示例**:
  ```
  GET /admin/queue/metrics
  ```

### `getPolicyOauthCredentialRefreshTime (GET /admin/policy/oauth/status/{id})`

* **请求方法**: `GET`
* **路径**: `/admin/policy/oauth/status/{id}`
* **请求参数**:
    * `id` (路径参数, `string`)
* **响应**: `OauthCredentialStatus` (OAuth 凭证状态)
* **说明**: 获取指定存储策略的 OAuth 凭证刷新状态。
* **请求示例**:
  ```
  GET /admin/policy/oauth/status/onedrive-123
  ```

### `sendCreateDavAccounts (PUT /devices/dav)`

* **请求方法**: `PUT`
* **路径**: `/devices/dav`
* **请求参数**:
    * **请求体 (body)**: `req` (`CreateDavAccountService`, 创建 DAV 账户的参数)
* **响应**: `DavAccount` (创建的 DAV 账户信息)
* **说明**: 创建 WebDAV 账户或设备。
* **请求示例**:
  ```json
  PUT /devices/dav
  Content-Type: application/json

  {
    "deviceId": "desktop-abc",
    "deviceName": "我的桌面",
    "username": "davuser"
  }
  ```

### `sendMountStoragePolicy (PATCH /file/policy)`

* **请求方法**: `PATCH`
* **路径**: `/file/policy`
* **请求参数**:
    * **请求体 (body)**: `req` (`MountPolicyService`, 挂载存储策略的参数)
* **响应**: `StoragePolicy[]` (挂载后的存储策略列表)
* **说明**: 将存储策略挂载到当前路径或文件上。
* **请求示例**:
  ```json
  PATCH /file/policy
  Content-Type: application/json

  {
    "uri": "/path/to/mount",
    "policyId": 456
  }
  ```

### `sendRenameFile (POST /file/rename)`

* **请求方法**: `POST`
* **路径**: `/file/rename`
* **请求参数**:
    * **请求体 (body)**: `req` (`RenameFileService`, 重命名文件的参数)
* **响应**: `FileResponse` (文件响应对象)
* **说明**: 重命名文件。
* **请求示例**:
  ```json
  POST /file/rename
  Content-Type: application/json

  {
    "uri": "/old/path/to/file",
    "newName": "new_file_name.txt"
  }
  ```

### `testNode (POST /admin/node/test)`

* **请求方法**: `POST`
* **路径**: `/admin/node/test`
* **请求参数**:
    * **请求体 (body)**: `args` (`TestNodeService`, 测试节点的参数)
* **响应**: `void`
* **说明**: 测试节点连接配置。
* **请求示例**:
  ```json
  POST /admin/node/test
  Content-Type: application/json

  {
    "node": {
      "address": "http://example-node:8080",
      "secret": "node-secret-key"
    }
  }
  ```

### `sendPrepareLogin (GET /session/prepare)`

* **请求方法**: `GET`
* **路径**: `/session/prepare`
* **请求参数**:
    * **查询参数 (query)**:
        * `email` (`字符串`, 邮箱地址)
* **响应**: `PrepareLoginResponse` (登录准备响应)
* **说明**: 准备用户登录流程，传递用户邮箱以获取登录提示或节点信息。
* **请求示例**:
  ```
  GET /session/prepare?email=user@example.com
  ```

### `sendUploadChunk (POST /file/upload/{sessionID}/{index})`

* **请求方法**: `POST`
* **路径**: `/file/upload/{sessionID}/{index}`
* **请求参数**:
    * `sessionID` (路径参数, `string`, 例如 `upload-session-123`)
    * `index` (路径参数, `number`, 例如 `0`)
    * **请求体 (body)**: `chunk` (`Blob`, 文件块的二进制数据)
    * **可选参数**:
        * `cancel` (`CancelToken`, 取消令牌, 可选)
        * `onProgress` (上传进度回调函数, 可选)
* **响应**: `UploadCredential` (上传凭证，用于后续上传)
* **说明**: 上传文件的分片（chunk）。`sessionID` 和 `index` 指定了上传会话和块序号，`chunk` 为文件数据。
* **请求示例**:
  ```
  POST /file/upload/upload-session-123/0
  Content-Type: application/octet-stream

  (文件第一个分片的二进制数据)
  ```

### `deleteGiftCode (DELETE /admin/giftCodes/{id})`

* **请求方法**: `DELETE`
* **路径**: `/admin/giftCodes/{id}`
* **请求参数**:
    * `id` (路径参数, 来自请求体 `DeleteGiftCodeService` 的 `id` 字段, `string` 或 `number`)
* **响应**: `void`
* **说明**: 删除指定 ID 的礼品码。
* **请求示例**:
  ```
  DELETE /admin/giftCodes/GIFTCODE123
  ```

### `sendUnlinkOpenID (DELETE /session/openid/{provider})`

* **请求方法**: `DELETE`
* **路径**: `/session/openid/{provider}`
* **请求参数**:
    * `provider` (路径参数, `OpenIDProvider`, OpenID 提供商，例如 `google`)
* **响应**: (未指定具体类型)
* **说明**: 解绑用户的 OpenID 账号。
* **请求示例**:
  ```
  DELETE /session/openid/google
  ```

### `getGiftCodeList (POST /admin/giftCodes)`

* **请求方法**: `POST`
* **路径**: `/admin/giftCodes`
* **请求参数**:
    * **请求体 (body)**: `args` (`AdminListService`, 分页查询参数)
* **响应**: `ListGiftCodeResponse` (礼品码列表响应)
* **说明**: 管理员获取礼品码列表。
* **请求示例**:
  ```json
  POST /admin/giftCodes
  Content-Type: application/json

  {
    "page": 1,
    "pageSize": 50
  }
  ```

### `sendReset (PATCH /user/reset/{uid})`

* **请求方法**: `PATCH`
* **路径**: `/user/reset/{uid}`
* **请求参数**:
    * `uid` (路径参数, 用户 ID, `string`, 例如 `user-abc-123`)
    * **请求体 (body)**: `req` (`ResetPasswordService`, 重置密码请求数据)
* **响应**: `User` (重置后的用户对象)
* **说明**: 重置指定用户的密码。
