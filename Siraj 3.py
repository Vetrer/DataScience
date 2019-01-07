import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)
#print treino de teste de dados
print(repr(data['train']))
print(repr(data['test']))

#criação do modelo
model = LightFm(loss='warp')
#treinar modelo
model.fit(data['train'], epachs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

    #numero dos usuario e itens
    n_users, n_items = data['train'].shape

    #gerar recomendações
    for user_id in user_ids:

        #modelo que preve que todos vão gostar
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

       #modelo que preve que eles vão gostar
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print os resuktas
        print("User %s" % user_id)
        print("    Known positives:")

        for x in known_positives[:3]:
            print("           %s" %x)

        print("      Recommended:")

        for x in top_items[:3]:
            print("           %s" %x)

sample_recommendation(model, data, [3, 25, 450]) 
    
