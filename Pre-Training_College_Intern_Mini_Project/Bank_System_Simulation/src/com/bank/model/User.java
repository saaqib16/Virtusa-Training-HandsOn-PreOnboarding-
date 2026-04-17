package com.bank.model;

public class User {
    private String userName;
    private String password;
    private Account account;

    public User(String userName, String password, Account account) {
        this.userName = userName;
        this.password = password;
        this.account = account;
    }

    public boolean login(String username, String password) {
        return userName.equals(username) && password.equals(this.password);
    }

    public Account getAccount() {
        return account;
    }
}
