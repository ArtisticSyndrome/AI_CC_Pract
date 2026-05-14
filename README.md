# AI Practicals

Collection of artificial intelligence practice programs, a practical notebook, and cloud-computing reference PDFs.

## Repository Layout

```text
.
+-- All_ai_pract.ipynb
+-- cloud_comp_pdf/
|   +-- CCP1 (1).pdf
|   +-- P3.pdf
|   +-- P4 (1).pdf
+-- seperate_Codes_AI/
    +-- 2_A_Star.py
    +-- BFS_DFS_Recurse.py
    +-- Greedy_SelectionSort.py
    +-- MedicalExpertSystem.py
    +-- bankcusbot.py
    +-- colourgraph.py
```

## Programs

| File | Description |
| --- | --- |
| `seperate_Codes_AI/BFS_DFS_Recurse.py` | Breadth-first search and recursive depth-first search on a sample graph. |
| `seperate_Codes_AI/2_A_Star.py` | A* search on a predefined weighted graph. |
| `seperate_Codes_AI/colourgraph.py` | Graph coloring using backtracking. |
| `seperate_Codes_AI/Greedy_SelectionSort.py` | Selection sort implementation. |
| `seperate_Codes_AI/MedicalExpertSystem.py` | Rule-based symptom checker. |
| `seperate_Codes_AI/bankcusbot.py` | Simple banking chatbot using regex and NLTK utilities. |
| `All_ai_pract.ipynb` | Notebook for AI practical work. |
| `cloud_comp_pdf/*.pdf` | Cloud-computing reference material. |

## Requirements

Most scripts use only the Python standard library. The banking chatbot requires NLTK:

```bash
pip install nltk
```

The first chatbot run may download NLTK `punkt` and `stopwords` data automatically.

## Usage

Run scripts from the repository root:

```bash
python seperate_Codes_AI/BFS_DFS_Recurse.py
python seperate_Codes_AI/2_A_Star.py
python seperate_Codes_AI/colourgraph.py
python seperate_Codes_AI/Greedy_SelectionSort.py
```

Interactive examples:

```bash
python seperate_Codes_AI/MedicalExpertSystem.py
python seperate_Codes_AI/bankcusbot.py
```

Open the notebook with Jupyter:

```bash
jupyter notebook All_ai_pract.ipynb
```

## Notes

These programs are intended for learning and demonstration. The medical expert system and banking chatbot are simple rule-based examples, not production systems.
