---
layout: post
title: How to get comments on a Jekyll blog
comments: true
---

1. Set up a Disqus account
2. Register your site here: <https://disqus.com/admin/create/> and note your site's "shortname".
3. Click Basic on the admin page (<https://*shortname*.disqus.com/admin/settings/general/>) and enter your Website URL (e.g. <http://hwheeler01.github.io/CompBio/>) and Save Changes.
4. Edit the `_config.yml` in your github repo to include your Disqus "shortname".
5. Include `comments: true` in the YAML Front Matter, see step 1 here: <https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions> (Note: step 2 is already included in the <https://github.com/barryclark/jekyll-now> repo

