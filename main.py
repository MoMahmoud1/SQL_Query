# Generate the following two result sets:
#
# Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
#
# Query the number of occurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
#
# There are a total of [occupation_count] [occupation]s.
#
# where [occupation_count] is the number of occurrences of occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.
#
# Note: There


set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(select case when Occupation=’Doctor’ then (@r1:=@r1+1) when Occupation=’Professor’ then (@r2:=@r2+1) when Occupation=’Singer’ then (@r3:=@r3+1) when Occupation=’Actor’ then (@r4:=@r4+1) end as RowNumber,
case when Occupation=’Doctor’ then Name end as Doctor,
case when Occupation=’Professor’ then Name end as Professor,
case when Occupation=’Singer’ then Name end as Singer,
case when Occupation=’Actor’ then Name end as Acto from OCCUPATIONS order by Name
) Temp group by RowNumber;