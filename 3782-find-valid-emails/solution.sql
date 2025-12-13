select user_id,email from Users where email REGEXP '^[a-zA-Z0-9]+@[a-zA-Z]+[.]com$' order by user_id;
