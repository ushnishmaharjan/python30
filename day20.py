import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="python30march"
)

myterminal=db.cursor()
insert_queiry =f"INSERT INTO `currency exchangerate` (`id`, `date`, `iso3`, `name`, `unit`, `buy`, `sell`) VALUES (NULL, '2026-04-01', 'NEP', 'Nepal ', '1', '150', '150');"
#myterminal.execute(insert_queiry)
db.commit()

#update command

#update_command="UPDATE `exchangerate` SET `buy` = '150' WHERE `exchangerate`.`id` = 2;"
#myterminal.execute(update_command)
#db.commit()
print(db)

delete_command="DELETE FROM `currency exchangerate` "
myterminal.execute(delete_command)
db.commit()