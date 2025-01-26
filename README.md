![Header](/docs/images/header.png)

<div align="center">

[![GitHub license](https://img.shields.io/github/license/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/blob/main/LICENCE)
![GitHub last commit](https://img.shields.io/github/last-commit/ndeleforge/binocle?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/network)
[![GitHub stars](https://img.shields.io/github/stars/ndeleforge/binocle?style=for-the-badge)](https://github.com/ndeleforge/binocle/stargazers)

</div>


# Table of contents
* [Installation](#Installation)
    * [Requirements](#Requirements)
    * [Virtual environment](#Virtual-environment)
        * [For Windows](#For-Windows)
        * [For Linux](#For-Linux)
    * [Launch](#Launch)
* [Usage and examples](#Usage-and-examples)
* [Engines in details](#Engines-in-details)
	* [Engines list](#Engines-list)
    * [How to add an engine](#How-to-add-an-engine)
* [Integration with terminal](#Integration-with-terminal)

# Installation
## Requirements

- Python is required.
- Download the last release OR launch the following command
```BASH
git clone https://github.com/ndeleforge/binocle.git
```
- Move into the folder of Binocle
```BASH
cd binocle
```

## Virtual environment

Even if it's optionnal, it is recommended to create a virutal environment.

### For Windows
```BASH
py -m venv venv
venv\Scripts\activate
```

### For Linux
```BASH
python3 -m venv .venv
source .venv/bin/activate
```

## Launch
- To install Python dependencies, launch the following commands
```BASH
pip install -r requirements.txt
```
- Launch Binocle
```BASH
cd launcher
binocle
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
## Engines list

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

# Integration with terminal

Binocle can be launched throught a terminal with the command `binocle`. The idea is to add Binocle folder in your *PATH* global variable.  
It is doable for Windows with `binocle.bat` and Linux with `binocle.sh` which both are a shortcut for `binocle.py`.
