from google import genai
from google.genai import types
import PIL.Image

client = genai.Client(api_key="AIzaSyBKkodP8T28FXLrAXR-Gzp56G8ZMqfr8-s")

def analyze_receipt(image_path):
    img = PIL.Image.open(image_path)
    prompt = "استخرج تفاصيل الحجز: الاسم، المبلغ، التاريخ، الحالة، ورقم الحجز."
    
    # سنستخدم 1.5-flash لأنه أكثر استقراراً في الحسابات المجانية
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=[prompt, img]
    )
    return response.text

try:
    print("جاري التحليل... (يرجى التأكد من مرور دقيقة على آخر محاولة)")
    result = analyze_receipt('test.jpg.jpeg')
    print("\n--- نتيجة فحص الحجز لروما بادل ---")
    print(result)
except Exception as e:
    print(f"حدث خطأ: {e}")