# <YOUR_IMPORTS>
import pandas as pd
import dill
import os
import warnings
warnings.filterwarnings("ignore")


def predict():
    #<YOUR_CODE>
    os.environ.get('PROJECT_PATH', '.')
    name = os.listdir('/home/aniskurbonov/airflow_hw/data/models')

    with open(f'/home/sirojiddin/airflow_hw/data/models/{name[0]}', 'rb') as file:
        model = dill.load(file)
    df_pred = pd.DataFrame(columns=['car_id', 'pred'])
    for filename in os.listdir('/home/aniskurbonov/airflow_hw/data/test'):
        with open(f'/home/aniskurbonov/airflow_hw/data/test/{filename}', 'r') as j:
            #print(str(j.read()))
            data = str(j.read())
            df = pd.DataFrame(eval(data), index=[0])
            pred = model.predict(df)
            x = {'car_id': df.id, 'pred': pred}
            df1 = pd.DataFrame(x)
            df_pred = pd.concat([df_pred, df1], axis=0,ignore_index=True)

    df_pred[['car_id','pred']].to_csv(f'/home/aniskurbonov/airflow_hw/data/predictions/pred_{name[0].split("_")[2].split(".")[0]}.csv', index=False)
    print("Done =)")

if __name__ == '__main__':
    predict()
