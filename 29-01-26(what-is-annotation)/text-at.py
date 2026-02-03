import pandas as pd

# Semtimental Annotation
data = {
    "text" : ["I love this product","This Service is bad","This prduct id ok"],
    "label" : ["positive","negative","neutral"]
}

df = pd.DataFrame(data)

print("\n Semtimental Annotation \n",df)

