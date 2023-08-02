# mre-for-playwrite-scrapy
A very simple MRE for an error with playwrite_scrapy

The error is that if you hit a page that uses a meta redirect, scrapy_playwright will
raise the following error:

```
ERROR: Error downloading <GET https://gidgidonihah.github.io/mre-for-playwrite-scrapy/>
Traceback (most recent call last):
  File "/virtualenvs/mre/lib/python3.10/site-packages/twisted/internet/defer.py", line 1693, in _inlineCallbacks
    result = context.run(
  File "/virtualenvs/mre/lib/python3.10/site-packages/twisted/python/failure.py", line 518, in throwExceptionIntoGenerator
    return g.throw(self.type, self.value, self.tb)
  File "/virtualenvs/mre/lib/python3.10/site-packages/scrapy/core/downloader/middleware.py", line 54, in process_request
    return (yield download_func(request=request, spider=spider))
  File "/virtualenvs/mre/lib/python3.10/site-packages/twisted/internet/defer.py", line 1065, in adapt
    extracted = result.result()
  File "/virtualenvs/mre/lib/python3.10/site-packages/scrapy_playwright/handler.py", line 301, in _download_request
    result = await self._download_request_with_page(request, page, spider)
  File "/virtualenvs/mre/lib/python3.10/site-packages/scrapy_playwright/handler.py", line 354, in _download_request_with_page
    body_str = await page.content()
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/async_api/_generated.py", line 9146, in content
    return mapping.from_maybe_impl(await self._impl_obj.content())
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/_impl/_page.py", line 462, in content
    return await self._main_frame.content()
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/_impl/_frame.py", line 415, in content
    return await self._channel.send("content")
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/_impl/_connection.py", line 61, in send
    return await self._connection.wrap_api_call(
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/_impl/_connection.py", line 482, in wrap_api_call
    return await cb()
  File "/virtualenvs/mre/lib/python3.10/site-packages/playwright/_impl/_connection.py", line 97, in inner_send
    result = next(iter(done)).result()
playwright._impl._api_types.Error: Unable to retrieve content because the page is navigating and changing the content.
```

The page content that will cause this found in docs/index.html
