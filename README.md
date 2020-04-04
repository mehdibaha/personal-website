# mehdibaha.com
[![Netlify Status](https://api.netlify.com/api/v1/badges/432d3911-222f-46b7-9d34-98dd9417aee4/deploy-status)](https://app.netlify.com/sites/mehdibaha/deploys)

This is the repository for my [personal website](https://mehdibaha.com).

## Quick start
This website is built with [Hugo](https://gohugo.io/) and [Sustain theme](https://github.com/nurlansu/hugo-sustain).

### Developing
To begin developement, you need to clone this repository (and the sub-theme) by running this command:
`git clone --depth 1 https://github.com/mehdibaha/personal-website`

After making your changes, you can preview the website on <http://localhost:1313/> by running:
`hugo serve -D`

It will automatically open <http://localhost:1313/> in your browser

### Publishing
To deploy, simply push to **master** and Netlify will handle the rest (more details in `netlify.toml`).

### Features
* Disqus is used in this website to allow comments in blog articles (`disqusShortname` in `config.toml`)
	- Link for the Disqus admin panel: https://mehdibaha.disqus.com/admin/
* Google Analytics is used for web usage statistics (`googleAnalytics` tracking id in `config.toml`)
    - Link for the Analytics admin panel: https://analytics.google.com (account: elmehdi.baha@gmail.com)
* The [projects list](https://mehdibaha.com/projects) is a list of my current Github repositories. To achieve syncing between the two:
    - I added `python sync_projects.py` to the `command` tag in `netlify.toml` so that each build updates the list of repositories displayed on my website.
    - Additionally, I added a Netlify build webhook which gets called by a [free cron service](https://cron-job.org/) each Monday.

