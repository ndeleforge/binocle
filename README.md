# Binocle

[![GitHub license](https://img.shields.io/github/license/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/blob/main/LICENCE)
![GitHub last commit](https://img.shields.io/github/last-commit/ndeleforge/binocle?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/network)
[![GitHub stars](https://img.shields.io/github/stars/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/stargazers)

An easily configurable CLI tool to search for anything, anywhere.

# Table of contents
- [Binocle](#binocle)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Launch](#launch)
- [Usage and examples](#usage-and-examples)
- [Engines in details](#engines-in-details)
  - [Default engine list](#default-engine-list)
  - [How to add an engine](#how-to-add-an-engine)

# Installation

- Python is required !
- Launch the following command :
```BASH
git clone https://github.com/ndeleforge/binocle.git
```
- Move into the folder of Binocle :
```BASH
cd binocle
```
- Even if it's optionnal, it is recommended to create a virutal environment :
```BASH
python -m venv .venv
source .venv/bin/activate
```
- Install Python dependencies in launching the following command :
```BASH
pip install -r requirements.txt
```

# Launch

You can launch Binocle wih this command :
```BASH
python source/binocle.py
```
It is very recommended to make an alias to launch it quicker. For example, for Linux :
```BASH
alias binocle="cd /path/to/Binocle && source .venv/bin/activate && python source/binocle.py"
```

# Usage and examples

Binocle has two ways of working :
- Using default engine search
```BASH
binocle "hello it is a super research"
```
- Specify an engine search
```BASH
binocle d "hello it is a super research"
```

Those two commands do exactly the same thing.  
In the `/config/config.json` file, a *default engine* is defined. By default, it is Duckduckgo but you can change it to anything which exists as engine in the `/config/engines.json` file.

To summarize, if only one argument is used then the default engine will be used. However, to specify another search engine, the engine keyword must be used before the query search.

More examples : 
- Search *My Super Research* on **Duckduckgo** : 
```BASH
binocle d "My Super Research"
```
- Search *SomeYoutuber* on **Youtube** : 
```BASH
binocle yt SomeYoutuber
```

There are also some optionnals arguments :
- `-v` or `--version` : show version
- `-h` or `--help` : show help
- `-l` or `--list` : show engines list

# Engines in details
## Default engine list

| Keyword | Search on
| ------------ | -------------------
| alt | [Alternative To](https://alternativeto.net)
| b | [Bing](https://www.bing.com)
| ch | [Chocolatey](https://chocolatey.org)
| d | [Duckduckgo](https://duckduckgo.com)
| e | [Ecosia](https://www.ecosia.org)
| g | [Google](https://google.com)
| gi | [Github](https://github.com)
| hltb | [HowLongTo Beat](https://howlongtobeat.com/)
| li | [LinkedIn](https://www.linkedin.com)
| meta | [Metacritic](https://metacritic.com)
| mal | [MyAnimeList](https://myanimelist.net)
| q | [Qwant](https://qwant.com)
| re | [Reddit](https://www.reddit.com)
| s | [Startpage](https://startpage.com)
| so  | [StackOverflow](https://stackoverflow.com)
| tw | [Twitch](https://twitch.com)
| wi | [Wikipedia](https://wikipedia.org/wiki/)
| yt | [Youtube](https://youtube.com)


## How to add an engine
An **engine** is composed of **3** mandatory values :
- *name* : must be a string and unique
- *keyword* : must be a string and unique
- *url* : must be a string and unique

Edit the `/config/engines.json` file and follow this template : 
```JSON
{
    "name": "My new engine",
    "keyword": "new",
    "url": "https://some.url"
}
```
