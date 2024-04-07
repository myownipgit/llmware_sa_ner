
from llmware.models import ModelCatalog

model = ModelCatalog().load_model("slim-sa-ner-tool")

text = ("Tesla stock declined yesterday 8% in premnarket trading after a poorly recieved event in San Francisco " "yesterday, in which the company indicated a likely shortfall in revenue.")

response = model.function_call(text, function="classify", params=["sentiment,person,organisation,place"])

print("response: ", response)

# ModelCatalog().tool_test_run("slim-sa-ner-tool")