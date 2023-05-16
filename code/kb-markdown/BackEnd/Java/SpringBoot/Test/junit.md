```text
runwith springrunner.class
@webmvctest
Mvctest
    @Autowired
    Mockmvc

    @mockbean
    ProdRepo repo 

    test()
        new prod() with filled
        add to list of product 
        when(repo.findAll()).thenReturn(prod list)

        objectwriter = new objectmapper().writer().pretty()


        // get 
        mockmvc.peform(get("/articles").contextPath("/prod"))
        .andExcept(status().isok())
        .andExcept(content().json(objectwriter.writevallueas string(prod list )))


        // post 
        when(repo.save(any())).thenReturn(prod list)
        mockmvc.peform(
            post("/articles")
            .contextPath("/prod")
            .contenttype(MediaType.app_json)
            .content(objectmapper.writevallueas string(prod single))
        )
        .andExcept(status().isok())
        .andExcept(content().json(objectwriter.writevallueas string(prod list )))

        // put
        when(repo.save(any())).thenReturn(prod list)

        mockmvc.peform(
            post("/articles")
            .contextPath("/prod")
            .contenttype(MediaType.app_json)
            .content(objectmapper.writevallueas string(prod single))
        )
        .andExcept(status().isok())
        .andExcept(content().json(objectwriter.writevallueas string(prod list )))



        // delete
        donothing.when(repo).deleteById(id);

        mockmvc.peform(
            delete("/articles")
            .contextPath("/prod")           
        )
        .andExcept(status().isok())


```

