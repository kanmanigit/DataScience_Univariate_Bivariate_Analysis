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

    def univariate(dataset,quan):
        table=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5 Rule","Lesser","Greater","Min","Max"],columns=quan)
        for quan_column_name in quan:
            table.loc["Mean",quan_column_name]=dataset[quan_column_name].mean()
            table.loc["Median",quan_column_name]=dataset[quan_column_name].median()
            table.loc["Mode",quan_column_name]=dataset[quan_column_name].mode()[0]
            table.loc["Q1:25%",quan_column_name] =dataset.describe()[quan_column_name]["25%"]
            table.loc["Q2:50%",quan_column_name]=dataset.describe()[quan_column_name]["50%"]
            table.loc["Q3:75%",quan_column_name]=dataset.describe()[quan_column_name]["75%"]
            table.loc["Q4:100%",quan_column_name]=dataset.describe()[quan_column_name]["max"]
            table.loc["IQR",quan_column_name]=table.loc["Q3:75%",quan_column_name]-table.loc["Q1:25%",quan_column_name]
            table.loc["1.5 Rule",quan_column_name]=1.5*table.loc["IQR",quan_column_name]
            table.loc["Lesser",quan_column_name]=table.loc["Q1:25%",quan_column_name]-table.loc["1.5 Rule",quan_column_name]
            table.loc["Greater",quan_column_name]=table.loc["Q3:75%",quan_column_name]+table.loc["1.5 Rule",quan_column_name]
            table.loc["Min",quan_column_name]=dataset[quan_column_name].min()
            table.loc["Max",quan_column_name]=dataset[quan_column_name].max()
        return table

    def freq_table(column_name):
        freq_table=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","CumSum"])
        freq_table["Unique_Values"]=dataset[column_name].value_counts().index
        freq_table["Frequency"]=dataset[column_name].value_counts().values
    
        no_of_rows=len(freq_table.index)
        
        freq_table["Relative_Frequency"]=(freq_table["Frequency"]/no_of_rows)
        freq_table["CumSum"]=freq_table["Relative_Frequency"].cumsum()
        return freq_table

    def finding_outliers(quan):
     #Finding if any lesser and Greater outliers
        lesser=[]
        greater=[]
        for quan_column_name in quan:
            if table.loc["Min",quan_column_name]<table.loc["Lesser",quan_column_name]:
                lesser.append(quan_column_name)
        
            if table.loc["Max",quan_column_name]>table.loc["Greater",quan_column_name]:
                greater.append(quan_column_name)
            
        print("lesser outlier in ",lesser)
        print("Greater outlier in ",greater)
        return lesser,greater

    def outliers_replacement(lesser,dataset):
        # To replace the outliers with the "Range" in the original dataset"
        
        for columnname in lesser:
            #dataset[columnname][dataset[columnname]<table.loc["Lesser",columnname]]=table.loc["Lesser",columnname]
            dataset.loc[dataset[columnname]<table.loc["Lesser",columnname],columnname]=table.loc["Lesser",columnname]
            
            
        for columnname in greater:
            #dataset[columnname][dataset[columnname]>table.loc["Greater",columnname]]=table.loc["Greater",columnname]
            dataset.loc[dataset[columnname]>table.loc["Greater",columnname],columnname]=table.loc["Greater",columnname] 
        return