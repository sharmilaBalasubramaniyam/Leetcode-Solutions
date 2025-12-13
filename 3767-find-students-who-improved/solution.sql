select student_id, subject, min_scr as first_score, max_scr as latest_score from
(select student_id, subject, score, exam_date,
FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date asc) as min_scr,
LAST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date asc) as max_scr,
ROW_NUMBER() OVER(PARTITION BY student_id, subject ORDER BY exam_date desc) as rn
from Scores) as t
where rn =1 and min_scr < max_scr
