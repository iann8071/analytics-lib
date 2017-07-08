import pymysql

connection = pymysql.connect(host='localhost',user='root',password='2wsxCDE#',db='race',
                             charset='utf8',cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    heldy = '2015'
    heldm = '0000'

    while True:
        insert_uma_data_at_the_time = """
    insert into uma_at_the_time (heldy, heldm, kettono, sosu, win, rentai, fukusyo)
    select
     racedtlhis.heldy,
     racedtlhis.heldm,
     racedtlhis.kettono,
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
         heldy,
         heldm,
         kettono,
         CONFTYAKU
        from
         racedtlhis
        where
         concat(heldy, heldm) = '{heldy}{heldm}'
    ) racedtlhis
    left outer join
    (
    select * from uma_at_the_time where (concat(heldy, heldm), kettono) in (select max(concat(heldy, heldm)), kettono from uma_at_the_time group by kettono)
    ) uma
    on racedtlhis.KETTONO = uma.KETTONO
        """.format(heldy=heldy, heldm=heldm)
        cursor.execute(insert_uma_data_at_the_time)
        connection.commit()
        result = cursor.fetchone()

        get_max_race_id_sql = """
            select
             heldy, heldm
            from
             racedtlhis
            where
             concat(heldy, heldm) = (
                select
                    min(concat(heldy, heldm)) as raceid
                from
                    racedtlhis
                where
                    concat(heldy, heldm) > '{heldy}{heldm}'
             )
        """.format(heldy=heldy, heldm=heldm)
        cursor.execute(get_max_race_id_sql)
        result = cursor.fetchone()
        print (result["heldy"] + result["heldm"])
        heldy = result["heldy"]
        heldm = result["heldm"]

        if heldy is None:
            break