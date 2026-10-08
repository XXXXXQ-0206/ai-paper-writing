# preliminaries corpus (11 sources)

@src https://arxiv.org/abs/2106.09685
@title LoRA: Low-Rank Adaptation of Large Language Models
@section Problem Statement

While our proposal is agnostic to training objective, we focus on language modeling as our motivating use case.

Below is a brief description of the language modeling problem and, in particular, the maximization of conditional probabilities given a task-specific prompt.

Suppose we are given a pre-trained autoregressive language model MATH parametrized by MATH .

For instance, MATH can be a generic multi-task learner such as GPT based on the Transformer architecture .

Consider adapting this pre-trained model to downstream conditional text generation tasks, such as summarization, machine reading comprehension (MRC), and natural language to SQL (NL2SQL).

Each downstream task is represented by a training dataset of context-target pairs: MATH , where both MATH and MATH are sequences of tokens.

For example, in NL2SQL, MATH is a natural language query and MATH its corresponding SQL command; for summarization, MATH is the content of an article and MATH its summary.

During full fine-tuning, the model is initialized to pre-trained weights MATH and updated to MATH by repeatedly following the gradient to maximize the conditional language modeling objective:

One of the main drawbacks for full fine-tuning is that for each downstream task, we learn a different set of parameters MATH whose dimension MATH equals MATH .

Thus, if the pre-trained model is large (such as GPT-3 with MATH ), storing and deploying many independent instances of fine-tuned models can be challenging, if at all feasible.

In this paper, we adopt a more parameter-efficient approach, where the task-specific parameter increment MATH is further encoded by a much smaller-sized set of parameters MATH with MATH .

The task of finding MATH thus becomes optimizing over MATH :

In the subsequent sections, we propose to use a low-rank representation to encode MATH that is both compute- and memory-efficient.

When the pre-trained model is GPT-3 175B, the number of trainable parameters MATH can be as small as MATH of MATH .

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section Preliminaries

Robot learning. We aim to learn robot policies to solve language-conditioned tasks from vision. Formally, we consider a sequential decision-making environment. At timestep MATH , the policy MATH is presented with a language instruction MATH and an initial image observation MATH . The policy produces an action distribution MATH from which an action MATH is sampled and applied to the robot. This process continues, with the policy iteratively producing actions MATH by sampling from a learned distribution MATH and applying those actions to the robot. The interaction ends when a termination condition is achieved.

The full interaction MATH from from the starting step MATH to terminating step MATH is referred to as an episode.

At the end of an episode, the agent will be given a binary reward MATH indicating whether the robot performed the instruction MATH . The goal is to learn a policy MATH that maximizes the average reward, in expectation over a distribution of instructions, starting states MATH , and transition dynamics.

RT-1 uses a Transformer to parameterize the policy MATH . Generally speaking, a Transformer is a sequence model mapping an input sequence MATH to an output sequence MATH using combinations of self-attention layers and fully-connected neural networks. While Transformers were originally designed for text sequences, where each input MATH and output MATH represents a text token, they have been extended to images as well as other modalities .

As detailed in the next section, we parameterize MATH by first mapping inputs MATH to a sequence MATH and action outputs MATH to a sequence MATH before using a Transformer to learn the mapping MATH .

Imitation learning methods train the policy MATH on a dataset MATH of demonstrations . Specifically, we assume access to a dataset MATH of episodes, all of which are successful (i.e., have a final reward of MATH ).

We learn MATH using behavioral cloning , which optimizes MATH by minimizing the negative log-likelihood of actions MATH given the images and language instructions.

@src https://arxiv.org/abs/2305.18290
@title Direct Preference Optimization: Your Language Model is Secretly a Reward Model
@section Preliminaries

We review the RLHF pipeline in (and later ). It usually includes three phases: 1) supervised fine-tuning (SFT); 2) preference sampling and reward learning and 3) RL optimization.

SFT: RLHF typically begins by fine-tuning a pre-trained LM with supervised learning on high-quality data for the downstream task(s) of interest (dialogue, summarization, etc.), to obtain a model MATH .

Reward Modelling Phase: In the second phase the SFT model is prompted with prompts MATH to produce pairs of answers MATH . These are then presented to human labelers who express preferences for one answer, denoted as MATH where MATH and MATH denotes the preferred and dispreferred completion amongst MATH respectively. The preferences are assumed to be generated by some latent reward model MATH , which we do not have access to. There are a number of approaches used to model preferences, the Bradley-Terry (BT) model being a popular choice (although more general Plackett-Luce ranking models are also compatible with the framework if we have access to several ranked answers). The BT model stipulates that the human preference distribution MATH can be written as:

Assuming access to a static dataset of comparisons MATH sampled from MATH , we can parametrize a reward model MATH and estimate the parameters via maximum likelihood. Framing the problem as a binary classification we have the negative log-likelihood loss:

where MATH is the logistic function. In the context of LMs, the network MATH is often initialized from the SFT model MATH with the addition of a linear layer on top of the final transformer layer that produces a single scalar prediction for the reward value . To ensure a reward function with lower variance, prior works normalize the rewards, such that MATH for all MATH .

RL Fine-Tuning Phase: During the RL phase, the learned reward function is used to provide feedback to the language model. Following prior works , the optimization is formulated as

where MATH is a parameter controlling the deviation from the base reference policy MATH , namely the initial SFT model MATH .

In practice, the language model policy MATH is also initialized to MATH . The added constraint is important, as it prevents the model from deviating too far from the distribution on which the reward model is accurate, as well as maintaining the generation diversity and preventing mode-collapse to single high-reward answers. Due to the discrete nature of language generation, this objective is not differentiable and is typically optimized with reinforcement learning. The standard approach has been to construct the reward function MATH , and maximize using PPO .

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Task Formulation

A model is given an issue text description and a complete codebase.

The model is then tasked to make an edit to the codebase to resolve the issue.

In practice, we represent edits as patch files, which specify which lines in the codebase to modify in order to resolve the issue.

To evaluate a proposed solution, we apply the generated patch, using unix's patch program, to the codebase and then execute the unit and system tests associated with the task instance.

If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue.

The metric for our benchmark is the percentage of task instances that are resolved.

Additional technical details in Appendix .

Traditional benchmarks in NLP typically involve only short input and output sequences and consider somewhat "contrived" problems created specifically for the benchmark.

In contrast, 's realistic construction setting imbues the dataset with unique properties, which we discuss below.

Since each task instance in consists of a large and complex codebase and a description of a relevant issue, solving requires demonstrating sophisticated skills and knowledge possessed by experienced software engineers but are not commonly evaluated in traditional code generation benchmarks.

Our collection process can be easily applied to any Python repository on GitHub and requires minimal human intervention.

Therefore, we can extend with a continual supply of new task instances and evaluate LMs on issues created after their training date, which ensures that the solution was not included in their training corpus.

Issue descriptions are typically long and detailed ( MATH words on average), and codebases regularly contain many thousands of files.

Solving requires identifying the relatively small number of lines that need to be edited to solve an issue amongst a sea of context.

For each task instance, there is at least one fail-to-pass test which was used to test the reference solution, and MATH of instances have at least two fail-to-pass tests.

These tests evaluate whether the model addressed the problem in the issue.

In addition, a median of MATH additional tests run to check whether prior functionality is properly maintained.

Unlike prior settings that may constrain edit scope to an individual function or class or provide cloze-style fill-in blanks , does not provide such explicit guidance.

Rather than merely having to produce a short code snippet,

our benchmark challenges models to generate revisions in multiple locations of a large codebase.

's reference solutions average editing MATH files, MATH functions, and MATH lines (added or removed).

The task of repository-scale code editing can serve as a level playing field to compare approaches ranging from retrieval and long-context models to decision-making agents, which could reason and act in code.

also allows creative freedom, as models can generate novel solutions that may deviate from the reference PR.

Evaluating LMs on SWE-bench can be time-consuming and, depending on the model, require a costly amount of compute or API credits.

Given that initial performance returns as presented in Section are quite low, 's difficulty makes it useful for gauging LM progress in the long term, but potentially intimidating for initial systems that attempt to make progress in the short term.

To encourage adoption of SWE-bench, we create a Lite subset of MATH instances from SWE-bench that have been sampled to be more self-contained, with a focus on evaluating functional bug fixes.

The full filtering criteria and dataset information is included in

SWE-bench Lite covers MATH of the original MATH repositories, with a similar diversity and distribution of task instances across repositories as the original.

Full details of the Lite split and filtering details are included in Appendix .

It is important to benchmark the performance of open models on alongside proprietary models.

At the time of writing, only the CodeLlama models are able to handle the very long contexts necessary.

However, we observe that the off-the-shelf CodeLlama variants are not capable of following the detailed instructions to generate repository-wide code edits, and typically output placeholder responses or unrelated code. To better evaluate the capabilities of these models, we perform supervised fine-tuning on the MATH billion- and MATH billion-parameter CodeLlama-Python models. The resulting models are specialized repository editors that can run on consumer hardware and resolve GitHub issues.

Training data. We follow our data collection procedure and collect MATH issue-PR pairs from an additional 37 popular Python package repositories. In contrast to Section , we do not require that pull requests contribute test changes.

This allows us to create a much larger training set to use for supervised fine-tuning.

To eliminate the risk of data contamination, the set of repositories in the training data is disjoint from those included in the evaluation benchmark.

Given the instructions, an issue text from GitHub and the relevant code files as the prompt, we finetune to generate the patch that solved the given issue (the "gold patch").

For memory efficiency, we fine-tune only the weights of the attention sublayer using LoRA , and exclude training sequences with more than MATH tokens, reducing the effective size of the training corpus to MATH instances. More details are provided in Appendix .

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Preliminary

Transformer models require explicit positional information, often in the form of position embedding, to represent the order of input tokens. Our work focuses on the RoPE position embedding, which is widely used in recent LLMs. For a token at position index MATH , its corresponding RoPE encoding can be simplified as follows:

MATH is the rotary angle of token at position MATH ,

MATH represents the rotation frequencies. In RoPE, the default base value of MATH is 10000.

Context window extension ratio MATH and positional interpolation . We define MATH as the ratio of extended context length MATH to the original length MATH : MATH .

To extend the context window from MATH to MATH , current positional interpolation methods

suggest downscaling rotation frequencies MATH based on extension ratio MATH . Let MATH , and MATH denote the actual rescale factor related to MATH ,

we unify these positional interpolation methods as follows:

positional interpolation (PI). PI suggests linear interpolation of position indices within the pre-trained length limit.

For a target extension ratio MATH , the rotation angles of all positions are linearly reduced by MATH across all RoPE dimensions.

However, this makes the position information very "crowded", hindering the model's ability distinguish closely positioned tokens. Therefore, PI tends to underperform at high extension ratios.

look at RoPE from an information encoding perspective and

apply the Neural Tangent Kernel (NTK) theory .

To mitigate the crowded-positions issue in PI, they suggest to distribute

interpolation pressure across RoPE dimensions.

It scales lower (high frequency) dimensions less and higher (low frequency) dimensions more, resulting in both positional interpolation and extrapolation, where MATH . The improved dynamic NTK adjusts the extension ratio at each position based on the current sequence length. Unlike PI, which necessitates fine-tuning, NTK-aware methods can extend context windows in non-fine-tuning scenarios, but usually with a maximum extension ratio of 4 MATH .

introduces a significant improvement to positional interpolation performance. It divides RoPE dimensions into three frequency-based groups, each with a different interpolation strategy. High frequency dimensions undergo extrapolation ( MATH =1), while low frequency dimensions use linear interpolation (PI). The RoPE dimensions that fall in-between employs the NTK.

The key of YaRN lies in its grouping of RoPE dimensions, which currently depends on human-led empirical experiments. This may result in sub-optimal performance for new LLMs.

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Problem Formulation

The two non-uniformities can lead to a vast solution space and introduce complexities in optimization. To address it, we frame the multidimensional non-uniform position interpolation optimization problem as a search problem.

For a LLM targeting a context window size of MATH and lengthy input documents MATH , where each MATH surpasses MATH in token length,

we denote the original rotary angle of the MATH dimension in RoPE embedding at token position MATH as MATH . The optimization problem is then formulated as follows:

where we introduce a set of rescale factors, MATH , to cover the two forms of non-uniformities. MATH and MATH denote the non-uniformity of RoPE dimensions and token positions, respectively. Specifically,

we use MATH to rescale the rotation angle for the MATH RoPE dimension, where MATH is the rescale factor and MATH is token position threshold. For initial MATH -1 token positions, the rescale factor MATH will not take effect, and the original RoPE rotary angle MATH is used. For tokens at positions MATH , the rescale factor is applied.

Given a target context window size of MATH , our objective is to find the optimal rescale factors ( MATH , MATH ,... MATH ...) from the MATH to MATH RoPE dimension. As a result, the target MATH , with the rescaled MATH , can achieve a minimum next token prediction loss, MATH (i.e., the perplexity), for input samples MATH with a token length of MATH .

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Problem Formulation

The two non-uniformities can lead to a vast solution space and introduce complexities in optimization. To address it, we frame the multidimensional non-uniform position interpolation optimization problem as a search problem.

For a LLM targeting a context window size of MATH and lengthy input documents MATH , where each MATH surpasses MATH in token length,

we denote the original rotary angle of the MATH dimension in RoPE embedding at token position MATH as MATH . The optimization problem is then formulated as follows:

where we introduce a set of rescale factors, MATH , to cover the two forms of non-uniformities. MATH and MATH denote the non-uniformity of RoPE dimensions and token positions, respectively. Specifically,

we use MATH to rescale the rotation angle for the MATH RoPE dimension, where MATH is the rescale factor and MATH is token position threshold. For initial MATH -1 token positions, the rescale factor MATH will not take effect, and the original RoPE rotary angle MATH is used. For tokens at positions MATH , the rescale factor is applied.

Given a target context window size of MATH , our objective is to find the optimal rescale factors ( MATH , MATH ,... MATH ...) from the MATH to MATH RoPE dimension. As a result, the target MATH , with the rescaled MATH , can achieve a minimum next token prediction loss, MATH (i.e., the perplexity), for input samples MATH with a token length of MATH .

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Collaborative Data Annotation

The process initiates with the application of InsTag , an open-set fine-grained tagger, to extract the underlying ontology from a large-scale instruction dataset.

Subsequent manual refinement ensures the accuracy of the extracted ontology.

Each instruction, with tags annotated, is evaluated for tag diversity, semantic richness, complexity, and intent completeness.

Based on these criteria, we select a set of representative instructions .

To enrich the instruction dataset, a self-evolution strategy is employed, prompting the Qwen models to add constraints or requirements to existing instructions, thereby increasing their complexity and ensuring a diverse range of difficulty levels within the dataset.

Multiple responses to an instruction are obtained using diverse generation strategies and Qwen models of different scales.

Annotators rank these responses based on their preferences, ensuring the best response meets established criteria, yielding both demonstration and preference data.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Annotation protocol

A diagram of the annotation protocol used in our data engine is shown in fig:samv_annot_guideline . The annotation task was separated into steps each carried out by a different annotator: Steps 1 and 2 focus on object selection, Steps 3 and 4 on masklet tracking, and Step 5 on quality verification. SAM 2 was deployed on GPU as an API and built into the annotation tool to enable interactive use.

Compared to image segmentation annotation, large-scale video segmentation annotation presents unique challenges which require innovations in the annotation task design and protocol. To improve our model's ability to "segment anything", it was important to focus annotation on challenging objects where SAM 2 struggled. We leveraged our online model in the loop setup to enable this, requesting annotators to use SAM 2 interactively to identify failure modes and then correct them.

We found the number of edited frames to be a proxy to the "challengingness" of an object as shown in tab:data-quality . Therefore, we asked annotators to annotate objects that required at least 2 edited frames with SAM 2 in the loop. To focus annotation on less prominent and more challenging cases, annotators were presented with videos pre-filled with verified satisfactory automatic masklets and asked to find un-annotated challenging objects. We further decouple the object selection task from the annotation task: in the selection task annotators focus on choosing the challenging objects in one frame, while in the annotation task annotators are presented with a challenging target object and requested to annotate the masklet consistently throughout the video.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Data annotation card

At a high level, what are the subjective aspects of your task?

Selecting objects to mask and track in a video is inherently a subjective task, and annotators might differ in their decision to mask objects.

What assumptions do you make about annotators?

We assume our annotators understand the PVS task and are well trained on video related tasks. Our annotators worked full time on our annotation task. This made it possible to train the annotators by sharing feedback on a regular basis.

How did you choose the specific wording of your task instructions? What steps, if any, were taken to verify the clarity of task instructions and wording for annotators?

(1) The task instructions included visual examples (images and videos) to provide clarity. (2) Annotators were well trained before working on production queues. (3) The research team shared feedback daily and met with the annotators weekly for Q&A sessions.

What, if any, risks did your task pose for annotators and were they informed of the risks prior to engagement with the task?

Annotators were informed to reject objectionable videos.

What are the precise instructions that were provided to annotators? See detail in for annotation instructions.

Are there certain perspectives that should be privileged? If so, how did you seek these perspectives out? We chose to work with annotators with previous video annotation experience.

Are there certain perspectives that would be harmful to include? If so, how did you screen these perspectives out? No.

Were sociodemographic characteristics used to select annotators for your task? If so, please detail the process.

For masklet annotations, sociodemographic characteristics were not used to select the annotators. For video collection, we emphasized the importance of diversity among the crowdworkers to our third-party vendor. While it was not a strict requirement, we encouraged the inclusion of a diverse group of crowdworkers to enrich the data collection process with a wide range of perspectives. This approach aimed to naturally incorporate diversity without imposing strict selection based on sociodemographic factors.

If you have any aggregated socio-demographic statistics about your annotator pool, please describe. Do you have reason to believe that sociodemographic characteristics of annotators may have impacted how they annotated the data? Why or why not?

Aggregated socio-demographic statistics about the crowdworkers who collected the videos are presented in .

Consider the intended context of use of the dataset and the individuals and communities that may be impacted by a model trained on this dataset. Are these communities represented in your annotator pool?

The SA-V dataset is a geographically diverse, publicly available, video segmentation dataset, as discussed in . In addition, we analyze the responsible AI axes of a model trained on the dataset, as discussed in .

What annotation platform did you utilize? At a high level, what considerations informed your decision to choose this platform? Did the chosen platform sufficiently meet the requirements you outlined for annotator pools? Are any aspects not covered?

We used an internal annotation platform.

What, if any, communication channels did your chosen platform offer to facilitate communication with annotators? How did this channel of communication influence the annotation process and/or resulting annotations?

The research team shared feedback daily and met with the annotators weekly to align on the task instructions and expectations and to hold Q&A sessions. Outside of those sessions, annotators had access to a spreadsheet and chat group to facilitate communication with the research team.

How much were annotators compensated? Did you consider any particular pay standards, when determining their compensation? If so, please describe.

(1) The video collecting crowdworkers were compensated with an hourly wage set by the vendor. (2) Annotators were compensated with an hourly wage set by the vendor.

How do you define the quality of annotations in your context, and how did you assess the quality in the dataset you constructed?

Annotators were required to follow a training before moving to production queues. Annotators followed a 2-day training session led by the vendor and then were asked to annotate jobs from a training queue. Annotators were able to move from training to production after the vendor Q&A team or the research team reviewed their work and assessed quality. On average, annotators spent 1 - 2 weeks in training before moving to production. Similarly, the vendor and research team Q&A manually reviewed the production queues’ annotations daily, sharing feedback daily.

Have you conducted any analysis on disagreement patterns? If so, what analyses did you use and what were the major findings? Did you analyze potential sources of disagreement?

The disagreement patterns were shared daily and weekly during feedback and Q&A sessions.

How do the individual annotator responses relate to the final labels released in the dataset? The final labels are after data cleaning and post processing from the individual annotator responses.

Do you have reason to believe the annotations in this dataset may change over time? Do you plan to update your dataset? No.

Are there any conditions or definitions that, if changed, could impact the utility of your dataset? No.

Will you attempt to track, impose limitations on, or otherwise influence how your dataset is used? If so, how?

The SA-V dataset is released under a permissive CC by 4.0 license.

Were annotators informed about how the data is externalized? If changes to the dataset are made, will they be informed? No.

Is there a process by which annotators can later choose to withdraw their data from the dataset? If so, please detail. No.

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Preliminaries

In recent years, denoising diffusion probabilistic models (DDPMs) have demonstrated unprecedented performance in text-to-image/video generation in continuous state spaces, particularly exemplified by the popular Stable Diffusion series . Concurrently, discrete denoising diffusion probabilistic models (D3PMs) have also shown impressive capabilities in modeling data in discrete form, featuring models like VQ-Diffusion and Copilot4D . Further, MaskGIT and Muse have demonstrated a simplified discrete diffusion that can effectively model discrete image tokens. Our Show-o model is built upon MaskGIT so that both such discrete visual and textual tokens can share a unified learning objective format.

In the following, we provide preliminaries for diffusion models and draw the connection between discrete diffusion and mask token prediction employed in MaskGIT.

In diffusion models, the forward process MATH corrupts the image data MATH into latent variables MATH in different noise level. The reverse Markov process is learned to iteratively remove the noises added to the latent variables towards the real image distribution MATH . In the continuous scenario, the transition distribution MATH is commonly characterized by a Gaussian distribution:

where the mean is MATH and the variance is MATH . For images tokenized into MATH (i.e., the codebook size) categorical random variables MATH and given a MATH state, the transition distribution is instead formulated by a stochastic transition matrix MATH :

where MATH , MATH indicates the row vector-matrix product, and MATH is a categorical distribution over the one-hot row vector MATH given by MATH . When the transition matrix MATH is applied to each image token in a sequence, the marginal and posterior at time step MATH and MATH , respectively, are formulated as:

where MATH because of the Markov property.

In the following, we introduce the Absorbing-Uniform Discrete Diffusion by defining the stochastic transition matrix MATH as follows:

where MATH is a one-hot vector with a value of 1 at the index of MATH token, MATH , and MATH . Here, MATH and MATH represent the probabilities of an image token transforming into the MATH token and non- MATH token at time step MATH , respectively. Specifically, the matrix form of MATH can be written as:

where MATH and MATH . Intuitively, during the corruption process, each image token in the sequence has a probability of MATH to be replaced by the MATH token, a chance of MATH to be uniformly diffused, and a probability of MATH remain unchanged. Besides, if a token turns into a MATH token, it will stay in the same MATH state during the following corruption process. Likewise, MATH can be accordingly derived. An illustration of the image corruption process using MATH token is provided in Fig. .

The evidence-lower bound (ELBO) for the variational diffusion models is:

Considering the proposition in and the following parameterization of the reverse process:

the variational lower bound can be further expressed under the image distribution MATH (referring to the proof provided by as detailed in the Appendix ):

When deriving this lower bound, the discrete diffusion paradigm can be further simplified by restricting each image token to be either unchanged or replaced with the MATH token, with no possibility of becoming other categorical variables.

The resulting lower bound is effectively the Cross-Entropy loss used in MaskGIT , which is the mask token prediction to learn a neural network MATH to reconstruct masked regions of MATH from the noised MATH . In this work, we follow MaskGIT to integrate this simplified discrete diffusion paradigm into Show-o because of its simplicity. Further, Muse has successfully scaled up such a paradigm for text-to-image models of 3B parameters using 460M image-text pairs.
