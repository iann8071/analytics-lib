import pymysql

connection = pymysql.connect(host='localhost',user='root',password='2wsxCDE#',db='race',
                             charset='utf8',cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:

    heldy = '2015'
    heldm = '0000'
    raceno = '00'

    while True:
        insert_player_data_at_the_time = """
        insert into player_at_the_time (heldy, heldm, raceno, jockeyname, sosu, WIN, RENTAI, FUKUSYO)
        select
         racedtlhis.heldy,
         racedtlhis.heldm,
         racedtlhis.raceno,
         racedtlhis.jockeyname,
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
             heldy = '{heldy}' and
             heldm = '{heldm}' and
             raceno = '{raceno}'
        ) racedtlhis
        left outer join (
            select heldy, heldm, raceno, p1.jockeyname, sosu, WIN, RENTAI, FUKUSYO from
            (
                select  max(concat(heldy, heldm, raceno)) as raceid, jockeyname from player_at_the_time
                where
                    concat(heldy, heldm, raceno) <= '{heldy}{heldm}{raceno}'
                group by jockeyname
            ) p1
            inner join (
                select concat(heldy, heldm, raceno) as raceid, heldy, heldm, raceno, jockeyname, sosu, WIN, RENTAI, FUKUSYO from player_at_the_time
            ) p2
            on p1.raceid = p2.raceid and p1.jockeyname = p2.jockeyname
        ) player_at_the_time
        on racedtlhis.jockeyname = player_at_the_time.jockeyname
        """.format(heldy=heldy, heldm=heldm, raceno=raceno)
        cursor.execute(insert_player_data_at_the_time)
        connection.commit()
        result = cursor.fetchone()

        get_max_race_id_sql = """
            select
             heldy, heldm, raceno
            from
             racedtlhis
            where
             concat(heldy, heldm, raceno) = (
                select
                    min(concat(heldy, heldm, raceno)) as raceid
                from
                    racedtlhis
                where
                    concat(heldy, heldm, raceno) > '{heldy}{heldm}{raceno}'
             )
        """.format(heldy=heldy, heldm=heldm,raceno=raceno)
        cursor.execute(get_max_race_id_sql)
        result = cursor.fetchone()
        print (result["heldy"] + result["heldm"] + result["raceno"])
        heldy = result["heldy"]
        heldm = result["heldm"]
        raceno = result["raceno"]

        if heldy is None:
            break

connection.close()