class univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for column_name in dataset.columns:
            if dataset[column_name].dtypes=='O': 
                qual.append(column_name)
            else:
                quan.append(column_name)
        return quan,qual