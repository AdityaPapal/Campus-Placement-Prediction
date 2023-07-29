from Logger.logger_class import Logger


class preprocessing:

   

    def __init__(self):

        self.log_writer = Logger()
        self.file_object = open('logs/data_preprocessing_logs.txt','a+')

    def remove_columns(self, data, columns):
    

        self.data = data
        self.columns = columns
        try:
            self.useful_data = self.data.drop(labels=self.columns, axis=1)  # drop the labels specified in the columns
            self.log_writer.log(
                self.file_object, 'Column removal Successful.'
                                  'Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.log_writer.log(
                self.file_object,'Exception occured in remove_columns method of the Preprocessor class.'
                                 'Exception message:  ' + str(
                                       e))
            self.log_writer.log(
                self.file_object, 'Column removal Unsuccessful.'
                                  'Exited the remove_columns method of the Preprocessor class')
            raise Exception()


    def separate_label_feature(self, data, label_column_name):
      
    
        self.log_writer.log(self.file_object, 'Entered the separate_label_feature method of the Preprocessor class')
        try:
            self.X = data.drop(labels=label_column_name,
                               axis=1)  # drop the columns specified and separate the feature columns
            self.Y = data[label_column_name]  # Filter the Label columns
            self.log_writer.log(
                self.file_object, 'Label Separation Successful.'
                                  'Exited the separate_label_feature method of the Preprocessor class')
            return self.X, self.Y
        except Exception as e:
            self.log_writer.log(
                self.file_object, 'Exception occured in separate_label_feature method of the Preprocessor class.'
                                  ' Exception message:  ' + str(
                                       e))
            self.log_writer.log(
                self.file_object,'Label Separation Unsuccessful. '
                                 'Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()

    def get_columns_with_zero_std_deviation(self, data):
        """
        Method Name: get_columns_with_zero_std_deviation
        Description: This method finds out the columns which have a standard deviation of zero.
        Output: List of the columns with standard deviation of zero
        On Failure: Raise Exception
        Written By: Aditya Agrawal

        """

        self.columns = data.columns
        self.data_n = data.describe()
        self.col_to_drop = []
        try:
            for x in self.columns:
                if (self.data_n[x]['std'] == 0):  # check if standard deviation is zero
                    self.col_to_drop.append(x)  # prepare the list of columns with standard deviation zero
            self.log_writer.log(
                self.file_object, 'Column search for Standard Deviation of Zero Successful.'
                                  'Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            return self.col_to_drop

        except Exception as e:
            self.log_writer.log(
                self.file_object,'Exception occured in get_columns_with_zero_std_deviation method '
                                 'of the Preprocessor class. Exception message:  ' + str(
                                       e))
            self.log_writer.log(
                self.file_object, 'Column search for Standard Deviation of Zero Failed.'
                                  ' Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            raise Exception()
