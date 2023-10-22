from ..models import ResponseModel


def get_datasets(request_data, count):
    dataset =[]
    labels = {}

    for hour in range(24):
         for label_data in request_data[hour]:
              adress = label_data["adress"]
              if adress not in labels:
                   labels[adress] = [0] * 24
    for hour in range(24):
         for label_data in request_data[hour]:
              labels[label_data["adress"]][hour] = label_data["avg"]
    
    for label in labels:
         dataset.append({
              "label": label,
              "data": labels[label],
         })
    
    return dataset