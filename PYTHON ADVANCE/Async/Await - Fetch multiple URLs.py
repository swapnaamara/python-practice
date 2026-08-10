import asyncio

async def fetch(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return name

async def main():
    results = await asyncio.gather(
        fetch("Task1", 2),
        fetch("Task2", 1),
        fetch("Task3", 3)
    )
    print(results)

asyncio.run(main())