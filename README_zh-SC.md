# Cloudreve 文档

Cloudreve 的非官方文档，提供了 [官方文档](https://docsv4.cloudreve.org) 中没有的内容，如 API 文档(包含 Pro 版本的路由部分)，以及未来可能编写社区版的二开文档

[English](README.md) | [简体中文](README_zh-SC.md)

[v3](v3.md) | [v4](v4.md)

[行为准则](CODE_OF_CONDUCT.md)

## 文档的格式

- 对于未完成的路由：
    - 只有 API 路由和请求方法，移动到文档的底部 `未知路由` 处。
    - 在上一条的前提下，知道路由的分类，则移动到对应的段落中。如果与已编写的任何标题不匹配，则新建标题。
    - 在上一条的前提下，知道路由的请求方法、参数以及返回值，则应明确写明。格式如下：
        ```markdown
        ### Ping 站点
        - 方法: `GET`
        - 路径: `/api/v4/site/ping`
        - 响应示例:
        ```json
        {
            "code":0,
            "data":"4.0.0",
            "msg":""
        }
        ```
    - 在上一条的前提下，如果返回值有多种可能，则也应明确说明。格式如下：
        ```markdown
        ### 登录准备
        - 方法: `GET`
        - 路径: `/api/v4/session/prepare`
        - 参数: 
            - `email`: 待登录用户的邮箱
        - 响应示例:
        ```json
        // 成功示例
        {
            "code":0,
            "data":{
                "webauthn_enabled":true,
                "sso_enabled":false,
                "password_enabled":true,
                "qq_enabled":false
                },
            "msg":""
        }

        // 失败示例 邮箱不能为空
        {
            "code":40001,
            "msg":"Email cannot be empty"
        }
        ```
    - 如果无法判定路由是否完成，则按情况具体处理。
- 对于已完成的路由
    - 以下前提可以提交 Pull Request 进行补充、修改或删除
        - 路由的请求方法、路径、请求体或返回值发生了变更
        - 文档中表达的内容不明确
        - 文档中的内容错误
        - 此路由侵犯了他人的合法权利
        - 其他需要修改文档的情形

## License

> SPDX-License-Identifier: GPL-3.0-or-later AND CC-BY-4.0

本API文档遵循 [GPLv3](LICENSE) 和 [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) 双协议授权。
当文档内容涉及原始程序社区版实现时适用GPLv3，其他内容适用CC-BY-4.0。