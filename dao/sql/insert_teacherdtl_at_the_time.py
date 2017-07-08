import pymysql

connection = pymysql.connect(host='localhost',user='root',password='2wsxCDE#',db='race',
                             charset='utf8',cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:

    heldy = '2015'
    heldm = '0000'
    racecoursecd = '00'
    raceno = '00'

    while True:
        insert_player_data_at_the_time = """
        insert into teacher_at_the_time (heldy, heldm, raceno, racecoursecd, trainername, sosu, WIN, RENTAI, FUKUSYO)
        select
         racedtlhis.heldy,
         racedtlhis.heldm,
         racedtlhis.raceno,
         racedtlhis.racecoursecd,
         racedtlhis.trainername,
         COALESCE(sosu, 0) + 1 as sosu,
         case
          when CONFTYAKU = 1 then round((round(COALESCE(sosu, 0) * COALESCE(win, 0) / 100) + 1) / (COALESCE(sosu, 0) + 1) * 100, 5)
          else round((round(COALESCE(sosu, 0) * COALESCE(win, 0) / 100)) / (COALESCE(sosu, 0) + 1) * 100, 5)
         end
         as WIN,
         case
          when CONFTYAKU <= 2 then round((round(COALESCE(sosu, 0) * COALESCE(RENTAI, 0) / 100) + 1) / (COALESCE(sosu, 0) + 1) * 100, 5)
          else round((round(COALESCE(sosu, 0) * COALESCE(RENTAI, 0) / 100)) / (COALESCE(sosu, 0) + 1) * 100, 5)
         end
         as RENTAI,
         case
          when CONFTYAKU <= 3 then round((round(COALESCE(sosu, 0) * COALESCE(FUKUSYO, 0) / 100) + 1) / (COALESCE(sosu, 0) + 1) * 100, 5)
          else round((round(COALESCE(sosu, 0) * COALESCE(FUKUSYO, 0) / 100)) / (COALESCE(sosu, 0) + 1) * 100, 5)
         end
         as FUKUSYO
        from
        (
            select
             *
            from
             racedtlhis
            where
             concat(heldy, heldm, raceno, racecoursecd) = (
                select
                 min(concat(heldy, heldm, raceno, racecoursecd))
                from
                 racedtlhis
                where
                 heldy = '{heldy}' and
                 heldm = '{heldm}' and
                 racecoursecd = '{racecoursecd}' and
                 raceno = '{raceno}'
             )
        ) racedtlhis
        left outer join (
            select heldy, heldm, raceno, racecoursecd, t1.trainername, sosu, WIN, RENTAI, FUKUSYO from
            (
                select  max(concat(heldy, heldm, raceno, racecoursecd)) as raceid, trainername from teacher_at_the_time
                where
                    concat(heldy, heldm, raceno, racecoursecd) <= '{heldy}{heldm}{raceno}{racecoursecd}'
                group by trainername
            ) t1
            inner join (
                select concat(heldy, heldm, raceno, racecoursecd) as raceid, heldy, heldm, raceno, racecoursecd, trainername, sosu, WIN, RENTAI, FUKUSYO from teacher_at_the_time
            ) t2
            on t1.raceid = t2.raceid and t1.trainername = t2.trainername
        ) teacher_at_the_time
        on racedtlhis.trainername = teacher_at_the_time.trainername
        """.format(heldy=heldy, heldm=heldm, racecoursecd=racecoursecd, raceno=raceno)
        cursor.execute(insert_player_data_at_the_time)
        connection.commit()
        result = cursor.fetchone()

        get_max_race_id_sql = """
            select
             heldy, heldm, raceno, racecoursecd
            from
             racedtlhis
            where
             concat(heldy, heldm, raceno, racecoursecd) = (
                select
                    min(concat(heldy, heldm, raceno, racecoursecd)) as raceid
                from
                    racedtlhis
                where
                    concat(heldy, heldm, raceno, racecoursecd) > '{heldy}{heldm}{raceno}{racecoursecd}'
             )
        """.format(heldy=heldy, heldm=heldm, racecoursecd=racecoursecd, raceno=raceno)
        cursor.execute(get_max_race_id_sql)
        result = cursor.fetchone()
        print (result["heldy"] + result["heldm"] + result["raceno"] + result["racecoursecd"])
        heldy = result["heldy"]
        heldm = result["heldm"]
        racecoursecd = result["racecoursecd"]
        raceno = result["raceno"]

        if heldy is None:
            break

connection.close()