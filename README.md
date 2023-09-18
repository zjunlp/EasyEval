# EasyEval

---

## 🔧Installation

**Installation for local development:**

```
git clone https://github.com/zjunlp/EasyEval
cd EasyEval
pip install -e .
```

---

## 📌Use EasyEval

### FairEval

> refer to the paper: [Large Language Models are not Fair Evaluators](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2305.17926v1.pdf).

**Example**

```python
from EasyEval.eval import FairEval

# Step1: Declare a eval class
eval = FairEval(answer_file_list=["YOUR-ANSWER-FILE1", "YOUR-ANSWER-FILE2"], question_file="YOUR-QUESTION-FILE",
            output="YOUR-OUTPUT-DIR", api_key="YOUR-KEY", eval_model='gpt-4')

# Step2: Get the result from LLM API service
eval.fair_eval()
```

---