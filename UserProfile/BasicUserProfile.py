import pandas as pd


class ProfileGenerator:

    def __init__(self, filename, outputfile):
        self.filename = filename
        self.outputfile = outputfile

    def remove_ex_columns(self):
        df = pd.read_csv(self.filename, low_memory=False).drop(
            columns=['employee_name', 'business_unit', 'functional_unit', 'department', 'supervisor'])
        return df

    def get_dataframe(self, filename):
        df = pd.read_csv(filename)
        return df

    def append_to_end(self, filename):
        self.filename = filename
        try:

            with open(self.outputfile, 'a') as csvfile:
                df = self.remove_ex_columns()
                df.to_csv(csvfile, header=False, index=False)
        except Exception as e:
            raise e

    def copy_to_profile_file(self):
        """
        run just first time to create basic profile for user
        output generate file as outputfile
        :return:
        """
        df = self.remove_ex_columns()
        try:
            df.to_csv(self.outputfile, index=False)
        except Exception as e:
            raise e

    def reindex_file(self):
        """
        index file from zero to ...
        :return:
        """
        try:
            df = pd.read_csv(self.outputfile)
            df.to_csv(self.outputfile)
        except Exception as e:
            raise e


if __name__ == "__main__":
    pg = ProfileGenerator('2010-01.csv', 'UserProfile.csv')
    # pg.copy_to_profile_file()

    # data = ['2010-02.csv', '2010-03.csv', '2010-04.csv', '2010-05.csv', '2010-06.csv']
    # for file in data:
    #     pg.append_to_end(file)
