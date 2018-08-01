from sqlalchemy import create_engine

db_string = "postgres://postgres:postgres@localhost:9879/BBLEARN"

db = create_engine(db_string)

userid = 'someuserid'

results = db.execute("select u.user_id, cm.course_id, cu.role \
                         from users u join course_users cu on u.pk1 = cu.users_pk1 \
                         join course_main cm on cu.crsmain_pk1 = cm.pk1 \
                         where u.user_id = '%s' " % userid)


for row in results:
    print('U: {} C: {} R: {}'.format(row.user_id, row.course_id, row.role)) 