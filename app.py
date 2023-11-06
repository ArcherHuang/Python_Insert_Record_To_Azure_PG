# test_item:
#   Option 1: accuracy test
#   Option 2: fairness test
#   Option 3: reliability(MRC) test
#   Option 4: multiple choice test
#   Option 5: Taiwan culture test
#   Option 6: Privacy test
#   Option 7: Prompt injection test

# evaluation_result:
#   {
#     "評測資料集編號": "",
#     "評測項目描述": "",
#     "評測方法": "",
#     "評測參數": "",
#     "評測程式版本號": "",
#     "評測結果": "",
#   }
#   {
#     "evaluationDatasetNo": "evaluationdatasets/97a37562-93a0-413d-b35f-d5dc72d22766",
#     "evaluationItemDescription": "",
#     "evaluationMethod": "",
#     "evaluationParameter": {
#       "aaa": "bbb111",
#     },
#     "evaluationCodeVersion": "GitHub Commit SHA",
#     "evaluationResult": "success",
# }

import db_ops

evaluation_result = {
    "evaluationDatasetNo": "evaluationdatasets/97a37562-93a0-413d-b35f-d5dc72d22766",
    "evaluationItemDescription": "",
    "evaluationMethod": "",
    "evaluationParameter": {
      "aaa": "bbb111",
    },
    "evaluationCodeVersion": "bd30d437bee125befd7d5162d8a9f7fcf9baf57b",
    "evaluationResult": "success",
}

model_info_id = "'8d2bf4e7-50ef-4b0e-a24a-a19b07d1a091'"
user_info_id = "'b662007b-3878-415b-a40d-a15dd8b9b15f'"
test_item = "'Option 1: accuracy test'"

db_ops.insert(evaluation_result, model_info_id, user_info_id, test_item)