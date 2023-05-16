package com.example.batch;

import org.springframework.batch.item.*;

public class CustomerProcessor implements ItemProcessor<Customer, Customer> {

    @Override
    public Customer process(Customer customer) throws Exception {
        if (customer.getCountry().equals("United States")) {
            return customer;
        } else {
            return null;
        }
    }
}