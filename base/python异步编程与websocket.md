

## websockets
https://blog.csdn.net/wuShiJingZuo/article/details/135244298


## asyncio:
1. https://blog.csdn.net/I_AM_MD/article/details/135005422
2. 基于协程和事件循环的异步代码库
3. 基本流程
    ```
    import asyncio
    
    #定义协程函数
    async def func1():
        print('1')
        await asyncio.sleep(1)
        print('2')
    
    async def func2():
        print('3')
        await asyncio.sleep(1)
        print('4')
    
    #创建协程对象
    task_list = [func1(), func2()]
   
    #放入事件循环
    asyncio.run(asyncio.wait(task_list))
    """
    loop = asyncio.get_event_loop()    # 获取事件循环
    loop.run_until_comlete( result )   # 运行事件循环
    """
    ```
3. await: 
    - await + 可等待的对象（协程对象、Task对象、Future对象）
    - done, pending = await asyncio.wait(task_list, timeout=None)
4. Task: 让协程加入事件循环中, 会被执行
    - asyncio.create_task()
    - loop.create_task() 
5. Future:
    - 等待被set_result
    - loop.create_future()
6. 与线程池关联：
    - fut = loop.run_in_executor(None, func1)
7. asyncio.Queue：https://blog.csdn.net/qq_41287993/article/details/132035815

