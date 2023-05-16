add httpclientmodule on app module
inject httpclient in ts
http.post(url, json).subscribe(callback);
http.get(url)
.pipe(map(callback))
.subscribe(callback);