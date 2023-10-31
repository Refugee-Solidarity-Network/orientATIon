# orientATIon

A research project evaluating the potentials and pitfalls of LLM-based chatbots for enabling personalized guidance to protection-seekers regarding procedures, their rights and obligations.

## Accessing the Development Environment

To make the development experience as smooth as possible, this project is using [GitPod](https://gitpod.io)'s Workspaces feature. This means that all contributors will have access to the same (containerized) development environment.

In order to access the GitPod Workspace, you'll need a Github account, and you'll have to be added to the [Refugee Solidarity Network organization](https://github.com/Refugee-Solidarity-Network) on Github, as well as to RSN's Amazon Web Services (AWS) organization.

Once you've been added to RSN's GitHub and AWS organizations, you'll be able to access the development environment by visiting [https://gitpod.io/#https://github.com/Refugee-Solidarity-Network/orientATIon](https://gitpod.io/#https://github.com/Refugee-Solidarity-Network/orientATIon).

**Note:** Because most of the work in this project will be done in Jupyter Notebooks, it is recommended to [use GitPod for the VS Code Desktop application](https://www.gitpod.io/docs/references/ides-and-editors/vscode).

#### Attach Your AWS Credentials to the Workspace

In order to access shared AWS services, it's necessary to attach your AWS credentials to the workspace each time it restarts. To do so, enter the following command in the local terminal: `aws sso login --no-browser` and follow the resulting prompts.

### Project Repository Structure

This project uses the following general structure:

```
.
├── data/
│   └── processed
├── docs/
├── notebooks/
├── reports/
├── .gitpod.Dockerfile
├── .gitpod.yml
├── configure_aws_with_gitpod.sh
├── README.md
└── requirements.txt
```

#### Notebook Naming Conventions

To keep things neat, please follow the naming convention `{YOUR_INITIALS}_{NOTEBOOK_TITLE}.ipnyb`. Notebook titles should be concise but descriptive of the individual notebook's function.

### Version Control and Collaboration with Git/Github

Since multiple contributors will be working within the same development environment and in this repository, we'll be using a Git-based workflow. Here a few important rules and reminders:

1. **Please commit your changes to a personal branch, and request that these changes be merged into the `main` branch with a Pull Request.** This type of workflow is essential to ensure that you do not inadvertendtly write over another contributor's code and to allow merge conflicts to be properly resolved.

2. Remember to commit and push your changes to your personal working branch! Because we're working in a collaborative (but ultimately, ephemeral) Docker container, local changes will not be persisted across sessions unless commited to the remote repository.

3. As different contributors will work on different aspects of this project and because we ultimately plan to publicize our research findings, please ensure that you document your contributions as you work. We will conduct most of our work in Jupyter Notebooks, allowing for text-rich descriptions of our process. Please also consider that other potential contributors may need to read and understand your commit messages and pull requests.

## Core Reference Documents

- [orientATIon Research Project Tasks Tracker](https://github.com/orgs/Refugee-Solidarity-Network/projects/1)
- [Guide for Onboarding New orientATIon Contributors](/docs/onboarding.md)
