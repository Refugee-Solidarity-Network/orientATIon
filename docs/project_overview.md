# orientATIon Project Overview & Research Plan

## Project Overview

**What is the "orientATIon" project about, and why is is written like that?**
The orientATIon project's goal is to evaluate the feasibility of an LLM-powered chatbot for providing general orientation to protection-seekers regarding asylum procedures and other rights and obligations. The "ATI" in the name "orientATIon" stands for **A**cess **T**o **I**nformation.

**Access to Information**: Refers to the duty shared by governments, I/NGOs and other actors to assist communities facing forced displacement and other types of vulnerable conditions to be aware of their legal rights, obligations and entitlements ("know-your-rights") as a necessary precursor to _enacting_ those rights.

## Research Plan

### Establish a Baseline

Use AWS’ Bedrock platform to establish a performance baseline for answering asylum-related questions by directly querying available models with asylum-related questions without any fine-tuning or external systems (like RAG).

### Methodological Evaluations

**Fine-Tuning:**
Use a subset of the 120 existing question-answer pairs to fine-tune models, with the aim of producing custom models that are more adept at understanding and responding to asylum-specific inquiries. Compare the performance of the fine-tuned model against baselines in terms of: accuracy, specificity and relevance.

**Retrieval-Augmented Generation (RAG):**
Create a system which retrieves relevant documents or data from a database (e.g., embeddings database with a VectorDB) and passes this information (context) to LLM models before generating an answer. Assess the RAG approach in terms of: response time, accuracy, specificity and relevance.

**Agent Toolchain Approach:**
Create a system of multiple tools or methods which LLM models are instructed to utilize in order to generate the best-possible response. For example, first retrieve a document, then summarize it, then answer the query. Evaluate the effectiveness of this approach in terms of: response time, accuracy, specificity and relevance.

**Other AI/NLP Advancements:**
The three methods indicated above are just some of the approaches being applied to improve LLM outputs. As a part of this research project, it will be necessary to monitor emerging methodologies and/or tools which could be incorporated for evaluation.

### Technical Evaluations

**Cost Monitoring:**
In addition to substantive evaluation of each methodology, overall token use should also be tracked in order to provide information on total operating costs.

**Non-English Language Outputs:**
It will also be important to evaluate the effectiveness of these models when working with non-English inputs and outputs. To do so, we can harness Q&A pairs currently available in ten different languages.

**Ethical Evaluation**
We will evaluate the ethical implications of our evaluation results and the intervention model as a whole, including review of and engagement with the work of leading ethicists in this field.

### Documentation and Synthesis

We’ll need to thoroughly document our process, findings, challenges, insights and conclusions for each methodology we evaluate. To facilitate this process, research will be conducted in interactive Jupyter Notebook files for Python.

At the close of each evaluation, we’ll synthesize the results. Once we’ve completed all evaluations, we’ll work together to generate comprehensive insights on the current state of LLM-powered chatbots and their application within the scope of assisting protection-seekers with accessing information on asylum procedures, their rights and obligations. We’ll highlight strengths, weaknesses, opportunities and threats.

### Peer Review and Feedback

We will strive to engage with AI researchers, engineers and ethicists in order to garner external perspectives and publicize our core findings (e.g., through engagements in workshops and conferences).

### Final Report Preparation

We will compile research findings, expert feedback and evaluation results into a comprehensive final report. This document should serve as a guide for any organization or individual seeking to understand the feasibility and challenges of LLM-powered chatbots in the legal and asylum domain.

We will open-source our research project, enabling others to reproduce our findings. We will seek out publication opportunities, including academic journals, self-publishing, and/or white paper publishing with sponsors.
