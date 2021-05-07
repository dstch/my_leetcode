#Table: Person 
#
# 
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| PersonId    | int     |
#| FirstName   | varchar |
#| LastName    | varchar |
#+-------------+---------+
#PersonId is the primary key column for this table.
# 
#
# Table: Address 
#
# 
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| AddressId   | int     |
#| PersonId    | int     |
#| City        | varchar |
#| State       | varchar |
#+-------------+---------+
#AddressId is the primary key column for this table.
# 
#
# 
#
# Write a SQL query for a report that provides the following information for eac
#h person in the Person table, regardless if there is an address for each of thos
#e people: 
#
# 
#FirstName, LastName, City, State
# 
# 👍 1200 👎 159


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select a.FirstName,a.LastName,b.City,b.State from Person a left join Address b on a.PersonId=b.PersonId
#leetcode submit region end(Prohibit modification and deletion)
