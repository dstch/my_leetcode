#Write a SQL query to delete all duplicate email entries in a table named Person
#, keeping only unique emails based on its smallest Id. 
#
# 
#+----+------------------+
#| Id | Email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#| 3  | john@example.com |
#+----+------------------+
#Id is the primary key column for this table.
# 
#
# For example, after running your query, the above Person table should have the 
#following rows: 
#
# 
#+----+------------------+
#| Id | Email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#+----+------------------+
# 
#
# Note: 
#
# Your output is the whole Person table after executing your sql. Use delete sta
#tement. 
# 👍 563 👎 843


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
delete from Person where Id not in (select t.Id from (select min(id) as id from Person group by email) t)
#leetcode submit region end(Prohibit modification and deletion)
