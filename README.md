Open Graph Scraper
===

My humble effort at a simple [open graph](http://ogp.me) scraper.

cURL examples:
---

```bash
$ curl -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://keywee.co
$ curl http://edo.shor.hiring.keywee.io/stories/111273543919972337457437777204483007572

$ curl -XPOST http://edo.shor.hiring.keywee.io/stories?url=http://ogp.me
$ curl http://edo.shor.hiring.keywee.io/stories/120732187575471516303930262373192735056

$ curl -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://nike.com
$ curl http://edo.shor.hiring.keywee.io/stories/229705522576361926541936424411801185566

$ curl -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://keywee.co/top-publishers-monetize-email-databases/
$ curl http://edo.shor.hiring.keywee.io/stories/223753070063240061380113065152799322714

$ curl -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://www.youtube.com/watch\?v\=N4mEzFDjqtA
$ curl http://edo.shor.hiring.keywee.io/stories/23092914356759104811691377274326953550

```

Missing url param `400 - Bad request`
```bash
$ curl -D - -XPOST http://edo.shor.hiring.keywee.io/stories?url=

HTTP/1.1 400 BAD REQUEST
...
url param is missing
```

Register new url results `201 - Created`. If url already exists return `200 - Ok` (no op)
```bash
$ curl -D - -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://httpbin.org/

HTTP/1.1 201 CREATED
...
311790385888870184647755638031157205566


$ curl -D - -XPOST http://edo.shor.hiring.keywee.io/stories?url=https://httpbin.org/

HTTP/1.1 200 OK
...
{"status":"Url already exist"}

```

Implementation Notes:
--
Some implementation notes should go here...