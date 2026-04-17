package com.bank.main;

import com.bank.model.Account;
import com.bank.model.SavingsAccount;
import com.bank.model.User;
import com.bank.service.BankService;

import java.util.Scanner;

public class MainApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BankService bank = new BankService();

        Account acc1 = new SavingsAccount(1, "John", 1000);
        User user1 = new User("john", "1234", acc1);
        bank.addUser(user1);

        System.out.println("Login:");
        String uname = sc.next();
        String pass = sc.next();

        User loggedIn = bank.authenticate(uname, pass);

        if (loggedIn != null) {
            System.out.println("Login successful");

            Account acc = loggedIn.getAccount();
            bank.deposit(acc, 500);
            bank.withdraw(acc, 200);

            System.out.println("Balance: " + acc.getBalance());
            bank.showTransactions(acc.getAccountNumber());
        } else {
            System.out.println("Invalid credentials");
        }
    }
}
