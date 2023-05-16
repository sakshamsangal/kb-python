# async and differ

## Normal

### <script src="" />

```javascript 
1. html parsing
2. if script tag comes (normal)
    1. stop html parsing
    2. download script
    3. execute script
3. html parsing if available
```

----------

## async: when order does not matter like google api

### <script async src="" />

``` javascript
1. html parsing and download script simultaneously
2. if script tags comes (async)
   1. execute script
3. html parsing if available
```

----------

## differ: use when order of code is matter

### <script defer src="" />

``` javascript
1. html parsing and download script simultaneously
2. html parsing finishes
3. execute script 
 ```