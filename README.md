# mehdibaha.com
This is the repository for my [personal website](https://mehdibaha.com).

## Quick start
This website is built with [Hugo](https://gohugo.io/) and [Sustain theme](https://github.com/nurlansu/hugo-sustain). 

## Developing
`hugo serve -D`

It will automatically open <http://localhost:1313/> in your browser

## Publishing
To deploy, simply push to regular master and Netlify will handle the rest (more details in `netlify.toml`).

## Features
* Disqus is used in this website to allow comments in blog articles (`disqusShortname` in config.toml`)
* Google Analytics is used for web usage statistics (`googleAnalytics` tracking id in config.toml`)

### Projects
The *Projects* list in my website is a list of my Github repositories. To sync the two lists:
* I added a call to `python sync_projects.py` in the `command` tag in `netlify.toml` so that each build updates the list of repositories displayed on my website.
* Each push to master triggers a build, but I also added a Netlify build webhook which gets called by a [free cron service](https://cron-job.org/) each Monday, so that I get regular updates of my projecs list even if I don't update my website.
