import json

def lambda_handler(event, context):
    # 1. รับค่าที่ส่งมาจาก URL (เช่น ?text=hello)
    # ถ้าไม่มีการส่งมา ให้ใช้ค่า Default
    query_params = event.get('queryStringParameters')
    user_text = "No text provided"
    
    if query_params and 'text' in query_params:
        user_text = query_params['text']
    
    # 2. จำลองการวิเคราะห์ (Keyword Matching)
    # ในโลกจริง ตรงนี้คือจุดที่เราจะเรียก AI Model
    sentiment = "Neutral 😐"
    score = 0.0
    
    # แปลงเป็นตัวเล็กเพื่อให้ตรวจง่าย
    lower_text = user_text.lower()
    
    positive_words = ['good', 'great', 'love', 'happy', 'awesome', 'best']
    negative_words = ['bad', 'sad', 'hate', 'angry', 'terrible', 'worst']
    
    if any(word in lower_text for word in positive_words):
        sentiment = "Positive 😊"
        score = 0.9
    elif any(word in lower_text for word in negative_words):
        sentiment = "Negative 😠"
        score = -0.9
        
    # 3. ส่งผลลัพธ์กลับ (Return JSON)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Serverless API Success!',
            'input': user_text,
            'result': sentiment,
            'confidence': score
        })
    }
