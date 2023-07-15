# From https://www.geeksforgeeks.org/python-taskgroups-with-asyncio/ 

import asyncio

async def square_number(n):
	for i in range(1,n+1):
		print("Square of ",i, "is ", i**2)
		await asyncio.sleep(0.001)

async def square_root(n):
	print("Square root of ",n," rounded to nearest integer is ",
		round(n**.5))

async def divide(num1,num2):
	if num2 == 0:
		raise Exception("Trying to Divide by Zero")
	else:
		print(num1/num2)

async def main():
	try:
		async with asyncio.TaskGroup() as task_group:
			task_group.create_task(square_number(5))
			task_group.create_task(square_root(25))
			task_group.create_task(square_root(18))

				# Returns Exception
			task_group.create_task(square_number("Geeks"))
			task_group.create_task(square_number('a'))
			task_group.create_task(divide(10,0))
	except* TypeError as te:
		for errors in te.exceptions:
			print(errors)
	except* Exception as ex:
		print(ex.exceptions)

		print("All different tasks of task_group has executed successfully!!")

"""Comment the Above main with Taskgroups and uncomment
	the below to see the tasks.gather()"""

async def gather_main():
	tasks = asyncio.gather(
		square_number(5),
		square_root(16),
		divide(15,0),
		square_root("Geek")
	)

	await tasks
print("==============================================")
print("Output of Taskgroup with Exception")
print("==============================================")
asyncio.run(main())

print("==============================================")
print("Output of asyncio.gather()")
print("==============================================")
asyncio.run(gather_main())
