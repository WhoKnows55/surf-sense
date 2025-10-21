# 🏄 SurfSense: A Conversational Agentic Framework for Surf Trip Planning with Integrated Forecasting

## 📝 Overview

[cite_start]**SurfSense** is a master's thesis project developed as a **conversational agent** [cite_start]designed to streamline and enhance the process of planning a surf trip. [cite_start]It addresses the current challenge of having to check various, scattered sources for essential information—like weather forecasts, wave conditions, tide charts, and practical logistics—by unifying them into a single, intelligent, conversational interface.

[cite_start]The core innovation is the integration of **Large Language Model (LLM)** capabilities with an **agentic framework** to provide surf planning advice, intelligent forecasting, and contextual awareness. [cite_start]This project was completed for the Master in Data Science and Advanced Analytics program at NOVA IMS Management School.

---

## ✨ Key Features & Objectives

[cite_start]SurfSense aims to provide a user-centered decision support system that overcomes the limitations of existing static forecasting tools.

* [cite_start]**Conversational Trip Planning:** Design a conversational agent that assists in **personalized surf trip planning**.
* [cite_start]**Integrated Surf Forecasting:** Integrate surf condition forecasting (e.g., **wave height, swell interval, tide**) using time series models (like **Prophet** or **ARIMA**) or external APIs (like **MagicSeaWeed** or **Stormglass**).
* [cite_start]**Contextual Enrichment:** Enrich planning capabilities with contextual data such as **beach accessibility, parking, and local surf spot characteristics**.
* [cite_start]**Modular Architecture:** Develop a modular forecasting integration that can operate in **low-resource or offline environments**.

---

## 🛠️ Methodological Approach

### System Architecture

[cite_start]The system utilizes a hybrid architecture combining a **Large Language Model (LLM)** with **LangChain**.

* [cite_start]**LLM + LangChain:** This setup orchestrates the agent's **reasoning**, manages the user **dialogue**, and executes external API calls, allowing the agent to carry out **multi-step planning** based on user inputs.
* [cite_start]**Forecasting Component:** This component integrates existing surf and weather forecast APIs (e.g., MagicSeaWeed or Stormglass) directly into the agentic workflow for real-time predictions, or uses lightweight time series models (Prophet or ARIMA).
* [cite_start]**Contextual Layer:** This layer is introduced for enriched recommendations and draws from auxiliary APIs or knowledge bases for **parking availability, beach reviews, and safety warnings**, adding **situational awareness** to the system.

### Expected Results

[cite_start]The primary deliverable is a **working prototype** of a conversational agent that intelligently assists users in planning surf trips, merging LLM capabilities with agentic-generated forecasts and local knowledge.

---

## 🚀 Installation and Usage

*(The specific installation steps will depend on the final implementation. Fill in these sections based on your code.)*

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/WhoKnows55/surf-sense.git]
    (https://github.com/WhoKnows55/surf-sense.git)
    cd surfsense-thesis
    ```
2.  **Setup Environment:**
    ```bash
    # Assuming Python and pip
    pip install -r requirements.txt
    ```
3.  **Configure API Keys:**
    * Set up necessary environmental variables for your LLM and external forecasting APIs (e.g., `OPENAI_API_KEY`, `STORMGALSS_API_KEY`).
    * *(Tip: Create a `.env` file based on the provided `.env.example`)*
4.  **Run the Application:**
    * *(Example for a Streamlit interface):*
        ```bash
        streamlit run app.py
        ```
    * *(Example for a console or API service):*
        ```bash
        python main.py
        ```

---

## 📚 Thesis Contributions

[cite_start]This project contributes to the fields of LLM agents, forecasting, and human-computer interaction by:

* [cite_start]**Real-time Forecasting Application:** Providing a prototype application of LLM-based agentic frameworks to **real-time forecasting and contextual planning**.
* [cite_start]**Modular Forecasting Integration:** Demonstrating a modular forecasting integration design that can operate effectively in both high- and **low-resource or offline environments**.

---

## 👤 Author & Supervisor

* [cite_start]**Author:** Joshua Wehr 
* **Year:** 2025
* [cite_start]**Program:** Master in Data Science and Advanced Analytics 
* [cite_start]**Supervisor:** Prof. Bruno Jardim 





## Phi3_mini.py as Conversational Chat Bot

This repository contains a small demo agent (`agents/Phi3_mini.py`) that runs a conversational loop using Hugging Face's transformers pipeline. The script is intentionally lightweight and can run on CPU or CUDA-capable GPUs.

1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

2. Install minimal dependencies:

```bash
pip install transformers torch
```

3. Run the conversational agent (force CPU if you don't have CUDA):

```bash
# force CPU
python3 agents/Phi3_mini.py --cpu

# use GPU if available
python3 agents/Phi3_mini.py
```

The default model is `microsoft/Phi-3-mini-4k-instruct`. The model will be downloaded automatically when first run. If the model
requires authentication, set your Hugging Face credentials before running (for example by using `huggingface-cli login` or
setting the `HUGGINGFACE_TOKEN` environment variable).

## Tests

There is a tiny import test under `tests/test_phi3_mini_import.py` that verifies the module can be imported. Run tests with pytest:

```bash
pip install pytest
pytest -q
```


## Have Fun Surfing! 🤙🏽
