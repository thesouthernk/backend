
from fastapi import APIRouter, Response, status
from ....models.api_models import Item, ItemList,ItemListDict
from typing import Optional, List

import pandas as pd
import os

router = APIRouter()

#Search 
@router.get("/search", response_model=ItemListDict)
async def search(name: str = None, category: str = None, nutrient: str = None):
    mainPath = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(mainPath+'/finalData.csv')
    data = data.fillna('')
    if name:
        data['description_str']=data.description.str.replace("[^A-Za-z]", '')
        name_str=[x for x in name if x.isalpha()]
        name_str = ''.join(name_str)
        data = data[data['description_str'].str.contains(name_str.replace("[^A-Za-z0-9]", ''), case=False)]
        
    if category:
        data = data[data['foodCategory'].str.contains(category, case=False)]
    if nutrient:
        data = data[data['name'].str.contains(nutrient, case=False)]
    if data.empty:
        return ItemListDict(items=data.to_dict(orient="records"))
    data = (data.groupby([data['description'],data['foodCategory'],data['proteinValue'],data['carbohydrateValue'],data['fatValue'],data['gramWeight'],data['portion']])
       .apply(lambda x: [{"name":k,"weight":v} for k, v in zip( x['name'],x['ammount'])])
       .reset_index(name='nutrients'))
    return ItemListDict(items=data.to_dict(orient="records"))

@router.post("/search_by_nutrients", response_model=ItemListDict)
async def search_by_nutrients(nutrientsList: Optional[List[str]] = []):
    if nutrientsList == []:
        mainPath = os.path.dirname(os.path.abspath(__file__))
        data = pd.read_csv(mainPath+'/finalData.csv')
        data = data.fillna('')
        data = (data.groupby([data['name'],data['type']])
       .apply(lambda x: [{k:v} for k, v in zip( x['description'],x['ammount'])])
       .reset_index(name='food'))
        return ItemListDict(items=data.to_dict(orient="records"))

    else:
        mainPath = os.path.dirname(os.path.abspath(__file__))
        data = pd.read_csv(mainPath+'/finalData.csv')
        data = data.fillna('')
        data = data[data['name'].isin(nutrientsList)]
        data = (data.groupby([data['name'],data['type']])
       .apply(lambda x: [{k:v} for k, v in zip( x['description'],x['ammount'])])
       .reset_index(name='food'))
        return ItemListDict(items=data.to_dict(orient="records"))
    
@router.get("/nutrients", response_model=ItemList)
async def nutrients():
    mainPath = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(mainPath+'/finalData.csv')
    data = data.fillna('')
    nutrientsList = data['name'].unique()
    return ItemList(items=nutrientsList.tolist())


