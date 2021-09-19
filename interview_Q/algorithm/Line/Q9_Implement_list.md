# Q9. Implement list

Q: You are about to implement a list with thumbnails (like LINE's "Friends" list). Usually, thumbnails take time to fetch. In this situation, please explain in detail what you would do to improve user experience (e.g., faster scroll and lower memory usage, etc.).

Ans:

Jeff's Answer:
```
Firstly, we can get all text info from the list. The list should provide callback function when we scroll to the bottom. The callback function supplies the info (ex, urls) to get thumbnails. Then we use the other thread to fetch thumbnails from the urls. Once thumbnails are fetched, the main thread goes to show them.
Using this way, we can get faster scrolling in user experience while we use cpu resource as needed.
```