import asyncio
import time

async def worker():
    print("worker 开始")
    await asyncio.sleep(0)
    print("worker 结束")


async def main():
    print("main 第1步")
    task1 = asyncio.create_task(worker())  # 注册到就绪队列，但worker不会立刻执行
    print("main 第2步")  # 这行仍然继续执行，worker还在排队
    print("main 第3步")
    task2 = asyncio.create_task(worker())
    await asyncio.sleep(0)  # 这里让出控制权，事件循环才调度worker
    print("main 结束")


asyncio.run(main())


async def call_llm(prompt: str) -> dict:
    """模拟调用 LLM API（网络 IO）"""
    await asyncio.sleep(1.2)  # 模拟网络延迟
    return {"model": "gpt-4", "text": f"LLM 对 '{prompt}' 的回复"}


async def analyze_ast(code: str) -> dict:
    """模拟 AST 分析（本地 IO + 计算）"""
    await asyncio.sleep(0.3)  # 模拟文件读取
    return {"functions": 3, "classes": 1, "lines": len(code)}


async def search_context(query: str) -> dict:
    """模拟向量搜索（网络 IO）"""
    await asyncio.sleep(0.5)
    return {"matches": [f"文档1 关于 {query}", f"文档2 关于 {query}"]}


async def run_sequential():
    """顺序执行"""
    start = time.time()
    llm = await call_llm("review this code")
    ast = await analyze_ast("def foo(): pass")
    ctx = await search_context("python")
    elapsed = time.time() - start
    print(f"顺序执行耗时{elapsed}s")
    return [llm, ast, ctx]


async def run_with_gather():
    start = time.time()
    llm, ast, ctx = await asyncio.gather(
        call_llm("review this code"),
        analyze_ast("def foo(): pass"),
        search_context("python"),
    )
    elapsed = time.time() - start
    print(f"gather耗时{elapsed}s")
    return [llm, ast, ctx]


async def run_with_wait():
    start = time.time()
    tasks = {
        asyncio.create_task(call_llm("review this code")),
        asyncio.create_task(analyze_ast("def foo(): pass")),
        asyncio.create_task(search_context("python")),
    }

    results = {}

    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for t in done:
            results[t.get_name()] = t.result
            print(f"{t.get_name()} 先完成 ({time.time() - start:.2f}s)")

    elapsed = time.time() - start
    print(f"wait: {elapsed:.2f}s")
    return list(results)


asyncio.run(run_sequential())  # ~2.0s
asyncio.run(run_with_gather())  # ~1.2s
asyncio.run(run_with_wait())  # ~1.2s（但先得到 AST 结果可以提前处理）
