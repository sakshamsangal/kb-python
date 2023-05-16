```

scanner is taking '\n' as string, so workaround for this is:
int size = Integer.parseInt(sc.nextLine()); 

For reference:
https://www.geeksforgeeks.org/why-is-scanner-skipping-nextline-after-use-of-other-next-functions/

```
