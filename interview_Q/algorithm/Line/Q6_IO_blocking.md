# Q6. IO blocking
Q: Please explain differences between "Blocking I/O" and "Non-blocking I/O".

```
Blocking IO means that a given thread cannot do anything more until the IO is fully finished.

Non-blocking IO means an IO request is queued straight away and the function returns. The actual IO is then processed at some later pointer by the kernel.
```