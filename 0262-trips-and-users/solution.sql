WITH valid_users as(
    select users_id from Users where banned = "No"
)
select request_at as Day , 
    round(sum(if(status != "completed",1,0))/count(*),2) as "Cancellation Rate"
    from Trips
    where  driver_id in (select * from valid_users) and 
    client_id in (select * from valid_users) and
    request_at between "2013-10-01" and "2013-10-03"
group by request_at
