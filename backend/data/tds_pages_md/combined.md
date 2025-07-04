

# File: 1._Development_Tools.md

---
title: "1. Development Tools"
original_url: "https://tds.s-anand.net/#/development-tools?id=development-tools"
downloaded_at: "2025-05-31T21:34:43.013026"
---

[Development Tools](#/development-tools?id=development-tools)
=============================================================

**NOTE**: The tools in this module are **PRE-REQUISITES** for the course. You would have used most of these before. If most of this is new to you, please take this course later.

Some tools are fundamental to data science because they are industry standards and widely used by data science professionals. Mastering these tools will align you with current best practices and making you more adaptable in a fast-evolving industry.

The tools we cover here are not just popular, they’re the core technology behind most of today’s data science and software development.

[Previous

Tools in Data Science](#/README)

[Next

Editor: VS Code](#/vscode)

---


# File: 2._Deployment_Tools.md

---
title: "2. Deployment Tools"
original_url: "https://tds.s-anand.net/#/deployment-tools?id=deployment-tools"
downloaded_at: "2025-05-31T21:34:11.680843"
---

[Deployment Tools](#/deployment-tools?id=deployment-tools)
==========================================================

Any application you build is likely to be deployed somewhere. This section covers the most popular tools involved in deploying an application.

[Previous

Version Control: Git, GitHub](#/git)

[Next

Markdown](#/markdown)

---


# File: 3._Large_Language_Models.md

---
title: "3. Large Language Models"
original_url: "https://tds.s-anand.net/#/large-language-models?id=large-language-models"
downloaded_at: "2025-05-31T21:38:05.752726"
---

[Large Language Models](#/large-language-models?id=large-language-models)
=========================================================================

This module covers the practical usage of large language models (LLMs).

**LLMs incur a cost.** For the May 2025 batch, use [aipipe.org](https://aipipe.org/) as a proxy.
Emails with `@ds.study.iitm.ac.in` get a **$1 per calendar month** allowance. (Don’t exceed that.)

Read the [AI Pipe documentation](https://github.com/sanand0/aipipe) to learn how to use it. But in short:

1. Replace `OPENAI_BASE_URL`, i.e. `https://api.openai.com/v1` with `https://aipipe.org/openrouter/v1...` or `https://aipipe.org/openai/v1...`
2. Replace `OPENAI_API_KEY` with the [`AIPIPE_TOKEN`](https://aipipe.org/login)
3. Replace model names, e.g. `gpt-4.1-nano`, with `openai/gpt-4.1-nano`

For example, let’s use [Gemini 2.0 Flash Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash-lite) via [OpenRouter](https://openrouter.ai/google/gemini-2.0-flash-lite-001) for chat completions and [Text Embedding 3 Small](https://platform.openai.com/docs/models/text-embedding-3-small) via [OpenAI](https://platform.openai.com/docs/) for embeddings:

```
curl https://aipipe.org/openrouter/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIPIPE_TOKEN" \
  -d '{
    "model": "google/gemini-2.0-flash-lite-001",
    "messages": [{ "role": "user", "content": "What is 2 + 2?"} }]
  }'

curl https://aipipe.org/openai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIPIPE_TOKEN" \
  -d '{ "model": "text-embedding-3-small", "input": "What is 2 + 2?" }'Copy to clipboardErrorCopied
```

Or using [`llm`](https://llm.datasette.io/):

```
llm keys set openai --value $AIPIPE_TOKEN

export OPENAI_BASE_URL=https://aipipe.org/openrouter/v1
llm 'What is 2 + 2?' -m openrouter/google/gemini-2.0-flash-lite-001

export OPENAI_BASE_URL=https://aipipe.org/openai/v1
llm embed -c 'What is 2 + 2' -m 3-smallCopy to clipboardErrorCopied
```

**For a 50% discount** (but slower speed), use [Flex processing](https://platform.openai.com/docs/guides/flex-processing) by adding `service_tier: "flex"` to your JSON request.

[AI Proxy - Jan 2025](#/large-language-models?id=ai-proxy-jan-2025)
-------------------------------------------------------------------

For the Jan 2025 batch, we had created API keys for everyone with an `iitm.ac.in` email to use `gpt-4o-mini` and `text-embedding-3-small`. Your usage is limited to **$1 per calendar month** for this course. Don’t exceed that.

**Use [AI Proxy](https://github.com/sanand0/aiproxy)** instead of OpenAI. Specifically:

1. Replace your API to `https://api.openai.com/...` with `https://aiproxy.sanand.workers.dev/openai/...`
2. Replace the `OPENAI_API_KEY` with the `AIPROXY_TOKEN` that someone will give you.

[Previous

Local LLMs: Ollama](#/ollama)

[Next

Prompt engineering](#/prompt-engineering)

---


# File: 4._Data_Sourcing.md

---
title: "4. Data Sourcing"
original_url: "https://tds.s-anand.net/#/data-sourcing?id=data-sourcing"
downloaded_at: "2025-05-31T21:36:04.377887"
---

[Data Sourcing](#/data-sourcing?id=data-sourcing)
=================================================

Before you do any kind of data science, you obviously have to get the data to be able to analyze it, visualize it, narrate it, and deploy it.
And what we are going to cover in this module is how you get the data.

There are three ways you can get the data.

1. The first is you can **download** the data. Either somebody gives you the data and says download it from here, or you are asked to download it from the internet because it’s a public data source. But that’s the first way—you download the data.
2. The second way is you can **query it** from somewhere. It may be on a database. It may be available through an API. It may be available through a library. But these are ways in which you can selectively query parts of the data and stitch it together.
3. The third way is you have to **scrape it**. It’s not directly available in a convenient form that you can query or download. But it is, in fact, on a web page. It’s available on a PDF file. It’s available in a Word document. It’s available on an Excel file. It’s kind of structured, but you will have to figure out that structure and extract it from there.

In this module, we will be looking at the tools that will help you either download from a data source or query from an API or from a database or from a library. And finally, how you can scrape from different sources.

[![Data Sourcing - Introduction](https://i.ytimg.com/vi_webp/1LyblMkJzOo/sddefault.webp)](https://youtu.be/1LyblMkJzOo)

Here are links used in the video:

* [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
* [IMDb Datasets](https://imdb.com/interfaces/)
* [Download the IMDb Datasets](https://datasets.imdbws.com/)
* [Explore the Internet Movie Database](https://gramener.com/imdb/)
* [What does the world search for?](https://gramener.com/search/)
* [HowStat - Cricket statistics](https://howstat.com/cricket/home.asp)
* [Cricket Strike Rates](https://gramener.com/cricket/)

[Previous

Project 1](#/project-tds-virtual-ta)

[Next

Scraping with Excel](#/scraping-with-excel)

---


# File: 5._Data_Preparation.md

---
title: "5. Data Preparation"
original_url: "https://tds.s-anand.net/#/data-preparation?id=data-preparation"
downloaded_at: "2025-05-31T21:37:03.310281"
---

[Data Preparation](#/data-preparation?id=data-preparation)
==========================================================

Data preparation is crucial because raw data is rarely perfect.

It often contains errors, inconsistencies, or missing values. For example, marks data may have ‘NA’ or ‘absent’ for non-attendees, which you need to handle.

This section teaches you how to clean up data, convert it to different formats, aggregate it if required, and get a feel for the data before you analyze.

Here are links used in the video:

* [Presentation used in the video](https://docs.google.com/presentation/d/1Gb0QnPUN1YOwM_O5EqDdXUdL-5Azp1Tf/view)
* [Scraping assembly elections - Notebook](https://colab.research.google.com/drive/1SP8yVxzmofQO48-yXF3rujqWk2iM0KSl)
* [Assembly election results (CSV)](https://github.com/datameet/india-election-data/blob/master/assembly-elections/assembly.csv)
* [`pdftotext` software](https://www.xpdfreader.com/pdftotext-man.html)
* [OpenRefine software](https://openrefine.org)
* [The most persistent party](https://gramener.com/election/parliament#story.ddp)
* [TN assembly election cartogram](https://gramener.com/election/cartogram?ST_NAME=Tamil%20Nadu)

[![Data Preparation - Introduction](https://i.ytimg.com/vi_webp/dF3zchJJKqk/sddefault.webp)](https://youtu.be/dF3zchJJKqk)

[Previous

Scraping: Live Sessions](#/scraping-live-sessions)

[Next

Data Cleansing in Excel](#/data-cleansing-in-excel)

---


# File: 6._Data_Analysis.md

---
title: "6. Data Analysis"
original_url: "https://tds.s-anand.net/#/data-analysis?id=data-analysis"
downloaded_at: "2025-05-31T21:39:25.324024"
---

[Data analysis](#/data-analysis?id=data-analysis)
=================================================

[Data Analysis: Introduction Podcast](https://drive.google.com/file/d/1isjtxFa43CLIFlLpo8mwwQfBog9VlXYl/view) by [NotebookLM](https://notebooklm.google.com/)

Once you’ve prepared the data, your next task is to analyze it to get insights that are not immediately obvious.

In this module, you’ll learn:

* **Statistical analysis**: Calculate correlations, regressions, forecasts, and outliers using **spreadsheets**
* **Data summarization**: Aggregate and pivot data using **Python** and **databases**.
* **Geo-data Collection & Processing**: Gather and process geospatial data using tools like Python (GeoPandas) and QGIS.
* **Geo-visualization**: Create and visualize geospatial data on maps using Excel, QGIS, and Python libraries such as Folium.
* **Network & Proximity Analysis**: Analyze geospatial relationships and perform network analysis to understand data distribution and clustering.
* **Storytelling & Decision Making**: Develop narratives and make informed decisions based on geospatial data insights.

[![Data Analysis - Introduction](https://i.ytimg.com/vi_webp/CRSljunxjnk/sddefault.webp)](https://youtu.be/CRSljunxjnk)

[Previous

Extracting Audio and Transcripts](#/extracting-audio-and-transcripts)

[Next

Correlation with Excel](#/correlation-with-excel)

---


# File: 7._Data_Visualization.md

---
title: "7. Data Visualization"
original_url: "https://tds.s-anand.net/#/data-visualization?id=data-visualization"
downloaded_at: "2025-05-31T21:35:19.316888"
---

[Data visualization](#/data-visualization?id=data-visualization)
================================================================

[![Data visualization](https://i.ytimg.com/vi_webp/XkxRDql00UU/sddefault.webp)](https://youtu.be/XkxRDql00UU)

[Previous

Network Analysis in Python](#/network-analysis-in-python)

[Next

Visualizing Forecasts with Excel](#/visualizing-forecasts-with-excel)

---


# File: AI_Code_Editors__GitHub_Copilot.md

---
title: "AI Code Editors: GitHub Copilot"
original_url: "https://tds.s-anand.net/#/github-copilot?id=ai-editor-github-copilot"
downloaded_at: "2025-05-31T21:37:23.376408"
---

[AI Editor: GitHub Copilot](#/github-copilot?id=ai-editor-github-copilot)
-------------------------------------------------------------------------

AI Code Editors like [GitHub Copilot](https://github.com/features/copilot), [Cursor](https://www.cursor.com/), [Windsurf](http://windsurf.com/), [Roo Code](https://roocode.com/), [Cline](https://cline.bot/), [Continue.dev](https://www.continue.dev/), etc. use LLMs to help you write code faster.

Most are built on top of [VS Code](#/vscode). These are now a standard tool in every developer’s toolkit.

[GitHub Copilot](https://github.com/features/copilot) is [free](https://github.com/features/copilot/plans) (as of May 2025) for 2,000 completions and 50 chats.

[![Getting started with GitHub Copilot | Tutorial (11 min)](https://i.ytimg.com/vi_webp/n0NlxUyA7FI/sddefault.webp)](https://youtu.be/n0NlxUyA7FI)

You should learn about:

* [Code Suggestions](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-code-suggestions-in-your-editor), which is a basic feature.
* [Using Chat](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide), which lets you code in natural language.
* [Changing the chat model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat). The free version includes Claude 3.5 Sonnet, a good coding model.
* [Prompts](https://docs.github.com/en/copilot/copilot-chat-cookbook) to understand how people use AI code editors.

[Previous

Editor: VS Code](#/vscode)

[Next

Python tools: uv](#/uv)

---


# File: AI_Terminal_Tools__llm.md

---
title: "AI Terminal Tools: llm"
original_url: "https://tds.s-anand.net/#/llm?id=key-features"
downloaded_at: "2025-05-31T21:38:13.947863"
---

[LLM CLI: llm](#/llm?id=llm-cli-llm)
------------------------------------

[`llm`](https://pypi.org/project/llm) is a command-line utility for interacting with large language models—simplifying prompts, managing models and plugins, logging every conversation, and extracting structured data for pipelines.

[![Language models on the command-line w/ Simon Willison](https://i.ytimg.com/vi_webp/QUXQNi6jQ30/sddefault.webp)](https://youtu.be/QUXQNi6jQ30?t=100)

### [Basic Usage](#/llm?id=basic-usage)

[Install llm](https://github.com/simonw/llm#installation). Then set up your [`OPENAI_API_KEY`](https://platform.openai.com/api-keys) environment variable. See [Getting started](https://github.com/simonw/llm?tab=readme-ov-file#getting-started).

**TDS Students**: See [Large Language Models](#/large-language-models) for instructions on how to get and use `OPENAI_API_KEY`.

```
# Run a simple prompt
llm 'five great names for a pet pelican'

# Continue a conversation
llm -c 'now do walruses'

# Start a memory-aware chat session
llm chat

# Specify a model
llm -m gpt-4.1-nano 'Summarize tomorrow’s meeting agenda'

# Extract JSON output
llm 'List the top 5 Python viz libraries with descriptions' \
  --schema-multi 'name,description'Copy to clipboardErrorCopied
```

Or use llm without installation using [`uvx`](#/uv):

```
# Run llm via uvx without any prior installation
uvx llm 'Translate "Hello, world" into Japanese'

# Specify a model
uvx llm -m gpt-4.1-nano 'Draft a 200-word blog post on data ethics'

# Use structured JSON output
uvx llm 'List the top 5 programming languages in 2025 with their release years' \
  --schema-multi 'rank,language,release_year'Copy to clipboardErrorCopied
```

### [Key Features](#/llm?id=key-features)

* **Interactive prompts**: `llm '…'` — Fast shell access to any LLM.
* **Conversational flow**: `-c '…'` — Continue context across prompts.
* **Model switching**: `-m MODEL` — Use OpenAI, Anthropic, local models, and more.
* **Structured output**: `llm json` — Produce JSON for automation.
* **Logging & history**: `llm logs path` — Persist every prompt/response in SQLite.
* **Web UI**: `datasette "$(llm logs path)"` — Browse your entire history with Datasette.
* **Persistent chat**: `llm chat` — Keep the model in memory across multiple interactions.
* **Plugin ecosystem**: `llm install PLUGIN` — Add support for new models, data sources, or workflows. ([Language models on the command-line - Simon Willison’s Weblog](https://simonwillison.net/2024/Jun/17/cli-language-models/?utm_source=chatgpt.com))

### [Practical Uses](#/llm?id=practical-uses)

* **Automated coding**. Generate code scaffolding, review helpers, or utilities on demand. For example, after running`llm install llm-cmd`, run `llm cmd 'Undo the last git commit'`. Inspired by [Simon’s post on using LLMs for rapid tool building](https://simonwillison.net/2025/Mar/11/using-llms-for-code/).
* **Transcript processing**. Summarize YouTube or podcast transcripts using Gemini. See [Putting Gemini 2.5 Pro through its paces](https://www.macstories.net/mac/llm-youtube-transcripts-with-claude-and-gemini-in-shortcuts/).
* **Commit messages**. Turn diffs into descriptive commit messages, e.g. `git diff | llm 'Write a concise git commit message explaining these changes'`. \
* **Data extraction**. Convert free-text into structured JSON for automation. [Structured data extraction from unstructured content using LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/).

[Previous

Terminal: Bash](#/bash)

[Next

Spreadsheet: Excel, Google Sheets](#/spreadsheets)

---


# File: Actor_Network_Visualization.md

---
title: "Actor Network Visualization"
original_url: "https://tds.s-anand.net/#/actor-network-visualization?id=actor-network-visualization"
downloaded_at: "2025-05-31T21:37:45.273391"
---

[Actor Network Visualization](#/actor-network-visualization?id=actor-network-visualization)
-------------------------------------------------------------------------------------------

Find the shortest path between Govinda & Angelina Jolie using IMDb data using Python: [networkx](https://pypi.org/project/networkx/) or [scikit-network](https://pypi.org/project/scikit-network).

[![Jolie No. 1](https://i.ytimg.com/vi_webp/lcwMsPxPIjc/sddefault.webp)](https://youtu.be/lcwMsPxPIjc)

* [Notebook: How this video was created](https://github.com/sanand0/jolie-no-1/blob/master/jolie-no-1.ipynb)
* [The data used to visualize the network](https://github.com/sanand0/jolie-no-1/blob/master/imdb-actor-pairing.ipynb)
* [The shortest path between actors](https://github.com/sanand0/jolie-no-1/blob/master/shortest-path.ipynb)
* [IMDB data](https://developer.imdb.com/non-commercial-datasets/)
* [Codebase](https://github.com/sanand0/jolie-no-1)

[Previous

Data Visualization with ChatGPT](#/data-visualization-with-chatgpt)

[Next

RAWgraphs](#/rawgraphs)

---


# File: Authentication__Google_Auth.md

---
title: "Authentication: Google Auth"
original_url: "https://tds.s-anand.net/#/google-auth?id=google-authentication-with-fastapi"
downloaded_at: "2025-05-31T21:33:56.737350"
---

[Google Authentication with FastAPI](#/google-auth?id=google-authentication-with-fastapi)
-----------------------------------------------------------------------------------------

Secure your API endpoints using Google ID tokens to restrict access to specific email addresses.

[![🔥 Python FastAPI Google Login Tutorial | OAuth2 Authentication (19 min)](https://i.ytimg.com/vi_webp/4ExQYRCwbzw/sddefault.webp)](https://youtu.be/4ExQYRCwbzw)

Google Auth is the most commonly implemented single sign-on mechanism because:

* It’s popular and user-friendly. Users can log in with their existing Google accounts.
* It’s secure: Google supports OAuth2 and OpenID Connect to handle authentication.

Here’s how you build a FastAPI app that identifies the user.

1. Go to the [Google Cloud Console – Credentials](https://console.developers.google.com/apis/credentials) and click **Create Credentials > OAuth client ID**.
2. Choose **Web application**, set your authorized redirect URIs (e.g., `http://localhost:8000/`).
3. Copy the **Client ID** and **Client Secret** into a `.env` file:

   ```
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secretCopy to clipboardErrorCopied
   ```
4. Create your FastAPI `app.py`:

```
# /// script
# dependencies = ["python-dotenv", "fastapi", "uvicorn", "itsdangerous", "httpx", "authlib"]
# ///

import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

load_dotenv()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="create-a-random-secret-key")

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/")
async def application(request: Request):
    user = request.session.get("user")
    # 3. For authenticated users: say hello
    if user:
        return f"Hello {user['email']}"
    # 2. For users who have just logged in, save their details in the session
    if "code" in request.query_params:
        token = await oauth.google.authorize_access_token(request)
        request.session["user"] = token["userinfo"]
        return RedirectResponse("/")
    # 1. For users who are logging in for the first time, redirect to Google login
    return await oauth.google.authorize_redirect(request, request.url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)Copy to clipboardErrorCopied
```

Now, run `uv run app.py`.

1. When you visit <http://localhost:8000/> you’ll be redirected to a Google login page.
2. When you log in, you’ll be redirected back to <http://localhost:8000/>
3. Now you’ll see the email ID you logged in with.

Instead of displaying the email, you can show different content based on the user. For example:

* Allow access to specfic users and not others
* Fetch the user’s personalized information
* Display different content based on the user

[Previous

Web Framework: FastAPI](#/fastapi)

[Next

Local LLMs: Ollama](#/ollama)

---


# File: BBC_Weather_API_with_Python.md

---
title: "BBC Weather API with Python"
original_url: "https://tds.s-anand.net/#/bbc-weather-api-with-python?id=bbc-weather-location-id-with-python"
downloaded_at: "2025-05-31T21:39:18.990140"
---

[BBC Weather location ID with Python](#/bbc-weather-api-with-python?id=bbc-weather-location-id-with-python)
-----------------------------------------------------------------------------------------------------------

[![BBC Weather location API with Python](https://i.ytimg.com/vi_webp/IafLrvnamAw/sddefault.webp)](https://youtu.be/IafLrvnamAw)

You’ll learn how to get the location ID of any city from the BBC Weather API – as a precursor to scraping weather data – covering:

* **Understanding API Calls**: Learn how backend API calls work when searching for a city on the BBC weather website.
* **Inspecting Web Interactions**: Use the browser’s inspect element feature to track API calls and understand the network activity.
* **Extracting Location IDs**: Identify and extract the location ID from the API response using Python.
* **Using Python Libraries**: Import and use requests, json, and urlencode libraries to make API calls and process responses.
* **Constructing API URLs**: Create structured API URLs dynamically with constant prefixes and query parameters using urlencode.
* **Building Functions**: Develop a Python function that accepts a city name, constructs the API call, and returns the location ID.

To open the browser Developer Tools on Chrome, Edge, or Firefox, you can:

* Right-click on the page and select “Inspect” to open the developer tools
* OR: Press `F12`
* OR: Press `Ctrl+Shift+I` on Windows
* OR: Press `Cmd+Opt+I` on Mac

Here are links and references:

* [BBC Location ID scraping - Notebook](https://colab.research.google.com/drive/1-iV-tbtRicKR_HXWeu4Hi5aXJCV3QdQp)
* [BBC Weather - Palo Alto (location ID: 5380748)](https://www.bbc.com/weather/5380748)
* [BBC Locator Service - Los Angeles](https://locator-service.api.bbci.co.uk/locations?api_key=AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&s=los%20angeles&a=true&format=json)
* Learn about the [`requests` package](https://docs.python-requests.org/en/latest/user/quickstart/). Watch [Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More](https://youtu.be/tb8gHvYlCFs)

[BBC Weather data with Python](#/bbc-weather-api-with-python?id=bbc-weather-data-with-python)
---------------------------------------------------------------------------------------------

[![Scrape BBC weather with Python](https://i.ytimg.com/vi_webp/Uc4DgQJDRoI/sddefault.webp)](https://youtu.be/Uc4DgQJDRoI)

You’ll learn how to scrape the live weather data of a city from the BBC Weather API, covering:

* **Introduction to Web Scraping**: Understand the basics of web scraping and its legality.
* **Libraries Overview**: Learn the importance of [`requests`](https://docs.python-requests.org/en/latest/user/quickstart/) and [`BeautifulSoup`](https://beautiful-soup-4.readthedocs.io/).
* **Fetching HTML**: Use [`requests`](https://docs.python-requests.org/en/latest/user/quickstart/) to fetch HTML content from a web page.
* **Parsing HTML**: Utilize [`BeautifulSoup`](https://beautiful-soup-4.readthedocs.io/) to parse and navigate the HTML content.
* **Identifying Data**: Inspect HTML elements to locate specific data (e.g., high and low temperatures).
* **Extracting Data**: Extract relevant data using [`BeautifulSoup`](https://beautiful-soup-4.readthedocs.io/)‘s `find_all()` function.
* **Data Cleanup**: Clean extracted data to remove unwanted elements.
* **Post-Processing**: Use regular expressions to split large strings into meaningful parts.
* **Data Structuring**: Combine extracted data into a structured pandas DataFrame.
* **Handling Special Characters**: Replace unwanted characters for better data manipulation.
* **Saving Data**: Save the cleaned data into CSV and Excel formats.

Here are links and references:

* [BBC Weather scraping - Notebook](https://colab.research.google.com/drive/1-gkMzE-TKe3U_yh1v0NPn4TM687H2Hcf)
* [BBC Locator Service - Mumbai](https://locator-service.api.bbci.co.uk/locations?api_key=AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&s=mumbai&a=true&format=json)
* [BBC Weather - Mumbai (location ID: 1275339)](https://www.bbc.com/weather/1275339)
* [BBC Weather API - Mumbai (location ID: 1275339)](https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/1275339)
* Learn about the [`json` package](https://docs.python.org/3/library/json.html). Watch [Python Tutorial: Working with JSON Data using the json Module](https://youtu.be/9N6a-VLBa2I)
* Learn about the [`BeautifulSoup` package](https://beautiful-soup-4.readthedocs.io/). Watch [Python Tutorial: Web Scraping with BeautifulSoup and Requests](https://youtu.be/ng2o98k983k)
* Learn about the [`pandas` package](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html). Watch
  + [Python Pandas Tutorial (Part 1): Getting Started with Data Analysis - Installation and Loading Data](https://youtu.be/ZyhVh-qRZPA)
  + [Python Pandas Tutorial (Part 2): DataFrame and Series Basics - Selecting Rows and Columns](https://youtu.be/zmdjNSmRXF4)
* Learn about the [`re` package](https://docs.python.org/3/library/re.html). Watch [Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)](https://youtu.be/K8L6KVGG-7o)
* Learn about the [`datetime` package](https://docs.python.org/3/library/datetime.html). Watch [Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones](https://youtu.be/eirjjyP2qcQ)

[Previous

Crawling with the CLI](#/crawling-cli)

[Next

Scraping IMDb with JavaScript](#/scraping-imdb-with-javascript)

---


# File: Base_64_Encoding.md

---
title: "Base 64 Encoding"
original_url: "https://tds.s-anand.net/#/base64-encoding?id=base-64-encoding"
downloaded_at: "2025-05-31T21:37:47.657158"
---

[Base 64 Encoding](#/base64-encoding?id=base-64-encoding)
=========================================================

Base64 is a method to convert binary data into ASCII text. It’s essential when you need to transmit binary data through text-only channels or embed binary content in text formats.

Watch this quick explanation of how Base64 works (3 min):

[![What is Base64? (3 min)](https://i.ytimg.com/vi_webp/8qkxeZmKmOY/sddefault.webp)](https://youtu.be/8qkxeZmKmOY)

Here’s how it works:

* It takes 3 bytes (24 bits) and converts them into 4 ASCII characters
* … using 64 characters: A-Z, a-z, 0-9, + and / (padding with `=` to make the length a multiple of 4)
* There’s a URL-safe variant of Base64 that replaces + and / with - and \_ to avoid issues in URLs
* Base64 adds ~33% overhead (since every 3 bytes becomes 4 characters)

Common Python operations with Base64:

```
import base64

# Basic encoding/decoding
text = "Hello, World!"
# Convert text to base64
encoded = base64.b64encode(text.encode()).decode()  # SGVsbG8sIFdvcmxkIQ==
# Convert base64 back to text
decoded = base64.b64decode(encoded).decode()        # Hello, World!
# Convert to URL-safe base64
url_safe = base64.urlsafe_b64encode(text.encode()).decode()  # SGVsbG8sIFdvcmxkIQ==

# Working with binary files (e.g., images)
with open('image.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()

# Data URI example (embed images in HTML/CSS)
data_uri = f"data:image/png;base64,{image_b64}"Copy to clipboardErrorCopied
```

Data URIs allow embedding binary data directly in HTML/CSS. This reduces the number of HTTP requests and also works offline. But it increases the file size.

For example, here’s an SVG image embedded as a data URI:

```
<img
  src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGNpcmNsZSBjeD0iMTYiIGN5PSIxNiIgcj0iMTUiIGZpbGw9IiMyNTYzZWIiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJtMTYgNyAyIDcgNyAyLTcgMi0yIDctMi03LTctMiA3LTJaIi8+PC9zdmc+"
/>Copy to clipboardErrorCopied
```

Base64 is used in many places:

* JSON: Encoding binary data in JSON payloads
* Email: MIME attachments encoding
* Auth: HTTP Basic Authentication headers
* JWT: Encoding tokens in web authentication
* SSL/TLS: PEM certificate format
* SAML: Encoding assertions in SSO
* Git: Encoding binary files in patches

Tools for working with Base64:

* [Base64 Decoder/Encoder](https://www.base64decode.org/) for online encoding/decoding
* [data: URI Generator](https://dopiaza.org/tools/datauri/index.php) converts files to Data URIs

[Previous

LLM Text Extraction](#/llm-text-extraction)

[Next

Vision Models](#/vision-models)

---


# File: Browser__DevTools.md

---
title: "Browser: DevTools"
original_url: "https://tds.s-anand.net/#/devtools?id=browser-devtools"
downloaded_at: "2025-05-31T21:35:09.446941"
---

[Browser: DevTools](#/devtools?id=browser-devtools)
---------------------------------------------------

[Chrome DevTools](https://developer.chrome.com/docs/devtools/overview/) is the de facto standard for web development and data analysis in the browser.
You’ll use this a lot when debugging and inspecting web pages.

Here are the key features you’ll use most:

1. **Elements Panel**

   * Inspect and modify HTML/CSS in real-time
   * Copy CSS selectors for web scraping
   * Debug layout issues with the Box Model

   ```
   // Copy selector in Console
   copy($0); // Copies selector of selected elementCopy to clipboardErrorCopied
   ```
2. **Console Panel**

   * JavaScript REPL environment
   * Log and debug data
   * Common console methods:

   ```
   console.table(data); // Display data in table format
   console.group("Name"); // Group related logs
   console.time("Label"); // Measure execution timeCopy to clipboardErrorCopied
   ```
3. **Network Panel**

   * Monitor API requests and responses
   * Simulate slow connections
   * Right-click on a request and select “Copy as fetch” to get the request.
4. **Essential Keyboard Shortcuts**

   * `Ctrl+Shift+I` (Windows) / `Cmd+Opt+I` (Mac): Open DevTools
   * `Ctrl+Shift+C`: Select element to inspect
   * `Ctrl+L`: Clear console
   * `$0`: Reference currently selected element
   * `$$('selector')`: Query selector all (returns array)

Videos from Chrome Developers (37 min total):

* [Fun & powerful: Intro to Chrome DevTools](https://youtu.be/t1c5tNPpXjs) (5 min)
* [Different ways to open Chrome DevTools](https://youtu.be/X65TAP8a530) (5 min)
* [Faster DevTools navigation with shortcuts and settings](https://youtu.be/xHusjrb_34A) (3 min)
* [How to log messages in the Console](https://youtu.be/76U0gtuV9AY) (6 min)
* [How to speed up your workflow with Console shortcuts](https://youtu.be/hdRDTj6ObiE) (6 min)
* [HTML vs DOM? Let’s debug them](https://youtu.be/J-02VNxE7lE) (5 min)
* [Caching demystified: Inspect, clear, and disable caches](https://youtu.be/mSMb-aH6sUw) (7 min)
* [Console message logging](https://youtu.be/76U0gtuV9AY) (6 min)
* [Console workflow shortcuts](https://youtu.be/hdRDTj6ObiE) (6 min)
* [HTML vs DOM debugging](https://youtu.be/J-02VNxE7lE) (5 min)
* [Cache inspection and management](https://youtu.be/mSMb-aH6sUw) (7 min)

[Previous

Unicode](#/unicode)

[Next

CSS Selectors](#/css-selectors)

---


# File: CI_CD__GitHub_Actions.md

---
title: "CI/CD: GitHub Actions"
original_url: "https://tds.s-anand.net/#/github-actions?id=cicd-github-actions"
downloaded_at: "2025-05-31T21:34:24.484390"
---

[CI/CD: GitHub Actions](#/github-actions?id=cicd-github-actions)
----------------------------------------------------------------

[GitHub Actions](https://github.com/features/actions) is a powerful automation platform built into GitHub. It helps automate your development workflow - running tests, deploying applications, updating datasets, retraining models, etc.

* Understand the basics of [YAML configuration files](https://docs.github.com/en/actions/writing-workflows/quickstart)
* Explore the [pre-built actions from the marketplace](https://github.com/marketplace?type=actions)
* How to [handle secrets securely](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
* [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
* Staying within the [free tier limits](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)
* [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)

Here is a sample `.github/workflows/iss-location.yml` that runs daily, appends the International Space Station location data into `iss-location.json`, and commits it to the repository.

```
name: Log ISS Location Data Daily

on:
  schedule:
    # Runs at 12:00 UTC (noon) every day
    - cron: "0 12 * * *"
  workflow_dispatch: # Allows manual triggering

jobs:
  collect-iss-data:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Fetch ISS location data
        run: | # python
          uv run --with requests python << 'EOF'
          import requests

          data = requests.get('http://api.open-notify.org/iss-now.json').text
          with open('iss-location.jsonl', 'a') as f:
              f.write(data + '\n')
          'EOF'

      - name: Commit and push changes
        run: | # shell
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add iss-location.jsonl
          git commit -m "Update ISS position data [skip ci]" || exit 0
          git pushCopy to clipboardErrorCopied
```

Tools:

* [GitHub CLI](https://cli.github.com/): Manage workflows from terminal
* [Super-Linter](https://github.com/github/super-linter): Validate code style
* [Release Drafter](https://github.com/release-drafter/release-drafter): Automate releases
* [act](https://github.com/nektos/act): Run actions locally

[![Github Actions CI/CD - Everything you need to know to get started](https://i.ytimg.com/vi_webp/mFFXuXjVgkU/sddefault.webp)](https://youtu.be/mFFXuXjVgkU)

* [How to handle secrets in GitHub Actions](https://youtu.be/1tD7km5jK70)

[Previous

Serverless hosting: Vercel](#/vercel)

[Next

Containers: Docker, Podman](#/docker)

---


# File: CORS.md

---
title: "CORS"
original_url: "https://tds.s-anand.net/#/cors?id=cors-cross-origin-resource-sharing"
downloaded_at: "2025-05-31T21:37:21.024622"
---

[CORS: Cross-Origin Resource Sharing](#/cors?id=cors-cross-origin-resource-sharing)
-----------------------------------------------------------------------------------

CORS (Cross-Origin Resource Sharing) is a security mechanism that controls how web browsers handle requests between different origins (domains, protocols, or ports). Data scientists need CORS for APIs serving data or analysis to a browser on a different domain.

Watch this practical explanation of CORS (3 min):

[![CORS in 100 Seconds](https://i.ytimg.com/vi_webp/4KHiSt0oLJ0/sddefault.webp)](https://youtu.be/4KHiSt0oLJ0)

Key CORS concepts:

* **Same-Origin Policy**: Browsers block requests between different origins by default
* **CORS Headers**: Server responses must include specific headers to allow cross-origin requests
* **Preflight Requests**: Browsers send OPTIONS requests to check if the actual request is allowed
* **Credentials**: Special handling required for requests with cookies or authentication

If you’re exposing your API with a GET request publicly, the only thing you need to do is set the HTTP header `Access-Control-Allow-Origin: *`.

Here are other common CORS headers:

```
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: trueCopy to clipboardErrorCopied
```

To implement CORS in FastAPI, use the [`CORSMiddleware` middleware](https://fastapi.tiangolo.com/tutorial/cors/):

```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Allow a specific domain
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
    allow_headers=["*"],  # Allow all headers
)Copy to clipboardErrorCopied
```

Testing CORS with JavaScript:

```
// Simple request
const response = await fetch("https://api.example.com/data", {
  method: "GET",
  headers: { "Content-Type": "application/json" },
});

// Request with credentials
const response = await fetch("https://api.example.com/data", {
  credentials: "include",
  headers: { "Content-Type": "application/json" },
});Copy to clipboardErrorCopied
```

Useful CORS debugging tools:

* [CORS Checker](https://cors-test.codehappy.dev/): Test CORS configurations
* Browser DevTools Network tab: Inspect CORS headers and preflight requests
* [cors-anywhere](https://github.com/Rob--W/cors-anywhere): CORS proxy for development

Common CORS errors and solutions:

* `No 'Access-Control-Allow-Origin' header`: Configure server to send proper CORS headers
* `Request header field not allowed`: Add required headers to `Access-Control-Allow-Headers`
* `Credentials flag`: Set both `credentials: 'include'` and `Access-Control-Allow-Credentials: true`
* `Wild card error`: Cannot use `*` with credentials; specify exact origins

[Previous

Tunneling: ngrok](#/ngrok)

[Next

REST APIs](#/rest-apis)

---


# File: CSS_Selectors.md

---
title: "CSS Selectors"
original_url: "https://tds.s-anand.net/#/css-selectors?id=css-selectors"
downloaded_at: "2025-05-31T21:36:12.372408"
---

[CSS Selectors](#/css-selectors?id=css-selectors)
-------------------------------------------------

CSS selectors are patterns used to select and style HTML elements on a web page. They are fundamental to web development and data scraping, allowing you to precisely target elements for styling or extraction.

For data scientists, understanding CSS selectors is crucial when:

* Web scraping with tools like Beautiful Soup or Scrapy
* Selecting elements for browser automation with Selenium
* Styling data visualizations and web applications
* Debugging website issues using browser DevTools

Watch this comprehensive introduction to CSS selectors (20 min):

[![Learn Every CSS Selector In 20 Minutes (20 min)](https://i.ytimg.com/vi_webp/l1mER1bV0N0/sddefault.webp)](https://youtu.be/l1mER1bV0N0)

The Mozilla Developer Network (MDN) provides detailed documentation on the three main types of selectors:

* [Basic CSS selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors): Learn about element (`div`), class (`.container`), ID (`#header`), and universal (`*`) selectors
* [Attribute selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Attribute_selectors): Target elements based on their attributes or attribute values (`[type="text"]`)
* [Combinators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Combinators): Use relationships between elements (`div > p`, `div + p`, `div ~ p`)

Practice your CSS selector skills with this interactive tool:

* [CSS Diner](https://flukeout.github.io/): A fun game that teaches CSS selectors through increasingly challenging levels

[Previous

Browser: DevTools](#/devtools)

[Next

JSON](#/json)

---


# File: Cleaning_Data_with_OpenRefine.md

---
title: "Cleaning Data with OpenRefine"
original_url: "https://tds.s-anand.net/#/cleaning-data-with-openrefine?id=cleaning-data-with-openrefine"
downloaded_at: "2025-05-31T21:36:14.667227"
---

[Cleaning Data with OpenRefine](#/cleaning-data-with-openrefine?id=cleaning-data-with-openrefine)
-------------------------------------------------------------------------------------------------

[![Cleaning data with OpenRefine](https://i.ytimg.com/vi_webp/zxEtfHseE84/sddefault.webp)](https://youtu.be/zxEtfHseE84)

This session covers the use of OpenRefine for data cleaning, focusing on resolving entity discrepancies:

* **Data Upload and Project Creation**: Import data into OpenRefine and create a new project for analysis.
* **Faceting Data**: Use text facets to group similar entries and identify frequency of address crumbs.
* **Clustering Methodology**: Apply clustering algorithms to merge similar entries with minor differences, such as punctuation.
* **Manual and Automated Clustering**: Learn to merge clusters manually or in one go, trusting the system’s clustering accuracy.
* **Entity Resolution**: Clean and save the data by resolving multiple versions of the same entity using Open Refine.

Here are links used in the video:

* [OpenRefine software](https://openrefine.org)
* [Dataset for OpenRefine](https://drive.google.com/file/d/1ccu0Xxk8UJUa2Dz4lihmvzhLjvPy42Ai/view)

[Previous

Data Preparation in the Editor](#/data-preparation-in-the-editor)

[Next

Profiling Data with Python](#/profiling-data-with-python)

---


# File: Containers__Docker,_Podman.md

---
title: "Containers: Docker, Podman"
original_url: "https://tds.s-anand.net/#/docker?id=containers-docker-podman"
downloaded_at: "2025-05-31T21:36:10.119778"
---

[Containers: Docker, Podman](#/docker?id=containers-docker-podman)
------------------------------------------------------------------

[Docker](https://www.docker.com/) and [Podman](https://podman.io/) are containerization tools that package your application and its dependencies into a standardized unit for software development and deployment.

Docker is the industry standard. Podman is compatible with Docker and has better security (and a slightly more open license). In this course, we recommend Podman but Docker works in the same way.

Initialize the container engine:

```
podman machine init
podman machine startCopy to clipboardErrorCopied
```

Common Operations. (You can use `docker` instead of `podman` in the same way.)

```
# Pull an image
podman pull python:3.11-slim

# Run a container
podman run -it python:3.11-slim

# List containers
podman ps -a

# Stop container
podman stop container_id

# Scan image for vulnerabilities
podman scan myapp:latest

# Remove container
podman rm container_id

# Remove all stopped containers
podman container pruneCopy to clipboardErrorCopied
```

You can create a `Dockerfile` to build a container image. Here’s a sample `Dockerfile` that converts a Python script into a container image.

```
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Typically, you would use `COPY . .` to copy files from the host machine,
# but here we're just using a simple script.
RUN echo 'print("Hello, world!")' > app.py
# Run the script
CMD ["python", "app.py"]Copy to clipboardErrorCopied
```

To build, run, and deploy the container, run these commands:

```
# Create an account on https://hub.docker.com/ and then login
podman login docker.io

# Build and run the container
podman build -t py-hello .
podman run -it py-hello

# Push the container to Docker Hub. Replace $DOCKER_HUB_USERNAME with your Docker Hub username.
podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello

# Push adding a specific tag, e.g. dev
TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAGCopy to clipboardErrorCopied
```

Tools:

* [Dive](https://github.com/wagoodman/dive): Explore image layers
* [Skopeo](https://github.com/containers/skopeo): Work with container images
* [Trivy](https://github.com/aquasecurity/trivy): Security scanner

[![Podman Tutorial Zero to Hero | Full 1 Hour Course](https://i.ytimg.com/vi_webp/YXfA5O5Mr18/sddefault.webp)](https://youtu.be/YXfA5O5Mr18)

[![Learn Docker in 7 Easy Steps - Full Beginner's Tutorial](https://i.ytimg.com/vi_webp/gAkwW2tuIqE/sddefault.webp)](https://youtu.be/gAkwW2tuIqE)

* Optional: For Windows, see [WSL 2 with Docker getting started](https://youtu.be/5RQbdMn04Oc)

[Previous

CI/CD: GitHub Actions](#/github-actions)

[Next

DevContainers: GitHub Codespaces](#/github-codespaces)

---


# File: Convert_HTML_to_Markdown.md

---
title: "Convert HTML to Markdown"
original_url: "https://tds.s-anand.net/#/convert-html-to-markdown?id=choosing-the-right-tool"
downloaded_at: "2025-05-31T21:38:02.157216"
---

[Converting HTML to Markdown](#/convert-html-to-markdown?id=converting-html-to-markdown)
----------------------------------------------------------------------------------------

When working with web content, converting HTML files to plain text or Markdown is a common requirement for content extraction, analysis, and preservation. For example:

* **Content analysis**: Extract clean text from HTML for natural language processing
* **Data mining**: Strip formatting to focus on the actual content
* **Offline reading**: Convert web pages to readable formats for e-readers or offline consumption
* **Content migration**: Move content between different CMS platforms
* **SEO analysis**: Extract headings, content structure, and text for optimization
* **Archive creation**: Store web content in more compact, preservation-friendly formats
* **Accessibility**: Convert content to formats that work better with screen readers

This tutorial covers both converting existing HTML files and combining web crawling with HTML-to-text conversion in a single workflow – all using the command line.

### [defuddle-cli](#/convert-html-to-markdown?id=defuddle-cli)

[defuddle-cli](https://github.com/defuddle/defuddle) specializes in HTML - Markdown conversion. It’s a bit slow and not very customizable but produces clean Markdown that preserves structure, links, and basic formatting. Best for content where preserving the document structure is important.

```
find . -name '*.html' -exec npx --package defuddle-cli -y defuddle parse {} --md -o {}.md \;Copy to clipboardErrorCopied
```

* `find . -name '*.html'`: Finds all HTML files in the current directory and subdirectories
* `-exec ... \;`: Executes the following command for each file found
* `npx --package defuddle-cli -y`: Installs and runs defuddle-cli without prompting
* `defuddle parse {} --md`: Parses the HTML file (represented by `{}`) and converts to markdown
* `-o {}.md`: Outputs to a file with the original name plus .md extension

### [Pandoc](#/convert-html-to-markdown?id=pandoc)

[Pandoc](https://pandoc.org/) is a bit slow and highly customizable, preserving almost all formatting elements, leading to verbose markdown. Best for academic or documentation conversion where precision matters.

Pandoc can convert from many other formats (such as Word, PDF, LaTeX, etc.) to Markdown and vice versa, making it one of most popular and versatele document convertors.

[![How to Convert a Word Document to Markdown for Free using Pandoc (12 min)](https://i.ytimg.com/vi/HPSK7q13-40/sddefault.jpg)](https://youtu.be/HPSK7q13-40)

```
find . -name '*.html' -exec pandoc -f html -t markdown_strict -o {}.md {} \;Copy to clipboardErrorCopied
```

* `find . -name '*.html'`: Finds all HTML files in the current directory and subdirectories
* `-exec ... \;`: Executes the following command for each file found
* `pandoc`: The Swiss Army knife of document conversion
* `-f html -t markdown_strict`: Convert from HTML format to strict markdown
* `-o {}.md {}`: Output to a markdown file, with the input file as the last argument

### [Lynx](#/convert-html-to-markdown?id=lynx)

[Lynx](https://lynx.invisible-island.net/) is fast and generates text (not Markdown) with minimal formatting. Lynx renders the HTML as it would appear in a text browser, preserving basic structure but losing complex formatting. Best for quick content extraction or when processing large numbers of files.

```
find . -type f -name '*.html' -exec sh -c 'for f; do lynx -dump -nolist "$f" > "${f%.html}.txt"; done' _ {} +Copy to clipboardErrorCopied
```

* `find . -type f -name '*.html'`: Finds all HTML files in the current directory and subdirectories
* `-exec sh -c '...' _ {} +`: Executes a shell command with batched files for efficiency
* `for f; do ... done`: Loops through each file in the batch
* `lynx -dump -nolist "$f"`: Uses the lynx text browser to render HTML as plain text
  + `-dump`: Output the rendered page to stdout
  + `-nolist`: Don’t include the list of links at the end
* `> "${f%.html}.txt"`: Save output to a .txt file with the same base name

### [w3m](#/convert-html-to-markdown?id=w3m)

[w3m](https://w3m.sourceforge.net/) is very slow processing with minimal formatting. w3m tends to be more thorough in its rendering than lynx but takes considerably longer. It supports basic JavaScript processing, making it better at handling modern websites with dynamic content. Best for cases where you need slightly better rendering than lynx, particularly for complex layouts and tables, and when some JavaScript processing is beneficial.

```
find . -type f -name '*.html' \
  -exec sh -c 'for f; do \
      w3m -dump -T text/html -cols 80 -no-graph "$f" > "${f%.html}.md"; \
    done' _ {} +Copy to clipboardErrorCopied
```

* `find . -type f -name '*.html'`: Finds all HTML files in the current directory and subdirectories
* `-exec sh -c '...' _ {} +`: Executes a shell command with batched files for efficiency
* `for f; do ... done`: Loops through each file in the batch
* `w3m -dump -T text/html -cols 80 -no-graph "$f"`: Uses the w3m text browser to render HTML
  + `-dump`: Output the rendered page to stdout
  + `-T text/html`: Specify input format as HTML
  + `-cols 80`: Set output width to 80 columns
  + `-no-graph`: Don’t show graphic characters for tables and frames
* `> "${f%.html}.md"`: Save output to a .md file with the same base name

### [Comparison](#/convert-html-to-markdown?id=comparison)

| Approach | Speed | Format Quality | Preservation | Best For |
| --- | --- | --- | --- | --- |
| defuddle-cli | Slow | High | Good structure and links | Content migration, publishing |
| pandoc | Slow | Very High | Almost everything | Academic papers, documentation |
| lynx | Fast | Low | Basic structure only | Quick extraction, large batches |
| w3m | Very Slow | Medium-Low | Basic structure with better tables | Improved readability over lynx |

### [Optimize Batch Processing](#/convert-html-to-markdown?id=optimize-batch-processing)

1. **Process in parallel**: Use GNU Parallel for multi-core processing:

   ```
   find . -name "*.html" | parallel "pandoc -f html -t markdown_strict -o {}.md {}"Copy to clipboardErrorCopied
   ```
2. **Filter files before processing**:

   ```
   find . -name "*.html" -type f -size -1M -exec pandoc -f html -t markdown {} -o {}.md \;Copy to clipboardErrorCopied
   ```
3. **Customize output format** with additional parameters:

   ```
   # For pandoc, preserve line breaks but simplify other formatting
   find . -name "*.html" -exec pandoc -f html -t markdown --wrap=preserve --atx-headers {} -o {}.md \;Copy to clipboardErrorCopied
   ```
4. **Handle errors gracefully**:

   ```
   find . -name "*.html" -exec sh -c 'for f; do pandoc -f html -t markdown "$f" -o "${f%.html}.md" 2>/dev/null || echo "Failed: $f" >> conversion_errors.log; done' _ {} +Copy to clipboardErrorCopied
   ```

### [Choosing the Right Tool](#/convert-html-to-markdown?id=choosing-the-right-tool)

* **Need speed with minimal formatting?** Use the lynx approach
* **Need precise, complete conversion?** Use pandoc
* **Need a balance of structure and cleanliness?** Try defuddle-cli
* **Working with complex tables?** w3m might render them better

Remember that the best approach depends on your specific use case, volume of files, and how you intend to use the converted text.

### [Combined Crawling and Conversion](#/convert-html-to-markdown?id=combined-crawling-and-conversion)

Sometimes you need to both crawl a website and convert its content to markdown or text in a single workflow, like [Crawl4AI](#/convert-html-to-markdown?id=crawl4ai) or [markdown-crawler](#/convert-html-to-markdown?id=markdown-crawler).

1. **For research/data collection**: Use a specialized crawler (like Crawl4AI) with post-processing conversion
2. **For simple website archiving**: Markdown-crawler provides a convenient all-in-one solution
3. **For high-quality conversion**: Use wget/wget2 for crawling followed by pandoc for conversion
4. **For maximum speed**: Combine wget with lynx in a pipeline

### [Crawl4AI](#/convert-html-to-markdown?id=crawl4ai)

[Crawl4AI](https://github.com/crawl4ai/crawl4ai) is designed for single-page extraction with high-quality content processing. Crawl4AI is optimized for AI training data extraction, focusing on clean, structured content rather than complete site preservation. It excels at removing boilerplate content and preserving the main article text.

```
uv venv
source .venv/bin/activate.fish
uv pip install crawl4ai
crawl4ai-setupCopy to clipboardErrorCopied
```

* `uv venv`: Creates a Python virtual environment using uv (a faster alternative to virtualenv)
* `source .venv/bin/activate.fish`: Activates the virtual environment (fish shell syntax)
* `uv pip install crawl4ai`: Installs the crawl4ai package
* `crawl4ai-setup`: Initializes crawl4ai’s required dependencies

### [markdown-crawler](#/convert-html-to-markdown?id=markdown-crawler)

[markdown-crawler](https://pypi.org/project/markdown-crawler/) combines web crawling with markdown conversion in one tool. It’s efficient for bulk processing but tends to produce lower-quality markdown conversion compared to specialized converters like pandoc or defuddle. Best for projects where quantity and integration are more important than perfect formatting.

```
uv venv
source .venv/bin/activate.fish
uv pip install markdown-crawler
markdown-crawler -t 5 -d 3 -b ./markdown https://study.iitm.ac.in/ds/Copy to clipboardErrorCopied
```

* `uv venv` and activation: Same as above
* `uv pip install markdown-crawler`: Installs the markdown-crawler package
* `markdown-crawler`: Runs the crawler with these options:
  + `-t 5`: Sets 5 threads for parallel crawling
  + `-d 3`: Limits crawl depth to 3 levels
  + `-b ./markdown`: Sets the base output directory
  + Final argument is the starting URL

[Previous

Convert PDFs to Markdown](#/convert-pdfs-to-markdown)

[Next

LLM Website Scraping](#/llm-website-scraping)

---


# File: Convert_PDFs_to_Markdown.md

---
title: "Convert PDFs to Markdown"
original_url: "https://tds.s-anand.net/#/convert-pdfs-to-markdown?id=tips-for-optimal-pdf-conversion"
downloaded_at: "2025-05-31T21:37:36.930314"
---

[Converting PDFs to Markdown](#/convert-pdfs-to-markdown?id=converting-pdfs-to-markdown)
----------------------------------------------------------------------------------------

PDF documents are ubiquitous in academic, business, and technical contexts, but extracting and repurposing their content can be challenging. This tutorial explores various command-line tools for converting PDFs to Markdown format, with a focus on preserving structure and formatting suitable for different use cases, including preparation for Large Language Models (LLMs).

Use Cases:

* **LLM training and fine-tuning**: Create clean text data from PDFs for AI model training
* **Knowledge base creation**: Transform PDFs into searchable, editable markdown documents
* **Content repurposing**: Convert academic papers and reports for web publication
* **Data extraction**: Pull structured content from PDF documents for analysis
* **Accessibility**: Convert PDFs to more accessible formats for screen readers
* **Citation and reference management**: Extract bibliographic information from academic papers
* **Documentation conversion**: Transform technical PDFs into maintainable documentation

### [PyMuPDF4LLM](#/convert-pdfs-to-markdown?id=pymupdf4llm)

[PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) is a specialized component of the PyMuPDF library that generates Markdown specifically formatted for Large Language Models. It produces high-quality markdown with good preservation of document structure. It’s specifically optimized for producing text that works well with LLMs, removing irrelevant formatting while preserving semantic structure. Requires PyTorch, which adds dependencies but enables more advanced processing capabilities.

PyMuPDF4LLM uses [MuPDF](https://mupdf.com/) as its PDF parsing engine. [PyMuPDF](https://pymupdf.readthedocs.io/) is emerging as a strong default for PDF text extraction due to its accuracy and performance in handling complex PDF structures.

```
PYTHONUTF8=1 uv run --with pymupdf4llm python -c 'import pymupdf4llm; h = open("pymupdf4llm.md", "w"); h.write(pymupdf4llm.to_markdown("$FILE.pdf"))'Copy to clipboardErrorCopied
```

* `PYTHONUTF8=1`: Forces Python to use UTF-8 encoding regardless of system locale
* `uv run --with pymupdf4llm`: Uses uv package manager to run Python with the pymupdf4llm package
* `python -c '...'`: Executes Python code directly from the command line
* `import pymupdf4llm`: Imports the PDF-to-Markdown module
* `h = open("pymupdf4llm.md", "w")`: Creates a file to write the markdown output
* `h.write(pymupdf4llm.to_markdown("$FILE.pdf"))`: Converts the PDF to markdown and writes to file

[Markitdown](#/convert-pdfs-to-markdown?id=markitdown)
------------------------------------------------------

[![Microsoft MarkItDown - Convert Files and Office Documents to Markdown - Install Locally (9 min)](https://i.ytimg.com/vi/v65Oyddfxeg/sddefault.jpg)](https://youtu.be/v65Oyddfxeg)

[Markitdown](https://github.com/microsoft/markitdown) is Microsoft’s tool for converting various document formats to Markdown, including PDFs, DOCX, XLSX, PPTX, and ZIP files. It’s a versatile multi-format converter that handles PDFs via PDFMiner, DOCX via Mammoth, XLSX via Pandas, and PPTX via Python-PPTX. Good for batch processing of mixed document types. The quality of PDF conversion is generally good but may struggle with complex layouts or heavily formatted documents.

```
PYTHONUTF8=1 uvx markitdown $FILE.pdf > markitdown.mdCopy to clipboardErrorCopied
```

* `PYTHONUTF8=1`: Forces Python to use UTF-8 encoding
* `uvx markitdown`: Runs the markitdown tool via the uv package manager
* `$FILE.pdf`: The input PDF file
* `> markitdown.md`: Redirects output to a markdown file

### [Unstructured](#/convert-pdfs-to-markdown?id=unstructured)

[Unstructured](https://unstructured.io/) is rapidly becoming the de facto library for parsing over 40 different file types. It is excellent for extracting text and tables from diverse document formats. Particularly useful for generating clean content to pass to LLMs. Strong community support and actively maintained.

[GROBID](#/convert-pdfs-to-markdown?id=grobid)
----------------------------------------------

If you specifically need to parse references from text-native PDFs or reliably OCR’ed ones, [GROBID](https://github.com/kermitt2/grobid) remains the de facto choice. It excels at extracting structured bibliographic information with high accuracy.

```
# Start GROBID service
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

# Process PDF with curl
curl -X POST -F "input=@paper.pdf" localhost:8070/api/processFulltextDocument > references.tei.xmlCopy to clipboardErrorCopied
```

### [Mistral OCR API](#/convert-pdfs-to-markdown?id=mistral-ocr-api)

[Mistral OCR](https://mistral.ai/products/ocr/) offers an end-to-end cloud API that preserves both text and layout, making it easier to isolate specific sections like References. It shows the most promise currently, though it requires post-processing.

[Azure Document Intelligence API](#/convert-pdfs-to-markdown?id=azure-document-intelligence-api)
------------------------------------------------------------------------------------------------

For enterprise users already in the Microsoft ecosystem, [Azure Document Intelligence](https://azure.microsoft.com/en-us/products/ai-services/document-intelligence) provides excellent raw OCR with enterprise SLAs. May require custom model training or post-processing to match GROBID’s reference extraction capabilities.

### [Other libraries](#/convert-pdfs-to-markdown?id=other-libraries)

[Docling](https://github.com/DS4SD/docling) is IBM’s document understanding library that supports PDF conversion. It can be challenging to install, particularly on Windows and some Linux distributions. Offers advanced document understanding capabilities beyond simple text extraction.

[MegaParse](https://github.com/QuivrHQ/MegaParse) takes a comprehensive approach using LibreOffice, Pandoc, Tesseract OCR, and other tools. It has Robust handling of different document types but requires an OpenAI API key for some features. Good for complex documents but has significant dependencies.

[Comparison of PDF-to-Markdown Tools](#/convert-pdfs-to-markdown?id=comparison-of-pdf-to-markdown-tools)
--------------------------------------------------------------------------------------------------------

| Tool | Strengths | Weaknesses | Best For |
| --- | --- | --- | --- |
| PyMuPDF4LLM | Structure preservation, LLM optimization | Requires PyTorch | AI training data, semantic structure |
| Markitdown | Multi-format support, simple usage | Less precise layout handling | Batch processing, mixed documents |
| Unstructured | Wide format support, active development | Can be resource-intensive | Production pipelines, integration |
| GROBID | Reference extraction excellence | Narrower use case | Academic papers, citations |
| Docling | Advanced document understanding | Installation difficulties | Research applications |
| MegaParse | Comprehensive approach | Requires OpenAI API | Complex documents, OCR needs |

How to pick:

* **Need LLM-ready content?** PyMuPDF4LLM is specifically designed for this
* **Working with multiple document formats?** Markitdown handles diverse inputs
* **Extracting academic references?** GROBID remains the standard
* **Building a production pipeline?** Unstructured offers the best integration options
* **Handling complex layouts?** Consider commercial OCR like Mistral or Azure Document Intelligence

The optimal approach depends on your specific requirements regarding accuracy, structure preservation, and the intended use of the extracted content.

[Tips for Optimal PDF Conversion](#/convert-pdfs-to-markdown?id=tips-for-optimal-pdf-conversion)
------------------------------------------------------------------------------------------------

1. **Pre-process PDFs** when possible:

   ```
   # Optimize a PDF for text extraction first
   ocrmypdf --optimize 3 --skip-text input.pdf optimized.pdfCopy to clipboardErrorCopied
   ```
2. **Try multiple tools** on the same document to compare results:
3. **Handle scanned PDFs** appropriately:

   ```
   # For scanned documents, run OCR first
   ocrmypdf --force-ocr input.pdf ocr_ready.pdf
   PYTHONUTF8=1 uvx markitdown ocr_ready.pdf > markitdown.mdCopy to clipboardErrorCopied
   ```
4. **Consider post-processing** for better results:

   ```
   # Simple post-processing example
   sed -i 's/\([A-Z]\)\./\1\.\n/g' output.md  # Add line breaks after sentencesCopy to clipboardErrorCopied
   ```

[Previous

Scraping PDFs with Tabula](#/scraping-pdfs-with-tabula)

[Next

Convert HTML to Markdown](#/convert-html-to-markdown)

---


# File: Correlation_with_Excel.md

---
title: "Correlation with Excel"
original_url: "https://tds.s-anand.net/#/correlation-with-excel?id=correlation-with-excel"
downloaded_at: "2025-05-31T21:39:04.004251"
---

[Correlation with Excel](#/correlation-with-excel?id=correlation-with-excel)
----------------------------------------------------------------------------

[![Correlation with Excel](https://i.ytimg.com/vi_webp/lXHCyhO7DmY/sddefault.webp)](https://youtu.be/lXHCyhO7DmY)

You’ll learn to calculate and interpret correlations using Excel, covering:

* **Enabling the Data Analysis Tool Pack**: Steps to enable the Excel data analysis tool pack.
* **Correlation Analysis**: Understanding statistical association between variables.
* **Creating a Correlation Matrix**: Steps to generate and interpret a correlation matrix.
* **Scatterplots and Trendlines**: Plotting data and adding trend lines to visualize correlations.
* **Analyzing Results**: Comparing correlation coefficients and understanding their implications.
* **Insights and Further Analysis**: Interpreting scatterplots and planning further analysis for deeper insights.

Here are the links used in the video:

* [Understand correlation](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/correlation-coefficient-r/v/correlation-coefficient-intuition-examples)
* [COVID-19 vaccinations data explorer - Website](https://ourworldindata.org/covid-vaccinations?country=OWID_WRL)
* [COVID-19 vaccinations - Correlations Excel file](https://docs.google.com/spreadsheets/d/1_vQF2i5ubKmHQMBqoTwsu6AlevWsQtTD/view#gid=790744269)

[Previous

6. Data Analysis](#/data-analysis)

[Next

Regression with Excel](#/regression-with-excel)

---


# File: Crawling_with_the_CLI.md

---
title: "Crawling with the CLI"
original_url: "https://tds.s-anand.net/#/crawling-cli?id=httrack"
downloaded_at: "2025-05-31T21:38:09.310793"
---

[Crawling with the CLI](#/crawling-cli?id=crawling-with-the-cli)
----------------------------------------------------------------

Since websites are a common source of data, we often download entire websites (crawling) and then process them offline.

Web crawling is essential in many data-driven scenarios:

* **Data mining and analysis**: Gathering structured data from multiple pages for market research, competitive analysis, or academic research
* **Content archiving**: Creating offline copies of websites for preservation or backup purposes
* **SEO analysis**: Analyzing site structure, metadata, and content to improve search rankings
* **Legal compliance**: Capturing website content for regulatory or compliance documentation
* **Website migration**: Creating a complete copy before moving to a new platform or design
* **Offline access**: Downloading educational resources, documentation, or reference materials for use without internet connection

The most commonly used tool for fetching websites is [`wget`](https://www.gnu.org/software/wget/). It is pre-installed in many UNIX distributions and easy to install.

[![Scraping Websites using Wget (8 min)](https://i.ytimg.com/vi/pLfH5TZBGXo/sddefault.jpg)](https://youtu.be/pLfH5TZBGXo)

To crawl the [IIT Madras Data Science Program website](https://study.iitm.ac.in/ds/) for example, you could run:

```
wget \
  --recursive \
  --level=3 \
  --no-parent \
  --convert-links \
  --adjust-extension \
  --compression=auto \
  --accept html,htm \
  --directory-prefix=./ds \
  https://study.iitm.ac.in/ds/Copy to clipboardErrorCopied
```

Here’s what each option does:

* `--recursive`: Enables recursive downloading (following links)
* `--level=3`: Limits recursion depth to 3 levels from the initial URL
* `--no-parent`: Restricts crawling to only URLs below the initial directory
* `--convert-links`: Converts all links in downloaded documents to work locally
* `--adjust-extension`: Adds proper extensions to files (.html, .jpg, etc.) based on MIME types
* `--compression=auto`: Automatically handles compressed content (gzip, deflate)
* `--accept html,htm`: Only downloads files with these extensions
* `--directory-prefix=./ds`: Saves all downloaded files to the specified directory

[wget2](https://gitlab.com/gnuwget/wget2) is a better version of `wget` and supports HTTP2, parallel connections, and only updates modified sites. The syntax is (mostly) the same.

```
wget2 \
  --recursive \
  --level=3 \
  --no-parent \
  --convert-links \
  --adjust-extension \
  --compression=auto \
  --accept html,htm \
  --directory-prefix=./ds \
  https://study.iitm.ac.in/ds/Copy to clipboardErrorCopied
```

There are popular free and open-source alternatives to Wget:

### [Wpull](#/crawling-cli?id=wpull)

[Wpull](https://github.com/ArchiveTeam/wpull) is a wget‐compatible Python crawler that supports on-disk resumption, WARC output, and PhantomJS integration.

```
uvx wpull \
  --recursive \
  --level=3 \
  --no-parent \
  --convert-links \
  --adjust-extension \
  --compression=auto \
  --accept html,htm \
  --directory-prefix=./ds \
  https://study.iitm.ac.in/ds/Copy to clipboardErrorCopied
```

### [HTTrack](#/crawling-cli?id=httrack)

[HTTrack](https://www.httrack.com/html/fcguide.html) is dedicated website‐mirroring tool with rich filtering and link‐conversion options.

```
httrack "https://study.iitm.ac.in/ds/" \
  -O "./ds" \
  "+*.study.iitm.ac.in/ds/*" \
  -r3Copy to clipboardErrorCopied
```

### [Robots.txt](#/crawling-cli?id=robotstxt)

`robots.txt` is a standard file found in a website’s root directory that specifies which parts of the site should not be accessed by web crawlers. It’s part of the Robots Exclusion Protocol, an ethical standard for web crawling.

**Why it’s important**:

* **Server load protection**: Prevents excessive traffic that could overload servers
* **Privacy protection**: Keeps sensitive or private content from being indexed
* **Legal compliance**: Respects website owners’ rights to control access to their content
* **Ethical web citizenship**: Shows respect for website administrators’ wishes

**How to override robots.txt restrictions**:

* **wget, wget2**: Use `-e robots=off`
* **httrack**: Use `-s0`
* **wpull**: Use `--no-robots`

**When to override robots.txt (use with discretion)**:

Only bypass `robots.txt` when:

* You have explicit permission from the website owner
* You’re crawling your own website
* The content is publicly accessible and your crawling won’t cause server issues
* You’re conducting authorized security testing

Remember that bypassing `robots.txt` without legitimate reason may:

* Violate terms of service
* Lead to IP banning
* Result in legal consequences in some jurisdictions
* Cause reputation damage to your organization

Always use the minimum necessary crawling speed and scope, and consider contacting website administrators for permission when in doubt.

[Previous

Scraping with Google Sheets](#/scraping-with-google-sheets)

[Next

BBC Weather API with Python](#/bbc-weather-api-with-python)

---


# File: Data_Aggregation_in_Excel.md

---
title: "Data Aggregation in Excel"
original_url: "https://tds.s-anand.net/#/data-aggregation-in-excel?id=data-aggregation-in-excel"
downloaded_at: "2025-05-31T21:36:28.355638"
---

[Data Aggregation in Excel](#/data-aggregation-in-excel?id=data-aggregation-in-excel)
-------------------------------------------------------------------------------------

[![Data aggregation in Excel](https://i.ytimg.com/vi_webp/NkpT0dDU8Y4/sddefault.webp)](https://youtu.be/NkpT0dDU8Y4)

You’ll learn data aggregation and visualization techniques in Excel, covering:

* **Data Cleanup**: Remove empty columns and rows with missing values.
* **Creating Excel Tables**: Convert raw data into tables for easier manipulation and formula application.
* **Date Manipulation**: Extract week, month, and year from date columns using Excel functions (WEEKNUM, TEXT).
* **Color Scales**: Apply color scales to visualize clusters and trends in data over time.
* **Pivot Tables**: Create pivot tables to aggregate data by location and date, summarizing values weekly and monthly.
* **Sparklines**: Use sparklines to visualize trends within pivot tables, making data patterns more apparent.
* **Data Bars**: Implement data bars for graphical illustrations of numerical columns, showing trends and waves.

Here are links used in the video:

* [COVID-19 data Excel file - raw data](https://docs.google.com/spreadsheets/d/14HLgSmME95q--6lcBv9pUstqHL183wTd/view)

[Previous

Splitting Text in Excel](#/splitting-text-in-excel)

[Next

Data Preparation in the Shell](#/data-preparation-in-the-shell)

---


# File: Data_Analysis_with_DuckDB.md

---
title: "Data Analysis with DuckDB"
original_url: "https://tds.s-anand.net/#/data-analysis-with-duckdb?id=data-analysis-with-duckdb"
downloaded_at: "2025-05-31T21:38:48.782580"
---

[Data Analysis with DuckDB](#/data-analysis-with-duckdb?id=data-analysis-with-duckdb)
-------------------------------------------------------------------------------------

[![Data Analysis with DuckDB](https://i.ytimg.com/vi_webp/4U0GqYrET5s/sddefault.webp)](https://youtu.be/4U0GqYrET5s)

You’ll learn how to perform data analysis using DuckDB and Pandas, covering:

* **Parquet for Data Storage**: Understand why Parquet is a faster, more compact, and better-typed storage format compared to CSV, JSON, and SQLite.
* **DuckDB Setup**: Learn how to install and set up DuckDB, along with integrating it into a Jupyter notebook environment.
* **File Format Comparisons**: Compare file formats by speed and size, observing the performance difference between saving and loading data in CSV, JSON, SQLite, and Parquet.
* **Faster Queries with DuckDB**: Learn how DuckDB uses parallel processing, columnar storage, and on-disk operations to outperform Pandas in speed and memory efficiency.
* **SQL Query Execution in DuckDB**: Run SQL queries directly on Parquet files and Pandas DataFrames to compute metrics such as the number of unique flight routes delayed by certain time intervals.
* **Memory Efficiency**: Understand how DuckDB performs analytics without loading entire datasets into memory, making it highly efficient for large-scale data analysis.
* **Mixing DuckDB and Pandas**: Learn to interleave DuckDB and Pandas operations, leveraging the strengths of both tools to perform complex queries like correlations and aggregations.
* **Ranking and Filtering Data**: Use SQL and Pandas to rank arrival delays by distance and extract key insights, such as the earliest flight arrival for each route.
* **Joining Data**: Create a cost analysis by joining datasets and calculating total costs of flight delays, demonstrating DuckDB’s speed in joining and aggregating large datasets.

Here are the links used in the video:

* [Data analysis with DuckDB - Notebook](https://drive.google.com/file/d/1Y9XSs-LeSz-ZmnQj4OGP-Q4yDkPJrmsZ/view)
* [Parquet file format](https://parquet.apache.org/) - a fast columnar storage format that’s becoming a de facto standard for big data
* [DuckDB](https://duckdb.org/) - a fast in-memory database that’s very good with large-scale analysis
* [Plotly Datasets](https://github.com/plotly/datasets/) - a collection of sample datasets for analysis. This includes the [Kaggle Flights Dataset](https://www.kaggle.com/datasets/usdot/flight-delays) that the notebook downloads as [2015\_flights.parquet](https://github.com/plotly/datasets/raw/master/2015_flights.parquet)

[Previous

Data Analysis with Datasette](#/data-analysis-with-datasette)

[Next

Data Analysis with ChatGPT](#/data-analysis-with-chatgpt)

---


# File: Data_Analysis_with_Python.md

---
title: "Data Analysis with Python"
original_url: "https://tds.s-anand.net/#/data-analysis-with-python?id=data-analysis-with-python"
downloaded_at: "2025-05-31T21:38:33.341032"
---

[Data Analysis with Python](#/data-analysis-with-python?id=data-analysis-with-python)
-------------------------------------------------------------------------------------

[![Data Analysis with Python](https://i.ytimg.com/vi_webp/ZPfZH14FK90/sddefault.webp)](https://youtu.be/ZPfZH14FK90)

You’ll learn practical data analysis techniques in Python using Pandas, covering:

* **Reading Parquet Files**: Utilize Pandas to read Parquet file formats for efficient data handling.
* **Dataframe Inspection**: Methods to preview and understand the structure of a dataset.
* **Pivot Tables**: Creating and interpreting pivot tables to summarize data.
* **Percentage Calculations**: Normalize pivot table values to percentages for better insights.
* **Correlation Analysis**: Calculate and interpret correlation between variables, including significance testing.
* **Statistical Significance**: Use statistical tests to determine the significance of observed correlations.
* **Datetime Handling**: Extract and manipulate date and time information from datetime columns.
* **Data Visualization**: Generate and customize heat maps to visualize data patterns effectively.
* **Leveraging AI**: Use ChatGPT to generate and refine analytical code, enhancing productivity and accuracy.

Here are the links used in the video:

* [Data analysis with Python - Notebook](https://colab.research.google.com/drive/1wEUEeF_e2SSmS9uf2-3fZJQ2kEFRnxah)
* [Card transactions dataset (Parquet)](https://drive.google.com/file/u/3/d/1XGvuFjoTwlybkw0cc9u34horMF9vMhrB/view)
* [10 minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
* [Python Pandas tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)

[Previous

Outlier Detection with Excel](#/outlier-detection-with-excel)

[Next

Data Analysis with SQL](#/data-analysis-with-sql)

---


# File: Data_Analysis_with_SQL.md

---
title: "Data Analysis with SQL"
original_url: "https://tds.s-anand.net/#/data-analysis-with-sql?id=data-analysis-with-sql"
downloaded_at: "2025-05-31T21:34:26.638118"
---

[Data Analysis with SQL](#/data-analysis-with-sql?id=data-analysis-with-sql)
----------------------------------------------------------------------------

[![Data Analysis with Databases](https://i.ytimg.com/vi_webp/Xn3QkYrThbI/sddefault.webp)](https://youtu.be/Xn3QkYrThbI)

You’ll learn how to perform data analysis using SQL (via Python), covering:

* **Database Connection**: How to connect to a MySQL database using SQLAlchemy and Pandas.
* **SQL Queries**: Execute SQL queries directly from a Python environment to retrieve and analyze data.
* **Counting Rows**: Use SQL to count the number of rows in a table.
* **User Activity Analysis**: Query and identify top users by post count.
* **Post Concentration**: Determine if a small percentage of users contribute the majority of posts using SQL aggregation.
* **Correlation Calculation**: Calculate the Pearson correlation coefficient between user attributes such as age and reputation.
* **Regression Analysis**: Compute the regression slope to understand the relationship between views and reputation.
* **Handling Large Data**: Perform calculations on large datasets by fetching aggregated values from the database rather than entire datasets.
* **Statistical Analysis in SQL**: Use SQL as a tool for statistical analysis, demonstrating its power beyond simple data retrieval.
* **Leveraging AI**: Use ChatGPT to generate SQL queries and Python code, enhancing productivity and accuracy.

Here are the links used in the video:

* [Data analysis with databases - Notebook](https://colab.research.google.com/drive/1j_5AsWdf0SwVHVgfbEAcg7vYguKUN41o)
* [SQLZoo](https://www.sqlzoo.net/wiki/SQL_Tutorial) has simple interactive tutorials to learn SQL
* [Stats database](https://relational-data.org/dataset/Stats) that has an anonymized dump of [stats.stackexchange.com](https://stats.stackexchange.com/)
* [Pandas `read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
* [SQLAlchemy docs](https://docs.sqlalchemy.org/)

[Previous

Data Analysis with Python](#/data-analysis-with-python)

[Next

Data Analysis with Datasette](#/data-analysis-with-datasette)

---


# File: Data_Cleansing_in_Excel.md

---
title: "Data Cleansing in Excel"
original_url: "https://tds.s-anand.net/#/data-cleansing-in-excel?id=data-cleansing-in-excel"
downloaded_at: "2025-05-31T21:35:07.240861"
---

[Data Cleansing in Excel](#/data-cleansing-in-excel?id=data-cleansing-in-excel)
-------------------------------------------------------------------------------

[![Clean up data in Excel](https://i.ytimg.com/vi_webp/7du7xkqeu4s/sddefault.webp)](https://youtu.be/7du7xkqeu4s)

You’ll learn basic but essential data cleaning techniques in Excel, covering:

* **Find and Replace**: Use Ctrl+H to replace or remove specific terms (e.g., removing “[more]” from country names).
* **Changing Data Formats**: Convert columns from general to numerical format.
* **Removing Extra Spaces**: Use the TRIM function to clean up unnecessary spaces in text.
* **Identifying and Removing Blank Cells**: Highlight and delete entire rows with blank cells using the “Go To Special” function.
* **Removing Duplicates**: Use the “Remove Duplicates” feature to eliminate duplicate entries, demonstrated with country names.

Here are links used in the video:

* [List of Largest Cities Excel file](https://docs.google.com/spreadsheets/d/1jl8tHGoxmIba4J78aJVfT9jtZv7lfCbV/view)

[Previous

5. Data Preparation](#/data-preparation)

[Next

Data Transformation in Excel](#/data-transformation-in-excel)

---


# File: Data_Preparation_in_the_Editor.md

---
title: "Data Preparation in the Editor"
original_url: "https://tds.s-anand.net/#/data-preparation-in-the-editor?id=data-preparation-in-the-editor"
downloaded_at: "2025-05-31T21:39:05.071642"
---

[Data Preparation in the Editor](#/data-preparation-in-the-editor?id=data-preparation-in-the-editor)
----------------------------------------------------------------------------------------------------

[![Data preparation in the editor](https://i.ytimg.com/vi_webp/99lYu43L9uM/sddefault.webp)](https://youtu.be/99lYu43L9uM)

You’ll learn how to use a text editor [Visual Studio Code](https://code.visualstudio.com/) to process and clean data, covering:

* **Format** JSON files
* **Find all** and multiple cursors to extract specific fields
* **Sort** lines
* **Delete duplicate** lines
* **Replace** text with multiple cursors

Here are the links used in the video:

* [City-wise product sales JSON](https://drive.google.com/file/d/1VEnKChf4i04iKsQfw0MwoJlfkOBGQ65B/view?usp=drive_link)

[Previous

Data Preparation in the Shell](#/data-preparation-in-the-shell)

[Next

Cleaning Data with OpenRefine](#/cleaning-data-with-openrefine)

---


# File: Data_Preparation_in_the_Shell.md

---
title: "Data Preparation in the Shell"
original_url: "https://tds.s-anand.net/#/data-preparation-in-the-shell?id=data-preparation-in-the-shell"
downloaded_at: "2025-05-31T21:36:00.819847"
---

[Data Preparation in the Shell](#/data-preparation-in-the-shell?id=data-preparation-in-the-shell)
-------------------------------------------------------------------------------------------------

[![Data preparation in the shell](https://i.ytimg.com/vi_webp/XEdy4WK70vU/sddefault.webp)](https://youtu.be/XEdy4WK70vU)

You’ll learn how to use UNIX tools to process and clean data, covering:

* `curl` (or `wget`) to fetch data from websites.
* `gzip` (or `xz`) to compress and decompress files.
* `wc` to count lines, words, and characters in text.
* `head` and `tail` to get the start and end of files.
* `cut` to extract specific columns from text.
* `uniq` to de-duplicate lines.
* `sort` to sort lines.
* `grep` to filter lines containing specific text.
* `sed` to search and replace text.
* `awk` for more complex text processing.

Here are the links used in the video:

* [Data preparation in the shell - Notebook](https://colab.research.google.com/drive/1KSFkQDK0v__XWaAaHKeQuIAwYV0dkTe8)
* [Data Science at the Command Line](https://jeroenjanssens.com/dsatcl/)

[Previous

Data Aggregation in Excel](#/data-aggregation-in-excel)

[Next

Data Preparation in the Editor](#/data-preparation-in-the-editor)

---


# File: Data_Storytelling.md

---
title: "Data Storytelling"
original_url: "https://tds.s-anand.net/#/data-storytelling?id=data-storytelling"
downloaded_at: "2025-05-31T21:38:43.337343"
---

[Data Storytelling](#/data-storytelling?id=data-storytelling)
=============================================================

[![Narrate a story](https://i.ytimg.com/vi_webp/aF93i6zVVQg/sddefault.webp)](https://youtu.be/aF93i6zVVQg)

[Previous

RAWgraphs](#/rawgraphs)

[Next

Narratives with LLMs](#/narratives-with-llms)

---


# File: Data_Transformation_in_Excel.md

---
title: "Data Transformation in Excel"
original_url: "https://tds.s-anand.net/#/data-transformation-in-excel?id=data-transformation-in-excel"
downloaded_at: "2025-05-31T21:34:22.341146"
---

[Data Transformation in Excel](#/data-transformation-in-excel?id=data-transformation-in-excel)
----------------------------------------------------------------------------------------------

[![Data transformation in Excel](https://i.ytimg.com/vi_webp/gR2IY5Naja0/sddefault.webp)](https://youtu.be/gR2IY5Naja0)

You’ll learn data transformation techniques in Excel, covering:

* **Calculating Ratios**: Compute metro area to city area and metro population to city population ratios.
* **Using Pivot Tables**: Create pivot tables to aggregate data and identify outliers.
* **Filtering Data**: Apply filters in pivot tables to analyze specific subsets of data.
* **Counting Data Occurrences**: Use pivot tables to count the frequency of specific entries.
* **Creating Charts**: Generate charts from pivot table data to visualize distributions and outliers.

Here are links used in the video:

* [List of Largest Cities Excel file](https://docs.google.com/spreadsheets/d/1jl8tHGoxmIba4J78aJVfT9jtZv7lfCbV/view)

[Previous

Data Cleansing in Excel](#/data-cleansing-in-excel)

[Next

Splitting Text in Excel](#/splitting-text-in-excel)

---


# File: Data_Transformation_with_dbt.md

---
title: "Data Transformation with dbt"
original_url: "https://tds.s-anand.net/#/data-analysis-with-chatgpt"
downloaded_at: "2025-05-31T21:35:05.054150"
---

404 - Not found
===============

---


# File: Data_Visualization_with_Seaborn.md

---
title: "Data Visualization with Seaborn"
original_url: "https://tds.s-anand.net/#/data-visualization-with-seaborn?id=data-visualization-with-seaborn"
downloaded_at: "2025-05-31T21:35:34.896791"
---

[Data Visualization with Seaborn](#/data-visualization-with-seaborn?id=data-visualization-with-seaborn)
-------------------------------------------------------------------------------------------------------

[Seaborn](https://seaborn.pydata.org/) is a data visualization library for Python. It’s based on Matplotlib but a bit easier to use, and a bit prettier.

[![Seaborn Tutorial : Seaborn Full Course](https://i.ytimg.com/vi_webp/6GUZXDef2U0/sddefault.webp)](https://youtu.be/6GUZXDef2U0)

[Previous

Visualizing Charts with Excel](#/visualizing-charts-with-excel)

[Next

Data Visualization with ChatGPT](#/data-visualization-with-chatgpt)

---


# File: Database__SQLite.md

---
title: "Database: SQLite"
original_url: "https://tds.s-anand.net/#/sqlite?id=database-sqlite"
downloaded_at: "2025-05-31T21:39:52.627950"
---

[Database: SQLite](#/sqlite?id=database-sqlite)
-----------------------------------------------

Relational databases are used to store data in a structured way. You’ll often access databases created by others for analysis.

PostgreSQL, MySQL, MS SQL, Oracle, etc. are popular databases. But the most installed database is [SQLite](https://www.sqlite.org/index.html). It’s embedded into many devices and apps (e.g. your phone, browser, etc.). It’s lightweight but very scalable and powerful.

Watch these introductory videos to understand SQLite and how it’s used in Python (34 min):

[![SQLite Introduction - Beginners Guide to SQL and Databases (22 min)](https://i.ytimg.com/vi_webp/8Xyn8R9eKB8/sddefault.webp)](https://youtu.be/8Xyn8R9eKB8)

[![SQLite Backend for Beginners - Create Quick Databases with Python and SQL (13 min)](https://i.ytimg.com/vi_webp/Ohj-CqALrwk/sddefault.webp)](https://youtu.be/Ohj-CqALrwk)

There are many non-relational databases (NoSQL) like [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html), [MongoDB](https://www.mongodb.com/docs/manual/), [Redis](https://redis.io/docs/latest/), etc. that you should know about and we may cover later.

Core Concepts:

```
-- Create a table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');

-- Query data
SELECT name, COUNT(*) as count
FROM users
GROUP BY name
HAVING count > 1;

-- Join tables
SELECT u.name, o.product
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.status = 'pending';Copy to clipboardErrorCopied
```

Python Integration:

```
import sqlite3
from pathlib import Path
import pandas as pd

async def query_database(db_path: Path, query: str) -> pd.DataFrame:
    """Execute SQL query and return results as DataFrame.

    Args:
        db_path: Path to SQLite database
        query: SQL query to execute

    Returns:
        DataFrame with query results
    """
    try:
        conn = sqlite3.connect(db_path)
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

# Example usage
db = Path('data.db')
df = await query_database(db, '''
    SELECT date, COUNT(*) as count
    FROM events
    GROUP BY date
''')Copy to clipboardErrorCopied
```

Common Operations:

1. **Database Management**

   ```
   -- Backup database
   .backup 'backup.db'

   -- Import CSV
   .mode csv
   .import data.csv table_name

   -- Export results
   .headers on
   .mode csv
   .output results.csv
   SELECT * FROM table;Copy to clipboardErrorCopied
   ```
2. **Performance Optimization**

   ```
   -- Create index
   CREATE INDEX idx_user_email ON users(email);

   -- Analyze query
   EXPLAIN QUERY PLAN
   SELECT * FROM users WHERE email LIKE '%@example.com';

   -- Show indexes
   SELECT * FROM sqlite_master WHERE type='index';Copy to clipboardErrorCopied
   ```
3. **Data Analysis**

   ```
   -- Time series aggregation
   SELECT
       date(timestamp),
       COUNT(*) as events,
       AVG(duration) as avg_duration
   FROM events
   GROUP BY date(timestamp);

   -- Window functions
   SELECT *,
       AVG(amount) OVER (
           PARTITION BY user_id
           ORDER BY date
           ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
       ) as moving_avg
   FROM transactions;Copy to clipboardErrorCopied
   ```

Tools to work with SQLite:

* [SQLiteStudio](https://sqlitestudio.pl/): Lightweight GUI
* [DBeaver](https://dbeaver.io/): Full-featured GUI
* [sqlite-utils](https://sqlite-utils.datasette.io/): CLI tool
* [Datasette](https://datasette.io/): Web interface

[Previous

Spreadsheet: Excel, Google Sheets](#/spreadsheets)

[Next

Version Control: Git, GitHub](#/git)

---


# File: DevContainers__GitHub_Codespaces.md

---
title: "DevContainers: GitHub Codespaces"
original_url: "https://tds.s-anand.net/#/github-codespaces?id=quick-setup"
downloaded_at: "2025-05-31T21:38:25.478335"
---

[IDE: GitHub Codespaces](#/github-codespaces?id=ide-github-codespaces)
----------------------------------------------------------------------

[GitHub Codespaces](https://github.com/features/codespaces) is a cloud-hosted development environment built right into GitHub that gets you coding faster with pre-configured containers, adjustable compute power, and seamless integration with workflows like Actions and Copilot.

**Why Codespaces helps**

* **Reproducible onboarding**: Say goodbye to “works on my machine” woes—everyone uses the same setup for assignments or demos.
* **Anywhere access**: Jump back into your project from a laptop, tablet, or phone without having to reinstall anything.
* **Rapid experimentation & debugging**: Spin up short-lived environments on any branch, commit, or PR to isolate bugs or test features, or keep longer-lived codespaces for big projects.

[![Introduction to GitHub Codespaces (5 min)](https://i.ytimg.com/vi_webp/-tQ2nxjqP6o/sddefault.webp)](https://www.youtube.com/watch?v=-tQ2nxjqP6o)

### [Quick Setup](#/github-codespaces?id=quick-setup)

1. [**From the GitHub UI**](https://github.com/codespaces)

   * Go to your repo and click **Code → Codespaces → New codespace**.
   * Pick the branch and machine specs (2–32 cores, 8–64 GB RAM), then click **Create codespace**.
2. [**In Visual Studio Code**](https://code.visualstudio.com/docs/remote/codespaces)

   * Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), choose **Codespaces: Create New Codespace**, and follow the prompts.
3. [**Via GitHub CLI**](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-with-github-cli)

   ```
   gh auth login
   gh codespace create --repo OWNER/REPO
   gh codespace list    # List all codespaces
   gh codespace code    # opens in your local VS Code
   gh codespace ssh     # SSH into the codepsaceCopy to clipboardErrorCopied
   ```

### [Features To Explore](#/github-codespaces?id=features-to-explore)

* **Dev Containers**: Set up your environment the same way every time using a `devcontainer.json` or your own Dockerfile. [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
* **Prebuilds**: Build bigger or more complex repos in advance so codespaces start up in a flash. [About prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
* **Port Forwarding**: Let Codespaces spot and forward the ports your web apps use automatically. [Forward ports in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)
* **Secrets & Variables**: Keep your environment variables safe in the Codespaces settings for your repo. [Manage Codespaces secrets](https://docs.github.com/en/enterprise-cloud@latest/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization)
* **Dotfiles Integration**: Bring in your dotfiles repo to customize shell settings, aliases, and tools in every codespace. [Personalizing your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account)
* **Machine Types & Cost Control**: Pick from VMs with 2 to 32 cores and track your usage in the billing dashboard. [Managing Codespaces costs](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)
* **VS Code & CLI Integration**: Flip between browser VS Code and your desktop editor, and script everything with the CLI. [VS Code Remote: Codespaces](https://code.visualstudio.com/docs/remote/codespaces)
* **GitHub Actions**: Power up prebuilds and your CI/CD right inside codespaces using Actions workflows. [Prebuilding your codespaces](https://docs.github.com/en/codespaces/prebuilding-your-codespaces)
* **Copilot in Codespaces**: Let Copilot help you write code with in-editor AI suggestions. [Copilot in Codespaces](https://docs.github.com/en/codespaces/reference/using-github-copilot-in-github-codespaces)

[Previous

Containers: Docker, Podman](#/docker)

[Next

Tunneling: ngrok](#/ngrok)

---


# File: Editor__VS_Code.md

---
title: "Editor: VS Code"
original_url: "https://tds.s-anand.net/#/vscode?id=editor-vs-code"
downloaded_at: "2025-05-31T21:39:46.357512"
---

[Editor: VS Code](#/vscode?id=editor-vs-code)
---------------------------------------------

Your editor is the most important tool in your arsenal. That’s where you’ll spend most of your time. Make sure you’re comfortable with it.

[**Visual Studio Code**](https://code.visualstudio.com/) is, *by far*, the most popular code editor today. According to the [2024 StackOverflow Survey](https://survey.stackoverflow.co/2024/technology/#1-integrated-development-environment) almost 75% of developers use it. We recommend you learn it well. Even if you use another editor, you’ll be working with others who use it, and it’s a good idea to have some exposure.

Watch these introductory videos (35 min) from the [Visual Studio Docs](https://code.visualstudio.com/docs) to get started:

* [Getting Started](https://code.visualstudio.com/docs/introvideos/basics): Set up and learn the basics of Visual Studio Code. (7 min)
* [Code Editing](https://code.visualstudio.com/docs/introvideos/codeediting): Learn how to edit and run code in VS Code. (3 min)
* [Productivity Tips](https://code.visualstudio.com/docs/introvideos/productivity): Become a VS Code power user with these productivity tips. (4 min)
* [Personalize](https://code.visualstudio.com/docs/introvideos/configure): Personalize VS Code to make it yours with themes. (2 min)
* [Extensions](https://code.visualstudio.com/docs/introvideos/extend): Add features, themes, and more to VS Code with extensions! (4 min)
* [Debugging](https://code.visualstudio.com/docs/introvideos/debugging): Get started with debugging in VS Code. (6 min)
* [Version Control](https://code.visualstudio.com/docs/introvideos/versioncontrol): Learn how to use Git version control in VS Code. (3 min)
* [Customize](https://code.visualstudio.com/docs/introvideos/customize): Learn how to customize your settings and keyboard shortcuts in VS Code. (6 min)

[Previous

1. Development Tools](#/development-tools)

[Next

AI Code Editors: GitHub Copilot](#/github-copilot)

---


# File: Embeddings.md

---
title: "Embeddings"
original_url: "https://tds.s-anand.net/#/embeddings?id=embeddings-openai-and-local-models"
downloaded_at: "2025-05-31T21:39:33.739830"
---

[Embeddings: OpenAI and Local Models](#/embeddings?id=embeddings-openai-and-local-models)
-----------------------------------------------------------------------------------------

Embedding models convert text into a list of numbers. These are like a map of text in numerical form. Each number represents a feature, and similar texts will have numbers close to each other. So, if the numbers are similar, the text they represent mean something similar.

This is useful because text similarity is important in many common problems:

1. **Search**. Find similar documents to a query.
2. **Classification**. Classify text into categories.
3. **Clustering**. Group similar items into clusters.
4. **Anomaly Detection**. Find an unusual piece of text.

You can run embedding models locally or using an API. Local models are better for privacy and cost. APIs are better for scale and quality.

| Feature | Local Models | API |
| --- | --- | --- |
| **Privacy** | High | Dependent on provider |
| **Cost** | High setup, low after that | Pay-as-you-go |
| **Scale** | Limited by local resources | Easily scales with demand |
| **Quality** | Varies by model | Typically high |

The [Massive Text Embedding Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard) provides comprehensive comparisons of embedding models. These models are compared on several parameters, but here are some key ones to look at:

1. **Rank**. Higher ranked models have higher quality.
2. **Memory Usage**. Lower is better (for similar ranks). It costs less and is faster to run.
3. **Embedding Dimensions**. Lower is better. This is the number of numbers in the array. Smaller dimensions are cheaper to store.
4. **Max Tokens**. Higher is better. This is the number of input tokens (words) the model can take in a *single* input.
5. Look for higher scores in the columns for Classification, Clustering, Summarization, etc. based on your needs.

### [Local Embeddings](#/embeddings?id=local-embeddings)

[![Guide to Local Embeddings with Sentence Transformers](https://i.ytimg.com/vi/OATCgQtNX2o/sddefault.jpg)](https://youtu.be/OATCgQtNX2o)

Here’s a minimal example using a local embedding model:

```
# /// script
# requires-python = "==3.12"
# dependencies = [
#   "sentence-transformers",
#   "httpx",
#   "numpy",
# ]
# ///

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('BAAI/bge-base-en-v1.5')  # A small, high quality model

async def embed(text: str) -> list[float]:
    """Get embedding vector for text using local model."""
    return model.encode(text).tolist()

async def get_similarity(text1: str, text2: str) -> float:
    """Calculate cosine similarity between two texts."""
    emb1 = np.array(await embed(text1))
    emb2 = np.array(await embed(text2))
    return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

async def main():
    print(await get_similarity("Apple", "Orange"))
    print(await get_similarity("Apple", "Lightning"))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())Copy to clipboardErrorCopied
```

Note the `get_similarity` function. It uses a [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to calculate the similarity between two embeddings.

### [OpenAI Embeddings](#/embeddings?id=openai-embeddings)

For comparison, here’s how to use OpenAI’s API with direct HTTP calls. Replace the `embed` function in the earlier script:

```
import os
import httpx

async def embed(text: str) -> list[float]:
    """Get embedding vector for text using OpenAI's API."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/embeddings",
            headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
            json={"model": "text-embedding-3-small", "input": text}
        )
        return response.json()["data"][0]["embedding"]Copy to clipboardErrorCopied
```

**NOTE**: You need to set the [`OPENAI_API_KEY`](https://platform.openai.com/api-keys) environment variable for this to work.

[Previous

Vision Models](#/vision-models)

[Next

Multimodal Embeddings](#/multimodal-embeddings)

---


# File: Extracting_Audio_and_Transcripts.md

---
title: "Extracting Audio and Transcripts"
original_url: "https://tds.s-anand.net/#/extracting-audio-and-transcripts?id=extracting-audio-and-transcripts"
downloaded_at: "2025-05-31T21:39:20.074278"
---

[Extracting Audio and Transcripts](#/extracting-audio-and-transcripts?id=extracting-audio-and-transcripts)
----------------------------------------------------------------------------------------------------------

[Media Processing: FFmpeg](#/extracting-audio-and-transcripts?id=media-processing-ffmpeg)
-----------------------------------------------------------------------------------------

[FFmpeg](https://ffmpeg.org/) is the standard command-line tool for processing video and audio files. It’s essential for data scientists working with media files for:

* Extracting audio/video for machine learning
* Converting formats for web deployment
* Creating visualizations and presentations
* Processing large media datasets

Basic Operations:

```
# Basic conversion
ffmpeg -i input.mp4 output.avi

# Extract audio
ffmpeg -i input.mp4 -vn output.mp3

# Convert format without re-encoding
ffmpeg -i input.mkv -c copy output.mp4

# High quality encoding (crf: 0-51, lower is better)
ffmpeg -i input.mp4 -preset slower -crf 18 output.mp4Copy to clipboardErrorCopied
```

Common Data Science Tasks:

```
# Extract frames for computer vision
ffmpeg -i input.mp4 -vf "fps=1" frames_%04d.png    # 1 frame per second
ffmpeg -i input.mp4 -vf "select='eq(n,0)'" -vframes 1 first_frame.jpg

# Create video from image sequence
ffmpeg -r 1/5 -i img%03d.png -c:v libx264 -vf fps=25 output.mp4

# Extract audio for speech recognition
ffmpeg -i input.mp4 -ar 16000 -ac 1 audio.wav      # 16kHz mono

# Trim video/audio for training data
ffmpeg -ss 00:01:00 -i input.mp4 -t 00:00:30 -c copy clip.mp4Copy to clipboardErrorCopied
```

Processing Multiple Files:

```
# Concatenate videos (first create files.txt with list of files)
echo "file 'input1.mp4'
file 'input2.mp4'" > files.txt
ffmpeg -f concat -i files.txt -c copy output.mp4

# Batch process with shell loop
for f in *.mp4; do
    ffmpeg -i "$f" -vn "audio/${f%.mp4}.wav"
doneCopy to clipboardErrorCopied
```

Data Analysis Features:

```
# Get media file information
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Display frame metadata
ffprobe -v quiet -print_format json -show_frames input.mp4

# Generate video thumbnails
ffmpeg -i input.mp4 -vf "thumbnail" -frames:v 1 thumb.jpgCopy to clipboardErrorCopied
```

Watch this introduction to FFmpeg (12 min):

[![FFmpeg in 12 Minutes](https://i.ytimg.com/vi_webp/MPV7JXTWPWI/sddefault.webp)](https://youtu.be/MPV7JXTWPWI)

Tools:

* [ffmpeg.lav.io](https://ffmpeg.lav.io/): Interactive command builder
* [FFmpeg Explorer](https://ffmpeg.guide/): Visual FFmpeg command generator
* [FFmpeg Buddy](https://evanhahn.github.io/ffmpeg-buddy/): Simple command generator

Tips:

1. Use `-c copy` when possible to avoid re-encoding
2. Monitor progress with `-progress pipe:1`
3. Use `-hide_banner` to reduce output verbosity
4. Test commands with small clips first
5. Use hardware acceleration when available (-hwaccel auto)

Error Handling:

```
# Validate file before processing
ffprobe input.mp4 2>&1 | grep "Invalid"

# Continue on errors in batch processing
ffmpeg -i input.mp4 output.mp4 -xerror

# Get detailed error information
ffmpeg -v error -i input.mp4 2>&1 | grep -A2 "Error"Copy to clipboardErrorCopied
```



[Media tools: yt-dlp](#/extracting-audio-and-transcripts?id=media-tools-yt-dlp)
-------------------------------------------------------------------------------

[yt-dlp](https://github.com/yt-dlp/yt-dlp) is a feature-rich command-line tool for downloading audio/video from thousands of sites. It’s particularly useful for extracting audio and transcripts from videos.

Install using your package manager:

```
# macOS
brew install yt-dlp

# Linux
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
chmod a+rx ~/.local/bin/yt-dlp

# Windows
winget install yt-dlpCopy to clipboardErrorCopied
```

Common operations for extracting audio and transcripts:

```
# Download audio only at lowest quality suitable for speech
yt-dlp -f "ba[abr<50]/worstaudio" \
       --extract-audio \
       --audio-format mp3 \
       --audio-quality 32k \
       "https://www.youtube.com/watch?v=VIDEO_ID"

# Download auto-generated subtitles
yt-dlp --write-auto-sub \
       --skip-download \
       --sub-format "srt" \
       "https://www.youtube.com/watch?v=VIDEO_ID"

# Download both audio and subtitles with custom output template
yt-dlp -f "ba[abr<50]/worstaudio" \
       --extract-audio \
       --audio-format mp3 \
       --audio-quality 32k \
       --write-auto-sub \
       --sub-format "srt" \
       -o "%(title)s.%(ext)s" \
       "https://www.youtube.com/watch?v=VIDEO_ID"

# Download entire playlist's audio
yt-dlp -f "ba[abr<50]/worstaudio" \
       --extract-audio \
       --audio-format mp3 \
       --audio-quality 32k \
       -o "%(playlist_index)s-%(title)s.%(ext)s" \
       "https://www.youtube.com/playlist?list=PLAYLIST_ID"Copy to clipboardErrorCopied
```

For Python integration:

```
# /// script
# requires-python = ">=3.9"
# dependencies = ["yt-dlp"]
# ///

import yt_dlp

def download_audio(url: str) -> None:
    """Download audio at speech-optimized quality."""
    ydl_opts = {
        'format': 'ba[abr<50]/worstaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '32'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_audio('https://www.youtube.com/watch?v=VIDEO_ID')Copy to clipboardErrorCopied
```

Tools:

* [ffmpeg](https://ffmpeg.org/): Required for audio extraction and conversion
* [whisper](https://github.com/openai/whisper): Can be used with yt-dlp for speech-to-text
* [gallery-dl](https://github.com/mikf/gallery-dl): Alternative for image-focused sites

Note: Always respect copyright and terms of service when downloading content.

[Whisper transcription](#/extracting-audio-and-transcripts?id=whisper-transcription)
------------------------------------------------------------------------------------

[Faster Whisper](https://github.com/SYSTRAN/faster-whisper) is a highly optimized implementation of OpenAI’s [Whisper model](https://github.com/openai/whisper), offering up to 4x faster transcription while using less memory.

You can install it via:

* `pip install faster-whisper`
* [Download Windows Standalone](https://github.com/Purfview/whisper-standalone-win/releases)

Here’s a basic usage example:

```
faster-whisper-xxl "video.mp4" --model medium --language enCopy to clipboardErrorCopied
```

Here’s my recommendation for transcribing videos. This saves the output in JSON as well as SRT format in the source directory.

```
faster-whisper-xxl --print_progress --output_dir source --batch_recursive \
                   --check_files --standard --output_format json srt \
                   --model medium --language en $FILECopy to clipboardErrorCopied
```

* `--model`: The OpenAI Whisper model to use. You can choose from:
  + `tiny`: Fastest but least accurate
  + `base`: Good for simple audio
  + `small`: Balanced speed/accuracy
  + `medium`: Recommended default
  + `large-v3`: Most accurate but slowest
* `--output_format`: The output format to use. You can pick multiple formats from:
  + `json`: Has the most detailed information including timing, text, quality, etc.
  + `srt`: A popular subtitle format. You can use this in YouTube, for example.
  + `vtt`: A modern subtitle format.
  + `txt`: Just the text transcript
* `--output_dir`: The directory to save the output files. `source` indicates the source directory, i.e. where the input `$FILE` is
* `--language`: The language of the input file. If you don’t specify it, it analyzes the first 30 seconds to auto-detect. You can speed it up by specifying it.

Run `faster-whisper-xxl --help` for more options.

[Gemini transcription](#/extracting-audio-and-transcripts?id=gemini-transcription)
----------------------------------------------------------------------------------

The [Gemini](https://gemini.google.com/) models from Google are notable in two ways:

1. They have a *huge* input context window. Gemini 2.0 Flash can accept 1M tokens, for example.
2. They can handle audio input.

This allows us to use Gemini to transcribe audio files.

LLMs are not good at transcribing audio *faithfully*. They tend to correct errors and meander from what was said. But they are intelligent. That enables a few powerful workflows. Here are some examples:

1. **Transcribe into other languages**. Gemini will handle the transcription and translation in a single step.
2. **Summarize audio transcripts**. For example, convert a podcast into a tutorial, or a meeting recording into actions.
3. **Legal Proceeding Analysis**. Extract case citations, dates, and other details from a legal debate.
4. **Medical Consultation Summary**. Extract treatments, medications, details of next visit, etc. from a medical consultation.

Here’s how to use Gemini to transcribe audio files.

1. Get a [Gemini API key](https://aistudio.google.com/app/apikey) from Google AI Studio.
2. Set the `GEMINI_API_KEY` environment variable to the API key.
3. Set the `MP3_FILE` environment variable to the path of the MP3 file you want to transcribe.
4. Run this code:

   ```
   curl -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-002:streamGenerateContent?alt=sse \
     -H "X-Goog-API-Key: $GEMINI_API_KEY" \
     -H "Content-Type: application/json" \
     -d "$(cat << EOF
   {
     "contents": [
       {
         "role": "user",
         "parts": [
           {
             "inline_data": {
               "mime_type": "audio/mp3",
               "data": "$(base64 --wrap=0 $MP3_FILE)"
             }
           },
           {"text": "Transcribe this"}
         ]
       }
     ]
   }
   EOF
   )"Copy to clipboardErrorCopied
   ```

[Previous

Transforming Images](#/transforming-images)

[Next

6. Data Analysis](#/data-analysis)

---


# File: Forecasting_with_Excel.md

---
title: "Forecasting with Excel"
original_url: "https://tds.s-anand.net/#/forecasting-with-excel?id=forecasting-with-excel"
downloaded_at: "2025-05-31T21:39:45.316079"
---

[Forecasting with Excel](#/forecasting-with-excel?id=forecasting-with-excel)
----------------------------------------------------------------------------

[![Forecasting with Excel](https://i.ytimg.com/vi_webp/QrTimmxwZw4/sddefault.webp)](https://youtu.be/QrTimmxwZw4)

Here are links used in the video:

* [FORECAST reference](https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99)
* [FORECAST.ETS reference](https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41)
* [Height-weight dataset](https://docs.google.com/spreadsheets/d/1iMFVPh8q9KgnfLwBeBMmX1GaFabP02FK/view) from [Kaggle](https://www.kaggle.com/datasets/burnoutminer/heights-and-weights-dataset)
* [Traffic dataset](https://docs.google.com/spreadsheets/d/1w2R0fHdLG5ZGW-papaK7wzWq_-WDArKC/view) from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset)

[Previous

Regression with Excel](#/regression-with-excel)

[Next

Outlier Detection with Excel](#/outlier-detection-with-excel)

---


# File: Function_Calling.md

---
title: "Function Calling"
original_url: "https://tds.s-anand.net/#/function-calling?id=how-to-define-functions"
downloaded_at: "2025-05-31T21:35:43.901109"
---

[Function Calling with OpenAI](#/function-calling?id=function-calling-with-openai)
----------------------------------------------------------------------------------

[Function Calling](https://platform.openai.com/docs/guides/function-calling) allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and AI assistants that need to interact with your backend systems.

OpenAI supports [Function Calling](https://platform.openai.com/docs/guides/function-calling) – a way for LLMs to suggest what functions to call and how.

[![OpenAI Function Calling - Full Beginner Tutorial](https://i.ytimg.com/vi_webp/aqdWSYWC_LI/sddefault.webp)](https://youtu.be/aqdWSYWC_LI)

Here’s a minimal example using Python and OpenAI’s function calling that identifies the weather in a given location.

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///

import httpx
import os
from typing import Dict, Any


def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": user_input}],
            "tools": tools,
            "tool_choice": "auto",
        },
    )
    return response.json()["choices"][0]["message"]


WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name or coordinates"}
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}

if __name__ == "__main__":
    response = query_gpt("What is the weather in San Francisco?", [WEATHER_TOOL])
    print([tool_call["function"] for tool_call in response["tool_calls"]])Copy to clipboardErrorCopied
```

### [How to define functions](#/function-calling?id=how-to-define-functions)

The function definition is a [JSON schema](https://json-schema.org/) with a few OpenAI specific properties.
See the [Supported schemas](https://platform.openai.com/docs/guides/structured-outputs#supported-schemas).

Here’s an example of a function definition for scheduling a meeting:

```
MEETING_TOOL = {
    "type": "function",
    "function": {
        "name": "schedule_meeting",
        "description": "Schedule a meeting room for a specific date and time",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Meeting date in YYYY-MM-DD format"
                },
                "time": {
                    "type": "string",
                    "description": "Meeting time in HH:MM format"
                },
                "meeting_room": {
                    "type": "string",
                    "description": "Name of the meeting room"
                }
            },
            "required": ["date", "time", "meeting_room"],
            "additionalProperties": False
        },
        "strict": True
    }
}Copy to clipboardErrorCopied
```

### [How to define multiple functions](#/function-calling?id=how-to-define-multiple-functions)

You can define multiple functions by passing a list of function definitions to the `tools` parameter.

Here’s an example of a list of function definitions for handling employee expenses and calculating performance bonuses:

```
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_expense_balance",
            "description": "Get expense balance for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    }
                },
                "required": ["employee_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_performance_bonus",
            "description": "Calculate yearly performance bonus for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    },
                    "current_year": {
                        "type": "integer",
                        "description": "Year to calculate bonus for"
                    }
                },
                "required": ["employee_id", "current_year"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]Copy to clipboardErrorCopied
```

Best Practices:

1. **Use Strict Mode**
   * Always set `strict: True` to ensure valid function calls
   * Define all required parameters
   * Set `additionalProperties: False`
2. **Use tool choice**
   * Set `tool_choice: "required"` to ensure that the model will always call one or more tools
   * The default is `tool_choice: "auto"` which means the model will choose a tool only if appropriate
3. **Clear Descriptions**
   * Write detailed function and parameter descriptions
   * Include expected formats and units
   * Mention any constraints or limitations
4. **Error Handling**
   * Validate function inputs before execution
   * Return clear error messages
   * Handle missing or invalid parameters

[Previous

Hybrid RAG with TypeSense](#/hybrid-rag-typesense)

[Next

LLM Agents](#/llm-agents)

---


# File: Geospatial_Analysis_with_Excel.md

---
title: "Geospatial Analysis with Excel"
original_url: "https://tds.s-anand.net/#/geospatial-analysis-with-excel?id=geospatial-analysis-with-excel"
downloaded_at: "2025-05-31T21:38:23.217068"
---

[Geospatial Analysis with Excel](#/geospatial-analysis-with-excel?id=geospatial-analysis-with-excel)
----------------------------------------------------------------------------------------------------

[![Geospatial analysis with Excel](https://i.ytimg.com/vi_webp/49LjxNvxyVs/sddefault.webp)](https://youtu.be/49LjxNvxyVs)

You’ll learn how to create a data-driven story about coffee shop coverage in Manhattan, covering:

* **Data Collection**: Collect and scrape data for coffee shop locations and census population from various sources.
* **Data Processing**: Use Python libraries like geopandas for merging population data with geographic maps.
* **Map Creation**: Generate coverage maps using tools like QGIS and Excel to visualize coffee shop distribution and population impact.
* **Visualization**: Create physical, Power BI, and video visualizations to present the data effectively.
* **Storytelling**: Craft a narrative around coffee shop competition, including strategic insights and potential market changes.

Here are links that explain how the video was made:

* [The Making of the Manhattan Coffee Kings](https://blog.gramener.com/the-making-of-manhattans-coffee-kings/)
* [Shaping and merging maps](https://blog.gramener.com/shaping-and-merging-maps/)
* [Visualizing data on 3D maps](https://blog.gramener.com/visualizing-data-on-3d-maps/)
* [Physical and digital 3D maps](https://blog.gramener.com/physical-and-digital-3d-maps/)

[Previous

Data Analysis with ChatGPT](#/data-analysis-with-chatgpt)

[Next

Geospatial Analysis with Python](#/geospatial-analysis-with-python)

---


# File: Geospatial_Analysis_with_Python.md

---
title: "Geospatial Analysis with Python"
original_url: "https://tds.s-anand.net/#/geospatial-analysis-with-python?id=geospatial-analysis-with-python"
downloaded_at: "2025-05-31T21:35:21.534379"
---

[Geospatial Analysis with Python](#/geospatial-analysis-with-python?id=geospatial-analysis-with-python)
-------------------------------------------------------------------------------------------------------

[![Geospatial analysis with Python](https://i.ytimg.com/vi_webp/m_qayAJt-yE/sddefault.webp)](https://youtu.be/m_qayAJt-yE)

You’ll learn how to perform geospatial analysis for location-based decision making, covering:

* **Distance Calculation**: Compute distances between various store locations and a reference point, such as the Empire State Building.
* **Data Visualization**: Visualize store locations on a map using Python libraries like Folium.
* **Store Density Analysis**: Determine the number of stores within a specified radius.
* **Proximity Analysis**: Identify the closest and farthest stores from a specific location.
* **Decision Making**: Use geospatial data to assess whether opening a new store is feasible based on existing store distribution.

Here are links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/1TwKw2pQ9XKSdTUUsTq_ulw7rb-xVhays?usp=sharing)
* Learn about the [`pandas` package](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) and [video](https://youtu.be/vmEHCJofslg)
* Learn about the [`numpy` package](https://numpy.org/doc/stable/user/whatisnumpy.html) and [video](https://youtu.be/8JfDAm9y_7s)
* Learn about the [`folium` package](https://python-visualization.github.io/folium/latest/) and [video](https://youtu.be/t9Ed5QyO7qY)
* Learn about the [`geopy` package](https://pypi.org/project/geopy/) and [video](https://youtu.be/3jj_5kVmPLs)

[Previous

Geospatial Analysis with Excel](#/geospatial-analysis-with-excel)

[Next

Geospatial Analysis with QGIS](#/geospatial-analysis-with-qgis)

---


# File: Geospatial_Analysis_with_QGIS.md

---
title: "Geospatial Analysis with QGIS"
original_url: "https://tds.s-anand.net/#/geospatial-analysis-with-qgis?id=geospatial-analysis-with-qgis"
downloaded_at: "2025-05-31T21:35:37.149524"
---

[Geospatial Analysis with QGIS](#/geospatial-analysis-with-qgis?id=geospatial-analysis-with-qgis)
-------------------------------------------------------------------------------------------------

[![Geospatial analysis with QGIS](https://i.ytimg.com/vi_webp/tJhehs0o-ik/sddefault.webp)](https://youtu.be/tJhehs0o-ik)

You’ll learn how to use QGIS for geographic data processing, covering:

* **Shapefiles and KML Files**: Create and manage shapefiles and KML files for storing and analyzing geographic information.
* **Downloading QGIS**: Install QGIS on different operating systems and familiarize yourself with its interface.
* **Geospatial Data**: Access and utilize shapefiles from sources like Diva-GIS and integrate them into QGIS projects.
* **Creating Custom Shapefiles**: Learn how to create custom shapefiles when existing ones are unavailable, including creating a shapefile for South Sudan.
* **Editing and Visualization**: Use QGIS tools to edit shapefiles, add attributes, and visualize geographic data with various styling and labeling options.
* **Exporting Data**: Export shapefiles or KML files for use in other applications, such as Google Earth.

Here are links used in the video:

* [QGIS Project](https://www.qgis.org/en/site/)
* [Shapefile Data](https://www.diva-gis.org/gdata)

[Previous

Geospatial Analysis with Python](#/geospatial-analysis-with-python)

[Next

Network Analysis in Python](#/network-analysis-in-python)

---


# File: Hybrid_RAG_with_TypeSense.md

---
title: "Hybrid RAG with TypeSense"
original_url: "https://tds.s-anand.net/#/hybrid-rag-typesense?id=embed-and-import-documents-into-typesense"
downloaded_at: "2025-05-31T21:39:51.577057"
---

[Hybrid Retrieval Augmented Generation (Hybrid RAG) with TypeSense](#/hybrid-rag-typesense?id=hybrid-retrieval-augmented-generation-hybrid-rag-with-typesense)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Hybrid RAG combines semantic (vector) search with traditional keyword search to improve retrieval accuracy and relevance. By mixing exact text matches with embedding-based similarity, you get the best of both worlds: precision when keywords are present, and semantic recall when phrasing varies. [TypeSense](https://typesense.org/) makes this easy with built-in hybrid search and automatic embedding generation.

Below is a fully self-contained Hybrid RAG tutorial using TypeSense, Python, and the command line.

### [Install and run TypeSense](#/hybrid-rag-typesense?id=install-and-run-typesense)

[Install TypeSense](https://typesense.org/docs/guide/install-typesense.html).

```
mkdir typesense-data

docker run -p 8108:8108 \
  -v typesense-data:/data typesense/typesense:28.0 \
  --data-dir /data \
  --api-key=secret-key \
  --enable-corsCopy to clipboardErrorCopied
```

* **`docker run`**: spins up a containerized TypeSense server on port 8108
  + `-p 8108:8108` maps host port to container port.
  + `-v typesense-data:/data` mounts a Docker volume for persistence.
  + `--data-dir /data` points TypeSense at that volume.
  + `--api-key=secret-key` secures your API.
  + `--enable-cors` allows browser-based requests.

**Expected output:**

* Docker logs showing TypeSense startup messages, such as `Started Typesense API server`.
* Listening on `http://0.0.0.0:8108`.

### [Embed and import documents into TypeSense](#/hybrid-rag-typesense?id=embed-and-import-documents-into-typesense)

Follow the steps in the [RAG with the CLI](#/rag-cli) tutorial to create a `chunks.json` that has one `{id, content}` JSON object per line.

[TypeSense supports automatic embedding of documents](https://typesense.org/docs/28.0/api/vector-search.html#option-b-auto-embedding-generation-within-typesense). We’ll use that capability.

Save the following as `addnotes.py` and run it with `uv run addnotes.py`.

```
# /// script
# requires-python = ">=3.13"
# dependencies = ["httpx"]
# ///
import json
import httpx
import os

headers = {"X-TYPESENSE-API-KEY": "secret-key"}

schema = {
    "name": "notes",
    "fields": [
        {"name": "id", "type": "string", "facet": False},
        {"name": "content", "type": "string", "facet": False},
        {
            "name": "embedding",
            "type": "float[]",
            "embed": {
                "from": ["content"],
                "model_config": {
                    "model_name": "openai/text-embedding-3-small",
                    "api_key": os.getenv("OPENAI_API_KEY"),
                },
            },
        },
    ],
}

with open("chunks.json", "r") as f:
    chunks = [json.loads(line) for line in f.readlines()]

with httpx.Client() as client:
    # Create the collection
    if client.get(f"http://localhost:8108/collections/notes", headers=headers).status_code == 404:
        r = client.post("http://localhost:8108/collections", json=schema, headers=headers)

    # Embed the chunks
    result = client.post(
        "http://localhost:8108/collections/notes/documents/import?action=emplace",
        headers={**headers, "Content-Type": "text/plain"},
        data="\n".join(json.dumps(chunk) for chunk in chunks),
    )
    print(result.text)Copy to clipboardErrorCopied
```

* **`httpx.Client`**: an HTTP client for Python.
* **Collection schema**: `id` and `content` fields plus an `embedding` field with auto-generated embeddings from OpenAI.
* **Auto-embedding**: the `embed` block instructs TypeSense to call the specified model for each document.
* **`GET /collections/notes`**: checks existence.
* **`POST /collections`**: creates the collection.
* **`POST /collections/notes/documents/import?action=emplace`**: bulk upsert documents, embedding them on the fly.

**Expected output:**

* A JSON summary string like `{"success": X, "failed": 0}` indicating how many docs were imported.
* (On timeouts, re-run until all chunks are processed.)

### [4. Run a hybrid search and answer a question](#/hybrid-rag-typesense?id=_4-run-a-hybrid-search-and-answer-a-question)

Now, we can use a single `curl` against the Multi-Search endpoint to combine keyword and vector search as a [hybrid search](https://typesense.org/docs/28.0/api/vector-search.html#hybrid-search):

```
Q="What does the author affectionately call the => syntax?"

payload=$(jq -n --arg coll "notes" --arg q "$Q" \
  '{
     searches: [
       {
         collection: $coll,
         q:           $q,
         query_by:    "content,embedding",
         sort_by:     "_text_match:desc",
         prefix:      false,
         exclude_fields: "embedding"
       }
     ]
   }'
)
curl -s 'http://localhost:8108/multi_search' \
  -H "X-TYPESENSE-API-KEY: secret-key" \
  -d "$payload" \
  | jq -r '.results[].hits[].document.content' \
  | llm -s "${Q} - \$Answer ONLY from these notes. Cite verbatim from the notes." \
  | uvx streamdownCopy to clipboardErrorCopied
```

* **`query_by: "content,embedding"`**: tells TypeSense to score by both keyword and vector similarity.
* **`sort_by: "_text_match:desc"`**: boosts exact text hits.
* **`exclude_fields: "embedding"`**: keeps responses lightweight.
* **`curl -d`**: posts the search request.
* **`jq -r`**: extracts each hit’s `content`. See [jq manual](https://stedolan.github.io/jq/manual/)
* **`llm -s`** and **`uvx streamdown`**: generate and stream a grounded answer.

**Expected output:**

* The raw matched snippets printed first.
* Then a concise, streamed LLM answer citing the note verbatim.

[Previous

RAG with the CLI)](#/rag-cli)

[Next

Function Calling](#/function-calling)

---


# File: Images__Compression.md

---
title: "Images: Compression"
original_url: "https://tds.s-anand.net/#/image-compression?id=images-compression"
downloaded_at: "2025-05-31T21:36:49.216023"
---

[Images: Compression](#/image-compression?id=images-compression)
----------------------------------------------------------------

Image compression is essential when deploying apps. Often, pages have dozens of images. Image analysis runs over thousands of images. The cost of storage and bandwidth can grow over time.

Here are things you should know when you’re compressing images:

* **Image dimensions** are the width and height of the image in pixels. This impacts image size a lot
* **Lossless** compression (PNG, WebP) preserves exact data
* **Lossy** compression (JPEG, WebP) removes some data for smaller files
* **Vector** formats (SVG) scale without quality loss
* **WebP** is the modern standard, supporting both lossy and lossless

Here’s a rule of thumb you can use as of 2025.

* Use SVG if you can (i.e. if it’s vector graphics or you can convert it to one)
* Else, reduce the image to as small as you can, and save as (lossy or lossless) WebP

Common operations with Python:

```
from pathlib import Path
from PIL import Image
import io

async def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Optimize for web
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

# Batch process images
paths = Path('images').glob('*.jpg')
for p in paths:
    await compress_image(p, p.with_suffix('.webp'))Copy to clipboardErrorCopied
```

Command line tools include [cwebp](https://developers.google.com/speed/webp/docs/cwebp), [pngquant](https://pngquant.org/), [jpegoptim](https://github.com/tjko/jpegoptim), and [ImageMagick](https://imagemagick.org/).

```
# Convert to WebP
cwebp -q 85 input.png -o output.webp

# Optimize PNG
pngquant --quality=65-80 image.png

# Optimize JPEG
jpegoptim --strip-all --all-progressive --max=85 image.jpg

# Convert and resize
convert input.jpg -resize 800x600 output.jpg

# Batch convert
mogrify -format webp -quality 85 *.jpgCopy to clipboardErrorCopied
```

Watch this video on modern image formats and optimization (15 min):

[![Modern Image Optimization (15 min)](https://i.ytimg.com/vi_webp/F1kYBnY6mwg/sddefault.webp)](https://youtu.be/F1kYBnY6mwg)

Tools for image optimization:

* [squoosh.app](https://squoosh.app/): Browser-based compression
* [ImageOptim](https://imageoptim.com/): GUI tool for Mac
* [sharp](https://sharp.pixelplumbing.com/): Node.js image processing
* [Pillow](https://python-pillow.org/): Python imaging library

[Previous

Markdown](#/markdown)

[Next

Static hosting: GitHub Pages](#/github-pages)

---


# File: Interactive_Notebooks__Marimo.md

---
title: "Interactive Notebooks: Marimo"
original_url: "https://tds.s-anand.net/#/marimo?id=interactive-notebooks-marimo"
downloaded_at: "2025-05-31T21:38:26.605932"
---

[Interactive Notebooks: Marimo](#/marimo?id=interactive-notebooks-marimo)
-------------------------------------------------------------------------

[Marimo](https://marimo.app/) is a new take on notebooks that solves some headaches of Jupyter. It runs cells reactively - when you change one cell, all dependent cells update automatically, just like a spreadsheet.

Marimo’s cells can’t be run out of order. This makes Marimo more reproducible and easier to debug, but requires a mental shift from the Jupyter/Colab way of working.

It also runs Python directly in the browser and is quite interactive. [Browse the gallery of examples](https://marimo.io/gallery). With a wide variety of interactive widgets, It’s growing popular as an alternative to Streamlit for building data science web apps.

Common Operations:

```
# Create new notebook
uvx marimo new

# Run notebook server
uvx marimo edit notebook.py

# Export to HTML
uvx marimo export notebook.pyCopy to clipboardErrorCopied
```

Best Practices:

1. **Cell Dependencies**

   * Keep cells focused and atomic
   * Use clear variable names
   * Document data flow between cells
2. **Interactive Elements**

   ```
   # Add interactive widgets
   slider = mo.ui.slider(1, 100)
   # Create dynamic Markdown
   mo.md(f"{slider} {"🟢" * slider.value}")Copy to clipboardErrorCopied
   ```
3. **Version Control**

   * Keep notebooks are Python files
   * Use Git to track changes
   * Publish on [marimo.app](https://marimo.app/) for collaboration

[!["marimo: an open-source reactive notebook for Python" - Akshay Agrawal (Nbpy2024)](https://i.ytimg.com/vi_webp/9R2cQygaoxQ/sddefault.webp)](https://youtu.be/9R2cQygaoxQ)

[Previous

Narratives with LLMs](#/narratives-with-llms)

[Next

HTML Slides: RevealJS](#/revealjs)

---


# File: JSON.md

---
title: "JSON"
original_url: "https://tds.s-anand.net/#/json?id=json"
downloaded_at: "2025-05-31T21:34:14.878686"
---

[JSON](#/json?id=json)
----------------------

JSON (JavaScript Object Notation) is the de facto standard format for data exchange on the web and APIs. Its human-readable format and widespread support make it essential for data scientists working with web services, APIs, and configuration files.

For data scientists, JSON is essential when:

* Working with REST APIs and web services
* Storing configuration files and metadata
* Parsing semi-structured data from databases like MongoDB
* Creating data visualization specifications (e.g., Vega-Lite)

Watch this comprehensive introduction to JSON (15 min):

[![JSON Crash Course](https://i.ytimg.com/vi_webp/GpOO5iKzOmY/sddefault.webp)](https://youtu.be/GpOO5iKzOmY)

Key concepts to understand in JSON:

* JSON only supports 6 data types: strings, numbers, booleans, null, arrays, and objects
* You can nest data. Arrays and objects can contain other data types, including other arrays and objects
* Always validate. Ensure JSON is well-formed. Comm errors: Trailing commas, missing quotes, and escape characters

[JSON Lines](https://jsonlines.org/) is a format that allows you to store multiple JSON objects in a single line.
It’s useful for logging and streaming data.

Tools you could use with JSON:

* [JSONLint](https://jsonlint.com/): Validate and format JSON
* [JSON Editor Online](https://jsoneditoronline.org/): Visual JSON editor and formatter
* [JSON Schema](https://json-schema.org/): Define the structure of your JSON data
* [jq](https://stedolan.github.io/jq/): Command-line JSON processor

Common Python operations with JSON:

```
import json

# Parse JSON string
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)

# Convert to JSON string
json_str = json.dumps(data, indent=2)

# Read JSON from file
with open('data.json') as f:
    data = json.load(f)

# Write JSON to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON data a Pandas DataFrame. JSON data is typically stored as an array of objects.
import pandas as pd
df = pd.read_json('data.json')

# Read JSON lines from file into a DataFrame. JSON lines are typically one line per object.
df = pd.read_json('data.jsonl', lines=True)Copy to clipboardErrorCopied
```

Practice JSON skills with these resources:

* [JSON Generator](https://json-generator.com/): Create sample JSON data
* [JSON Path Finder](https://jsonpathfinder.com/): Learn to navigate complex JSON structures
* [JSON Schema Validator](https://www.jsonschemavalidator.net/): Validate JSON against schemas

[Previous

CSS Selectors](#/css-selectors)

[Next

Terminal: Bash](#/bash)

---


# File: JavaScript_tools__npx.md

---
title: "JavaScript tools: npx"
original_url: "https://tds.s-anand.net/#/npx?id=javascript-tools-npx"
downloaded_at: "2025-05-31T21:35:48.393002"
---

[JavaScript tools: npx](#/npx?id=javascript-tools-npx)
------------------------------------------------------

[npx](https://docs.npmjs.com/cli/v8/commands/npx) is a command-line tool that comes with npm (Node Package Manager) and allows you to execute npm package binaries and run one-off commands without installing them globally. It’s essential for modern JavaScript development and data science workflows.

For data scientists, npx is useful when:

* Running JavaScript-based data visualization tools
* Converting notebooks and documents
* Testing and formatting code
* Running development servers

Here are common npx commands:

```
# Run a package without installing
npx http-server .                # Start a local web server
npx prettier --write .           # Format code or docs
npx eslint .                     # Lint JavaScript
npx typescript-node script.ts    # Run TypeScript directly
npx esbuild app.js               # Bundle JavaScript
npx jsdoc .                      # Generate JavaScript docs

# Run specific versions
npx prettier@3.2 --write .        # Use prettier 3.2

# Execute remote scripts (use with caution!)
npx github:user/repo            # Run from GitHubCopy to clipboardErrorCopied
```

Watch this introduction to npx (6 min):

[![What you can do with npx (6 min)](https://i.ytimg.com/vi_webp/55WaAoZV_tQ/sddefault.webp)](https://youtu.be/55WaAoZV_tQ)

[Previous

Python tools: uv](#/uv)

[Next

Unicode](#/unicode)

---


# File: LLM_Agents.md

---
title: "LLM Agents"
original_url: "https://tds.s-anand.net/#/llm-agents?id=limitations-and-challenges"
downloaded_at: "2025-05-31T21:38:36.687429"
---

[LLM Agents: Building AI Systems That Can Think and Act](#/llm-agents?id=llm-agents-building-ai-systems-that-can-think-and-act)
-------------------------------------------------------------------------------------------------------------------------------

LLM Agents are AI systems that can define and execute their own workflows to accomplish tasks. Unlike simple prompt-response patterns, agents make multiple LLM calls, use tools, and adapt their approach based on intermediate results. They represent a significant step toward more autonomous AI systems.

[![Building LLM Agents with LangChain (13 min)](https://i.ytimg.com/vi_webp/DWUdGhRrv2c/sddefault.webp)](https://youtu.be/DWUdGhRrv2c)

### [What Makes an Agent?](#/llm-agents?id=what-makes-an-agent)

An LLM agent consists of three core components:

1. **LLM Brain**: Makes decisions about what to do next
2. **Tools**: External capabilities the agent can use (e.g., web search, code execution)
3. **Memory**: Retains context across multiple steps

Agents operate through a loop:

* Observe the environment
* Think about what to do
* Take action using tools
* Observe results
* Repeat until task completion

### [Command-Line Agent Example](#/llm-agents?id=command-line-agent-example)

We’ve created a minimal command-line agent called [`llm-cmd-agent.py`](llm-cmd-agent.py) that:

1. Takes a task description from the command line
2. Generates code to accomplish the task
3. Automatically extracts and executes the code
4. Passes the results back to the LLM
5. Provides a final answer or tries again if the execution fails

Here’s how it works:

```
uv run llm-cmd-agent.py "list all Python files under the current directory, recursively, by size"
uv run llm-cmd-agent.py "convert the largest Markdown file to HTML"Copy to clipboardErrorCopied
```

The agent will:

1. Generate a shell script to list files with their sizes
2. Execute the script in a subprocess
3. Capture the output (stdout and stderr)
4. Pass the output back to the LLM for interpretation
5. Present a final answer to the user

Under the hood, the agent follows this workflow:

1. Initial prompt to generate a shell script
2. Code extraction from the LLM response
3. Code execution in a subprocess
4. Result interpretation by the LLM
5. Error handling and retry logic if needed

This demonstrates the core agent loop of:

* Planning (generating code)
* Execution (running the code)
* Reflection (interpreting results)
* Adaptation (fixing errors if needed)

### [Agent Architectures](#/llm-agents?id=agent-architectures)

Different agent architectures exist for different use cases:

1. **ReAct** (Reasoning + Acting): Interleaves reasoning steps with actions
2. **Reflexion**: Adds self-reflection to improve reasoning
3. **MRKL** (Modular Reasoning, Knowledge and Language): Combines neural and symbolic modules
4. **Plan-and-Execute**: Creates a plan first, then executes steps

### [Real-World Applications](#/llm-agents?id=real-world-applications)

LLM agents can be applied to various domains:

1. **Research assistants** that search, summarize, and synthesize information
2. **Coding assistants** that write, debug, and explain code
3. **Data analysis agents** that clean, visualize, and interpret data
4. **Customer service agents** that handle queries and perform actions
5. **Personal assistants** that manage schedules, emails, and tasks

### [Project Ideas](#/llm-agents?id=project-ideas)

Here are some practical agent projects you could build:

1. **Study buddy agent**: Helps create flashcards, generates practice questions, and explains concepts
2. **Job application assistant**: Searches job listings, tailors resumes, and prepares interview responses
3. **Personal finance agent**: Categorizes expenses, suggests budgets, and identifies savings opportunities
4. **Health and fitness coach**: Creates workout plans, tracks nutrition, and provides motivation
5. **Course project helper**: Breaks down assignments, suggests resources, and reviews work

### [Best Practices](#/llm-agents?id=best-practices)

1. **Clear instructions**: Define the agent’s capabilities and limitations
2. **Effective tool design**: Create tools that are specific and reliable
3. **Robust error handling**: Agents should recover gracefully from failures
4. **Memory management**: Balance context retention with token efficiency
5. **User feedback**: Allow users to correct or guide the agent

### [Limitations and Challenges](#/llm-agents?id=limitations-and-challenges)

Current LLM agents face several challenges:

1. **Hallucination**: Agents may generate false information or tool calls
2. **Planning limitations**: Complex tasks require better planning capabilities
3. **Tool integration complexity**: Each new tool adds implementation overhead
4. **Context window constraints**: Limited memory for long-running tasks
5. **Security concerns**: Tool access requires careful permission management

[Previous

Function Calling](#/function-calling)

[Next

LLM Image Generation](#/llm-image-generation)

---


# File: LLM_Evals.md

---
title: "LLM Evals"
original_url: "https://tds.s-anand.net/#/llm-evals?id=llm-evaluations-with-promptfoo"
downloaded_at: "2025-05-31T21:36:07.824602"
---

[LLM Evaluations with PromptFoo](#/llm-evals?id=llm-evaluations-with-promptfoo)
-------------------------------------------------------------------------------

Test-drive your prompts and models with automated, reliable evaluations.

[![🚀 Test Driven Prompt Engineering with PromptFoo (12 min)](https://i.ytimg.com/vi_webp/KhINc5XwhKs/sddefault.webp)](https://youtu.be/KhINc5XwhKs)

PromptFoo is a test-driven development framework for LLMs:

* **Developer-first**: Fast CLI with live reload & caching ([promptfoo.dev](https://promptfoo.dev))
* **Multi-provider**: Works with OpenAI, Anthropic, HuggingFace, Ollama & more ([GitHub](https://github.com/promptfoo/promptfoo))
* **Assertions**: Built‑in (`contains`, `equals`) & model‑graded (`llm-rubric`) ([docs](https://www.promptfoo.dev/docs/configuration/expected-outputs/))
* **CI/CD**: Integrate evals into pipelines for regression safety ([CI/CD guide](https://www.promptfoo.dev/docs/integrations/ci-cd/))

To run PromptFoo:

1. Install Node.js & npm ([nodejs.org](https://nodejs.org/))
2. Set up your [`OPENAI_API_KEY`](https://platform.openai.com/api-keys) environment variable
3. Configure `promptfooconfig.yaml`. Below is an example:

```
prompts:
  - |
    Summarize this text: "{{text}}"
  - |
    Please write a concise summary of: "{{text}}"

providers:
  - openai:gpt-3.5-turbo
  - openai:gpt-4

tests:
  - name: summary_test
    vars:
      text: "PromptFoo is an open-source CLI and library for evaluating and testing LLMs with assertions, caching, and matrices."
    assertions:
      - contains-all:
          values:
            - "open-source"
            - "LLMs"
      - llm-rubric:
          instruction: |
            Score the summary from 1 to 5 for:
            - relevance: captures the main info?
            - clarity: wording is clear and concise?
          schema:
            type: object
            properties:
              relevance:
                type: number
                minimum: 1
                maximum: 5
              clarity:
                type: number
                minimum: 1
                maximum: 5
            required: [relevance, clarity]
            additionalProperties: false

commandLineOptions:
  cache: trueCopy to clipboardErrorCopied
```

Now, you can run the evaluations and see the results.

```
# Execute all tests
npx -y promptfoo eval -c promptfooconfig.yaml

# List past evaluations
npx -y promptfoo list evals

# Launch interactive results viewer on port 8080
npx -y promptfoo view -p 8080Copy to clipboardErrorCopied
```

PromptFoo caches API responses by default (TTL 14 days). You can disable it with `--no-cache` or clear it.

```
# Disable cache for this run
echo y | promptfoo eval --no-cache -c promptfooconfig.yaml

# Clear all cache
echo y | promptfoo cache clearCopy to clipboardErrorCopied
```

[Previous

LLM Speech](#/llm-speech)

[Next

Project 1](#/project-tds-virtual-ta)

---


# File: LLM_Image_Generation.md

---
title: "LLM Image Generation"
original_url: "https://tds.s-anand.net/#/images/project-tds-virtual-ta-q1.webp"
downloaded_at: "2025-05-31T21:38:57.511603"
---

404 - Not found
===============

---


# File: LLM_Sentiment_Analysis.md

---
title: "LLM Sentiment Analysis"
original_url: "https://tds.s-anand.net/#/llm-sentiment-analysis?id=llm-sentiment-analysis"
downloaded_at: "2025-05-31T21:39:27.409721"
---

[LLM Sentiment Analysis](#/llm-sentiment-analysis?id=llm-sentiment-analysis)
----------------------------------------------------------------------------

[OpenAI’s API](https://platform.openai.com/) provides access to language models like GPT 4o, GPT 4o mini, etc.

For more details, read OpenAI’s guide for:

* [Text Generation](https://platform.openai.com/docs/guides/text-generation)
* [Vision](https://platform.openai.com/docs/guides/vision)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Start with this quick tutorial:

[![OpenAI API Quickstart: Send your First API Request](https://i.ytimg.com/vi_webp/Xz4ORA0cOwQ/sddefault.webp)](https://youtu.be/Xz4ORA0cOwQ)

Here’s a minimal example using `curl` to generate text:

```
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{ "role": "user", "content": "Write a haiku about programming." }]
  }'Copy to clipboardErrorCopied
```

Let’s break down the request:

* `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
* `-H "Content-Type: application/json"`: The content type of the request.
* `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
* `-d`: The request body.
  + `"model": "gpt-4o-mini"`: The model to use for text generation.
  + `"messages":`: The messages to send to the model.
    - `"role": "user"`: The role of the message.
    - `"content": "Write a haiku about programming."`: The content of the message.

[![LLM Sentiment Analysis](https://i.ytimg.com/vi_webp/_D46QrX-2iU/sddefault.webp)](https://youtu.be/_D46QrX-2iU)

This video explains how to use large language models (LLMs) for sentiment analysis and classification, covering:

* **Sentiment Analysis**: Use OpenAI API to identify the sentiment of movie reviews as positive or negative.
* **Prompt Engineering**: Learn how to craft effective prompts to get desired results from LLMs.
* **LLM Training**: Understand how to train LLMs by providing examples and feedback.
* **OpenAI API Integration**: Integrate OpenAI API into Python code to perform sentiment analysis.
* **Tokenization**: Learn about tokenization and its impact on LLM input and cost.
* **Zero-Shot, One-Shot, and Multi-Shot Learning**: Understand different approaches to using LLMs for learning.

Here are the links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs)
* [Movie reviews dataset](https://drive.google.com/file/d/1X33ao8_PE17c3htkQ-1p2dmW2xKmOq8Q/view)
* [OpenAI Playground](https://platform.openai.com/playground/chat)
* [OpenAI Pricing](https://openai.com/api/pricing/)
* [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
* [OpenAI API Reference](https://platform.openai.com/docs/api-reference/)
* [OpenAI Docs](https://platform.openai.com/docs/overview)

[Previous

TDS GPT Reviewer](#/tds-gpt-reviewer)

[Next

LLM Text Extraction](#/llm-text-extraction)

---


# File: LLM_Speech.md

---
title: "LLM Speech"
original_url: "https://tds.s-anand.net/#/llm-speech?id=openai-tts-1-for-text-to-speech-generation"
downloaded_at: "2025-05-31T21:39:44.271954"
---

[OpenAI TTS-1 for Text-to-Speech Generation](#/llm-speech?id=openai-tts-1-for-text-to-speech-generation)
--------------------------------------------------------------------------------------------------------

OpenAI’s Text-to-Speech API (TTS-1) converts text into natural-sounding speech using state-of-the-art neural models. Released in March 2025, it offers multiple voices and control over speaking style and speed.

[![Audio Models in the API (15 min)](https://i.ytimg.com/vi_webp/lXb0L16ISAc/sddefault.webp)](https://youtu.be/lXb0L16ISAc)

### [Simple speech generation](#/llm-speech?id=simple-speech-generation)

To generate speech from text, send a POST request to the speech endpoint:

```
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "Hello! This is a test of the OpenAI text to speech API.",
    "voice": "alloy"
  }' --output speech.mp3Copy to clipboardErrorCopied
```

### [Generation options](#/llm-speech?id=generation-options)

Control the output with these parameters:

* `model`: `tts-1` (standard) or `tts-1-hd` (higher quality)
* `input`: Text to convert (max 4096 characters)
* `voice`: `alloy`, `echo`, `fable`, `onyx`, `nova`, or `shimmer`
* `response_format`: `mp3` (default), `opus`, `aac`, or `flac`
* `speed`: 0.25 to 4.0 (default 1.0)

```
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-hd",
    "input": "Welcome to our podcast! Today we will be discussing artificial intelligence.",
    "voice": "nova",
    "response_format": "mp3",
    "speed": 1.2
  }' --output podcast_intro.mp3Copy to clipboardErrorCopied
```

### [Costs and optimization](#/llm-speech?id=costs-and-optimization)

Pricing per 1,000 characters:

* `tts-1`: $0.015
* `tts-1-hd`: $0.030

To optimize costs:

* Use `tts-1` for drafts, `tts-1-hd` for final versions
* Batch process text in chunks
* Cache frequently used phrases
* Choose lower quality formats for testing

[Google Gemini Speech Studio for Text-to-Speech](#/llm-speech?id=google-gemini-speech-studio-for-text-to-speech)
----------------------------------------------------------------------------------------------------------------

Google’s Gemini Speech Studio offers advanced text-to-speech capabilities with support for multiple languages, voices, and speaking styles.

[![Getting Started with Gemini Speech Studio (7 min)](https://i.ytimg.com/vi_webp/Rx8PmBo9vfI/sddefault.webp)](https://youtu.be/Rx8PmBo9vfI)

For this, you need a `GOOGLE_API_KEY`. You can:

1. Go to the Google Cloud Console: <https://console.cloud.google.com/apis/library/texttospeech.googleapis.com>, select or create the project you want and click **Enable**.
2. **Create an API key**. In the Console, navigate to **APIs & Services → Credentials** and click **+ Create Credentials → API key**. Copy the generated key (it’ll look like `AIza…`).

### [Simple speech generation](#/llm-speech?id=simple-speech-generation-1)

Generate speech using the Gemini API:

```
curl -X POST "https://texttospeech.googleapis.com/v1/text:synthesize?key=$GOOGLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": { "text": "Hello, welcome to Gemini Speech Studio!" },
    "voice": { "languageCode": "en-US", "name": "en-US-Neural2-A" },
    "audioConfig": { "audioEncoding": "MP3" }
  }' | jq -r .audioContent | base64 --decode > gemini-speech.mp3Copy to clipboardErrorCopied
```

### [Generation options](#/llm-speech?id=generation-options-1)

Customize synthesis with these parameters:

* `voice`:
  + `languageCode`: Language code (e.g., “en-US”, “es-ES”)
  + `name`: Voice model name
  + `ssmlGender`: “NEUTRAL”, “MALE”, or “FEMALE”
* `audioConfig`:
  + `audioEncoding`: “MP3”, “WAV”, “OGG\_OPUS”
  + `speakingRate`: 0.25 to 4.0
  + `pitch`: -20.0 to 20.0
  + `volumeGainDb`: Volume adjustment

```
curl -X POST "https://texttospeech.googleapis.com/v1/text:synthesize?key=$GOOGLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "text": "This is a demonstration of advanced speech settings."
    },
    "voice": {
      "languageCode": "en-US",
      "name": "en-US-Neural2-D"
    },
    "audioConfig": {
      "audioEncoding": "MP3",
      "speakingRate": 1.2,
      "pitch": 2.0,
      "volumeGainDb": 1.0
    }
  }' | jq -r .audioContent | base64 --decode > gemini-options.mp3Copy to clipboardErrorCopied
```

### [SSML support](#/llm-speech?id=ssml-support)

Both APIs support Speech Synthesis Markup Language (SSML) for fine-grained control:

```
curl -X POST "https://texttospeech.googleapis.com/v1/text:synthesize?key=$GOOGLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "ssml": "<speak>Hello <break time=\"1s\"/> This text has a pause and <emphasis level=\"strong\">emphasized words</emphasis>.</speak>"
    },
    "voice": { "languageCode": "en-US", "name": "en-US-Neural2-A" },
    "audioConfig": { "audioEncoding": "MP3" }
  }' | jq -r .audioContent | base64 --decode > gemini-ssml.mp3Copy to clipboardErrorCopied
```

### [Costs and optimization](#/llm-speech?id=costs-and-optimization-1)

Pricing (per character):

* Standard voices: $0.000004
* Neural voices: $0.000016
* Neural2 voices: $0.000024

To optimize:

* Use standard voices for development
* Cache common phrases
* Batch process where possible
* Choose appropriate audio quality

### [Python implementation](#/llm-speech?id=python-implementation)

Here’s a simple Python wrapper for both APIs:

```
import requests
import base64
import os

openai_key = os.getenv("OPENAI_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

def generate_openai_speech(text, voice="alloy", model="tts-1"):
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={"Authorization": f"Bearer {openai_key}"},
        json={"model": model, "input": text, "voice": voice}
    )
    return response.content

def generate_gemini_speech(text, voice_name="en-US-Neural2-A"):
    response = requests.post(
        f"https://texttospeech.googleapis.com/v1/text:synthesize?key={google_key}",
        json={
            "input": {"text": text},
            "voice": {"languageCode": "en-US", "name": voice_name},
            "audioConfig": {"audioEncoding": "MP3"}
        }
    )
    return base64.b64decode(response.json()["audioContent"])

if __name__ == "__main__":
    with open("openai_speech.mp3", "wb") as f:
        f.write(generate_openai_speech("Hello from OpenAI's text to speech API!"))
    with open("gemini_speech.mp3", "wb") as f:
        f.write(generate_gemini_speech("Hello from Google's Gemini Speech Studio!"))Copy to clipboardErrorCopied
```

[Previous

LLM Image Generation](#/llm-image-generation)

[Next

LLM Evals](#/llm-evals)

---


# File: LLM_Text_Extraction.md

---
title: "LLM Text Extraction"
original_url: "https://tds.s-anand.net/#/llm-text-extraction?id=llm-text-extraction"
downloaded_at: "2025-05-31T21:38:11.626048"
---

[LLM Text Extraction](#/llm-text-extraction?id=llm-text-extraction)
-------------------------------------------------------------------

[JSON](#/json) is one of the most widely used formats in the world for applications to exchange data.

[![LLM Extraction](https://i.ytimg.com/vi_webp/72514uGffPE/sddefault.webp)](https://youtu.be/72514uGffPE)

This video explains how to use LLMs to extract structure from unstructured data, covering:

* **LLM for Data Extraction**: Use OpenAI’s API to extract structured information from unstructured data like addresses.
* **JSON Schema**: Define a JSON schema to ensure consistent and structured output from the LLM.
* **Prompt Engineering**: Craft effective prompts to guide the LLM’s response and improve accuracy.
* **Data Cleaning**: Use string functions and OpenAI’s API to clean and standardize data.
* **Data Analysis**: Analyze extracted data using Pandas to gain insights.
* **LLM Limitations**: Understand the limitations of LLMs, including potential errors and inconsistencies in output.
* **Production Use Cases**: Explore real-world applications of LLMs for data extraction, such as customer service email analysis.

Here are the links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/1Z8mG-RPTSYY4qwkoNdzRTc4StbnwOXeE)
* [JSON Schema](https://json-schema.org/)
* [Function calling](https://platform.openai.com/docs/guides/function-calling)

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied
[JSON Schema](https://json-schema.org/overview/what-is-jsonschema), so you don’t need to worry about the model omitting a required key,
or hallucinating an invalid enum value.

```
curl https://api.openai.com/v1/chat/completions \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "gpt-4o-2024-08-06",
  "messages": [
    { "role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step." },
    { "role": "user", "content": "how can I solve 8x + 7 = -23" }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "math_response",
      "strict": true
      "schema": {
        "type": "object",
        "properties": {
          "steps": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": { "explanation": { "type": "string" }, "output": { "type": "string" } },
              "required": ["explanation", "output"],
              "additionalProperties": false
            }
          },
          "final_answer": { "type": "string" }
        },
        "required": ["steps", "final_answer"],
        "additionalProperties": false
      }
    }
  }
}'Copy to clipboardErrorCopied
```

Here’s what the `response_format` tells OpenAI. The items marked ⚠️ are OpenAI specific requirements for the JSON schema.

* `"type": "json_schema"`: We want you to generate a JSON response that follows this schema.
* `"json_schema":`: We’re going to give you a schema.
  + `"name": "math_response"`: The schema is called `math_response`. (We can call it anything.)
  + `"strict": true`: Follow the schema exactly.
  + `"schema":`: Now, here’s the actual JSON schema.
    - `"type": "object"`: Return an object. ⚠️ The root object **must** be an object.
    - `"properties":`: The object has these properties:
      * `"steps":`: There’s a `steps` property.
        + `"type": "array"`: It’s an array.
        + `"items":`: Each item in the array…
          - `"type": "object"`: … is an object.
          - `"properties":`: The object has these properties:
            * `"explanation":`: There’s an `explanation` property.
              + `"type": "string"`: … which is a string.
            * `"output":`: There’s an `output` property.
              + `"type": "string"`: … which is a string, too.
          - `"required": ["explanation", "output"]`: ⚠️ You **must** add `"required": [...]` and include **all** fields int he object.
          - `"additionalProperties": false`: ⚠️ OpenAI requires every object to have `"additionalProperties": false`.
      * `"final_answer":`: There’s a `final_answer` property.
        + `"type": "string"`: … which is a string.
    - `"required": ["steps", "final_answer"]`: ⚠️ You **must** add `"required": [...]` and include **all** fields in the object.
    - `"additionalProperties": false`: ⚠️ OpenAI requires every object to have `"additionalProperties": false`.

[Previous

LLM Sentiment Analysis](#/llm-sentiment-analysis)

[Next

Base 64 Encoding](#/base64-encoding)

---


# File: LLM_Video_Screen-Scraping.md

---
title: "LLM Video Screen-Scraping"
original_url: "https://tds.s-anand.net/#/llm-video-screen-scraping?id=quick-start-example"
downloaded_at: "2025-05-31T21:38:27.727501"
---

[LLM Video Screen-Scraping](#/llm-video-screen-scraping?id=llm-video-screen-scraping)
-------------------------------------------------------------------------------------

Video screen-scraping with LLMs is a powerful technique for extracting structured data from screen recordings. This approach works with any visible screen content and bypasses traditional web scraping limitations like authentication or anti-scraping measures.

[![Screen Scraping with Gemini](https://i.ytimg.com/vi_webp/2G1LqS6qO5s/sddefault.webp)](https://youtu.be/2G1LqS6qO5s)

Key benefits:

* No setup cost or authentication handling
* Works with any visible screen content
* Full control over data exposure
* Extremely cost-effective (< $0.001 per short video)
* Bypasses anti-scraping measures
* Handles varying formats and layouts

### [Quick Start Example](#/llm-video-screen-scraping?id=quick-start-example)

Here’s a basic workflow using Google’s AI Studio and Gemini:

1. **Record the Screen**
   * Use QuickTime (Mac) or Windows Game Bar (Windows), Screen2Gif, or any tool of your choice
   * Select specific screen area containing target data
   * Record scrolling/clicking through content
   * Keep recordings short (30-60 seconds)
2. **Process with Gemini**
   * Upload to [Google AI Studio](https://makersuite.google.com/app/prompts)
   * Select Gemini 1.5 Flash (cost-effective)
   * Prompt for structured output (JSON/CSV)

Example prompt for extracting tabular data:

```
Turn this video into a JSON array where each item has:
{
  "date": "yyyy-mm-dd",
  "amount": float
}Copy to clipboardErrorCopied
```

### [Cost Calculation](#/llm-video-screen-scraping?id=cost-calculation)

Gemini 1.5 Flash pricing (as of January 2025):

* $0.075 per million tokens
* Cost per frame ~ 250 tokens
* Cost for 24 hours of video at 1 frame per second ~ $1.62!

### [Best Practices](#/llm-video-screen-scraping?id=best-practices)

1. **Recording Quality**
   * Frame only relevant content
   * Pause briefly on important data
   * Maintain consistent scroll speed
   * Use high contrast display settings
2. **Data Validation**
   * Always verify critical data manually
   * Use spot-checking for large datasets
   * Consider running multiple passes
   * Log and review any anomalies
3. **Error Handling**
   * Request data in simple formats (CSV/JSON)
   * Include validation in prompts
   * Split long videos into segments
   * Handle missing/partial data gracefully

### [Use Cases](#/llm-video-screen-scraping?id=use-cases)

1. **Data Extraction**
   * Email content aggregation
   * Dashboard metrics collection
   * Protected web content
   * Legacy system data
2. **Data Journalism**
   * Public records analysis
   * Time-series data collection
   * Interactive visualization data
   * Government website scraping
3. **Business Intelligence**
   * Competitor pricing analysis
   * Market research data
   * Internal system migration
   * Legacy report conversion

Tools:

* [Google AI Studio](https://aistudio.google.com/app/prompts): Process videos with Gemini
* [QuickTime Player](https://support.apple.com/guide/quicktime-player/welcome/mac): Screen recording (Mac)
* [Screen2Gif](https://www.screentogif.com/): Screen recording (Windows)
* [OBS Studio](https://obsproject.com/): Advanced screen recording (cross-platform)

References:

* [Simon Willison’s Video Scraping Tutorial](https://simonwillison.net/2024/Oct/17/video-scraping/)
* [Gemini API Documentation](https://ai.google.dev/docs)

[Previous

LLM Website Scraping](#/llm-website-scraping)

[Next

Web Automation with Playwright](#/web-automation-with-playwright)

---


# File: LLM_Website_Scraping.md

---
title: "LLM Website Scraping"
original_url: "https://tds.s-anand.net/#/llm-website-scraping?id=llm-website-scraping"
downloaded_at: "2025-05-31T21:35:13.830042"
---

[LLM Website Scraping](#/llm-website-scraping?id=llm-website-scraping)
----------------------------------------------------------------------

[Previous

Convert HTML to Markdown](#/convert-html-to-markdown)

[Next

LLM Video Screen-Scraping](#/llm-video-screen-scraping)

---


# File: Local_LLMs__Ollama.md

---
title: "Local LLMs: Ollama"
original_url: "https://tds.s-anand.net/#/ollama?id=key-features"
downloaded_at: "2025-05-31T21:37:42.909111"
---

[Local LLM Runner: Ollama](#/ollama?id=local-llm-runner-ollama)
---------------------------------------------------------------

[`ollama`](https://github.com/ollama/ollama) is a command-line tool for running open-source large language models entirely on your own machine—no API keys, no vendor lock-in, full control over models and performance.

[![Run AI Models Locally: Ollama Tutorial (Step-by-Step Guide + WebUI)](https://i.ytimg.com/vi_webp/Lb5D892-2HY/sddefault.webp)](https://youtu.be/Lb5D892-2HY)

### [Basic Usage](#/ollama?id=basic-usage)

[Download Ollama for macOS, Linux, or Windows](https://ollama.com/) and add the binary to your `PATH`. See the full [Docs ↗](https://ollama.com/docs) for installation details and troubleshooting.

```
# List installed and available models
ollama list

# Download/pin a specific model version
ollama pull gemma3:1b-it-qat

# Run a one-off prompt
ollama run gemma3:1b-it-qat 'Write a haiku about data visualization'

# Launch a persistent HTTP API on port 11434
ollama serve

# Interact programmatically over HTTP
curl -X POST http://localhost:11434/api/chat \
     -H 'Content-Type: application/json' \
     -d '{"model":"gemma3:1b-it-qat","prompt":"Hello, world!"}'Copy to clipboardErrorCopied
```

### [Key Features](#/ollama?id=key-features)

* **Model management**: `list`/`pull` — Install and switch among Llama 3.3, DeepSeek-R1, Gemma 3, Mistral, Phi-4, and more.
* **Local inference**: `run` — Execute prompts entirely on-device for privacy and zero latency beyond hardware limits.
* **Persistent server**: `serve` — Expose a local REST API for multi-session chats and integration into scripts or apps.
* **Version pinning**: `pull model:tag` — Pin exact model versions for reproducible demos and experiments.
* **Resource control**: `--threads` / `--context` — Tune CPU/GPU usage and maximum context window for performance and memory management.

### [Real-World Use Cases](#/ollama?id=real-world-use-cases)

* **Quick prototyping**. Brainstorm slide decks or blog outlines offline, without worrying about API quotas: `ollama run gemma-3 'Outline a slide deck on Agile best practices'`
* **Data privacy**. Summarize sensitive documents on-device, retaining full control of your data: `cat financial_report.pdf | ollama run phi-4 'Summarize the key findings'`
* **CI/CD integration**. Validate PR descriptions or test YAML configurations in your pipeline without incurring API costs: `git diff origin/main | ollama run llama2 'Check for style and clarity issues'`
* **Local app embedding**. Power a desktop or web app via the local REST API for instant LLM features: `curl -X POST http://localhost:11434/api/chat -d '{"model":"mistral","prompt":"Translate to German"}'`

Read the full [Ollama docs ↗](https://github.com/ollama/ollama/tree/main/docs) for advanced topics like custom model hosting, GPU tuning, and integrating with your development workflows.

[Previous

Authentication: Google Auth](#/google-auth)

[Next

3. Large Language Models](#/large-language-models)

---


# File: Markdown.md

---
title: "Markdown"
original_url: "https://tds.s-anand.net/#/markdown?id=documentation-markdown"
downloaded_at: "2025-05-31T21:38:29.970979"
---

[Documentation: Markdown](#/markdown?id=documentation-markdown)
---------------------------------------------------------------

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It’s the standard for documentation in software projects and data science notebooks.

Watch this introduction to Markdown (19 min):

[![Markdown Crash Course (19 min)](https://i.ytimg.com/vi_webp/HUBNt18RFbo/sddefault.webp)](https://youtu.be/HUBNt18RFbo)

Common Markdown syntax:

```
# Heading 1
## Heading 2

**bold** and *italic*

- Bullet point
- Another point
  - Nested point

1. Numbered list
2. Second item

[Link text](https://url.com)
![Image alt](image.jpg)

```python
# Code block
def hello():
    print("Hello")
```

> BlockquoteCopy to clipboardErrorCopied
```

There is also a [GitHub Flavored Markdown](https://github.github.com/gfm/) standard which is popular. This includes extensions like:

```
- [ ] Incomplete task
- [x] Completed task

~~Strikethrough~~

Tables:

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |
Copy to clipboardErrorCopied
```

Tools for working with Markdown:

* [markdown2](https://pypi.org/project/markdown2/): Python library to convert Markdown to HTML
* [markdownlint](https://github.com/DavidAnson/markdownlint): Linting
* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): VS Code extension
* [pandoc](https://pandoc.org/): Convert between formats

[Previous

2. Deployment Tools](#/deployment-tools)

[Next

Images: Compression](#/image-compression)

---


# File: Multimodal_Embeddings.md

---
title: "Multimodal Embeddings"
original_url: "https://tds.s-anand.net/#/multimodal-embeddings?id=_2-jina-ai"
downloaded_at: "2025-05-31T21:38:19.737742"
---

[Multimodal Embeddings](#/multimodal-embeddings?id=multimodal-embeddings)
-------------------------------------------------------------------------

Multimodal embeddings map **text** and **images** into the **same** vector space, enabling direct comparison between, say, a caption — “A cute cat” — and an image of that cat. This unified representation powers real-world applications like:

* **Cross-modal search** (e.g. “find images of a sunset” via text queries)
* **Content recommendation** (suggesting visually similar products to text descriptions)
* **Clustering & retrieval** (grouping documents and their associated graphics)
* **Anomaly detection** (spotting unusual image–text pairings)

By reducing different data types to a common numeric form, you unlock richer search, enhanced recommendations, and tighter integration of visual and textual data.

[Get API keys](#/multimodal-embeddings?id=get-api-keys)
-------------------------------------------------------

Below are the steps to grab a free API key for each provider.

### [Nomic Atlas](#/multimodal-embeddings?id=nomic-atlas)

1. **Sign up** at the Nomic Atlas homepage:
   👉 <https://atlas.nomic.ai/> ([Atlas | Nomic Atlas Documentation](https://docs.nomic.ai/atlas/quick-start "Quickstart | Nomic Atlas Documentation"))
2. Once logged in, open the **Dashboard** and navigate to **Settings → API Keys**.
3. Click **Create API Key**, name it, and copy the generated key.

Set in your shell:

```
export NOMIC_API_KEY="your-nomic-api-key"Copy to clipboardErrorCopied
```

### [Jina AI](#/multimodal-embeddings?id=jina-ai)

1. **Visit** the Jina AI Embeddings page:
   👉 <https://jina.ai/embeddings/> ([Jina AI](https://jina.ai/embeddings/ "Embedding API - Jina AI"))
2. Click **Get Started** (no credit card needed) and register for a free account. Every new key comes with **1 million free tokens**.
3. In the dashboard, go to **API Key & Billing** and copy your key.

Set in your shell:

```
export JINA_API_KEY="your-jina-api-key"Copy to clipboardErrorCopied
```

### [Google Vertex AI](#/multimodal-embeddings?id=google-vertex-ai)

1. **Sign up** for Google Cloud’s free tier (90 days, $300 credit):
   👉 <https://cloud.google.com/free> ([Google Cloud](https://cloud.google.com/free "Free Trial and Free Tier Services and Products - Google Cloud"))
2. In the Cloud Console, open **APIs & Services → Credentials**:
   👉 <https://console.cloud.google.com/apis/credentials> ([Google Cloud](https://cloud.google.com/docs/authentication/api-keys "Manage API keys | Authentication - Google Cloud"))
3. Click **Create credentials → API key**, then copy the key.

Set in your shell:

```
export GOOGLE_API_KEY="your-google-api-key"
export PROJECT_ID="your-gcp-project-id"Copy to clipboardErrorCopied
```

[Example Requests](#/multimodal-embeddings?id=example-requests)
---------------------------------------------------------------

Below are fully-workable snippets that:

* **Embed two texts** (“A cute cat”, “A cardboard box”)
* **Embed two images** (`cat.jpg`, `box.png`)
* **Send** them to the respective API

Replace variables (`$NOMIC_API_KEY`, `$JINA_API_KEY`, `$GOOGLE_API_KEY`, `$PROJECT_ID`) before running.

### [1. Nomic Atlas](#/multimodal-embeddings?id=_1-nomic-atlas)

Text Embeddings

```
curl -X POST "https://api-atlas.nomic.ai/v1/embedding/text" \
  -H "Authorization: Bearer $NOMIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "nomic-embed-text-v1.5",
        "task_type": "search_document",
        "texts": ["A cute cat", "A cardboard box"]
      }'Copy to clipboardErrorCopied
```

Image Embeddings

```
curl -X POST "https://api-atlas.nomic.ai/v1/embedding/image" \
  -H "Authorization: Bearer $NOMIC_API_KEY" \
  -F "model=nomic-embed-vision-v1.5" \
  -F "images=@cat.jpg" \
  -F "images=@box.png"Copy to clipboardErrorCopied
```

### [2. Jina AI](#/multimodal-embeddings?id=_2-jina-ai)

Jina’s unified `/v1/embeddings` endpoint accepts text strings **and** base64-encoded image bytes in one batch. ([Jina AI](https://jina.ai/embeddings/ "Embedding API - Jina AI"))

```
curl -X POST "https://api.jina.ai/v1/embeddings" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
        \"model\": \"jina-clip-v2\",
        \"input\": [
          {\"text\":\"A cute cat\"},
          {\"text\":\"A cardboard box\"},,
          {\"image\":\"$(base64 -w 0 cat.jpg)\"},
          {\"image\":\"$(base64 -w 0 box.png)\"}
        ]
      }"Copy to clipboardErrorCopied
```

### [3. Google Vertex AI Multimodal Embeddings](#/multimodal-embeddings?id=_3-google-vertex-ai-multimodal-embeddings)

Vertex AI’s multimodal model (`multimodalembedding@001`) takes JSON instances combining text and **base64** image data. ([Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-embeddings-api "Multimodal embeddings API | Generative AI on Vertex AI"))

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://us-central1-aiplatform.googleapis.com/v1/projects/$PROJECT_ID/locations/us-central1/publishers/google/models/multimodalembedding@001:predict?key=$GOOGLE_API_KEY" \
  -d "{
        \"instances\": [
          {
            \"text\": \"A cute cat\",
            \"image\": {\"bytesBase64Encoded\": \"$(base64 -w 0 cat.jpg)\"}
          },
          {
            \"text\": \"A cardboard box\",
            \"image\": {\"bytesBase64Encoded\": \"$(base64 -w 0 box.png)\"}
          }
        ]
      }"Copy to clipboardErrorCopied
```

With these steps, you’re all set to explore and experiment with multimodal embeddings across text + image data—unifying your applications’ visual and linguistic understanding.

[Previous

Embeddings](#/embeddings)

[Next

Topic modeling](#/topic-modeling)

---


# File: Narratives_with_LLMs.md

---
title: "Narratives with LLMs"
original_url: "https://tds.s-anand.net/#/narratives-with-llms?id=narratives-with-llms"
downloaded_at: "2025-05-31T21:39:08.273815"
---

[Narratives with LLMs](#/narratives-with-llms?id=narratives-with-llms)
----------------------------------------------------------------------

#TODO

[Previous

Data Storytelling](#/data-storytelling)

[Next

Interactive Notebooks: Marimo](#/marimo)

---


# File: Network_Analysis_in_Python.md

---
title: "Network Analysis in Python"
original_url: "https://tds.s-anand.net/#/network-analysis-in-python?id=network-analysis-in-python"
downloaded_at: "2025-05-31T21:33:44.111059"
---

[Network Analysis in Python](#/network-analysis-in-python?id=network-analysis-in-python)
----------------------------------------------------------------------------------------

[![Talk: Exploring the Movie Actor Network in Python](https://i.ytimg.com/vi_webp/uPL3VuRqOy4/sddefault.webp)](https://youtu.be/uPL3VuRqOy4)

You’ll learn how to use network analysis to identify clusters and connections between nodes in a dataset, covering:

* **Network Construction**: Build a network from the IMDB database, where nodes represent actors and edges represent shared movie appearances.
* **Clustering**: Apply clustering techniques to detect communities within the network, using scikit-learn’s network library.
* **Matrix Operations**: Utilize matrix operations to efficiently analyze actor relationships and interactions.
* **Community Detection**: Implement algorithms to identify and interpret clusters, examining how different actor clusters are connected.
* **Application of Findings**: Explore practical applications of network analysis, such as social network analysis and its potential uses in various domains.

Here are links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/1VRlAOfREGwflv7v2VmN-6O_wqRno4Xcq?usp=sharing)
* [Exploring the Movie Actor Network in Python](https://youtu.be/6hzLw80qxto)
* [Jupyter Notebook - Shortest Path](https://colab.research.google.com/drive/1-b0pA1O6rCS-ZwU_MWdCzx0CEI_WnyZ2)
* [Jupyter Notebook - Actor network](https://colab.research.google.com/drive/1Lps2fkRlyPAnR63hDOihzCaMvo_RU6Ds)
* [IMDb Datasets](https://developer.imdb.com/non-commercial-datasets/)
* Learn about the [`sknetwork` package](https://scikit-network.readthedocs.io/en/latest/use_cases/votes.html)
* Learn about the [scipy.sparse matrices](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/) and [video](https://youtu.be/v_S7cOL5ZWU)
* [Introduction to Kumu](https://youtu.be/fwiz7PnipgQ)
* [Network analysis with Kumu](https://docs.kumu.io/guides/disciplines/sna-network-mapping)
* [Introduction to Systems and Network Mapping with Kumu](https://www.coursera.org/projects/systems-network-kumu)

[Previous

Geospatial Analysis with QGIS](#/geospatial-analysis-with-qgis)

[Next

7. Data Visualization](#/data-visualization)

---


# File: Nominatim_API_with_Python.md

---
title: "Nominatim API with Python"
original_url: "https://tds.s-anand.net/#/nominatim-api-with-python?id=nominatim-api-with-python"
downloaded_at: "2025-05-31T21:39:06.130113"
---

[Nominatim API with Python](#/nominatim-api-with-python?id=nominatim-api-with-python)
-------------------------------------------------------------------------------------

[![Nominatim Open Street Map with Python](https://i.ytimg.com/vi_webp/f0PZ-pphAXE/sddefault.webp)](https://youtu.be/f0PZ-pphAXE)

You’ll learn how to get the latitude and longitude of any city from the Nominatim API.

* **Introduction to Nominatim**: Understand how Nominatim, from OpenStreetMap, works similarly to Google Maps for geocoding.
* **Installation and Import**: Learn to install and import [geopy](https://geopy.readthedocs.io/) and [nominatim](https://nominatim.org/).
* **Using the Locator**: Create a locator object using Nominatim and set up a user agent.
* **Geocoding an Address**: Use `locator.geocode` to input an address (e.g., Eiffel Tower) and fetch geocoded data.
* **Extracting Data**: Access detailed information like latitude, longitude, bounding box, and accurate address from the JSON response.
* **Classifying Locations**: Identify the type of place (e.g., tourism, university) using the response data.
* **Practical Example**: Geocode “IIT Madras” and retrieve its full address, type (university), and other relevant information.

Here are links and references:

* [Geocoding using Nominatim - Notebook](https://colab.research.google.com/drive/1-vvP-UyMjHgBqc-hdsUhm3Bsbgi7oO6g)
* Learn about the [`geocoders` module in the `geopy` package](https://geopy.readthedocs.io/)
* Learn about the [`nominatim` package](https://nominatim.org/release-docs/develop/api/Overview/)
* If you get a HTTP Error 403 from Nominatim, use your email ID or your name instead of “myGeocoder” in `Nominatim(user_agent="myGeocoder")`

[Previous

Scraping IMDb with JavaScript](#/scraping-imdb-with-javascript)

[Next

Wikipedia Data with Python](#/wikipedia-data-with-python)

---


# File: Notebooks__Google_Colab.md

---
title: "Notebooks: Google Colab"
original_url: "https://tds.s-anand.net/#/colab?id=notebooks-google-colab"
downloaded_at: "2025-05-31T21:39:34.793729"
---

[Notebooks: Google Colab](#/colab?id=notebooks-google-colab)
------------------------------------------------------------

[Google Colab](https://colab.research.google.com/) is a free, cloud-based Jupyter notebook environment that’s become indispensable for data scientists and ML practitioners. It’s particularly valuable because it provides free access to GPUs and TPUs, and for easy sharing of code and execution results.

While Colab is excellent for prototyping and learning, its free tier has limitations - notebooks time out after 12 hours, and GPU access can be inconsistent.

Learn how to mount Google Drive for persistent storage, manage dependencies with `!pip install` commands, as these are common pain points when getting started.

[![Get started with Google Colaboratory (3 min)](https://i.ytimg.com/vi_webp/inN8seMm7UI/sddefault.webp)](https://youtu.be/inN8seMm7UI)

* [Google Colab features you may have missed](https://youtu.be/rNgswRZ2C1Y)
* [How to mount Google Drive to Google Colab](https://youtu.be/8HvugBq5NKg)
* [How to take advantage of GPUs and TPUs for your ML project](https://youtu.be/tCYSce6l8gA)

[Previous

Static hosting: GitHub Pages](#/github-pages)

[Next

Serverless hosting: Vercel](#/vercel)

---


# File: Outlier_Detection_with_Excel.md

---
title: "Outlier Detection with Excel"
original_url: "https://tds.s-anand.net/#/outlier-detection-with-excel?id=outlier-detection-with-excel"
downloaded_at: "2025-05-31T21:39:07.192775"
---

[Outlier Detection with Excel](#/outlier-detection-with-excel?id=outlier-detection-with-excel)
----------------------------------------------------------------------------------------------

[![Outlier detection with Excel](https://i.ytimg.com/vi_webp/sUTJb0F9eBw/sddefault.webp)](https://youtu.be/sUTJb0F9eBw)

You’ll learn how to identify and handle outliers in data using Excel, covering:

* **Understanding Outliers**: Definition of outliers and their impact on statistical analysis.
* **Calculating Quartiles**: Using Excel formulas to calculate Q1 (first quartile) and Q3 (third quartile).
* **Interquartile Range (IQR)**: Finding the IQR by subtracting Q1 from Q3.
* **Determining Bounds**: Calculating lower and upper bounds using 1.5 times the IQR.
* **Identifying Outliers**: Using Excel functions to determine if data points fall outside the calculated bounds.
* **Visualizing Data**: Creating box plots to visualize outliers and data distribution.
* **Handling Outliers**: Deciding whether to exclude or keep outliers based on their impact on analysis.

Here are the links used in the video:

* [Understand distributions and outliers](https://www.khanacademy.org/math/ap-statistics/quantitative-data-ap/xfb5d8e68:describing-distribution-quant/v/classifying-distributions)
* [COVID-19 vaccinations data - Excel](https://docs.google.com/spreadsheets/d/1_vQF2i5ubKmHQMBqoTwsu6AlevWsQtTD/view#gid=790744269)

[Previous

Forecasting with Excel](#/forecasting-with-excel)

[Next

Data Analysis with Python](#/data-analysis-with-python)

---


# File: Parsing_JSON.md

---
title: "Parsing JSON"
original_url: "https://tds.s-anand.net/#/parsing-json?id=sql-json-functions"
downloaded_at: "2025-05-31T21:39:59.974451"
---

[Parsing JSON](#/parsing-json?id=parsing-json)
----------------------------------------------

JSON is everywhere—APIs, logs, configuration files—and its nested or large structure can challenge memory and processing. In this tutorial, we’ll explore tools to flatten, stream, and query JSON data efficiently.

For example, we’ll often need to process a multi-gigabyte log file from a web service where each record is a JSON object.

[![JSON Parsing in Python](https://i.ytimg.com/vi/1lxrb_ezP-g/sddefault.jpg)](https://youtu.be/1lxrb_ezP-g)

This requires us to handle complex nested structures, large files that don’t fit in memory, or extract specific fields. Here are the key tools and techniques for efficient JSON parsing:

| Tool | Extract from JSON… | Why |
| --- | --- | --- |
| [jq](#/parsing-json?id=command-line-json-processing-with-jq) | JSON in the shell | Quick data exploration and pipeline processing |
| [JMESPath](#/parsing-json?id=jmespath-queries) | JSON in Python | Handle complex queries with a clean syntax |
| [ijson](#/parsing-json?id=streaming-with-ijson) | JSON streams in Python | Parse streaming/large JSON files memory-efficiently |
| [Pandas](#/parsing-json?id=pandas-json-columns) | JSON columns in Python | Fast analysis of structured data |
| [SQL JSON](#/parsing-json?id=sql-json-functions) | JSON in databases | Combine structured and semi-structured data |
| [DuckDB](#/parsing-json?id=duckdb-json-processing) | JSON anywhere | Fast analysis of JSON files / databases without loading to memory |

**Examples:**

* Use Pandas when you need to transform API responses into a DataFrame for further analysis.
* Leverage ijson when dealing with huge JSON logs where memory is at a premium.
* Apply jq for quick, iterative exploration directly in your terminal.

Practice with these resources:

* [JSONPath Online Evaluator](https://jsonpath.com/): Test JSON queries
* [jq play](https://jqplay.org/): Interactive jq query testing
* [DuckDB JSON Tutorial](https://duckdb.org/docs/data/json): Learn DuckDB JSON functions

### [Command-line JSON Processing with jq](#/parsing-json?id=command-line-json-processing-with-jq)

[jq](https://jqlang.org/) is a versatile command-line tool for slicing, filtering, and transforming JSON. It excels in quick data exploration and can be integrated into shell scripts for automated data pipelines.

**Example:** Sifting through server logs in JSON Lines format to extract error messages or aggregate metrics without launching a full-scale ETL process.

```
# Extract specific fields from JSONL
cat data.jsonl | jq -c 'select(.type == "user") | {id, name}'

# Transform JSON structure
cat data.json | jq '.items[] | {name: .name, count: .details.count}'

# Filter and aggregate
cat events.jsonl | jq -s 'group_by(.category) | map({category: .[0].category, count: length})'Copy to clipboardErrorCopied
```

### [JMESPath Queries](#/parsing-json?id=jmespath-queries)

[JMESPath](https://jmespath.org/) offers a declarative query language to extract and transform data from nested JSON structures without needing verbose code. It’s a neat alternative when you want to quickly pull out specific values or filter collections based on conditions.

**Example:** Extracting user emails or filtering out inactive records from a complex JSON payload received from a cloud service.

```
import jmespath

# Example queries
data = {
    "locations": [
        {"name": "Seattle", "state": "WA", "info": {"population": 737015}},
        {"name": "Portland", "state": "OR", "info": {"population": 652503}}
    ]
}

# Find all cities with population > 700000
cities = jmespath.search("locations[?info.population > `700000`].name", data)Copy to clipboardErrorCopied
```

### [Streaming with ijson](#/parsing-json?id=streaming-with-ijson)

Loading huge JSON files all at once can quickly exhaust system memory. [ijson](https://ijson.readthedocs.io/en/latest/) lets you stream and process JSON incrementally. This method is ideal when your JSON file is too large or when you only need to work with part of the data.

**Example:** Processing a continuous feed from an API that returns a large JSON array, such as sensor data or event logs, while filtering on the fly.

```
import ijson

async def process_large_json(filepath: str) -> list:
    """Process a large JSON file without loading it entirely into memory."""
    results = []

    with open(filepath, 'rb') as file:
        # Stream objects under the 'items' key
        parser = ijson.items(file, 'items.item')
        async for item in parser:
            if item['value'] > 100:  # Process conditionally
                results.append(item)

    return resultsCopy to clipboardErrorCopied
```

### [Pandas JSON Columns](#/parsing-json?id=pandas-json-columns)

[Pandas](https://pandas.pydata.org/) makes it easy to work with tabular data that includes JSON strings. When you receive API data where one column holds nested JSON, flattening these structures lets you analyze and visualize the data using familiar DataFrame operations.

**Example:** Flattening customer records stored as nested JSON in a CSV file to extract demographic details and spending patterns.

```
import pandas as pd

# Parse JSON strings in a column
df = pd.DataFrame({'json_col': ['{"name": "Alice", "age": 30}', '{"name": "Bob", "age": 25}']})
df['parsed'] = df['json_col'].apply(pd.json_normalize)

# Normalize nested JSON columns
df = pd.read_csv('data.csv')
df_normalized = pd.json_normalize(
    df['nested_json'].apply(json.loads),
    record_path=['items'],        # List of nested objects to unpack
    meta=['id', 'timestamp']      # Keep these columns from parent
)Copy to clipboardErrorCopied
```

### [SQL JSON Functions](#/parsing-json?id=sql-json-functions)

[SQL](https://en.wikipedia.org/wiki/SQL:2016) supports built-in JSON functions allow you to query and manipulate JSON stored within relational databases.
These are implemented by most popular databases, including
[SQLite](https://www.sqlite.org/json1.html),
[PostgreSQL](https://www.postgresql.org/docs/current/functions-json.html), and
[MySQL](https://dev.mysql.com/doc/refman/8.4/en/json-function-reference.html).
This is especially handy when you have a hybrid data model, combining structured tables with semi-structured JSON columns.

**Example:** An application that stores user settings or application logs as JSON in a SQLite database, enabling quick lookups and modifications without external JSON parsing libraries.

```
SELECT
    json_extract(data, '$.name') as name,
    json_extract(data, '$.details.age') as age
FROM users
WHERE json_extract(data, '$.active') = trueCopy to clipboardErrorCopied
```

### [DuckDB JSON Processing](#/parsing-json?id=duckdb-json-processing)

[DuckDB](https://duckdb.org/) shines when analyzing JSON/JSONL files directly, making it a powerful tool for data analytics without the overhead of loading entire datasets into memory. Its SQL-like syntax simplifies exploratory analysis on nested data.

**Example:** Performing ad-hoc analytics on streaming JSON logs from a web service, such as calculating average response times or aggregating user behavior metrics.

```
SELECT
    json_extract_string(data, '$.user.name') as name,
    avg(json_extract_float(data, '$.metrics.value')) as avg_value
FROM read_json_auto('data/*.jsonl')
GROUP BY 1
HAVING avg_value > 100Copy to clipboardErrorCopied
```

[Previous

Profiling Data with Python](#/profiling-data-with-python)

[Next

Data Transformation with dbt](#/dbt)

---


# File: Profiling_Data_with_Python.md

---
title: "Profiling Data with Python"
original_url: "https://tds.s-anand.net/#/profiling-data-with-python?id=profile-data-with-python"
downloaded_at: "2025-05-31T21:36:56.246125"
---

[Profile Data with Python](#/profiling-data-with-python?id=profile-data-with-python)
------------------------------------------------------------------------------------

[![Discover the data profile with Python](https://i.ytimg.com/vi_webp/kFVxdBhLa_A/sddefault.webp)](https://youtu.be/kFVxdBhLa_A)

This session covers the use of the `pandas_profiling` library for generating comprehensive data reports in Python:

* **Library Installation and Import**: Learn how to install and import the pandas\_profiling library.
* **Profile Report Generation**: Generate an HTML report with a single line of code using ProfileReport.
* **Descriptive Statistics**: View detailed descriptive statistics such as variance, standard deviation, and kurtosis.
* **Outlier Detection**: Identify and analyze outliers within the dataset.
* **Correlation Analysis**: Understand how variables are correlated with each other using visual representations.
* **Handling Missing Values**: Get insights on missing data and decide on imputation or removal strategies.
* **Initial Data Insights**: Use the report to gather early warnings and insights before starting the data cleaning and modeling process.

Here are links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/1hFo_zvBuKw_ugxRjX4XUSh65-hAvl7X0)
* [Pandas Profiling output](https://drive.google.com/file/d/1cqu52zgddCJqzbLd7xqDC2RXPNkufFlN/view)
* Learn about the [`pandas_profiling` package](https://github.com/ydataai/ydata-profiling). [Video](https://youtu.be/Ef169VELt5o)
* Learn about the [`google.colab` package](https://colab.research.google.com/notebooks/io.ipynb)

[Previous

Cleaning Data with OpenRefine](#/cleaning-data-with-openrefine)

[Next

Parsing JSON](#/parsing-json)

---


# File: Project_1.md

---
title: "Project 1"
original_url: "https://tds.s-anand.net/#/project-tds-virtual-ta?id=scrape-the-data"
downloaded_at: "2025-05-31T21:39:02.922036"
---

[Project: TDS Virtual TA](#/project-tds-virtual-ta?id=project-tds-virtual-ta)
=============================================================================

Create a virtual Teaching Assistant Discourse responder.

[Background](#/project-tds-virtual-ta?id=background)
----------------------------------------------------

You are a clever student who has joined IIT Madras’ Online Degree in Data Science. You have just enrolled in the [Tools in Data Science](https://tds.s-anand.net/#/2025-01/) course.

Out of kindness for your teaching assistants, you have decided to build an API that can automatically answer student questions on their behalf based on:

* [Course content](https://tds.s-anand.net/#/2025-01/) with content for TDS Jan 2025 as on 15 Apr 2025.
* [TDS Discourse posts](https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34) with content from 1 Jan 2025 - 14 Apr 2025.

[Scrape the data](#/project-tds-virtual-ta?id=scrape-the-data)
--------------------------------------------------------------

To make sure you can answer these questions, you will need to extract the data from the above source.

[Create an API](#/project-tds-virtual-ta?id=create-an-api)
----------------------------------------------------------

Your application exposes an API endpoint. You may host it anywhere. Let’s assume it’s at `https://app.example.com/api/`.

The endpoint must accept a POST request, e.g. `POST https://app.example.com/api/` with a student question as well as optional base64 file attachments as JSON.

For example, here’s how anyone can make a request:

```
curl "https://app.example.com/api/" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?\", \"image\": \"$(base64 -w0 project-tds-virtual-ta-q1.webp)\"}"Copy to clipboardErrorCopied
```

This is a [real question](https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939) and uses this [screenshot](#/images/project-tds-virtual-ta-q1.webp):

![Screenshot](/images/project-tds-virtual-ta-q1.webp)

The response must be a JSON object like this:

```
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
      "text": "Use the model that’s mentioned in the question."
    },
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
      "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
    }
  ]
}Copy to clipboardErrorCopied
```

[Evaluate your application](#/project-tds-virtual-ta?id=evaluate-your-application)
----------------------------------------------------------------------------------

Here are a few [sample questions and evaluation parameters](project-tds-virtual-ta-promptfoo.yaml). These are **indicative**. The actual evaluation could ask *any* realistic student question.

To run this:

1. Edit [`project-tds-virtual-ta-promptfoo.yaml`](project-tds-virtual-ta-promptfoo.yaml) to replace `providers[0].config.url` with your API URL.
2. Run this script:

   ```
   npx -y promptfoo eval --config project-tds-virtual-ta-promptfoo.yamlCopy to clipboardErrorCopied
   ```

[Deploy your application](#/project-tds-virtual-ta?id=deploy-your-application)
------------------------------------------------------------------------------

Deploy your application to a public URL that can be accessed by anyone. You may use any platform.

(If you use ngrok, ensure that it is running continuously until you get your results.)

[Share your code](#/project-tds-virtual-ta?id=share-your-code)
--------------------------------------------------------------

* [Create a new *public* GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
* [Add an MIT `LICENSE` file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
* Commit and push your code

[Submit your URL](#/project-tds-virtual-ta?id=submit-your-url)
--------------------------------------------------------------

Submit your GitHub repository URL and your API endpoint URL at <https://exam.sanand.workers.dev/tds-project-virtual-ta>

[Evaluation](#/project-tds-virtual-ta?id=evaluation)
----------------------------------------------------

* **Pre-requisites**: Your repository **MUST** meet the following criteria to be eligible for evaluation
  + Your GitHub repository exists and is publicly accessible
  + Your GitHub repository has a `LICENSE` file with the MIT license in the root folder
* We will use a modified version of [`project-tds-virtual-ta-promptfoo.yaml`](project-tds-virtual-ta-promptfoo.yaml) with 10 realistic questions. Correct answers will be awarded up to 2 marks each.
* Your score will be the sum of the marks above. No normalization. What you get is what you get.

Bonus:

* 1 mark if your GitHub repo includes a script that scrapes the Discourse posts across a date range from a Discourse course page like [TDS](https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34)
* 2 marks if we deploy your solution (with minimal modifications) as an official solution for students to use.

[Previous

LLM Evals](#/llm-evals)

[Next

4. Data Sourcing](#/data-sourcing)

---


# File: Prompt_engineering.md

---
title: "Prompt engineering"
original_url: "https://tds.s-anand.net/#/prompt-engineering?id=think-step-by-step"
downloaded_at: "2025-05-31T21:38:08.140672"
---

[Prompt Engineering](#/prompt-engineering?id=prompt-engineering)
----------------------------------------------------------------

Prompt engineering is the process of crafting effective prompts for large language models (LLMs).

One of the best ways to approach prompt engineering is to think of LLMs as a smart colleague (with amnesia) who needs explicit instructions.

The most authoritative guides are from the LLM providers themselves:

* [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/)
* [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)
* [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)

Here are some best practices:

### [Use prompt optimizers](#/prompt-engineering?id=use-prompt-optimizers)

They rewrite your prompt to improve it. Explore:

* [Anthropic Prompt Optimizer](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver)
* [OpenAI Prompt Generation](https://platform.openai.com/docs/guides/prompt-generation)
* [Google AI-powered prompt writing tools](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/ai-powered-prompt-writing)

### [Be clear, direct, and detailed](#/prompt-engineering?id=be-clear-direct-and-detailed)

Be explicit and thorough. Include all necessary context, goals, and details so the model understands the full picture.

* **BAD**: *Explain gravitation lensing.* (Reason: Vague and lacks context or detail.)
* **GOOD**: *Explain the concept of gravitational lensing to a high school student who understands basic physics, including how it’s observed and its significance in astronomy.* (Reason: Specifies the audience, scope, and focus.)

> When you ask a question, don’t be vague. Spell it out. Give every detail the listener needs.
> The clearer you are, the better the answer you’ll get.
> For example, don’t just say, Explain Gravitation Lensing.
> Say, Explain the concept of gravitational lensing to a high school student who understands basic physics, including how it’s observed and its significance in astronomy.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-include-details-in-your-query-to-get-more-relevant-answers)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/clear-instructions)

### [Give examples](#/prompt-engineering?id=give-examples)

Provide 2-3 relevant examples to guide the model on the style, structure, or format you expect. This helps the model produce outputs consistent with your desired style.

* **BAD**: *Explain how to tie a bow tie.* (Reason: No examples or reference points given.)
* **GOOD**:
  *Explain how to tie a bow tie. For example:*

  1. *To tie a shoelace, you cross the laces and pull them tight…*
  2. *To tie a necktie, you place it around the collar and loop it through…*

  *Now, apply a similar step-by-step style to describe how to tie a bow tie.* (Reason: Provides clear examples and a pattern to follow.)

> Give examples to the model. If you want someone to build a house, show them a sketch. Don’t just say ‘build something.’
> Giving examples is like showing a pattern. It makes everything easier to follow.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-provide-examples)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples)

### [Think step by step](#/prompt-engineering?id=think-step-by-step)

Instruct the model to reason through the problem step by step. This leads to more logical, well-structured answers.

* **BAD**: *Given this transcript, is the customer satisfied?* (Reason: No prompt for structured reasoning.)
* **GOOD**: *Given this transcript, is the customer satisfied? Think step by step.* (Reason: Directly instructs the model to break down reasoning into steps.)

> Ask the model to think step by step. Don’t ask the model to just give the final answer right away.
> That’s like asking someone to answer with the first thing that pops into their head.
> Instead, ask them to break down their thought process into simple moves — like showing each rung of a ladder as they climb.
> For example, when thinking step by step, the model could, A, list each customer question, B, find out if it was addressed, and C, decide that the agent answered only 2 out of the 3 questions.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#strategy-give-models-time-to-think)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/break-down-prompts)

### [Assign a role](#/prompt-engineering?id=assign-a-role)

Specify a role or persona for the model. This provides context and helps tailor the response style.

* **BAD**: *Explain how to fix a software bug.* (Reason: No role or perspective given.)
* **GOOD**: *You are a seasoned software engineer. Explain how to fix a software bug in legacy code, including the debugging and testing process.* (Reason: Assigns a clear, knowledgeable persona, guiding the style and depth.)

> Tell the model who they are. Maybe they’re a seasoned software engineer fixing a legacy bug, or an experienced copy editor revising a publication.
> By clearly telling the model who they are, you help them speak with just the right expertise and style.
> Suddenly, your explanation sounds like it’s coming from a true specialist, not a random voice.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-ask-the-model-to-adopt-a-persona)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/assign-role)

### [Use XML to structure your prompt](#/prompt-engineering?id=use-xml-to-structure-your-prompt)

Use XML tags to separate different parts of the prompt clearly. This helps the model understand structure and requirements.

* **BAD**: *Here’s what I want: Provide a summary and then an example.* (Reason: Unstructured, no clear separation of tasks.)
* **GOOD**:

  ```
  <instructions>
    Provide a summary of the concept of machine learning.
  </instructions>
  <example>
    Then provide a simple, concrete example of a machine learning application (e.g., an email spam filter).
  </example>Copy to clipboardErrorCopied
  ```

  (Reason: Uses XML tags to clearly distinguish instructions from examples.)

> Think of your request like a box. XML tags are neat little labels on that box.
> They help keep parts sorted, so nothing gets lost in the shuffle.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts)

### [Use Markdown to format your output](#/prompt-engineering?id=use-markdown-to-format-your-output)

Encourage the model to use Markdown for headings, lists, code blocks, and other formatting features to produce structured, easily readable answers.

* **BAD**: *Give me the steps in plain text.* (Reason: No specific formatting instructions, less readable.)
* **GOOD**: *Provide the steps in a markdown-formatted list with ### headings for each section and numbered bullet points.* (Reason: Directly instructs to use Markdown formatting, making output more structured and clear.)
* **BAD**: *Correct the spelling and show the corrections.* (Reason: No specific formatting instructions)
* **GOOD**: *Correct the spelling, showing <ins>additions</ins> and <del>deletions</del>.* (Reason: Directly instructs to use HTML formatting, making output more structured and clear.)

> Markdown is a simple formatting language that all models understand.
> You can have them add neat headings, sections, bold highlights, and bullet points.
> These make complex documents more scannable and easy on the eyes.

### [Use JSON for machine-readable output](#/prompt-engineering?id=use-json-for-machine-readable-output)

When you need structured data, ask for a JSON-formatted response. This ensures the output is machine-readable and organized.

* **BAD**: *Just list the items.* (Reason: Unstructured plain text makes parsing harder.)
* **GOOD**:

  ```
  Organize as an array of objects in a JSON format, like this:

  ```json
  [
    { "name": "Item 1", "description": "Description of Item 1" },
    { "name": "Item 2", "description": "Description of Item 2" },
    { "name": "Item 3", "description": "Description of Item 3" }
  ]
  ```Copy to clipboardErrorCopied
  ```

  (Reason: Instructing JSON format ensures structured, machine-readable output.)

Note: Always use [JSON schema](#/playground?id=attachments) if possible. [JSON schema](https://json-schema.org/) is a way to describe the structure of JSON data. An easy way to get the JSON schema is to give ChatGPT sample output and ask it to generate the schema.

> Imagine you’re organizing data for a big project. Plain text is like dumping everything into one messy pile — it’s hard to find what you need later.
> JSON, on the other hand, is like packing your data into neat, labeled boxes within boxes.
> Everything has its place: fields like ‘name,’ ‘description,’ and ‘value’ make the data easy to read, especially for machines.
> For example, instead of just listing items, you can structure them as a JSON array, with each item as an object.
> That way, when you hand it to a program, it’s all clear and ready to use.

### [Prefer Yes/No answers](#/prompt-engineering?id=prefer-yesno-answers)

Convert rating or percentage questions into Yes/No queries. LLMs handle binary choices better than numeric scales.

* **BAD**: *On a scale of 1-10, how confident are you that this method works?* (Reason: Asks for a numeric rating, which can be imprecise.)
* **GOOD**: *Is this method likely to work as intended? Please give a reasoning and then answer Yes or No.* (Reason: A binary question simplifies the response and clarifies what’s being asked.)

> Don’t ask ‘On a scale of one to five…’. Models are not good with numbers.
> They don’t know how to grade something 7 versus 8 on a 10 point scale. ‘Yes or no?’ is simple. It’s clear. It’s quick.
> So, break your question into simple parts that they can answer with just a yes or a no.

### [Ask for reason first, then the answer](#/prompt-engineering?id=ask-for-reason-first-then-the-answer)

Instruct the model to provide its reasoning steps *before* stating the final answer. This makes it less likely to justify itself and more likely to think deeper, leading to more accurate results.

* **BAD**: *What is the best route to take?* (Reason: Direct question without prompting reasoning steps first.)
* **GOOD**: *First, explain your reasoning step by step for how you determine the best route. Then, after you’ve reasoned it out, state your final recommendation for the best route.* (Reason: Forces the model to show its reasoning process before giving the final answer.)

> BEFORE making its final choice, have the model talk through their thinking. Reasoning first, answer second.
> That way, the model won’t be tempted to justify an answer that they gave impulsively. It is also more likely to think deeper.

### [Use proper spelling and grammar](#/prompt-engineering?id=use-proper-spelling-and-grammar)

A well-written, grammatically correct prompt clarifies expectations. Poorly structured prompts can confuse the model.

* **BAD**: *xplin wht the weirless netork do? make shur to giv me a anser??* (Reason: Poor spelling and unclear instructions.)
* **GOOD**: *Explain what a wireless network does. Please provide a detailed, step-by-step explanation.* (Reason: Proper spelling and clarity lead to a more coherent response.)

> If your question sounds like gibberish, expect a messy answer. Speak cleanly.
> When you do, the response will be much clearer.

[Video Tutorials](#/prompt-engineering?id=video-tutorials)
----------------------------------------------------------

Watch [Prompt Engineering Tutorial – Master ChatGPT and LLM Responses (41 min)](https://youtu.be/_ZvnD73m40o). It covers:

1. Basics of **AI and large language models**.
2. How to write clear and detailed prompts to improve answers.
3. Tips for creating interactive and personalized AI responses.
4. Advanced topics like **AI mistakes** (hallucinations) and **text embeddings** (how AI understands words).
5. Fun examples, like making AI write poems or correct grammar.

[![Prompt Engineering Tutorial – Master ChatGPT and LLM Responses](https://i.ytimg.com/vi_webp/_ZvnD73m40o/sddefault.webp)](https://youtu.be/_ZvnD73m40o)

[Previous

3. Large Language Models](#/large-language-models)

[Next

TDS TA Instructions](#/tds-ta-instructions)

---


# File: Python_tools__uv.md

---
title: "Python tools: uv"
original_url: "https://tds.s-anand.net/#/uv?id=python-tools-uv"
downloaded_at: "2025-05-31T21:38:10.468176"
---

[Python tools: uv](#/uv?id=python-tools-uv)
-------------------------------------------

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager that’s becoming the standard for running Python scripts. It replaces tools like pip, conda, pipx, poetry, pyenv, twine, and virtualenv into one, enabling:

* **Python Version Management**: uv installs and manages *multiple* Python versions, allowing developers to specify and switch between versions seamlessly.
* **Virtual Environment Handling**: It automates the creation and management of virtual environments, ensuring isolated and consistent development spaces for different projects.
* **Dependency Management**: With support for the pyproject.toml format, uv enables precise specification of project dependencies. It maintains a universal lockfile, uv.lock, to ensure reproducible installations across different systems.
* **Project Execution**: The `uv run` command allows for the execution of scripts and applications within the managed environment, streamlining development workflows.

Here are some commonly used commands:

```
# Replace python with uv. This automatically installs Python and dependencies.
uv run script.py

# Run a Python script directly from the Internet
uv run https://example.com/script.py

# Run a Python script without installing
uvx ruff

# Use a specific Python version
uv run --python 3.11 script.py

# Add dependencies to your script
uv add httpx --script script.py

# Create a virtual environment at .venv
uv venv

# Install packages to your virtual environment
uv pip install httpxCopy to clipboardErrorCopied
```

Here are some useful tools you can run with `uvx` without installation:

```
uvx --from jupyterlab jupyter-lab   # Jupyter notebook
uvx marimo      # Interactive notebook
uvx llm         # Chat with LLMs from the command line
uvx openwebui   # Chat with LLMs via the browser
uvx httpie      # Make HTTP requests
uvx datasette   # Browse SQLite databases
uvx markitdown  # Convert PDF to Markdown
uvx yt-dlp      # Download YouTube videos
uvx asciinema   # Record your terminal and play itCopy to clipboardErrorCopied
```

uv uses [inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) for dependencies.
The eliminates the need for `requirements.txt` or virtual environments. For example:

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
# ]
# ///Copy to clipboardErrorCopied
```

[![uv - Python package and project management | Inline Script Metadata (28 min)](https://i.ytimg.com/vi_webp/igWlYl3asKw/sddefault.webp)](https://youtu.be/igWlYl3asKw?t=1240)




[Previous

AI Code Editors: GitHub Copilot](#/github-copilot)

[Next

JavaScript tools: npx](#/npx)

---


# File: RAG_with_the_CLI).md

---
title: "RAG with the CLI)"
original_url: "https://tds.s-anand.net/#/rag-cli?id=_1-clone-the-repository"
downloaded_at: "2025-05-31T21:38:47.705686"
---

[Retrieval Augmented Generation (RAG) with the CLI](#/rag-cli?id=retrieval-augmented-generation-rag-with-the-cli)
-----------------------------------------------------------------------------------------------------------------

Retrieval Augmented Generation (RAG) combines retrieval (searching a knowledge base) with generation (using an LLM) to produce answers grounded in your own documents. Instead of relying solely on a general-purpose LLM, RAG lets you feed it the most relevant chunks from your corpus at query time, improving accuracy, reducing hallucinations, and allowing you to answer domain‑specific questions without fine‑tuning.

In particular, you can answer questions that are hard to answer with a keyword search. For example:

```
Q="What does the author affectionately call the => syntax?"
# Answer: fat arrow

Q="What lets you walk every child node of a ts.Node?"
# Answer: node.getChildren()

Q="What are code pieces like comments and whitespace that aren’t in the AST called?"
# Answer: trivia

Q="Which operator converts any value into an explicit boolean?"
# Answer: !!Copy to clipboardErrorCopied
```

You can implement RAG entirely from your terminal, without writing a single line of application code. Below is a step‑by‑step example using the TypeScript book as a data source.

### [1. Clone the repository](#/rag-cli?id=_1-clone-the-repository)

```
git clone --depth 1 https://github.com/basarat/typescript-book
cd typescript-bookCopy to clipboardErrorCopied
```

* `--depth 1` fetches only the latest commit to minimize download size.
* `cd typescript-book` moves into the project folder.

You’ll now be in a new folder `typescript-book` containing the repo.

### [2. Split Markdown files into chunks](#/rag-cli?id=_2-split-markdown-files-into-chunks)

```
(
  shopt -s globstar
  for f in **/*.md; do
    uvx --from split_markdown4gpt mdsplit4gpt "$f" --model gpt-4o --limit 4096 --separator "===SPLIT===" \
    | sed '1s/^/===SPLIT===\n/' \
    | jq -R -s -c --arg file "$f" '
      split("===SPLIT===")[1:]
      | to_entries
      | map({
          id: ($file + "#" + (.key | tostring)),
          content: .value
        })[]
    '
  done
) | tee chunks.jsonCopy to clipboardErrorCopied
```

* `shopt -s globstar`: lets `**/*.md` match Markdown files in all subdirectories. [bash shopt manual](https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html)
* `uvx --from split_markdown4gpt mdsplit4gpt`: [a tool](https://github.com/twardoch/split-markdown4gpt) that splits Markdown into LLM‑sized chunks:
  + `--model gpt-4o`: uses GPT‑4o token limits
  + `--limit 4096`: max tokens per chunk
  + `--separator "===SPLIT==="`: custom split marker
* `sed '1s/^/===SPLIT===\n/'`: ensures the very first chunk starts with the separator (GNU sed manual)
* `jq -R -s -c --arg file "$f"`: uses [jq](https://stedolan.github.io/jq/manual/) to convert chunks to JSON
  + `-R`: read raw input
  + `-s`: slurp entire input into a single string
  + `-c`: compact JSON output
  + builds an array of objects `{id, content}`, where `id` is `filename#chunkIndex`
* `tee chunks.json`: writes the resulting JSON array to `chunks.json` while printing it to stdout.

You’ll now have a `chunks.json` that has one `{id, content}` JSON object per line.

### [3. Generate embeddings](#/rag-cli?id=_3-generate-embeddings)

```
llm embed-multi typescript-book --model 3-small --store --format nl chunks.jsonCopy to clipboardErrorCopied
```

* `embed-multi`: computes embeddings for each entry in `chunks.json`.
* `typescript-book`: a namespace or collection name for storage.
* `--model 3-small`: selects the embedding model.
* `--store`: save embeddings in the default backend.
* `--format nl`: input is newline‑delimited JSON. [llm CLI embed-multi](https://github.com/kerenter/llm#embed-multi)

This stores the embeddings in a collection called `typescript-book`.

```
llm collections path  # shows where the collections are stored
llm collections delete typescript-book  # deletes the typescript-book collectionCopy to clipboardErrorCopied
```

### [4. Find similar topics](#/rag-cli?id=_4-find-similar-topics)

```
llm similar typescript-book -n 3 -c "What does the author affectionately call the => syntax?"Copy to clipboardErrorCopied
```

This returns the 3 chunksmost similar to the question posed.

* `similar`: retrieves the top `n` most similar chunks from the embeddings store.
* `-n 3`: return three results.
* `-c`: the user’s query string.

### [5. Answer a question using retrieved context](#/rag-cli?id=_5-answer-a-question-using-retrieved-context)

```
Q="What does the author affectionately call the => syntax?"
llm similar typescript-book -n 3 -c "$Q" \
  | jq '.content' \
  | llm -s "$Q - Answer ONLY from these notes. Cite verbatim from notes." \
  | uvx streamdownCopy to clipboardErrorCopied
```

This answers the question in natural language following these steps:

1. Store the query in `Q`.
2. Retrieve the top 3 matching chunks.
3. `jq '.content'` extracts just the text snippets.
4. Pipe into `llm -s`, instructing the model:
   * `-s`: stream a prompt directly to the LLM.
   * `"$Q - Answer ONLY from these notes. Cite verbatim from notes."`: ensures the response is grounded.
5. `uvx streamdown` formats the streamed LLM output for easy reading.

[Previous

Vector databases](#/vector-databases)

[Next

Hybrid RAG with TypeSense](#/hybrid-rag-typesense)

---


# File: RAWgraphs.md

---
title: "RAWgraphs"
original_url: "https://tds.s-anand.net/#/rawgraphs?id=rawgraphs"
downloaded_at: "2025-05-31T21:38:28.850239"
---

[RAWgraphs](#/rawgraphs?id=rawgraphs)
-------------------------------------

[![RAWGraphs 1.0 - Introduction (1 min)](https://i.ytimg.com/vi_webp/2TtYlty-M5g/sddefault.webp)](https://youtu.be/2TtYlty-M5g)

* [RAWgraphs](https://www.rawgraphs.io/)
* [How to make Alluvial Diagram](https://youtu.be/6BYac2Pmnno)
* [How to make Sankey Diagram](https://youtu.be/DYTiKjH6oFM)
* [How to make Beeswarm Plot](https://youtu.be/RPHiEzbCatA)
* [How to make Bump Chart](https://youtu.be/K-weHCSQb58)
* [How to make Circle Packing](https://youtu.be/inm_fR-oykw)
* [How to make Treemap](https://youtu.be/W_MuNYWjhfc)
* [How to make Streamgraph](https://youtu.be/Iu8Me9QO8mg)
* [How to make Sunburst Diagram](https://youtu.be/knqimV7RVbI)
* [How to make Voronoi Diagram](https://youtu.be/I7nn29giVug)
* [How to make Hexagonal Binning](https://youtu.be/Q03sVDj32l4)

[Previous

Actor Network Visualization](#/actor-network-visualization)

[Next

Data Storytelling](#/data-storytelling)

---


# File: REST_APIs.md

---
title: "REST APIs"
original_url: "https://tds.s-anand.net/#/rest-apis?id=rest-apis"
downloaded_at: "2025-05-31T21:36:53.896228"
---

[REST APIs](#/rest-apis?id=rest-apis)
-------------------------------------

REST (Representational State Transfer) APIs are the standard way to build web services that allow different systems to communicate over HTTP. They use standard HTTP methods and JSON for data exchange.

Watch this comprehensive introduction to REST APIs (52 min):

[![REST API Crash Course - Introduction + Full Python API Tutorial (52)](https://i.ytimg.com/vi_webp/qbLc5a9jdXo/sddefault.webp)](https://youtu.be/qbLc5a9jdXo)

Key Concepts:

1. **HTTP Methods**
   * `GET`: Retrieve data
   * `POST`: Create new data
   * `PUT/PATCH`: Update existing data
   * `DELETE`: Remove data
2. **Status Codes**
   * `2xx`: Success (200 OK, 201 Created)
   * `4xx`: Client errors (400 Bad Request, 404 Not Found)
   * `5xx`: Server errors (500 Internal Server Error)

Here’s a minimal REST API using FastAPI. Run this `server.py` script via `uv run server.py`:

```
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

# Create a list of items that will act like a database
items: List[Dict[str, float | int | str]] = []

# Create a GET endpoint that returns all items
@app.get("/items")
async def get_items() -> List[Dict[str, float | int | str]]:
    return items

# Create a GET endpoint that returns a specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Dict[str, float | int | str]:
    if item := next((i for i in items if i["id"] == item_id), None):
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a POST endpoint that creates a new item
@app.post("/items")
async def create_item(item: Dict[str, float | str]) -> Dict[str, float | int | str]:
    new_item = {"id": len(items) + 1, "name": item["name"], "price": float(item["price"])}
    items.append(new_item)
    return new_item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)Copy to clipboardErrorCopied
```

Test the API with curl:

```
# Get all items
curl http://localhost:8000/items

# Create an item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Book", "price": 29.99}'

# Get specific item
curl http://localhost:8000/items/1Copy to clipboardErrorCopied
```

Best Practices:

1. **Use Nouns for Resources**
   * Good: `/users`, `/posts`
   * Bad: `/getUsers`, `/createPost`
2. **Version Your API**

   ```
   /api/v1/users
   /api/v2/usersCopy to clipboardErrorCopied
   ```
3. **Handle Errors Consistently**

   ```
   {
     "error": "Not Found",
     "message": "User 123 not found",
     "status_code": 404
   }Copy to clipboardErrorCopied
   ```
4. **Use Query Parameters for Filtering**

   ```
   /api/posts?status=published&category=techCopy to clipboardErrorCopied
   ```
5. **Implement Pagination**

   ```
   /api/posts?page=2&limit=10Copy to clipboardErrorCopied
   ```

Tools:

* [Postman](https://www.postman.com/): API testing and documentation
* [Swagger/OpenAPI](https://swagger.io/): API documentation
* [HTTPie](https://httpie.io/): Modern command-line HTTP client
* [JSON Schema](https://json-schema.org/): API request/response validation

Learn more about REST APIs:

* [REST API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
* [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)
* [Google API Design Guide](https://cloud.google.com/apis/design)

[Previous

CORS](#/cors)

[Next

Web Framework: FastAPI](#/fastapi)

---


# File: Regression_with_Excel.md

---
title: "Regression with Excel"
original_url: "https://tds.s-anand.net/#/regression-with-excel?id=regression-with-excel"
downloaded_at: "2025-05-31T21:39:09.342440"
---

[Regression with Excel](#/regression-with-excel?id=regression-with-excel)
-------------------------------------------------------------------------

[![Regression with Excel](https://i.ytimg.com/vi_webp/AERQBMIHwXA/sddefault.webp)](https://youtu.be/AERQBMIHwXA)

You’ll learn to perform regression analysis using Excel, covering:

* **Data Preparation**: Understanding the cleaned dataset and necessary columns for analysis.
* **Enabling the Tool**: How to enable the Data Analysis Tool Pack in Excel.
* **Types of Regression**: Differences between simple and multiple linear regression.
* **Setting Up Regression**: Steps to input dependent (new deaths) and independent variables (new cases, new tests, new vaccinations, stringency index) for the analysis.
* **Interpreting Output**: Reading the regression output, focusing on adjusted R-squared, significance value (F-test), and P-values.
* **Coefficient Interpretation**: Understanding the impact of each independent variable on the dependent variable, including scaling factors (per 1000 units).
* **Model Evaluation**: Evaluating the model based on significance values and understanding the implications of unexpected results (e.g., stringency index).
* **Further Analysis**: Recognizing the need for additional analysis when encountering unexpected or inconclusive results.

Here are the links used in the video:

* [Understand regression](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/least-squares-regression/v/calculating-the-equation-of-a-regression-line)
* [COVID-19 vaccinations - Regression Excel file](https://docs.google.com/spreadsheets/d/1YZLb9ozhmc-8KQ7EaaTgs57QT6dHju5u/view#gid=242862119)
* [COVID-19 vaccinations - Regression Model 2 Excel file](https://docs.google.com/spreadsheets/d/1KAolaOQC-P_6gXaw3jgUc7GWKAHfOrsi/view#gid=824457557)

[Previous

Correlation with Excel](#/correlation-with-excel)

[Next

Forecasting with Excel](#/forecasting-with-excel)

---


# File: Scheduled_Scraping_with_GitHub_Actions.md

---
title: "Scheduled Scraping with GitHub Actions"
original_url: "https://tds.s-anand.net/#/scheduled-scraping-with-github-actions?id=video-tutorials"
downloaded_at: "2025-05-31T21:38:12.796512"
---

[Scheduled Scraping with GitHub Actions](#/scheduled-scraping-with-github-actions?id=scheduled-scraping-with-github-actions)
----------------------------------------------------------------------------------------------------------------------------

GitHub Actions provides an excellent platform for running web scrapers on a schedule. This tutorial shows how to automate data collection from websites using GitHub Actions workflows.

### [Key Concepts](#/scheduled-scraping-with-github-actions?id=key-concepts)

* **Scheduling**: Use [cron syntax](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) to run scrapers at specific times
* **Dependencies**: Install required packages like `httpx`, `lxml`
* **Data Storage**: Save scraped data to files and commit back to the repository
* **Error Handling**: Implement robust error handling for network issues and HTML parsing
* **Rate Limiting**: Respect website terms of service and implement delays between requests

Here’s a sample `scrape.py` that scrapes the IMDb Top 250 movies using httpx and lxml:

```
import json
import httpx
from datetime import datetime, UTC
from lxml import html
from typing import List, Dict


def scrape_imdb() -> List[Dict[str, str]]:
    """Scrape IMDb Top 250 movies using httpx and lxml.

    Returns:
        List of dictionaries containing movie title, year, and rating.
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; IMDbBot/1.0)"}
    response = httpx.get("https://www.imdb.com/chart/top/", headers=headers)
    response.raise_for_status()

    tree = html.fromstring(response.text)
    movies = []

    for item in tree.cssselect(".ipc-metadata-list-summary-item"):
        title = (
            item.cssselect(".ipc-title__text")[0].text_content()
            if item.cssselect(".ipc-title__text")
            else None
        )
        year = (
            item.cssselect(".cli-title-metadata span")[0].text_content()
            if item.cssselect(".cli-title-metadata span")
            else None
        )
        rating = (
            item.cssselect(".ipc-rating-star")[0].text_content()
            if item.cssselect(".ipc-rating-star")
            else None
        )

        if title and year and rating:
            movies.append({"title": title, "year": year, "rating": rating})

    return movies


# Scrape data and save with timestamp
now = datetime.now(UTC)
with open(f'imdb-top250-{now.strftime("%Y-%m-%d")}.json', "a") as f:
    f.write(json.dumps({"timestamp": now.isoformat(), "movies": scrape_imdb()}) + "\n")Copy to clipboardErrorCopied
```

Here’s a sample `.github/workflows/imdb-top250.yml` that runs the scraper daily and saves the data:

```
name: Scrape IMDb Top 250

on:
  schedule:
    # Runs at 00:00 UTC every day
    - cron: "0 0 * * *"
  workflow_dispatch: # Allow manual triggers

jobs:
  scrape-imdb:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Run scraper
        run: | # python
          uv run --with httpx,lxml,cssselect python scrape.py

      - name: Commit and push changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add *.json
          git commit -m "Update IMDb Top 250 data [skip ci]" || exit 0
          git pushCopy to clipboardErrorCopied
```

### [Best Practices](#/scheduled-scraping-with-github-actions?id=best-practices)

1. **Cache Dependencies**: Use GitHub’s caching to speed up package installation
2. **Handle Errors**: Implement retries and error logging
3. **Rate Limiting**: Add delays between requests to avoid overwhelming servers
4. **Data Validation**: Verify scraped data structure before saving
5. **Monitoring**: Set up notifications for workflow failures

### [Tools and Resources](#/scheduled-scraping-with-github-actions?id=tools-and-resources)

* [httpx](https://www.python-httpx.org/): Async HTTP client
* [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
* [GitHub Actions Documentation](https://docs.github.com/en/actions)

### [Video Tutorials](#/scheduled-scraping-with-github-actions?id=video-tutorials)

[![How to run Github Actions on a Schedule](https://i.ytimg.com/vi_webp/eJG86J200nM/sddefault.webp)](https://youtu.be/eJG86J200nM)

[Previous

Web Automation with Playwright](#/web-automation-with-playwright)

[Next

Scraping emarketer.com](#/scraping-emarketer)

---


# File: Scraping_IMDb_with_JavaScript.md

---
title: "Scraping IMDb with JavaScript"
original_url: "https://tds.s-anand.net/#/scraping-imdb-with-javascript?id=scraping-imdb-with-javascript"
downloaded_at: "2025-05-31T21:35:23.779824"
---

[Scraping IMDb with JavaScript](#/scraping-imdb-with-javascript?id=scraping-imdb-with-javascript)
-------------------------------------------------------------------------------------------------

[![Scraping the IMDb with Browser JavaScript](https://i.ytimg.com/vi_webp/YVIKZqZIcCo/sddefault.webp)](https://youtu.be/YVIKZqZIcCo)

You’ll learn how to scrape the [IMDb Top 250 movies](https://www.imdb.com/chart/top) directly in the browser using JavaScript on the Chrome DevTools, covering:

* **Access Developer Tools**: Use F12 or right-click > Inspect to open developer tools in Chrome or Edge.
* **Inspect Elements**: Identify and inspect HTML elements using the Elements tab.
* **Query Selectors**: Use `document.querySelectorAll` and `document.querySelector` to find elements by CSS class.
* **Extract Text Content**: Retrieve text content from elements using JavaScript.
* **Functional Programming**: Apply [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
  and [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
  for concise data processing.
* **Data Structuring**: Collect and format data into an array of arrays.
* **Copying Data**: Use the copy function to transfer data to the clipboard.
* **Convert to Spreadsheet**: Use online tools to convert JSON data to CSV or Excel format.
* **Text Manipulation**: Perform text splitting and cleaning in Excel for final data formatting.

Here are links and references:

* [IMDB Top 250 movies](https://www.imdb.com/chart/top/)
* [Learn about Chrome Devtools](https://developer.chrome.com/docs/devtools/overview/)

[Previous

BBC Weather API with Python](#/bbc-weather-api-with-python)

[Next

Nominatim API with Python](#/nominatim-api-with-python)

---


# File: Scraping_PDFs_with_Tabula.md

---
title: "Scraping PDFs with Tabula"
original_url: "https://tds.s-anand.net/#/scraping-pdfs-with-tabula?id=scraping-pdfs-with-tabula"
downloaded_at: "2025-05-31T21:38:31.104082"
---

[Scraping PDFs with Tabula](#/scraping-pdfs-with-tabula?id=scraping-pdfs-with-tabula)
-------------------------------------------------------------------------------------

[![Scrape PDFs with Tabula Python library](https://i.ytimg.com/vi_webp/yDoKlKyxClQ/sddefault.webp)](https://youtu.be/yDoKlKyxClQ)

You’ll learn how to scrape tables from PDFs using the `tabula` Python library, covering:

* **Import Libraries**: Use Beautiful Soup for URL parsing and Tabula for extracting tables from PDFs.
* **Specify Save Location**: Mount Google Drive to save scraped PDFs.
* **Identify PDF URLs**: Parse the given URL to identify and select all PDF links.
* **Download PDFs**: Loop through identified links, saving each PDF to the specified location.
* **Extract Tables**: Use Tabula to read tabular content from the downloaded PDFs.
* **Control Extraction Area**: Specify page and area coordinates to accurately extract tables, avoiding extraneous text.
* **Save Extracted Data**: Convert the extracted table data into structured formats like CSV for further analysis.

Here are links and references:

* [PDF Scraping - Notebook](https://colab.research.google.com/drive/102Fv2Ji0J4mvao3mCse52E7Th8bZiuyf)
* Learn about the [`tabula` package](https://tabula-py.readthedocs.io/en/latest/tabula.html)
* Learn about the [`pandas` package](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html). [Video](https://youtu.be/vmEHCJofslg)

[Previous

Wikipedia Data with Python](#/wikipedia-data-with-python)

[Next

Convert PDFs to Markdown](#/convert-pdfs-to-markdown)

---


# File: Scraping__Live_Sessions.md

---
title: "Scraping: Live Sessions"
original_url: "https://tds.s-anand.net/#/scraping-live-sessions?id=scraping-live-sessions"
downloaded_at: "2025-05-31T21:39:30.556374"
---

[Scraping: Live Sessions](#/scraping-live-sessions?id=scraping-live-sessions)
-----------------------------------------------------------------------------

[![Intro to Web scraping and HTML](https://i.ytimg.com/vi_webp/cAriusuJsmw/sddefault.webp)](https://youtu.be/cAriusuJsmw)

Fundamentals of web scraping with urllib and BeautifulSoup

[![Fundamentals of web scraping with urllib and BeautifulSoup](https://i.ytimg.com/vi_webp/I3auyTYORTs/sddefault.webp)](https://youtu.be/I3auyTYORTs)

Intermediate web scraping use of cookies

[![Intermediate web scraping use of cookies](https://i.ytimg.com/vi_webp/DryMIxMf3VU/sddefault.webp)](https://youtu.be/DryMIxMf3VU)

XML intro and scraping

[![XML intro and scraping](https://i.ytimg.com/vi_webp/8S_jvsjtaYg/sddefault.webp)](https://youtu.be/8S_jvsjtaYg)

[Previous

Scraping emarketer.com](#/scraping-emarketer)

[Next

5. Data Preparation](#/data-preparation)

---


# File: Scraping_emarketer.com.md

---
title: "Scraping emarketer.com"
original_url: "https://tds.s-anand.net/#/scraping-emarketer?id=scraping-emarketer"
downloaded_at: "2025-05-31T21:35:16.027531"
---

[Scraping emarketer](#/scraping-emarketer?id=scraping-emarketer)
----------------------------------------------------------------

In this live scraping session, we explore a real-life scenario where Straive had to scrape data from emarketer.com for a demo. This is a fairly realistic and representative way of how one might go about scraping a website.

[![Live scraping session](https://i.ytimg.com/vi_webp/ZzUsDE1XjhE/sddefault.webp)](https://youtu.be/ZzUsDE1XjhE)

You’ll learn:

* **Scraping**: How to extract data from web pages, including constructing URLs, fetching page content, and parsing HTML using packages like [`lxml`](https://lxml.de/) and [`httpx`](https://www.python-httpx.org/).
* **Caching**: Implementing a caching strategy to avoid redundant data fetching for efficiency and reliability.
* **Error Handling and Debugging**: Practical tips for troubleshooting, such as using liberal print statements, breakpoints for in-depth debugging, and the concept of “rubber duck debugging” to clarify problems.
* **LLMs**: Benefits of Gemini / ChatGPT for code suggestions and troubleshooting.
* **Real-World Application**: How quick proofs of concept to showcase capabilities to clients, emphasizing practice over theory.

[Previous

Scheduled Scraping with GitHub Actions](#/scheduled-scraping-with-github-actions)

[Next

Scraping: Live Sessions](#/scraping-live-sessions)

---


# File: Scraping_with_Excel.md

---
title: "Scraping with Excel"
original_url: "https://tds.s-anand.net/#/scraping-with-excel?id=scraping-with-excel"
downloaded_at: "2025-05-31T21:33:51.449948"
---

[Scraping with Excel](#/scraping-with-excel?id=scraping-with-excel)
-------------------------------------------------------------------

[![Weather Scraping with Excel: Get the Data](https://i.ytimg.com/vi_webp/OCl6UdpmzRQ/sddefault.webp)](https://youtu.be/OCl6UdpmzRQ)

You’ll learn how to [import tables on the web using Excel](https://support.microsoft.com/en-au/office/import-data-from-the-web-b13eed81-33fe-410d-9247-1747269c28e4), covering:

* **Data Import from Web**: Use the query feature in Excel to scrape data from websites.
* **Establishing Web Connections**: Connect Excel to a web page using a URL.
* **Using Query Editor**: Navigate the query editor to view and manage web data tables.
* **Loading Data**: Load data from the web into Excel for further manipulation.
* **Data Transformation**: Remove unnecessary columns and transform data as needed.
* **Applying Transformations**: Track applied steps in the sequence for reproducibility.
* **Refreshing Data**: Refresh the imported data to get the latest updates from the web.

Here are links used in the video:

* [Chennai Weather Forecast](https://www.timeanddate.com/weather/india/chennai/ext)
* [Excel Scraping Workbook](https://docs.google.com/spreadsheets/d/1a12ApZMD6CTiKRyO4RuauOO8IdYgACRL/view)

If you use Excel on Mac, the process is a bit different. See [Importing External Data Into Excel on Mac](https://youtu.be/PuqVoVNWF20).

[Previous

4. Data Sourcing](#/data-sourcing)

[Next

Scraping with Google Sheets](#/scraping-with-google-sheets)

---


# File: Scraping_with_Google_Sheets.md

---
title: "Scraping with Google Sheets"
original_url: "https://tds.s-anand.net/#/scraping-with-google-sheets?id=scraping-with-google-sheets"
downloaded_at: "2025-05-31T21:38:42.252616"
---

[Scraping with Google Sheets](#/scraping-with-google-sheets?id=scraping-with-google-sheets)
-------------------------------------------------------------------------------------------

[![Scraping with Google Sheets](https://i.ytimg.com/vi_webp/eYQEk7XJM7s/sddefault.webp)](https://youtu.be/eYQEk7XJM7s)

You’ll learn how to [import tables on the web using Google Sheets’s `=IMPORTHTML()` formula](https://support.google.com/docs/answer/3093339?hl=en), covering:

* **Import HTML Formula**: Use =IMPORTHTML(URL, “query”, index) to fetch tables or lists from a web page.
* **Granting Access**: Allow access for formulas to fetch data from external sources.
* **Checking Imported Data**: Verify if the imported table matches the data on the web page.
* **Handling Errors**: Understand common issues and how to resolve them.
* **Sorting Data**: Copy imported data as values and sort it within Google Sheets.
* **Freezing Rows**: Use frozen rows to maintain headers while sorting.
* **Live Formulas**: Learn how web data updates automatically when the source changes.
* **Other Import Functions**: IMPORTXML, IMPORTFEED, IMPORTRANGE, and IMPORTDATA for advanced data fetching options.

Here are links used in the video:

* [Google sheet used in the video](https://docs.google.com/spreadsheets/d/1Qp_YTh1-hJHxjMWE_GofkvLIKgEdKxb6NFImpId3z9o/view)
* [`IMPORTHTML()`](https://support.google.com/docs/answer/3093339)
* [`IMPORTXML()`](https://support.google.com/docs/answer/3093342)
* [Demographics of India](https://en.wikipedia.org/wiki/Demographics_of_India)
* [List of highest grossing Indian films](https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films)

[Previous

Scraping with Excel](#/scraping-with-excel)

[Next

Crawling with the CLI](#/crawling-cli)

---


# File: Serverless_hosting__Vercel.md

---
title: "Serverless hosting: Vercel"
original_url: "https://tds.s-anand.net/#/vercel?id=serverless-hosting-vercel"
downloaded_at: "2025-05-31T21:38:44.422893"
---

[Serverless hosting: Vercel](#/vercel?id=serverless-hosting-vercel)
-------------------------------------------------------------------

Serverless platforms let you rent a single function instead of an entire machine. They’re perfect for small web tools that *don’t need to run all the time*. Here are some common real-life uses:

* A contact form that emails you when someone wants to hire you (runs for 2-3 seconds, a few times per day)
* A tool that converts uploaded photos to black and white (runs for 5-10 seconds when someone uploads a photo)
* A chatbot that answers basic questions about your business hours (runs for 1-2 seconds per question)
* A newsletter sign-up that adds emails to your mailing list (runs for 1 second per sign-up)
* A webhook that posts your Etsy sales to Discord (runs for 1 second whenever you make a sale)

You only pay when someone uses your tool, and the platform automatically handles busy periods. For example, if 100 people fill out your contact form at once, the platform creates 100 temporary copies of your code to handle them all. When they’re done, these copies disappear. It’s cheaper than running a full-time server because you’re not paying for the time when no one is using your tool - most tools are idle 95% of the time!

Rather than writing a full program, serverless platforms let you write functions. These functions are called via HTTP requests. They run in a cloud environment and are scaled up and down automatically. But this means you write programs in a different style. For example:

* You can’t `pip install` packages - you have to use `requirements.txt`
* You can’t read or write files from the file system - you can only use APIs.
* You can’t run commands (e.g. `subprocess.run()`)

[Vercel](https://vercel.com/) is a cloud platform optimized for frontend frameworks and serverless functions. Vercel is tightly integrated with GitHub. Pushing to your repository automatically triggers new deployments.

Here’s a [quickstart](https://vercel.com/docs/functions/runtimes/python). [Sign-up with Vercel](https://vercel.com/signup). Create an empty `git` repo with this `api/index.py` file.

To deploy a FastAPI app, add a `requirements.txt` file with `fastapi` as a dependency.

```
fastapiCopy to clipboardErrorCopied
```

Add your FastAPI code to a file, e.g. `main.py`.

```
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}Copy to clipboardErrorCopied
```

Add a `vercel.json` file to the root of your repository.

```
{
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}Copy to clipboardErrorCopied
```

On the command line, run:

* `npx vercel` to deploy a test version
* `npx vercel --prod` to deploy to production

**Environment Variables**. Use `npx vercel env add` to add environment variables. In your code, use `os.environ.get('SECRET_KEY')` to access them.

### [Videos](#/vercel?id=videos)

[![Vercel Product Walkthrough](https://i.ytimg.com/vi_webp/sPmat30SE4k/sddefault.webp)](https://youtu.be/sPmat30SE4k)

[![Deploy FastAPI on Vercel | Quick and Easy Tutorial](https://i.ytimg.com/vi_webp/8R-cetf_sZ4/sddefault.webp)](https://youtu.be/8R-cetf_sZ4)

[Previous

Notebooks: Google Colab](#/colab)

[Next

CI/CD: GitHub Actions](#/github-actions)

---


# File: Splitting_Text_in_Excel.md

---
title: "Splitting Text in Excel"
original_url: "https://tds.s-anand.net/#/splitting-text-in-excel?id=splitting-text-in-excel"
downloaded_at: "2025-05-31T21:39:21.126288"
---

[Splitting Text in Excel](#/splitting-text-in-excel?id=splitting-text-in-excel)
-------------------------------------------------------------------------------

[![Convert text-to-columns in Excel](https://i.ytimg.com/vi_webp/fQeADnqiOAg/sddefault.webp)](https://youtu.be/fQeADnqiOAg)

You’ll learn how to transform a single-column data set into multiple, organized columns based on specific delimiters using the “Text to Columns” feature.

Here are links used in the video:

* [US Senate Legislation - Votes](https://www.senate.gov/legislative/votes_new.htm)

[Previous

Data Transformation in Excel](#/data-transformation-in-excel)

[Next

Data Aggregation in Excel](#/data-aggregation-in-excel)

---


# File: Spreadsheet__Excel,_Google_Sheets.md

---
title: "Spreadsheet: Excel, Google Sheets"
original_url: "https://tds.s-anand.net/#/spreadsheets?id=spreadsheet-excel-google-sheets"
downloaded_at: "2025-05-31T21:38:49.861983"
---

[Spreadsheet: Excel, Google Sheets](#/spreadsheets?id=spreadsheet-excel-google-sheets)
--------------------------------------------------------------------------------------

You’ll use spreadsheets for data cleaning and exploration. The most popular spreadsheet program is [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) followed by [Google Sheets](https://www.google.com/sheets/about/).

You may be already familiar with these. If not, make sure to learn the basics of both.

Go through the [**Microsoft Excel** video training](https://support.microsoft.com/en-us/office/excel-video-training-9bc05390-e94c-46af-a5b3-d7c22f6990bb) and make sure you cover:

* [Intro to Excel](https://support.microsoft.com/en-us/office/create-a-new-workbook-ae99f19b-cecb-4aa0-92c8-7126d6212a83)
* [Rows & columns](https://support.microsoft.com/en-us/office/insert-or-delete-rows-and-columns-6f40e6e4-85af-45e0-b39d-65dd504a3246)
* [Cells](https://support.microsoft.com/en-us/office/move-or-copy-cells-and-cell-contents-803d65eb-6a3e-4534-8c6f-ff12d1c4139e)
* [Formatting](https://support.microsoft.com/en-us/office/available-number-formats-in-excel-0afe8f52-97db-41f1-b972-4b46e9f1e8d2)
* [Formulas & Functions](https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173)
* [Tables](https://support.microsoft.com/en-us/office/create-and-format-tables-e81aa349-b006-4f8a-9806-5af9df0ac664)
* [PivotTables](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576)

Watch this video for an introduction to **Google Sheets** (49 min):

[![Google Sheets Tutorial for Beginners (49 min)](https://i.ytimg.com/vi_webp/TENAbUa-R-w/sddefault.webp)](https://youtu.be/TENAbUa-R-w)

[Previous

AI Terminal Tools: llm](#/llm)

[Next

Database: SQLite](#/sqlite)

---


# File: Static_hosting__GitHub_Pages.md

---
title: "Static hosting: GitHub Pages"
original_url: "https://tds.s-anand.net/#/github-pages?id=static-hosting-github-pages"
downloaded_at: "2025-05-31T21:39:47.394679"
---

[Static hosting: GitHub Pages](#/github-pages?id=static-hosting-github-pages)
-----------------------------------------------------------------------------

[GitHub Pages](https://pages.github.com/) is a free hosting service that turns your GitHub repository directly into a static website whenever you push it. This is useful for sharing analysis results, data science portfolios, project documentation, and more.

Common Operations:

```
# Create a new GitHub repo
mkdir my-site
cd my-site
git init

# Add your static content
echo "<h1>My Site</h1>" > index.html

# Push to GitHub
git add .
git commit -m "feat(pages): initial commit"
git push origin main

# Enable GitHub Pages from the main branch on the repo settings pageCopy to clipboardErrorCopied
```

Best Practices:

1. **Keep it small**
   * [Optimize images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/Multimedia). Prefer SVG over WEBP over 8-bit PNG.
   * [Preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload) critical assets like stylesheets
   * Avoid committing large files like datasets, videos, etc. directly. Explore [Git LFS](https://git-lfs.github.com/) instead.

Tools:

* [GitHub Desktop](https://desktop.github.com/): GUI for Git operations
* [GitHub CLI](https://cli.github.com/): Command line interface
* [GitHub Actions](https://github.com/features/actions): Automation

[![Host a website using GitHub Pages](https://i.ytimg.com/vi_webp/WqOXxoGSpbs/sddefault.webp)](https://youtube.com/shorts/WqOXxoGSpbs)

[![Deploy your first GitHub Pages Website](https://i.ytimg.com/vi_webp/sT_zXIX3ZA0/sddefault.webp)](https://youtu.be/sT_zXIX3ZA0)

[Previous

Images: Compression](#/image-compression)

[Next

Notebooks: Google Colab](#/colab)

---


# File: TDS_GPT_Reviewer.md

---
title: "TDS GPT Reviewer"
original_url: "https://tds.s-anand.net/#/tds-gpt-reviewer?id=content-creation-prompts"
downloaded_at: "2025-05-31T21:39:29.502552"
---

[TDS GPT Reviewer](#/tds-gpt-reviewer?id=tds-gpt-reviewer)
==========================================================

After the later parts of this course’s contents were written, we ran it through a [Technical Content Reviewer GPT](https://chatgpt.com/g/g-6777656ed3b8819187b6f17d9f343853-technical-content-reviewer).

Take a look at the GPT’s instructions. These were generated by the [OpenAI Prompt Generation](https://platform.openai.com/docs/guides/prompt-generation) tool.

```
As a **Content Reviewer** for a high school–level course on Tools in Data Science, your job is to evaluate provided content (such as text, code snippets, or references) with a focus on correctness, clarity, and conciseness, and offer actionable feedback for improvement.

1. **Check for Correctness and Consistency**
   - Verify technical and factual accuracy.
   - Ensure internal consistency without contradictions.
2. **Check for Clarity and Approachability**
   - Ensure content is understandable for a high school student with limited prior knowledge.
   - Identify and simplify jargon or advanced concepts.
3. **Check for Conciseness**
   - Assess if content is direct and free of unnecessary verbosity.
   - Identify areas for streamlining to enhance readability.
4. **Provide Feedback for Improvement**
   - Offer actionable suggestions for fixing, clarifying, or reorganizing content.
   - Propose alternative phrasing if text is vague, complex, or verbose.

# Steps

1. Carefully read the entire content before forming conclusions.
2. List factual inconsistencies or missing details causing confusion.
3. Suggest simpler terms or analogies for complex language.
4. Point out unnecessary repetition or filler text.
5. Provide direct examples of how to improve the highlighted issues.

# Output Format

Respond using **Markdown** with the following structure:

1. **Summary of Findings**
   - A concise paragraph outlining overall strengths and weaknesses.
2. **Detailed Review**
   - **Correctness and Consistency**: Note factual errors or inconsistencies, suggesting corrections.
   - **Clarity and Approachability**: Identify overly advanced or unclear sections, offering simpler alternatives.
   - **Conciseness**: Highlight long or repetitive sections with suggestions for tightening the text.
3. **Actionable Improvement Suggestions**
   - Provide specific sentences, bullet points, or rewritten examples to illustrate improvements.

# Notes

- Maintain a constructive review tone, not content generation.
- Even if content is perfect, confirm with suggestions for minor improvements (e.g., adding an example or clarifying a subtle point).Copy to clipboardErrorCopied
```

[Content creation prompts](#/tds-gpt-reviewer?id=content-creation-prompts)
--------------------------------------------------------------------------

In addition, here are a few prompts used to create the content:

1. **Video summaries**. Transcribe the video via [YouTube Transcript](https://youtubetranscript.com/) or Whisper. Then: `Summarize this video transcript crisply for a high school student.`

[Previous

TDS TA Instructions](#/tds-ta-instructions)

[Next

LLM Sentiment Analysis](#/llm-sentiment-analysis)

---


# File: TDS_TA_Instructions.md

---
title: "TDS TA Instructions"
original_url: "https://tds.s-anand.net/#/tds-ta-instructions?id=tds-ta-instructions"
downloaded_at: "2025-05-31T21:35:11.622685"
---

[TDS TA Instructions](#/tds-ta-instructions?id=tds-ta-instructions)
===================================================================

The TDS TA is a virtual assistant that helps you with your doubts.

It has been trained on course content created as follows:

```
# Clone the course repository
git clone https://github.com/sanand0/tools-in-data-science-public.git
cd tools-in-data-science-public

# Create a prompt file for the TA
PYTHONUTF8=1 uvx files-to-prompt --cxml *.md -o tds-content.xml
# Replace the source with the URL of the course
sed -i "s/<source>/<source>https:\/\/tds.s-anand.net\/#\//g" tds-content.xmlCopy to clipboardErrorCopied
```

Additionally, we visit each of the evaluation links on <https://exam.sanand.workers.dev/>, [copy it as Markdown](https://tools.s-anand.net/page2md/), and add it to the content, called `ga1.md`, `ga2.md`, etc.

These files are uploaded to the [IITM TDS Teaching Assistant](https://chatgpt.com/g/g-mZqKVxKDx-iitm-tds-teaching-assistant).

Take a look at the GPT’s instructions. These were generated by the [OpenAI Prompt Generation](https://platform.openai.com/docs/guides/prompt-generation) tool.

```
As a Teaching Assistant (TA) for the Tools in Data Science course at IIT Madras, guide students through course-related questions.

1. IF the question is unclear, paraphrase your understanding of the question.
2. Cite all relevant sections from `tds-content.xml` or `ga*.md`. Begin with: "According to [this reference](https://tds.s-anand.net/#/...), ...". Cite ONLY from the relevant <source>. ALWAYS cite verbatim. Mention ALL material relevant to the question.
3. Search online for additional answers. Share results WITH CITATION LINKS.
4. Think step-by-step. Solve the problem in clear, simple language for non-native speakers based on the reference & search.
5. Follow-up: Ask thoughtful questions to help students explore and learn.Copy to clipboardErrorCopied
```

[Previous

Prompt engineering](#/prompt-engineering)

[Next

TDS GPT Reviewer](#/tds-gpt-reviewer)

---


# File: Terminal__Bash.md

---
title: "Terminal: Bash"
original_url: "https://tds.s-anand.net/#/bash?id=terminal-bash"
downloaded_at: "2025-05-31T21:36:42.255936"
---

[Terminal: Bash](#/bash?id=terminal-bash)
-----------------------------------------

UNIX shells are the de facto standard in the data science world and [Bash](https://www.gnu.org/software/bash/) is the most popular.
This is available by default on Mac and Linux.

On Windows, install [Git Bash](https://git-scm.com/downloads) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to get a UNIX shell.

Watch this video to install WSL (12 min).

[![How to Install Ubuntu on Windows 10 (WSL) (12 min)](https://i.ytimg.com/vi_webp/X-DHaQLrBi8/sddefault.webp)](https://youtu.be/X-DHaQLrBi8)

Watch this video to understand the basics of Bash and UNIX shell commands (75 min).

[![Beginner's Guide to the Bash Terminal (75 min)](https://i.ytimg.com/vi_webp/oxuRxtrO2Ag/sddefault.webp)](https://youtu.be/oxuRxtrO2Ag)

Essential Commands:

```
# File Operations
ls -la               # List all files with details
cd path/to/dir       # Change directory
pwd                  # Print working directory
cp source dest       # Copy files
mv source dest       # Move/rename files
rm -rf dir           # Remove directory recursively

# Text Processing
grep "pattern" file  # Search for pattern
sed 's/old/new/' f   # Replace text
awk '{print $1}' f   # Process text by columns
cat file | wc -l     # Count lines

# Process Management
ps aux               # List processes
kill -9 PID          # Force kill process
top                  # Monitor processes
htop                 # Interactive process viewer

# Network
curl url             # HTTP requests
wget url             # Download files
nc -zv host port     # Test connectivity
ssh user@host        # Remote login

# Count unique values in CSV column
cut -d',' -f1 data.csv | sort | uniq -c

# Quick data analysis
awk -F',' '{sum+=$2} END {print sum/NR}' data.csv  # Average
sort -t',' -k2 -n data.csv | head                  # Top 10

# Monitor log in real-time
tail -f log.txt | grep --color 'ERROR'Copy to clipboardErrorCopied
```

Bash Scripting Essentials:

```
#!/bin/bash

# Variables
NAME="value"
echo $NAME

# Loops
for i in {1..5}; do
    echo $i
done

# Conditionals
if [ -f "file.txt" ]; then
    echo "File exists"
fi

# Functions
process_data() {
    local input=$1
    echo "Processing $input"
}Copy to clipboardErrorCopied
```

Productivity Tips:

1. **Command History**

   ```
   history         # Show command history
   Ctrl+R         # Search history
   !!             # Repeat last command
   !$             # Last argumentCopy to clipboardErrorCopied
   ```
2. **Directory Navigation**

   ```
   pushd dir      # Push directory to stack
   popd           # Pop directory from stack
   cd -           # Go to previous directoryCopy to clipboardErrorCopied
   ```
3. **Job Control**

   ```
   command &      # Run in background
   Ctrl+Z         # Suspend process
   bg             # Resume in background
   fg             # Resume in foregroundCopy to clipboardErrorCopied
   ```
4. **Useful Aliases** - typically added to `~/.bashrc`

   ```
   alias ll='ls -la'
   alias gs='git status'
   alias jupyter='jupyter notebook'
   alias activate='source venv/bin/activate'Copy to clipboardErrorCopied
   ```

[Previous

JSON](#/json)

[Next

AI Terminal Tools: llm](#/llm)

---


# File: Tools_in_Data_Science.md

---
title: "Tools in Data Science"
original_url: "https://tds.s-anand.net/#/../function-calling?id=how-to-define-functions"
downloaded_at: "2025-05-31T21:45:17.142743"
---

[Function Calling with OpenAI](#/../function-calling?id=function-calling-with-openai)
-------------------------------------------------------------------------------------

[Function Calling](https://platform.openai.com/docs/guides/function-calling) allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and AI assistants that need to interact with your backend systems.

OpenAI supports [Function Calling](https://platform.openai.com/docs/guides/function-calling) – a way for LLMs to suggest what functions to call and how.

[![OpenAI Function Calling - Full Beginner Tutorial](https://i.ytimg.com/vi_webp/aqdWSYWC_LI/sddefault.webp)](https://youtu.be/aqdWSYWC_LI)

Here’s a minimal example using Python and OpenAI’s function calling that identifies the weather in a given location.

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///

import httpx
import os
from typing import Dict, Any


def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": user_input}],
            "tools": tools,
            "tool_choice": "auto",
        },
    )
    return response.json()["choices"][0]["message"]


WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name or coordinates"}
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}

if __name__ == "__main__":
    response = query_gpt("What is the weather in San Francisco?", [WEATHER_TOOL])
    print([tool_call["function"] for tool_call in response["tool_calls"]])Copy to clipboardErrorCopied
```

### [How to define functions](#/../function-calling?id=how-to-define-functions)

The function definition is a [JSON schema](https://json-schema.org/) with a few OpenAI specific properties.
See the [Supported schemas](https://platform.openai.com/docs/guides/structured-outputs#supported-schemas).

Here’s an example of a function definition for scheduling a meeting:

```
MEETING_TOOL = {
    "type": "function",
    "function": {
        "name": "schedule_meeting",
        "description": "Schedule a meeting room for a specific date and time",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Meeting date in YYYY-MM-DD format"
                },
                "time": {
                    "type": "string",
                    "description": "Meeting time in HH:MM format"
                },
                "meeting_room": {
                    "type": "string",
                    "description": "Name of the meeting room"
                }
            },
            "required": ["date", "time", "meeting_room"],
            "additionalProperties": False
        },
        "strict": True
    }
}Copy to clipboardErrorCopied
```

### [How to define multiple functions](#/../function-calling?id=how-to-define-multiple-functions)

You can define multiple functions by passing a list of function definitions to the `tools` parameter.

Here’s an example of a list of function definitions for handling employee expenses and calculating performance bonuses:

```
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_expense_balance",
            "description": "Get expense balance for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    }
                },
                "required": ["employee_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_performance_bonus",
            "description": "Calculate yearly performance bonus for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    },
                    "current_year": {
                        "type": "integer",
                        "description": "Year to calculate bonus for"
                    }
                },
                "required": ["employee_id", "current_year"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]Copy to clipboardErrorCopied
```

Best Practices:

1. **Use Strict Mode**
   * Always set `strict: True` to ensure valid function calls
   * Define all required parameters
   * Set `additionalProperties: False`
2. **Use tool choice**
   * Set `tool_choice: "required"` to ensure that the model will always call one or more tools
   * The default is `tool_choice: "auto"` which means the model will choose a tool only if appropriate
3. **Clear Descriptions**
   * Write detailed function and parameter descriptions
   * Include expected formats and units
   * Mention any constraints or limitations
4. **Error Handling**
   * Validate function inputs before execution
   * Return clear error messages
   * Handle missing or invalid parameters

---


# File: Topic_modeling.md

---
title: "Topic modeling"
original_url: "https://tds.s-anand.net/#/topic-modeling?id=topic-modeling"
downloaded_at: "2025-05-31T21:39:35.840713"
---

[Topic Modeling](#/topic-modeling?id=topic-modeling)
----------------------------------------------------

[![LLM Topic Modeling](https://i.ytimg.com/vi_webp/eQUNhq91DlI/sddefault.webp)](https://youtu.be/eQUNhq91DlI)

You’ll learn to use text embeddings to find text similarity and use that to create topics automatically from text, covering:

* **Embeddings**: How large language models convert text into numerical representations.
* **Similarity Measurement**: Understanding how similar embeddings indicate similar meanings.
* **Embedding Visualization**: Using tools like Tensorflow Projector to visualize embedding spaces.
* **Embedding Applications**: Using embeddings for tasks like classification and clustering.
* **OpenAI Embeddings**: Using OpenAI’s API to generate embeddings for text.
* **Model Comparison**: Exploring different embedding models and their strengths and weaknesses.
* **Cosine Similarity**: Calculating cosine similarity between embeddings for more reliable similarity measures.
* **Embedding Cost**: Understanding the cost of generating embeddings using OpenAI’s API.
* **Embedding Range**: Understanding the range of values in embeddings and their significance.

Here are the links used in the video:

* [Jupyter Notebook](https://colab.research.google.com/drive/15L075RLrwXkxa29EGT-1sNm_dqJRBTe_)
* [Tensorflow projector](https://projector.tensorflow.org/)
* [Embeddings guide](https://platform.openai.com/docs/guides/embeddings)
* [Embeddings reference](https://platform.openai.com/docs/api-reference/embeddings)
* [Clustering on scikit-learn](https://scikit-learn.org/stable/modules/clustering.html)
* [Massive text embedding leaderboard (MTEB)](https://huggingface.co/spaces/mteb/leaderboard)
* [`gte-large-en-v1.5` embedding model](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)
* [Embeddings similarity threshold](https://www.s-anand.net/blog/embeddings-similarity-threshold/)

[Previous

Multimodal Embeddings](#/multimodal-embeddings)

[Next

Vector databases](#/vector-databases)

---


# File: Transforming_Images.md

---
title: "Transforming Images"
original_url: "https://tds.s-anand.net/#/transforming-images?id=image-processing-with-imagemagick"
downloaded_at: "2025-05-31T21:38:41.161445"
---

[Transforming Images](#/transforming-images?id=transforming-images)
-------------------------------------------------------------------

### [Image Processing with PIL (Pillow)](#/transforming-images?id=image-processing-with-pil-pillow)

[![Python Tutorial: Image Manipulation with Pillow (16 min)](https://i.ytimg.com/vi_webp/6Qs3wObeWwc/sddefault.webp)](https://youtu.be/6Qs3wObeWwc)

[Pillow](https://python-pillow.org/) is Python’s leading library for image processing, offering powerful tools for editing, analyzing, and generating images. It handles various formats (PNG, JPEG, GIF, etc.) and provides operations from basic resizing to complex filters.

Here’s a minimal example showing common operations:

```
# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow"]
# ///

from PIL import Image, ImageEnhance, ImageFilter

async def process_image(path: str) -> Image.Image:
    """Process an image with basic enhancements."""
    with Image.open(path) as img:
        # Convert to RGB to ensure compatibility
        img = img.convert('RGB')

        # Resize maintaining aspect ratio
        img.thumbnail((800, 800))

        # Apply enhancements
        img = (ImageEnhance.Contrast(img)
               .enhance(1.2))

        return img.filter(ImageFilter.SHARPEN)

if __name__ == "__main__":
    import asyncio
    img = asyncio.run(process_image("input.jpg"))
    img.save("output.jpg", quality=85)Copy to clipboardErrorCopied
```

Key features and techniques you’ll learn:

* **Image Loading and Saving**: Handle various formats with automatic conversion
* **Basic Operations**: Resize, rotate, crop, and flip images
* **Color Manipulation**: Adjust brightness, contrast, and color balance
* **Filters and Effects**: Apply blur, sharpen, and other visual effects
* **Drawing**: Add text, shapes, and overlays to images
* **Batch Processing**: Handle multiple images efficiently
* **Memory Management**: Process large images without memory issues

### [Basic Image Operations](#/transforming-images?id=basic-image-operations)

Common operations for resizing, cropping, and rotating images:

```
from PIL import Image

async def transform_image(
    path: str,
    size: tuple[int, int],
    rotation: float = 0
) -> Image.Image:
    """Transform image with basic operations."""
    with Image.open(path) as img:
        # Resize with anti-aliasing
        img = img.resize(size, Image.LANCZOS)

        # Rotate around center
        if rotation:
            img = img.rotate(rotation, expand=True)

        # Auto-crop empty edges
        img = img.crop(img.getbbox())

        return imgCopy to clipboardErrorCopied
```

### [Color and Enhancement](#/transforming-images?id=color-and-enhancement)

Adjust image appearance with built-in enhancement tools:

```
from PIL import ImageEnhance, ImageOps

async def enhance_image(
    img: Image.Image,
    brightness: float = 1.0,
    contrast: float = 1.0,
    saturation: float = 1.0
) -> Image.Image:
    """Apply color enhancements to image."""
    enhancers = [
        (ImageEnhance.Brightness, brightness),
        (ImageEnhance.Contrast, contrast),
        (ImageEnhance.Color, saturation)
    ]

    for Enhancer, factor in enhancers:
        if factor != 1.0:
            img = Enhancer(img).enhance(factor)

    return imgCopy to clipboardErrorCopied
```

### [Filters and Effects](#/transforming-images?id=filters-and-effects)

Apply visual effects and filters to images:

```
from PIL import ImageFilter

def apply_effects(img: Image.Image) -> Image.Image:
    """Apply various filters and effects."""
    effects = {
        'blur': ImageFilter.GaussianBlur(radius=2),
        'sharpen': ImageFilter.SHARPEN,
        'edge': ImageFilter.FIND_EDGES,
        'emboss': ImageFilter.EMBOSS
    }

    return {name: img.filter(effect)
            for name, effect in effects.items()}Copy to clipboardErrorCopied
```

### [Drawing and Text](#/transforming-images?id=drawing-and-text)

Add text, shapes, and overlays to images:

```
from PIL import Image, ImageDraw, ImageFont

async def add_watermark(
    img: Image.Image,
    text: str,
    font_size: int = 30
) -> Image.Image:
    """Add text watermark to image."""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Position text at bottom-right
    x = img.width - text_width - 10
    y = img.height - text_height - 10

    # Add text with shadow
    draw.text((x+2, y+2), text, font=font, fill='black')
    draw.text((x, y), text, font=font, fill='white')

    return imgCopy to clipboardErrorCopied
```

### [Memory-Efficient Processing](#/transforming-images?id=memory-efficient-processing)

Handle large images without loading them entirely into memory:

```
from PIL import Image
import os

async def process_large_images(
    input_dir: str,
    output_dir: str,
    max_size: tuple[int, int]
) -> None:
    """Process multiple large images efficiently."""
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with Image.open(input_path) as img:
            # Process in chunks using thumbnail
            img.thumbnail(max_size)
            img.save(output_path, optimize=True)Copy to clipboardErrorCopied
```

Practice with these resources:

* [Pillow Documentation](https://pillow.readthedocs.io/): Complete API reference
* [Python Image Processing Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/): In-depth guide
* [Sample Images Dataset](https://www.kaggle.com/datasets/lamsimon/celebs): Test images for practice

Watch these tutorials for hands-on demonstrations:

[![Image Processing Tutorial for beginners with Python PIL in 30 mins](https://i.ytimg.com/vi_webp/dkp4wUhCwR4/sddefault.webp)](https://youtu.be/dkp4wUhCwR4)

### [Image Processing with ImageMagick](#/transforming-images?id=image-processing-with-imagemagick)

[ImageMagick](https://imagemagick.org/) is a powerful command-line tool for image manipulation, offering features beyond what’s possible with Python libraries. It’s particularly useful for:

* Batch processing large image collections
* Complex image transformations
* High-quality format conversion
* Creating image thumbnails
* Adding text and watermarks

Basic Operations:

```
# Format conversion
convert input.png output.jpg

# Resize image (maintains aspect ratio)
convert input.jpg -resize 800x600 output.jpg

# Compress image quality
convert input.jpg -quality 85 output.jpg

# Rotate image
convert input.jpg -rotate 90 output.jpgCopy to clipboardErrorCopied
```

Common Data Science Tasks:

```
# Create thumbnails for dataset preview
convert input.jpg -thumbnail 200x200^ -gravity center -extent 200x200 thumb.jpg

# Normalize image for ML training
convert input.jpg -normalize -strip output.jpg

# Extract dominant colors
convert input.jpg -colors 5 -unique-colors txt:

# Generate image statistics
identify -verbose input.jpg | grep -E "Mean|Standard|Kurtosis"Copy to clipboardErrorCopied
```

Batch Processing:

```
# Convert all images in a directory
mogrify -format jpg *.png

# Resize multiple images
mogrify -resize 800x600 -path output/ *.jpg

# Add watermark to images
for f in *.jpg; do
    convert "$f" -gravity southeast -draw "text 10,10 'Copyright'" "watermarked/$f"
doneCopy to clipboardErrorCopied
```

Advanced Features:

```
# Apply image effects
convert input.jpg -blur 0x3 blurred.jpg
convert input.jpg -sharpen 0x3 sharp.jpg
convert input.jpg -edge 1 edges.jpg

# Create image montage
montage *.jpg -geometry 200x200+2+2 montage.jpg

# Extract image channels
convert input.jpg -separate channels_%d.jpg

# Composite images
composite overlay.png -gravity center base.jpg output.jpgCopy to clipboardErrorCopied
```

Watch this ImageMagick tutorial (16 min):

[![ImageMagick Introduction (16 min)](https://i.ytimg.com/vi_webp/wjcBOoReYc0/sddefault.webp)](https://youtu.be/wjcBOoReYc0)

Tools:

* [Fred’s ImageMagick Scripts](http://www.fmwconcepts.com/imagemagick/): Useful script collection
* [ImageMagick Online Studio](https://magickstudio.imagemagick.org/): Visual command builder

Tips:

1. Use `-strip` to remove metadata and reduce file size
2. Monitor memory usage with `-limit memory 1GB`
3. Use `-define` for format-specific options
4. Process in parallel with `-parallel`
5. Use `-monitor` to track progress

Error Handling:

```
# Check image validity
identify -regard-warnings input.jpg

# Get detailed error information
convert input.jpg output.jpg 2>&1 | grep -i "error"

# Set resource limits
convert -limit memory 1GB -limit map 2GB input.jpg output.jpgCopy to clipboardErrorCopied
```

For Python integration:

```
# /// script
# requires-python = ">=3.9"
# dependencies = ["Wand"]
# ///

from wand.image import Image

async def process_image(path: str) -> None:
    """Process image with ImageMagick via Wand."""
    with Image(filename=path) as img:
        # Basic operations
        img.resize(800, 600)
        img.normalize()

        # Apply effects
        img.sharpen(radius=0, sigma=3)

        # Save with compression
        img.save(filename='output.jpg')Copy to clipboardErrorCopied
```

Note: Always install ImageMagick before using the Wand Python binding.

[Previous

Data Transformation with dbt](#/dbt)

[Next

Extracting Audio and Transcripts](#/extracting-audio-and-transcripts)

---


# File: Tunneling__ngrok.md

---
title: "Tunneling: ngrok"
original_url: "https://tds.s-anand.net/#/ngrok?id=tunneling-ngrok"
downloaded_at: "2025-05-31T21:38:37.790607"
---

[Tunneling: ngrok](#/ngrok?id=tunneling-ngrok)
----------------------------------------------

[Ngrok](https://ngrok.com/) is a tool that creates secure tunnels to your localhost, making your local development server accessible to the internet. It’s essential for testing webhooks, sharing work in progress, or debugging applications in production-like environments.

[![ngrok in 60 seconds](https://i.ytimg.com/vi_webp/dfMdLGZLXSg/sddefault.webp)](https://youtu.be/dfMdLGZLXSg)

Run the command `uvx ngrok http 8000` to create a tunnel to your local server on port 8000. This generates a public URL that you can share with others.

To get started, log into `ngrok.com` and [get an authtoken from the dashboard](https://dashboard.ngrok.com/get-started/your-authtoken). Copy it. Then run:

```
ngrok config add-authtoken $YOUR_AUTHTOKENCopy to clipboardErrorCopied
```

Now you can forward any local port to the internet. For example:

```
# Start a local server on port 8000
uv run -m http.server 8000

# Start HTTP tunnel
uvx ngrok http 8000Copy to clipboardErrorCopied
```

Here are useful things you can do with `ngrok http`:

* `ngrok http file://.` to serve local files
* `--response-header-add "Access-Control-Allow-Origin: *"` to enable CORS
* `--oauth google --oauth-client-id $CLIENT_ID --oauth-client-secret $SECRET --oauth-allow-domain example.com --oauth-allow-email user@example.org` to restrict users to @example.com and [user@example.org](mailto:user@example.org) using Google Auth
* `--ua-filter-deny ".*bot$"` to reject user agents ending with `bot`

[Previous

DevContainers: GitHub Codespaces](#/github-codespaces)

[Next

CORS](#/cors)

---


# File: Unicode.md

---
title: "Unicode"
original_url: "https://tds.s-anand.net/#/unicode?id=unicode"
downloaded_at: "2025-05-31T21:38:32.219619"
---

[Unicode](#/unicode?id=unicode)
-------------------------------

Ever noticed when you copy-paste some text and get garbage symbols? Or see garbage when you load a CSV file? This video explains why. It covers how computers store text (called character encoding) and why it sometimes goes wonky.

Learn about ASCII (the original 7-bit encoding system that could only handle 128 characters), why that wasn’t enough for global languages, and how modern solutions like Unicode save the day by letting us use any character from any language.

Some programs try to guess encodings (sometimes badly!). A signature called BOM (Byte Order Mark)helps computers know exactly how to read text files correctly.

Learn how Unicode, UTF-8 and character encoding works. This is a common gotcha when building apps that handle international text - something bootcamps often skip but developers and data scientists regularly face in the real world.

Unicode is fundamental for data scientists working with international data. Here are key concepts you need to understand:

* **Character Encodings**: Different ways to represent text in computers
  + ASCII (7-bit): Limited to 128 characters, English-only
  + UTF-8: Variable-width encoding, backwards compatible with ASCII
  + UTF-16: Fixed-width encoding, used in Windows and Java
  + UTF-32: Fixed-width encoding, memory inefficient but simple

Common encoding issues you’ll encounter:

```
# Reading files with explicit encoding
with open('file.txt', encoding='utf-8') as f:
    text = f.read()

# Handling encoding errors
import pandas as pd
df = pd.read_csv('data.csv', encoding='utf-8', errors='replace')

# Detecting file encoding
import chardet
with open('unknown.txt', 'rb') as f:
    result = chardet.detect(f.read())
print(result['encoding'])Copy to clipboardErrorCopied
```

[![Code Pages, Character Encoding, Unicode, UTF-8 and the BOM - Computer Stuff They Didn't Teach You #2 (17 min)](https://i.ytimg.com/vi_webp/jeIBNn5Y5fI/sddefault.webp)](https://youtu.be/jeIBNn5Y5fI)

[Previous

JavaScript tools: npx](#/npx)

[Next

Browser: DevTools](#/devtools)

---


# File: Vector_databases.md

---
title: "Vector databases"
original_url: "https://tds.s-anand.net/#/vector-databases?id=lancedb"
downloaded_at: "2025-05-31T21:40:04.242071"
---

[Vector Databases](#/vector-databases?id=vector-databases)
----------------------------------------------------------

Vector databases are specialized databases that store and search vector embeddings efficiently.

Use vector databases when your embeddings exceed available memory or when you want it run fast at scale. (This is important. If your code runs fast and fits in memory, you **DON’T** need a vector database. You can can use `numpy` for these tasks.)

Vector databases are an evolving space.

The first generation of vector databases were written in C and typically used an algorithm called [HNSW](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world) (a way to approximately find the nearest neighbor). Some popular ones are:

* **[chroma 19,637 ⭐ May 2025](https://github.com/chroma-core/chroma)**
* **[qdrant 23,341 ⭐ May 2025](https://github.com/qdrant/qdrant)**
* **[lancedb 6,327 ⭐ May 2025](https://github.com/lancedb/lancedb)**
* **[faiss 34,684 ⭐ May 2025](https://github.com/facebookresearch/faiss)**
* **[milvus 34,476 ⭐ May 2025](https://github.com/milvus-io/milvus)**
* **[weaviate 13,222 ⭐ May 2025](https://github.com/weaviate/weaviate)**

In addition, most relational databases now support vector search. For example:

* **[DuckDB](https://duckdb.org/)**: Supports vector search with [`vss`](https://duckdb.org/docs/extensions/vss.html).
* **[SQLite](https://www.sqlite.org/)**: Supports vector search with [`sqlite-vec`](https://github.com/asg017/sqlite-vec).
* **[PostgreSQL](https://www.postgresql.org/)**: Supports vector search with [`pgvector`](https://github.com/pgvector/pgvector).

Take a look at this [Vector DB Comparison](https://superlinked.com/vector-db-comparison).

Watch this Vector Database Tutorial (3 min):

[![Vector databases are so hot right now. WTF are they? (3 min)](https://i.ytimg.com/vi/klTvEwg3oJ4/sddefault.jpg)](https://youtu.be/klTvEwg3oJ4)

### [ChromaDB](#/vector-databases?id=chromadb)

Here’s a minimal example using Chroma:

```
# /// script
# requires-python = "==3.12"
# dependencies = [
#   "chromadb",
#   "sentence-transformers",
# ]
# ///

import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

async def setup_vector_db():
    """Initialize Chroma DB with an embedding function."""
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="BAAI/bge-base-en-v1.5"
    )
    client = chromadb.PersistentClient(path="./vector_db")
    collection = client.create_collection(
        name="documents",
        embedding_function=sentence_transformer_ef
    )
    return collection

async def search_similar(collection, query: str, n_results: int = 3) -> list[dict]:
    """Search for documents similar to the query."""
    d = collection.query(query_texts=[query], n_results=n_results)
    return [
        {"id": id, "text": text, "distance": distance}
        for id, text, distance in zip(d["ids"][0], d["documents"][0], d["distances"][0])
    ]

async def main():
    collection = await setup_vector_db()

    # Add some documents
    collection.add(
        documents=["Apple is a fruit", "Orange is citrus", "Computer is electronic"],
        ids=["1", "2", "3"]
    )

    # Search
    results = await search_similar(collection, "fruit")
    print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())Copy to clipboardErrorCopied
```

### [LanceDB](#/vector-databases?id=lancedb)

Here’s the same example using LanceDB:

```
# /// script
# requires-python = "==3.12"
# dependencies = [
#   "lancedb",
#   "pyarrow",
#   "sentence-transformers",
# ]
# ///

import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer

async def setup_vector_db():
    """Initialize LanceDB with an embedding function."""
    model = SentenceTransformer("BAAI/bge-base-en-v1.5")
    db = lancedb.connect("./vector_db")

    # Create table with schema for documents
    table = db.create_table(
        "documents",
        schema=pa.schema([
            pa.field("id", pa.string()),
            pa.field("text", pa.string()),
            pa.field("vector", pa.list_(pa.float32(), list_size=768))
        ])
    )
    return table, model

async def search_similar(table, model, query: str, n_results: int = 3) -> list[dict]:
    """Search for documents similar to the query."""
    query_embedding = model.encode(query)
    results = table.search(query_embedding).limit(n_results).to_list()
    return [{"id": r["id"], "text": r["text"], "distance": float(r["_distance"])} for r in results]

async def main():
    table, model = await setup_vector_db()

    # Add some documents
    documents = ["Apple is a fruit", "Orange is citrus", "Computer is electronic"]
    embeddings = model.encode(documents)

    table.add(data=[
        {"id": str(i), "text": text, "vector": embedding}
        for i, (text, embedding) in enumerate(zip(documents, embeddings), 1)
    ])

    # Search
    results = await search_similar(table, model, "fruit")
    print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())Copy to clipboardErrorCopied
```

### [DuckDB](#/vector-databases?id=duckdb)

Here’s the same example using DuckDB:

```
# /// script
# requires-python = "==3.12"
# dependencies = [
#   "duckdb",
#   "sentence-transformers",
# ]
# ///

import duckdb
from sentence_transformers import SentenceTransformer

async def setup_vector_db() -> tuple[duckdb.DuckDBPyConnection, SentenceTransformer]:
    """Initialize DuckDB with VSS extension and embedding model."""
    # Initialize model
    model = SentenceTransformer("BAAI/bge-base-en-v1.5")
    vector_dim = model.get_sentence_embedding_dimension()

    # Setup DuckDB with VSS extension
    conn = duckdb.connect(":memory:")
    conn.install_extension("vss")
    conn.load_extension("vss")

    # Create table with vector column
    conn.execute(f"""
        CREATE TABLE documents (
            id VARCHAR,
            text VARCHAR,
            vector FLOAT[{vector_dim}]
        )
    """)

    # Create HNSW index for vector similarity search
    conn.execute("CREATE INDEX vector_idx ON documents USING HNSW (vector)")
    return conn, model

async def search_similar(conn: duckdb.DuckDBPyConnection, model: SentenceTransformer,
                        query: str, n_results: int = 3) -> list[dict]:
    """Search for documents similar to query using vector similarity."""
    # Encode query to vector
    query_vector = model.encode(query).tolist()

    # Search using HNSW index with explicit FLOAT[] cast
    results = conn.execute("""
        SELECT id, text, array_distance(vector, CAST(? AS FLOAT[768])) as distance
        FROM documents
        ORDER BY array_distance(vector, CAST(? AS FLOAT[768]))
        LIMIT ?
    """, [query_vector, query_vector, n_results]).fetchall()

    return [{"id": r[0], "text": r[1], "distance": float(r[2])} for r in results]

async def main():
    conn, model = await setup_vector_db()

    # Add sample documents
    documents = ["Apple is a fruit", "Orange is citrus", "Computer is electronic"]
    embeddings = model.encode(documents).tolist()

    # Insert documents and vectors
    conn.executemany("""
        INSERT INTO documents (id, text, vector)
        VALUES (?, ?, ?)
    """, [(str(i), text, embedding)
          for i, (text, embedding) in enumerate(zip(documents, embeddings), 1)])

    # Search similar documents
    results = await search_similar(conn, model, "fruit")
    print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())Copy to clipboardErrorCopied
```

[Previous

Topic modeling](#/topic-modeling)

[Next

RAG with the CLI)](#/rag-cli)

---


# File: Version_Control__Git,_GitHub.md

---
title: "Version Control: Git, GitHub"
original_url: "https://tds.s-anand.net/#/git?id=version-control-git-github"
downloaded_at: "2025-05-31T21:39:26.375606"
---

[Version Control: Git, GitHub](#/git?id=version-control-git-github)
-------------------------------------------------------------------

[Git](https://git-scm.com/) is the de facto standard for version control of software (and sometimes, data as well). It’s a system that keeps track of changes you make to files and folders. It allows you to revert to a previous state, compare changes, etc. It’s a central tool in any developer’s workflow.

[GitHub](https://github.com/) is the most popular hosting service for Git repositories. It’s a website that shows your code, allows you to collaborate with others, and provides many useful tools for developers.

Watch these introductory videos to learn the basics of Git and GitHub (98 min):

[![Git Tutorial for Beginners: Command-Line Fundamentals (30 min)](https://i.ytimg.com/vi_webp/HVsySz-h9r4/sddefault.webp)](https://youtu.be/HVsySz-h9r4)

[![Git and GitHub for Beginners - Crash Course (68 min)](https://i.ytimg.com/vi_webp/RGOj5yH7evk/sddefault.webp)](https://youtu.be/RGOj5yH7evk)

Essential Git Commands:

```
# Repository Setup
git init                   # Create new repo
git clone url              # Clone existing repo
git remote add origin url  # Connect to remote

# Basic Workflow
git status                 # Check status
git add .                  # Stage all changes
git commit -m "message"    # Commit changes
git push origin main       # Push to remote

# Branching
git branch                 # List branches
git checkout -b feature    # Create/switch branch
git merge feature          # Merge branch
git rebase main            # Rebase on main

# History
git log --oneline          # View history
git diff commit1 commit2   # Compare commits
git blame file             # Show who changed whatCopy to clipboardErrorCopied
```

Best Practices:

1. **Commit Messages**

   ```
   # Good commit message format
   type(scope): summary

   Detailed description of changes.

   # Examples
   feat(api): add user authentication
   fix(db): handle null values in queryCopy to clipboardErrorCopied
   ```
2. **Branching Strategy**

   * main: Production code
   * develop: Integration branch
   * feature/\*: New features
   * hotfix/\*: Emergency fixes
3. **Code Review**

   * Keep PRs small (<400 lines)
   * Use draft PRs for WIP
   * Review your own code first
   * Respond to all comments

Essential Tools

* [GitHub Desktop](https://desktop.github.com/): GUI client
* [GitLens](https://gitlens.amod.io/): VS Code extension
* [gh](https://cli.github.com/): GitHub CLI
* [pre-commit](https://pre-commit.com/): Git hooks

[Previous

Database: SQLite](#/sqlite)

[Next

2. Deployment Tools](#/deployment-tools)

---


# File: Vision_Models.md

---
title: "Vision Models"
original_url: "https://tds.s-anand.net/#/data-analysis-with-datasette"
downloaded_at: "2025-05-31T21:36:26.075981"
---

404 - Not found
===============

---


# File: Visualizing_Animated_Data_with_Flourish.md

---
title: "Visualizing Animated Data with Flourish"
original_url: "https://tds.s-anand.net/#/visualizing-animated-data-with-flourish?id=visualizing-animated-data-with-flourish"
downloaded_at: "2025-05-31T21:39:24.278477"
---

[Visualizing Animated Data with Flourish](#/visualizing-animated-data-with-flourish?id=visualizing-animated-data-with-flourish)
-------------------------------------------------------------------------------------------------------------------------------

[![Visualizing animated data with Flourish](https://i.ytimg.com/vi_webp/JrnIu5Bm8i4/sddefault.webp)](https://youtu.be/JrnIu5Bm8i4)

[Previous

Visualizing Animated Data with PowerPoint](#/visualizing-animated-data-with-powerpoint)

[Next

Visualizing Network Data with Kumu](#/visualizing-network-data-with-kumu)

---


# File: Visualizing_Animated_Data_with_PowerPoint.md

---
title: "Visualizing Animated Data with PowerPoint"
original_url: "https://tds.s-anand.net/#/visualizing-animated-data-with-powerpoint?id=visualizing-animated-data-with-powerpoint"
downloaded_at: "2025-05-31T21:39:22.175700"
---

[Visualizing Animated Data with PowerPoint](#/visualizing-animated-data-with-powerpoint?id=visualizing-animated-data-with-powerpoint)
-------------------------------------------------------------------------------------------------------------------------------------

[![Visualizing animated data with PowerPoint](https://i.ytimg.com/vi_webp/umHlPDFVWr0/sddefault.webp)](https://youtu.be/umHlPDFVWr0)

* [How to make a bar chart race in PowerPoint](https://blog.gramener.com/bar-chart-race-in-powerpoint/)

[Previous

Visualizing Forecasts with Excel](#/visualizing-forecasts-with-excel)

[Next

Visualizing Animated Data with Flourish](#/visualizing-animated-data-with-flourish)

---


# File: Visualizing_Charts_with_Excel.md

---
title: "Visualizing Charts with Excel"
original_url: "https://tds.s-anand.net/#/visualizing-charts-with-excel?id=visualizing-charts-with-excel"
downloaded_at: "2025-05-31T21:38:20.877181"
---

[Visualizing Charts with Excel](#/visualizing-charts-with-excel?id=visualizing-charts-with-excel)
-------------------------------------------------------------------------------------------------

[![Visualizing charts with Google Data StudioTools to visualize numbers](https://i.ytimg.com/vi_webp/sORnCj52COw/sddefault.webp)](https://youtu.be/sORnCj52COw?t=1813s)

[Previous

Visualizing Network Data with Kumu](#/visualizing-network-data-with-kumu)

[Next

Data Visualization with Seaborn](#/data-visualization-with-seaborn)

---


# File: Visualizing_Forecasts_with_Excel.md

---
title: "Visualizing Forecasts with Excel"
original_url: "https://tds.s-anand.net/#/visualizing-forecasts-with-excel?id=visualizing-forecasts-with-excel"
downloaded_at: "2025-05-31T21:38:50.942736"
---

[Visualizing Forecasts with Excel](#/visualizing-forecasts-with-excel?id=visualizing-forecasts-with-excel)
----------------------------------------------------------------------------------------------------------

[![Visualizing forecasts with Excel](https://i.ytimg.com/vi_webp/judFpVgfsV4/sddefault.webp)](https://youtu.be/judFpVgfsV4)

* [Excel File](https://docs.google.com/spreadsheets/d/1a6cSbmZKjX_ZzBsWWrPQwU_4KgRNMwc0/view#gid=1138079165)

[Previous

7. Data Visualization](#/data-visualization)

[Next

Visualizing Animated Data with PowerPoint](#/visualizing-animated-data-with-powerpoint)

---


# File: Visualizing_Network_Data_with_Kumu.md

---
title: "Visualizing Network Data with Kumu"
original_url: "https://tds.s-anand.net/#/visualizing-network-data-with-kumu?id=visualizing-network-data-with-kumu"
downloaded_at: "2025-05-31T21:38:15.105926"
---

[Visualizing Network Data with Kumu](#/visualizing-network-data-with-kumu?id=visualizing-network-data-with-kumu)
----------------------------------------------------------------------------------------------------------------

[![Visualizing network data with Kumu](https://i.ytimg.com/vi_webp/OndB17bigkc/sddefault.webp)](https://youtu.be/OndB17bigkc)

* [Kumu](https://kumu.io)
* [IMDB data](https://developer.imdb.com/non-commercial-datasets/)
* [Jupyter Notebook](https://colab.research.google.com/drive/1CHR68fw7lZC9H2JtVW4LXpUvNwfM_VE-?usp=sharing)

[![Network analysis – filtering by year](https://i.ytimg.com/vi_webp/oi4fDzqsCes/sddefault.webp)](https://youtu.be/oi4fDzqsCes)

[Previous

Visualizing Animated Data with Flourish](#/visualizing-animated-data-with-flourish)

[Next

Visualizing Charts with Excel](#/visualizing-charts-with-excel)

---


# File: Web_Automation_with_Playwright.md

---
title: "Web Automation with Playwright"
original_url: "https://tds.s-anand.net/#/data-visualization-with-chatgpt"
downloaded_at: "2025-05-31T21:36:46.887653"
---

404 - Not found
===============

---


# File: Web_Framework__FastAPI.md

---
title: "Web Framework: FastAPI"
original_url: "https://tds.s-anand.net/#/fastapi?id=web-framework-fastapi"
downloaded_at: "2025-05-31T21:38:22.071317"
---

[Web Framework: FastAPI](#/fastapi?id=web-framework-fastapi)
------------------------------------------------------------

[FastAPI](https://fastapi.tiangolo.com/) is a modern Python web framework for building APIs with automatic interactive documentation. It’s fast, easy to use, and designed for building production-ready REST APIs.

Here’s a minimal FastAPI app, `app.py`:

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)Copy to clipboardErrorCopied
```

Run this with `uv run app.py`.

1. **Handle errors by raising HTTPException**

   ```
   from fastapi import HTTPException

   async def get_item(item_id: int):
       if not valid_item(item_id):
           raise HTTPException(
               status_code=404,
               detail=f"Item {item_id} not found"
           )Copy to clipboardErrorCopied
   ```
2. **Use middleware for logging**

   ```
   from fastapi import Request
   import time

   @app.middleware("http")
   async def add_timing(request: Request, call_next):
       start = time.time()
       response = await call_next(request)
       response.headers["X-Process-Time"] = str(time.time() - start)
       return responseCopy to clipboardErrorCopied
   ```

Tools:

* [FastAPI CLI](https://fastapi.tiangolo.com/tutorial/fastapi-cli/): Project scaffolding
* [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation
* [SQLModel](https://sqlmodel.tiangolo.com/): SQL databases
* [FastAPI Users](https://fastapi-users.github.io/): Authentication

Watch this FastAPI Course for Beginners (64 min):

[![FastAPI Course for Beginners (64 min)](https://i.ytimg.com/vi_webp/tLKKmouUams/sddefault.webp)](https://youtu.be/tLKKmouUams)

[Previous

REST APIs](#/rest-apis)

[Next

Authentication: Google Auth](#/google-auth)

---


# File: Wikipedia_Data_with_Python.md

---
title: "Wikipedia Data with Python"
original_url: "https://tds.s-anand.net/#/wikipedia-data-with-python?id=wikipedia-data-with-python"
downloaded_at: "2025-05-31T21:39:23.226490"
---

[Wikipedia Data with Python](#/wikipedia-data-with-python?id=wikipedia-data-with-python)
----------------------------------------------------------------------------------------

[![Wikipedia data with Wikimedia Python library](https://i.ytimg.com/vi_webp/b6puvm-QEY0/sddefault.webp)](https://youtu.be/b6puvm-QEY0)

You’ll learn how to scrape data from Wikipedia using the `wikipedia` Python library, covering:

* **Installing and Importing**: Use pip install to get the Wikipedia library and import it with import wikipedia as wk.
* **Keyword Search**: Use the search function to find Wikipedia pages containing a specific keyword, limiting results with the results argument.
* **Fetching Summaries**: Use the summary function to get a concise summary of a Wikipedia page, limiting sentences with the sentences argument.
* **Retrieving Full Pages**: Use the page function to obtain the full content of a Wikipedia page, including sections and references.
* **Accessing URLs**: Retrieve the URL of a Wikipedia page using the url attribute of the page object.
* **Extracting References**: Use the references attribute to get all reference links from a Wikipedia page.
* **Fetching Images**: Access all images on a Wikipedia page via the images attribute, which returns a list of image URLs.
* **Extracting Tables**: Use the pandas.read\_html function to extract tables from the HTML content of a Wikipedia page, being mindful of table indices.

Here are links and references:

* [Wikipedia Library - Notebook](https://colab.research.google.com/drive/1-w8Jo6xcQs2jK0NxNddPW4HVCZhXmTBe)
* Learn about the [`wikipedia` package](https://wikipedia.readthedocs.io/en/latest/)

**NOTE**: Wikipedia is constantly edited. The page may be different now from when the video was recorded. Handle accordingly.

[Previous

Nominatim API with Python](#/nominatim-api-with-python)

[Next

Scraping PDFs with Tabula](#/scraping-pdfs-with-tabula)

---
