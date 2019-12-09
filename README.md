# minor-redesign
智能运营项目

后端基本模型

- ![智能化运营](./doc/img/智能化运营.png)

# 模型
```
articleId: long
userId:long
importance:int
tags:[]
content:text
title：text
```

# 数据
分两张表，一张表article 只存储原生的文章，原生的标签
```json

{
  "articleId":"articeld",
  "title":"title",
  "content":"content",
  "tags":["a","b"]
}

```
一张表为user 
```
{
    "userId":"userId"
    "articleId":"articleId", # 这里的articleId对应着article表中的articleId
    "title":"title",  # 这里的title不一定是原来的title,因为用户会改
    "content":"content", # 用户会改
    "tags":"", # 用户会改
    "weight":"" # 重要性
}
```

# 辅助编选
- 需要编辑的
  - 标签编辑
  - 文章编辑
  - 重要性编辑
  - article/userId={userId}&articleId={articleId}

- 需要显示的
  - 文章列表
  - article/userId={userId}
  - 接口定义
    - article/userId=

- 上传功能
  - 简单头部解析

