---
layout: single
title:  "log on tricks"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
categories: 
  - Jekyll
tags:
  - github
---

Github misc commands
---
1. The support for password authentication was removed, and there is a need to generate Personal Token for pushes.

```bash
git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git

```

Reference: https://techglimpse.com/git-push-github-token-based-passwordless/?fbclid=IwAR0rKIEN0u66i9uFqcSS0YeTTPyvqDF87TkG1zgJSTNRwLol1ZxcSEKMHI4


