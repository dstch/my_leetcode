#Write a SQL query to get the second highest salary from the Employee table. 
#
# 
#+----+--------+
#| Id | Salary |
#+----+--------+
#| 1  | 100    |
#| 2  | 200    |
#| 3  | 300    |
#+----+--------+
# 
#
# For example, given the above Employee table, the query should return 200 as th
#e second highest salary. If there is no second highest salary, then the query sh
#ould return null. 
#
# 
#+---------------------+
#| SecondHighestSalary |
#+---------------------+
#| 200                 |
#+---------------------+
# 
# 👍 1133 👎 557


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select (select distinct(Salary) from Employee order by Salary desc limit 1,1)  as SecondHighestSalary
#leetcode submit region end(Prohibit modification and deletion)
