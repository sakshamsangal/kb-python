```
{{username | uppercase}}
{{username | date}}

## para pipes 

date: 'fullDate'

## chaining pipes
date: 'fullDate' | uppercase

## custom pipe 

shorten.pipe.ts 

@Pipe({
    name: 'shorten'
})
implements PipeTransform 

transform(value: any) {
    return value.substr(0, 10);
}
{{username |shorten}}

## para custom pipe
```

@Pipe({
name: 'shorten'
})
implements PipeTransform

transform(value: any, limit: number) {
return value.substr(0, 10);
}
{{username |shorten:15}}

```

## filter pipe 
```

ng g p filter

```
```