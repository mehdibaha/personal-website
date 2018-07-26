# mehdibaha.com

[![Build status](https://travis-ci.org/mehdibaha/personal-website.svg?branch=master)](https://travis-ci.org/mehdibaha/personal-website)

My [personal website](https://mehdibaha.com).

## Quick start
This website is built using [Hugo](https://gohugo.io/), with the [Sustain theme](https://github.com/nurlansu/hugo-sustain) enabled.

To setup the repository, run:

```bash
git clone https://github.com/mehdibaha/personal-website
./init_theme # init the submodule theme
```

### Disqus

To use this feature, uncomment and fill out the `disqusShortname` parameter in config.toml`

### Google Analytics

To add Google Analytics, simply sign up to Google Analytics to obtain your Google Tracking ID, and add this tracking ID to the `googleAnalytics` parameter in `config.toml`.

## Developing

`hugo serve -D`

It will automatically open <http://localhost:1313/> in your browser

## Publishing

### Netlify

To deploy, simply push to regular master and Netlify will handle the rest.

Details in `netlify.toml`