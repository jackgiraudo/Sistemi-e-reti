import queue

coda  = queue.Queue()
#enqueue -> put
#dequeueu -> get

coda.put(3)
coda.put(5)
coda.put(19)

print(coda.get())
print(coda.queue)