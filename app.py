import torch 
import gradio as gr

from transformers import pipeline


pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",torch_dtype= torch.bfloat16)   


def summary(input):
    output = pipe(input)
    return output[0]['summary_text']


gr.close_all()



demo = gr.Interface(fn=summary,
                    inputs=[gr.Textbox(label="Input text to summarize",lines=6)],
                    outputs=[gr.Textbox(label="Summarized text",lines=4)],
                    title="Text Summarizer",
                    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT")
demo.launch()
