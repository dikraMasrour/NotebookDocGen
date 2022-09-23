import gradio as gr
import gradio_run as grun

def classify(file):
    classification_tuple = grun.main(file)
    return classification_tuple[0], classification_tuple[1]
            

demo = gr.Interface(
    fn=classify,
    inputs=gr.File(file_count='1', label='Notebook'),
    outputs=[gr.Text(label='Notebook predicted domain'), gr.Text(label='Notebook predicted technique')]
)

demo.launch(share=True)
