---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
This is a subset of my publications. Full list see [(resume)](http://luoluo-l.github.io/files/resume_lll_aug_2022.pdf). 

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
