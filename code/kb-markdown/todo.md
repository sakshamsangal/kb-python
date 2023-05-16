```

| food         | recipe | ingredient |  
|--------------|--------|------------|
| aaloparantha | ...    | ....       |
| pizza        | ...    | ....       |


| customer | 1   | 2   | 3   | 4   | 5   |
|----------|-----|-----|-----|-----|-----|
| saksham  | i1  | i2  | i3  | i4  | i5  |
|          |     |     |     |     |     |
// input, Here 1096782 is customerId
{
    "1096782": {
        ingredients:[
            "potato",
            "butter",
            "blackPepper",
            "greenChilli",
            "wheat"
        ]
    }
    
}


// output
getRecipe/{customerId}
[
    {
        "alooParatha": {
            ["Step 1 ... ", "Step 2 ..."]
        }
    }
]

food | reciepe | ingredients
aalopatha | .... | ....
pizza | .... | ...


title Post ingredients api
1->2:POST /ingredients
2->3:save ingredients in database
'2->4:train the AI model with this data
1<--2:show the list of recipes\nusing get recipes api
```
- build type
  - maven
  - gradle
- controller
  - api
    - expose
      - get
        - secure
          - role
        - header
        - query param
        - path variable
        - success
        - error
      - post
        - secure
          - role
        - header
        - payload
        - success
        - error
    - consume
      - mode
        - web client
        - rest template
      - header
      - query param
      - path variable
      - success
      - error
      - payl


























