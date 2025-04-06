# Cloudreve Documentation

Unofficial documentation for Cloudreve, providing content not available in the [official documentation](https://docsv4.cloudreve.org), such as API documentation (including routes for the Pro version), and possibly future development documentation for the community version.

[English](README.md) | [简体中文](README_zh-SC.md)

[v3](v3.md) | [v4](v4.md)

[Code of Conduct](CODE_OF_CONDUCT.md)

## Document Format

- For incomplete routes:
    - Routes with only API path and request method should be moved to the bottom of the document under `未知路由`.
    - If the route category is known, move it to the corresponding section. If it doesn't match any existing headers, create a new one.
    - If the request method, parameters, and return values are known, they should be clearly specified. Format as follows:
        ```markdown
        ### Ping Site
        - Method: `GET`
        - Path: `/api/v4/site/ping`
        - Response example:
        ```json
        {
            "code":0,
            "data":"4.0.0",
            "msg":""
        }
        ```
    - If there are multiple possible return values, they should also be clearly explained. Format as follows:
        ```markdown
        ### Login Preparation
        - Method: `GET`
        - Path: `/api/v4/session/prepare`
        - Parameters: 
            - `email`: Email of the user attempting to login
        - Response examples:
        ```json
        // Success example
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

        // Failure example - Email cannot be empty
        {
            "code":40001,
            "msg":"Email cannot be empty"
        }
        ```
    - If it cannot be determined whether a route is complete, handle it on a case-by-case basis.
- For completed routes:
    - Pull Requests for supplements, modifications, or deletions can be submitted in the following cases:
        - The route's request method, path, request body, or response has changed
        - The content expressed in the documentation is unclear
        - The content in the documentation is incorrect
        - The route infringes upon the legal rights of others
        - Other situations requiring documentation changes

## License

> SPDX-License-Identifier: GPL-3.0-or-later AND CC-BY-4.0

This API documentation is dual-licensed under [GPLv3](LICENSE) and [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
The GPLv3 applies when the documentation involves the original community version implementation, while CC-BY-4.0 applies to other content.