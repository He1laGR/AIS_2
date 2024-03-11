from db_executor import execute
from models import User


def filter_users(surname_mask: str, name_mask: str):
    users = []
    for item in execute("SELECT "
                       "user_id, "
                       "login, "
                       "password, "
                       "first_name, "
                       "last_name, "
                       "email, "
                       "phone_number "
                       "FROM delivery_service.user " +
                       "WHERE last_name like CONCAT('%', %s, '%') "
                       "and first_name like CONCAT('%', %s, '%');", (surname_mask, name_mask)):
        user = User()
        user.user_id = item[0]
        user.login = item[1]
        user.password = item[2]
        user.first_name = item[3]
        user.last_name = item[4]
        user.email = item[5]
        user.phone_number = item[6]
        users.append(user)

    return users


def get_user_by_login(login: str):
    users = []
    for item in execute("SELECT "
                       "user_id, "
                       "login, "
                       "password, "
                       "first_name, "
                       "last_name, "
                       "email, "
                       "phone_number "
                       "FROM delivery_service.user " +
                       "WHERE login = %s;", (login,)):
        user = User()
        user.user_id = item[0]
        user.login = item[1]
        user.password = item[2]
        user.first_name = item[3]
        user.last_name = item[4]
        user.email = item[5]
        user.phone_number = item[6]
        users.append(user)

    if len(users) == 1:
        return users[0]
    else:
        return 'Пользователя с таким логином нет'


def create_user(user: User):
    return execute("INSERT INTO delivery_service.user "
                   "(login, password, first_name, last_name, email, phone_number) "
                   "VALUES(%s, %s, %s, %s, %s) RETURNING user_id", (
                       user.login,
                       user.password,
                       user.first_name,
                       user.last_name,
                       user.email,
                       user.phone_number
                   ))
