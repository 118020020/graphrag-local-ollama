## 🤝 Contributing

**Based on the original version by TheAiSingularity, which connects Ollama and GraphRAG, this version further fixes some bugs, makes it even easier for implementation, and adds the testing for the [Acquired Dataset for RAG Evaluation](https://www.kaggle.com/datasets/harrywang/acquired-podcast-transcripts-and-rag-evaluation/)**

# 🚀 GraphRAG Local Ollama - Knowledge Graph

Welcome to **GraphRAG Local Ollama**! This repository is an exciting adaptation of Microsoft's [GraphRAG](https://github.com/microsoft/graphrag), tailored to support local models downloaded using Ollama. Say goodbye to costly OpenAPI models and hello to efficient, cost-effective local inference using Ollama!

## 📄 Research Paper

For more details on the GraphRAG implementation, please refer to the [GraphRAG paper](https://arxiv.org/pdf/2404.16130).

**Paper Abstract**

The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs)to answer questions over private and/or previously unseen document collections.However, RAG fails on global questions directed at an entire text corpus, suchas “What are the main themes in the dataset?”, since this is inherently a queryfocused summarization (QFS) task, rather than an explicit retrieval task. PriorQFS methods, meanwhile, fail to scale to the quantities of text indexed by typicalRAG systems. To combine the strengths of these contrasting methods, we proposea Graph RAG approach to question answering over private text corpora that scaleswith both the generality of user questions and the quantity of source text to be indexed. Our approach uses an LLM to build a graph-based text index in two stages:first to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely-related entities. Given aquestion, each community summary is used to generate a partial response, beforeall partial responses are again summarized in a final response to the user. For aclass of global sensemaking questions over datasets in the 1 million token range,we show that Graph RAG leads to substantial improvements over a na¨ıve RAGbaseline for both the comprehensiveness and diversity of generated answers. 

## 🌟 Features

- **Local Model Support:** Leverage local models with Ollama for LLM and embeddings.
- **Cost-Effective:** Eliminate dependency on costly OpenAPI models.
- **Easy Setup:** Simple and straightforward setup process.

## 📦 Installation and Setup

Follow these steps to set up this repository and use GraphRag with local models provided by Ollama :


1. **Create and activate a new conda environment:**
    ```bash
    conda create -n graphrag-ollama-local python=3.10
    conda activate graphrag-ollama-local
    ```

2. **Install Ollama:**
    - Visit [Ollama's website](https://ollama.com/) for installation instructions.
    - Or, run:
    ```bash
    pip install ollama
    ```

3. **Download the required models using Ollama, we can choose any llm and embedding model provided under Ollama:**
    ```bash
    ollama pull llama3:8b  #llm
    ollama pull nomic-embed-text  #embedding
    ```

4. **Clone the repository:**
    ```bash
    git clone https://github.com/118020020/graphrag-local-ollama.git
    ```

5. **Navigate to the repository directory:**
    ```bash
    cd graphrag-local-ollama/
    ```

6. **Install the graphrag package ** This is the most important step :**
    ```bash
    pip install -e .
    ```

7. **Init the testing environment**
    ```bash
    python -m graphrag.index --init --root ./ragtest
    ```

8. **Edit the settings.yaml file**
   Replace the original settings.yaml file under ./ragtest by the one under graphrag-local-ollama if you want to use llama3:8b as llm and nomic_embed_text as embedding model. 

9. **Find the ./ragtest/input folder, and put your sample data (you can download from kaggle in this case) in it. Notice that the data should be .txt format**
   The default dataset used is airbnb.txt under [Acquired Dataset for RAG Evaluation](https://www.kaggle.com/datasets/harrywang/acquired-podcast-transcripts-and-rag-evaluation/).

10. **Run the indexing, which creates a graph:**
    ```bash
    python -m graphrag.index --root ./ragtest
    ```

11. **Run a query: Only supports Global method or you can run query using the python file graph_rag_qa.py** 
    ```bash
    python -m graphrag.query --root ./ragtest --method global "When did Airbnb go public? What was the price per share?"
    ```
    or
     ```bash
    python graph_rag_script_qa.py
    ```
    graph_rag_abnb_qa.py is a file written to implement all the questions within one specific data file (find the script under path ./graphrag-local-ollama).

12. **Result for testing the 3 qa questions can be found at graph_rag_qa_result_airbnb.txt**
    Here shows the 3 questions:
    1). When did Airbnb go public, what was the price per share? 2). Why did Wimdu unlike Airbnb not take off? 3). Why does market fragmentation work for airline industry but could't work for Airbnb?
    Find the detailed answer in graph_rag_qa_result_airbnb.txt. The answer structre is as follows:
    * *Answer:
        INFO: the basic setup of the LLM model
        SUCCESS: the real answers for the questions here. * *
    
    
**Graphs can be saved which further can be used for visualization by changing the graphml to "true" in the settings.yaml :**
    
    snapshots:
    graphml: true
    
**To visualize the generated graphml files, you can use : https://gephi.org/users/download/ or the script provided in the repo visualize-graphml.py :**

Pass the path to the .graphml file to the below line in visualize-graphml.py:

    graph = nx.read_graphml('output/20240708-161630/artifacts/summarized_graph.graphml') 

13. **Visualize .graphml :**

    ```bash
    python visualize-graphml.py
    ```




## Citations

- Original GraphRAG repository by Microsoft: [GraphRAG](https://github.com/microsoft/graphrag)
- Ollama: [Ollama](https://ollama.com/)

---

By following the above steps, you can set up and use local models with GraphRAG, making the process more cost-effective and efficient.
