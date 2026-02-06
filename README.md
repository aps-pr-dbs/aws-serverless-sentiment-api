# ⚡ Serverless Sentiment Analysis API on AWS

โปรเจกต์นี้คือการพัฒนา **REST API แบบ Serverless 100%** บน AWS Cloud โดยไม่ต้องมีการเช่า Server ทิ้งไว้ (No-Ops) ระบบจะทำงานเมื่อมีการเรียกใช้เท่านั้น (Event-driven)

## 🚀 Live Demo
ทดลองยิง API ผ่าน Browser ได้ทันที (รันบน AWS Lambda จริง):
👉 **[Click to Test API](https://4wnon6hefi.execute-api.ap-southeast-1.amazonaws.com/default/my-serverless-api?text=I%20love%20serverless%20architecture)**

---

## 🏗 Architecture
ระบบถูกออกแบบโดยใช้สถาปัตยกรรม **FaaS (Function as a Service)** เพื่อลดค่าใช้จ่ายและรองรับการขยายตัวอัตโนมัติ

* **Compute:** AWS Lambda (Python 3.12) - รันโค้ดเฉพาะตอนมี Request
* **API Gateway:** HTTP API - ประตูเชื่อมต่อระหว่างโลกภายนอกและ Lambda
* **Cost Efficiency:** **$0.00** maintenance cost (Scale to Zero เมื่อไม่มีคนใช้งาน)

## 💻 Code Logic (Python)
```python
# ตัวอย่าง Logic การทำงาน
def lambda_handler(event, context):
    text = event['queryStringParameters']['text']
    # Process sentiment...
    return {"result": "Positive", "confidence": 0.9}
