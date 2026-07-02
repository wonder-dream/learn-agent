# FastAPI 基础：路由 + 请求/响应模型

> 笔记模板，用你自己的话填空。每个 `<!-- ... -->` 是一道待填项。

---

## 一、FastAPI 应用是什么

### 1.1 FastAPI 在整个系统中扮演什么角色？

<!-- 用自己的话描述：FastAPI 做的事，它在 Agent 系统中处于什么位置 -->

- FastAPI 是一个 ~~python 后端框架~~<span style="color:red">ASGI Web 框架</span>，它在我的 Agent 项目里负责 ~~搭建后端系统，实现 API 的转接路由~~<span style="color:red">接收 HTTP 请求、校验参数、分发到业务逻辑并返回响应——是 Agent 对外的"接口层"</span>

### 1.2 为什么选 FastAPI 而不是 Flask / Django？

<!-- 从 async 支持、自动文档、Pydantic 集成三个角度回答 -->

- Async 支持：__原生支持 async/await，路由函数可以直接用 async def，与 httpx 异步调用无缝衔接__
- 自动文档：__自动生成 Swagger UI（/docs）和 ReDoc（/redoc），可以直接在浏览器里测试接口__
- Pydantic 集成：__请求体和响应模型直接复用 Pydantic BaseModel，校验/序列化/文档三步合一，不需要手写校验逻辑__

### 1.3 ASGI vs WSGI

<!-- 一句话解释区别，为什么 Agent 开发需要 ASGI -->

- WSGI 是 __同步服务器网关接口__，ASGI 是 __异步服务器网关接口__
- Agent 开发需要 ASGI 因为 __agent 系统运行时最长时间的是在等待 IO 通信而不是计算密集型，所以使用异步方法可以更大程度利用 CPU__

### 1.4 uvicorn 是什么？

<!-- uvicorn 和 FastAPI 的分工 -->

- FastAPI 负责  __处理 HTTP 请求的解析、路由分发、参数校验和响应序列化——业务逻辑层__
- uvicorn 负责 ~~转发路由请求到对应的应用~~<span style="color:red">接收网络字节流，解析成 HTTP 请求对象后交给 FastAPI（ASGI app），再把响应发回客户端——它是"网络层"，不做路由</span>
- `--reload` 参数的作用是 __每次修改代码自动重新加载服务器，不用手动关闭重启__

---

## 二、路由：把 URL 和函数"接"在一起

### 2.1 装饰器路由是怎么工作的？

<!-- 用自己的话解释 @app.get("/path") 做了什么 -->

- `@app.get("/xxx")` 本质是 ~~一个装饰器~~<span style="color:red">一个路由注册装饰器</span>（回顾 Day 02 装饰器）
- 它把 ~~请求地址~~<span style="color:red">被装饰的函数</span> 注册到了 ~~路由表~~<span style="color:red">FastAPI 内部路由表（url → handler 的映射）</span>
- GET / POST / PUT / DELETE 分别对应 REST 的 ~~get/post/put/delete~~<span style="color:red">查 / 增 / 改（全量替换）/ 删</span>

### 2.2 路由匹配的优先级

<!-- 静态路径 vs 动态路径，谁先匹配？ -->

- 如果 `/reviews/{review_id}` 写在 `/reviews/active` 前面，会发生什么？__静态路由会失效，永远无法使用__
- 正确做法：__把静态路由放置在动态路由前，先匹配静态再匹配动态__

---

## 三、三种参数，三种来源

### 3.1 路径参数（Path Parameter）

<!-- 用自己的话描述：写在什么位置、怎么声明、什么时候用 -->

- 定义方式：__写在路径中用 {} 包裹，函数参数名与占位符名一致__
- 自动行为：__自动转换成类型注解中标注的类型，且必须填（URL 里不提供就匹配不到路由）__（类型转换、必填校验）
- 适合传什么：~~资源查询~~<span style="color:red">资源定位——例如 review_id、user_id，用于"找哪个资源"</span>

### 3.2 查询参数（Query Parameter）

<!-- 用自己的话描述：写在什么位置、怎么声明、什么时候用 -->

- 定义方式：__函数参数不在路径模板中且不是 Pydantic model 类型，自动视为查询参数__
- 自动行为：__可以设默认值，不传就用默认值__
- 适合传什么：~~分页~~<span style="color:red">筛选条件 / 分页参数 / 排序字段——例如 ?status=open&page=2&page_size=20</span>

### 3.3 请求体（Request Body）

<!-- 用自己的话描述：什么时候用、怎么声明 -->

- 定义方式：~~和查询参数定义方式相同~~<span style="color:red">函数参数的类型注解为 Pydantic BaseModel 子类，FastAPI 自动把请求体 JSON 解析成该类型的实例</span>
- FastAPI 自动做的三件事：
  1. ________________
  
     读取请求体中的 JSON 字符串并解析成 Python dict
  2. ________________
  
     用声明的 Pydantic model 对 dict 做完整校验（类型 + 约束）
  3. ________________
  
     将校验通过的 model 实例作为参数传入路由函数

### 3.4 三种参数对比表

| | 路径参数 | 查询参数 | 请求体 |
|---|---|---|---|
| URL 里长什么样 | __/route/{arg}__ | __/route?arg__ | __/route__ |
| 必填还是可选 | 必填 | __有默认值就是可选__ | __看 类中怎么定义的__ |
| 适合传什么 | __资源 ID__ | __筛选/分页条件__ | __复杂数据结构__ |
| FastAPI 怎么识别 | ~~找同名的参数~~<span style="color:red">路径模板 `{name}` 与函数参数名匹配</span> | ~~类似关键字参数~~<span style="color:red">函数参数不在路径模板中、且非 Pydantic model 类型 → 自动视为查询参数</span> | ~~函数参数类型是 pydantic model~~<span style="color:red">函数参数类型注解为 BaseModel 子类 → 自动从请求体解析</span> |
| 自动类型转换 | ~~转换成类型注解~~<span style="color:red">按类型注解自动转换（`/42` → int 42）</span> | ~~转换成类型注解~~<span style="color:red">按类型注解自动转换（`?limit=10` → int 10）</span> | ~~通过 pydantic 的完整性校验~~<span style="color:red">Pydantic 完整校验 + 类型强制转换（如 `"123"` → int 123）</span> |

---

## 四、Pydantic × FastAPI：校验一次，三处受益

### 4.1 请求体校验

<!-- 用 Pydantic model 做请求体，非法数据会发生什么？ -->

- 如果前端传了 `{"file_path": 123}`（int 而不是 str），FastAPI 会 ~~报错~~<span style="color:red">返回 422 响应，响应体中包含 Pydantic 生成的错误详情（哪个字段错了、为什么错）</span>
- HTTP 状态码是 __422__（Unprocessable Entity）
- 这个 422 是 FastAPI 自动生成的，不需要你写任何 try/except——非法数据根本不会到达你的路由函数

### 4.2 response_model 的三个作用

<!-- 用自己的话写 -->

1. __避免多余的敏感字段被返回__（过滤多余字段）
2. __通过 pydantic 完整性校验保证输出格式__（校验输出）
3. __用于自动文档界面的生成__（生成文档）

### 4.3 response_model 是怎么过滤字段的？

<!-- 底层原理：是 FastAPI 做的还是 Pydantic 做的？ -->

- 本质是 Pydantic 的 __model_validate__ 方法
- 返回了 response_model 里没有的字段 → __丢弃__（丢弃 / 报错？）
- 返回数据缺少 response_model 里的必填字段 → __报错__（丢弃 / 报错？）

### 4.4 HTTPException

<!-- 什么场景该主动抛 HTTPException？ -->

- 用法：~~__~~<span style="color:red">`raise HTTPException(status_code=400, detail="具体原因")`——当数据通过了 Pydantic 校验但违反了业务规则时，例如 `review_id` 是合法的 int 但在数据库中不存在（404），或者参数在语义上不合理（如负数 ID）</span>
- 和 Pydantic ValidationError 的区别：
  - ValidationError 是 ~~pydantic 没校验通过时抛出的，422状态码~~<span style="color:red">Pydantic 在构造实例时因类型/约束不符自动抛出的，FastAPI 捕获后返回 422</span>（谁抛的？什么状态码？）
  - HTTPException 是 ~~fastapi 在服务异常时抛的，400状态码~~<span style="color:red">你在路由函数中主动抛出的业务异常，状态码由你指定（不限于 400）</span>（谁抛的？什么状态码？）

| 错误来源 | HTTP 状态码 | 含义 | 示例 |
|----------|-----------|------|------|
| Pydantic 校验失败 | __422__ | 输入数据不合法 | 传了 `"abc"` 给 `int` 字段 |
| 你主动抛 HTTPException | __400__ | 业务规则不通过 | `review_id < 0` |
| 代码未处理异常 | __500__ | 代码崩了 | `1 / 0` |

---

## 五、自动交互式文档

### 5.1 两个文档地址

- Swagger UI：~~__~~<span style="color:red">`/docs`——交互式 API 文档，可以直接在页面里填入参数并点击"Execute"发送真实请求，等同于图形化的 curl</span>
- ReDoc：~~__~~<span style="color:red">`/redoc`——只读的 API 文档，排版更清晰，适合给前端同事或外部调用方查阅</span>
- OpenAPI JSON：~~__~~<span style="color:red">`/openapi.json`——以上两个文档的数据源，标准 OpenAPI 3.0 格式 JSON，前端可以用它自动生成 TypeScript 类型定义和请求函数</span>

### 5.2 文档信息从哪里来？

<!-- 这些文档上的字段描述、类型、校验规则是从哪里自动提取的？ -->

- 路由列表：来自 __装饰自动注册的__
- 请求参数类型：来自 __类型注解__
- 请求体 Schema：来自 __类型注解__
- 响应 Schema：来自 __response_model__

---

## 六、完整请求生命周期

<!-- 用你自己的话描述：一个 POST /review 请求从进入到返回的完整过程 -->

```
1. uvicorn 收到 HTTP 请求
   ↓
2. FastAPI 匹配路由 → 从 URL 中进行匹配
   ↓
3. 解析参数 → 从 URL 或者请求体中解析参数
   ↓
4. Pydantic 校验请求体 → 校验完成将就绪的实例交给业务代码
   ↓
5. 执行你的路由函数 → 执行业务代码
   ↓
6. response_model 过滤 + 序列化 → 标准化返回数据
   ↓
7. 返回 JSON 响应
```

---

## 七、常见错误

<!-- 今天踩过的坑，记下来以后别再踩 -->

- [x] ~~路径参数只在 URL 中需要 {} 在代码中不需要~~<span style="color:red">路径参数在 URL 模板中用 `{参数名}` 声明占位，在函数签名中用同名参数接收——路径里的 `{}`和函数参数必须一一对应</span>

- [x] ~~路由函数的返回值是一个字典~~<span style="color:red">路由函数可以返回 dict / list / Pydantic model，FastAPI 全部自动转为 JSON，不需要手写 json.dumps()</span>

- [x] ~~只要返回复杂数据类型一定需要 response_model~~<span style="color:red">response_model 主要作用是过滤敏感字段和生成文档，简单的 dict 返回可以不用，但正式项目建议一律声明</span>

---

## 八、常用命令速查

```bash
# 启动开发服务器
uvicorn main:app --reload

# 指定端口
uvicorn main:app --reload --port 8080

# 查看自动生成的 OpenAPI JSON
curl http://localhost:8000/openapi.json

# Swagger UI
# 浏览器打开 http://localhost:8000/docs

# ReDoc
# 浏览器打开 http://localhost:8000/redoc
```

---

## 九、一句话总结（考试级精简）

- FastAPI 应用：~~__~~<span style="color:red">ASGI Web 框架，用装饰器把 URL 路径和业务函数绑定，自动完成参数解析、Pydantic 校验和 JSON 序列化</span>
- 路由装饰器：~~__~~<span style="color:red">`@app.get/post/put/delete(path)` 把函数注册到路由表，请求来了自动匹配</span>
- 路径参数：~~__~~<span style="color:red">URL 中的 `{变量}`，必填，自动类型转换——用于定位"哪个资源"</span>
- 查询参数：~~__~~<span style="color:red">`?key=value`，函数签名中声明默认值即视为可选——用于筛选/分页/排序</span>
- 请求体：~~__~~<span style="color:red">POST/PUT 时携带的 JSON，参数类型为 Pydantic model 时 FastAPI 自动解析校验</span>
- response_model：~~__~~<span style="color:red">声明响应 Schema，自动过滤多余字段、校验输出、生成文档——三合一安全网</span>
- HTTPException：~~__~~<span style="color:red">开发者主动抛出的 HTTP 异常，状态码自定义，用于表达"校验通过但业务不合法"</span>
- Swagger UI：~~__~~<span style="color:red">`/docs` 自动生成的交互式 API 文档，源于类型注解和 Pydantic model</span>

---

*笔记整理于 2026-06-30*
