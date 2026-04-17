
USE Library_Audit;

CREATE TABLE Books(
	BookID INT primary key,
    Title varchar(100),
    Author varchar(100),
    Category varchar(50)
);

CREATE table Students(
	StudentID INT PRIMARY KEY,
    StudentName varchar(100),
    Email varchar(100),
    JoinDate date
);


Create table IssuedBooks(
	IssueID INT primary key,
    BookID INT,
    StudentID INT,
    IssueDate DATE,
    ReturnDate DATE,
    
    foreign key(BookID) references Books(BookID),
    foreign key(StudentID) references Students(StudentID)
);



