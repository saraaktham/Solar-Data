
-- Find instances with DNI larger than 100
select count(*) from "loc_Colorado Spring" lcs  lp where "DNI" >100;

-- Find instances with temperature lower than 10 and DNI larger than 100
select count(*) from "loc_Colorado Spring" lcs where "DNI">100 and "Temperature" <10;