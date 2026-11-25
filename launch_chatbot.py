"""Launch the existing notebook app with the installed Python environment."""
import json
from pathlib import Path

def main():
    notebook = Path(__file__).with_name('rag_chatbot.ipynb')
    data = json.loads(notebook.read_text(encoding='utf-8'))
    namespace = {'__name__': '__main__'}
    for index, cell in enumerate(data['cells']):
        if cell['cell_type'] == 'code':
            exec(compile(''.join(cell['source']), str(notebook) + ':cell' + str(index), 'exec'), namespace)
    namespace['premium_chatbot'].block_thread()

if __name__ == '__main__':
    main()
