from cProfile import label
import gradio as gr
import tempfile
import doc_generator as dg

def generate_doc(file):
    documented_file = dg.main(file)
    return documented_file
            

demo = gr.Interface(
    fn=generate_doc,
    inputs=gr.File(file_count='1', label='Notebook'),
    outputs=gr.File(file_count='1', label='Documented Notebook')
)

demo.launch(share=True)