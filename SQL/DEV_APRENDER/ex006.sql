SELECT ProductNumber, Name
FROM Production.Product
WHERE ProductID >= 1 and ProductID <= 4;

---

SELECT TOP 4 ProductNumber, Name
FROM Production.Product
ORDER BY ProductID ASC;
