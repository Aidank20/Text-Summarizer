import requests
from Config import API_KEY
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
headers={"Authorization": f"Bearer {API_KEY}"}
def summarize_text(text):
    payload={
        "inputs": text,
        "parameters": {
            "max_length": 100,
            "min_length": 30,
            "do_sample": False        
        }
    }
    try:
        response=requests.post(API_URL, headers=headers, json=payload)
        if response.status_code==200:
            return response.json()[0]['summary_text']
        else:
            return f"Error!: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error,Request Failed: {str(e)}"
def main():
    print("---- Text Summarizer ---")
    print("Type your text, then press Enter to summarize\nType 'exit' to quit.")
    while True:
        user_input=input("paste or type your text here: ").strip()
        if user_input.lower()=="quit":
            print("Exiting. Goodbye!")
            break
        if not user_input:
            print("Please enter some text to summarize.")
            continue
        print("Summarizing...")
        summary=summarize_text(user_input)
        print("\n--- Summary ---\n")
        print(summary)
if __name__=="__main__":
    main()
