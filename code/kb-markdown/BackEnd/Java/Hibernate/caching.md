## level 1 cache, hiberante hit db only once for same data

```
mark test with transactional
write multpile findAll() method
select stmt is executed onl once
without transactional l1 cache wont work 
```

## dlete cache

```
entity manager(hib. session) add 
use evict to delete by creating session 

```


