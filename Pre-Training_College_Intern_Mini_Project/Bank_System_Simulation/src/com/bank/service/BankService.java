package com.bank.service;

import com.bank.model.Account;
import com.bank.model.Transaction;
import com.bank.model.User;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BankService {
    private List<User> users = new ArrayList<>();
    private Map<Integer, List<Transaction>> transactions = new HashMap<>();

    public void addUser(User user) {
        users.add(user);
    }

    public User authenticate(String username, String password) {
        for (User u : users) {
            if (u.login(username, password)) {
                return u;
            }
        }
        return null;
    }

    public void deposit(Account acc, double amount) {
        acc.deposit(amount);
        addTransaction(acc.getAccountNumber(), "Deposit", amount);
    }

    public void withdraw(Account acc, double amount) {
        acc.withdraw(amount);
        addTransaction(acc.getAccountNumber(), "Withdraw", amount);
    }

    public void transfer(Account from, Account to, double amount) {
        from.withdraw(amount);
        to.deposit(amount);
        addTransaction(from.getAccountNumber(), "Transfer Sent", amount);
        addTransaction(to.getAccountNumber(), "Transfer Received", amount);
    }

    private void addTransaction(int accNo, String type, double amount) {
        transactions.putIfAbsent(accNo, new ArrayList<>());
        transactions.get(accNo).add(new Transaction(type, amount));
    }

    public void showTransactions(int accNo) {
        List<Transaction> list = transactions.get(accNo);
        if (list != null) {
            list.forEach(System.out::println);
        }
    }
}
