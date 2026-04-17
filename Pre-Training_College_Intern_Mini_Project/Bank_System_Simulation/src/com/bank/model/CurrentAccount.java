package com.bank.model;

public class CurrentAccount extends Account {
    private double overdraftLimit = 5000;

    public CurrentAccount(int accNo, String name, double balance) {
        super(accNo, name, balance);
    }

    @Override
    public void withdraw(double amount) {
        if (balance + overdraftLimit >= amount) {
            balance -= amount;
        } else {
            System.out.println("Limit Exceeded");
        }
    }
}
