import psycopg

class Database():
    def __init__(self):
        self.connection = self.connection_db()

    def connection_db(self):
        '''
        Функция для подключения к БД
        :return: connection object
        '''
        try:
            conn = psycopg.connect(
                host = "localhost",
                user = 'postgres',
                password = '1234',
                dbname = 'demolearning',
                port = 5432
            )
            print("Подключение установлено")
            return conn
        except Exception as error:
            print(f'Ошибка подключения: {error}')
            return None

    def take_all_partners(self):
        '''
        Функция получения информации о всех партнерах
        :return: partner_info - список с инфо о партнере
        '''
        try:
            query = '''
                select * from partners_import;
                '''

            cursor = self.connection.cursor()
            cursor.execute(query)
            partner_info = []

            for row in cursor.fetchall():
                partner_info.append({
                    'type_partner': row[0].strip(),
                    'partner_name': row[1].strip(),
                    'director': row[2].strip(),
                    'email_partner': row[3].strip(),
                    'partner_phone': row[4].strip(),
                    'ur_adres': row[5].strip(),
                    'inn_partner': row[6].strip(),
                    'rate_partner': row[7].strip(),
                })
            self.connection.commit()
            cursor.close()
            print(partner_info)
            return partner_info
        except Exception as error:
            print(error)
            return []

    def sum_cost_partners(self, partner_name):
        '''
        Функция для получения стоимости продаж партнера
        :return: cost
        '''
        try:
            query = f'''
                select SUM(count_products) FROM partner_products_import
                 WHERE partner_name_fk = '{partner_name}';
                '''

            cursor = self.connection.cursor()
            cursor.execute(query)
            cost = cursor.fetchone()[0]
            if cost:
                print(cost)
                return cost
            else:
                return None

        except Exception as error:
            print(f'Ошибка: {error}')