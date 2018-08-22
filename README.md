Open Graph Scraper
===

My humble effort at a simple [open graph](http://ogp.me) scraper.

cURL examples:
---

```bash
$ curl -D - -XPOSThttp://edo.shor.hiring.keywee.io/stories?url=https://keywee.co
$ curl -D -http://edo.shor.hiring.keywee.io/stories/111273543919972337457437777204483007572

$ curl -D - -XPOSThttp://edo.shor.hiring.keywee.io/stories?url=http://ogp.me
$ curl -D -http://edo.shor.hiring.keywee.io/stories/120732187575471516303930262373192735056

$ curl -D - -XPOSThttp://edo.shor.hiring.keywee.io/stories?url=https://nike.com
$ curl -D -http://edo.shor.hiring.keywee.io/stories/229705522576361926541936424411801185566

$ curl -D - -XPOSThttp://edo.shor.hiring.keywee.io/stories?url=https://keywee.co/top-publishers-monetize-email-databases/
$ curl -D -http://edo.shor.hiring.keywee.io/stories/223753070063240061380113065152799322714

$ curl -D - -XPOSThttp://edo.shor.hiring.keywee.io/stories?url=https://www.youtube.com/watch\?v\=N4mEzFDjqtA
$ curl -D -http://edo.shor.hiring.keywee.io/stories/23092914356759104811691377274326953550

```

Implementation Notes:
--
Some implementation notes should go here...