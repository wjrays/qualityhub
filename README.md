# QualityHub

基于 pytest 和 requests 构建的 OWASP Juice Shop 自动化测试项目。

## 已实现功能

- 首页可用性检查
- 商品搜索接口测试
- 无搜索结果场景测试
- 商品字段类型与价格范围校验
- pytest 参数化测试
- pytest fixture 环境地址管理

## 技术栈

- Python
- pytest
- requests
- Docker
- Git
- GitHub

## 项目结构

```text
qualityhub/
├── tests/
│   ├── conftest.py
│   └── test_products.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 被测系统

本项目使用 OWASP Juice Shop 作为本地被测系统。

```text
http://localhost:3000
```

## 运行测试

安装依赖：

```bash
pip install -r requirements.txt
```

确保 Juice Shop 正在运行，然后执行：

```bash
pytest tests -v
```

## 当前测试场景

1. 验证首页返回 HTTP 200。
2. 使用多组关键词搜索商品。
3. 验证接口业务状态和数据类型。
4. 验证商品名称与搜索词匹配。
5. 验证不存在的商品返回空列表。