package com.bank.model;

public class SavingsAccount extends Account{
    public SavingsAccount(int accNo, String name,double balance){
        super(accNo,name,balance);
    }

    @Override
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance-=amount;
        }else{
            System.out.println("Insufficient Balance");

        }
    }
}
