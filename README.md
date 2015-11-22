# pypi-alerts

A service for monitoring PyPI packages

##Background

At YunoJuno we have a Django project that includes almost 100 external packages. In order to manage updates to these we have a rolling development task that comes around in the first week of each month, and includes the following:

1. Using `pip list --outdated` list out all available updates
2. Group updates (using [semver](http://semver.org/)) into Major, Minor, Patch, Other
3. Apply patch updates in a single update / commit
4. Apply minor updates as a second commit
5. Take a view on major updates

This project addresses the first two points - monitoring your existing requirements against the latest available, and grouping the updates. Let's say you run the following:

```shell
$ pip list --outdated
Pillow (Current: 2.9.0 Latest: 3.0.0 [sdist])
redis (Current: 2.10.3 Latest: 2.10.5 [wheel])
responses (Current: 0.3.0 Latest: 0.5.0 [wheel])
```

This would be rendered as:

Package | Current | Major | Minor | Patch | Other
--------|---------|-------|-------|-------|-------
Pillow | 2.9.0 | 3.0.0
redis | 2.10.3 ||| 2.10.5
responses | 0.3.0 || 0.5.0 

As a standalone function this is of moderate value - for 100 packages it saves ten minutes fiddling around with the format in a text editor. The more significant value is the constant monitoring of packages (on a daily basis). This will work thus:

1. Upload your `requirements.txt` file to the service
2. View updates (as above), with a unique URL for your project
3. Enter your email address for alerts
4. The service will refresh your project (daily), and email you with any updates found

And that's it. There are probably lots more things it could do, but that's all for now.
