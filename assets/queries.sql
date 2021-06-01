/* get wr max demand and max demand time for day*/
select date_key,
    max_demand,
    max_demand_time,
    state_name
from REPORTING_UAT.state_demand_requirement
where state_name = 'WR'
    and date_key = 20210520;
/* get wr max consumption mu for day*/
select date_key,
    day_energy_demand_met
from REPORTING_UAT.regional_availability_demand
where date_key = 20210520;
/* get wr IR sch actual MU for day*/
select SUM(TOTAL_IR_ACTUAL) AS reg_act,
    sum(TOTAL_IR_SCHEDULE) AS reg_sch
from REPORTING_UAT.INTER_REGIONAL_SCHEDULE_ACTUAL
WHERE date_key = 20210520
GROUP BY DATE_KEY;
/* get wr freq band data for day*/
select FREQ6_VALUE AS f_49_9,
    FREQ8_VALUE AS f_50_5,
    FREQ7_VALUE AS band_perc
from REPORTING_UAT.FREQUENCY_PROFILE
where date_key = 20210520;
/* get wr freq stats for day*/
SELECT MAX_FREQ,
    MAX_TIME,
    MIN_FREQ,
    MIN_TIME,
    FREQ_VARIATION_INDEX
FROM REPORTING_UAT.FREQUENCY_PROFILE_MAX_MIN fpmm
WHERE DATE_KEY = 20210520