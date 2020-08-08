import mysql.connector

class db_wrapper(object):

    # Hard-coded connection params
    __host = "184.169.248.53"
    __user = "root"
    __pswd = "example"
    __db_name = "kpMats"

    __mat_tab_name = "Materials"

    @property
    def table_names(self):
        """Returns all table names in the db"""
        cursor = self._db.cursor()
        cursor.execute("SHOW TABLES")

        return [str(x[0]) for x in cursor]

    @property
    def material_names(self):
        """Returns list of material names from table Materials"""
        result = self.__get_table_data_raw(db_wrapper.__mat_tab_name)

        return [str(x[0]) for x in result]

    def __init__(self):
        """Instantiate with default params"""
        self._db = mysql.connector.connect(
            host=db_wrapper.__host,
            user=db_wrapper.__user,
            password=db_wrapper.__pswd,
            database=db_wrapper.__db_name)

        self._mat_map = self.__set_material_dict()

    def __set_material_dict(self):
        """Maps material names to sets of property table names"""
        # Get all material property tables as a set
        tab_names = self.table_names
        tab_names.remove(db_wrapper.__mat_tab_name)
        tab_names = set(tab_names)

        # Initialize material dict with empty sets
        mat_map = {curr_key:set() for curr_key in self.material_names}

        for curr_key in mat_map:
            for curr_tab_name in tab_names:
                # Add table to set if it starts with material name
                if curr_tab_name.startswith(curr_key):
                    mat_map[curr_key].add(curr_tab_name)

            # Remove spoken for table names
            tab_names -= mat_map[curr_key]

        return mat_map

    def __get_table_data_raw(self, tab_name):
        """Returns full table contents"""
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM " + tab_name)

        return cursor.fetchall()

    def get_mat_prop_table_names(self, mat_name):
        """Returns set of material property table names for given material"""
        # TODO: Add error handling?
        return self._mat_map[mat_name]



