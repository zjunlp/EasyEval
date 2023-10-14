# EasyEval

---

## 🔧Installation

**Installation for local development:**

```
git clone https://github.com/zjunlp/EasyEval
cd EasyEval
pip install -e .
```
**Installation using PyPI:**
```
pip install easyeval -i https://pypi.org/simple
```
---

## 📌Use EasyEval

### FairEval

> `FairEval` is the class for  two simple yet effective strategies,
> namely Multiple Evidence Calibration (MEC) and Balanced Position Calibration (BPC) to calibrate the positional bias of LLMs.
> Refer to the paper: [Large Language Models are not Fair Evaluators](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2305.17926v1.pdf).

**Example**

**Step1: Provide the question json file for evaluation.** Here is an example of the data:
```json
{"question_id": 1, "text": "How can I improve my time management skills?"}
{"question_id": 2, "text": "What are the most effective ways to deal with stress?"}
```
**Step2: Provide the answer json files for evaluation.** Note that the question_id  must be consistent with the question file. Here is an example of the data:
```json
{"question_id": 1, "text": "Here are some tips to improve your time management skills:\n\n1. Create a schedule: Make a to-do list for the day ..."}
{"question_id": 2, "text": "Here are some effective ways to deal with stress:\n\n1. Exercise regularly: Physical activity can help reduce stress and improve mood ..."}
```
**Step3: Evaluation**
```python
from EasyEval.eval import FairEval

# Declare a eval class
eval = FairEval(answer_file_list=["YOUR-ANSWER-FILE1", "YOUR-ANSWER-FILE2"], question_file="YOUR-QUESTION-FILE",
                output="YOUR-OUTPUT-FILE", api_key="YOUR-KEY", eval_model='gpt-4', bpc=1, k=3)


# Get the result from LLM API service
eval.fair_eval()
```

---

## 🎉Contributors

<a href="https://github.com/zjunlp/EasyEval/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zjunlp/EasyEval" />
</a>