SELECT s.StudentID,s.StudentName,b.Title,ib.IssueDate,
CURRENT_DATE - ib.IssueDate AS DaysOverdue
FROM IssuedBooks ib
JOIN Students s ON ib.StudentID = s.StudentID
JOIN Books b ON ib.BookID = b.BookID
WHERE ib.ReturnDate IS NULL AND ib.IssueDate < CURRENT_DATE - INTERVAL 14 day;