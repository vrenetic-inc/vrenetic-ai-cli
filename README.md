
vrenetic-ai
===========

VRenetic AI Cli tools.

Usage
-----

```bash
$ vrenetic-ai --version
vrenetic-ai 0.0.1

$ vrenetic-ai --help
usage: vrenetic-ai [-h] [-v] [--version] [-vv] {nn-run,nn-show} ...

VRenetic AI Cli

positional arguments:
  {nn-run,nn-show}     Sub-command help
    nn-run             Neural Network Run
    nn-show            Neural Network Show

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        set loglevel to INFO
  --version            show program's version number and exit
  -vv, --very-verbose  set loglevel to DEBUG
```

Contract v.1
------------

### Input DTOs

#### User entity

```json
{
    "user-name": "Chris",
    "user-age": "36",
    "system-user-role": "user|trial|studio|afu",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
}
```

#### User Preferences entity

```json
{
    "prefer-region-own-max": "70%",
    "prefer-source-type-spherical360-max": "40%"
}
```

#### Content entity

```json
{
    "content-type": "live|capsule|photo",
    "content-age": "10m",
    "content-projection": "flat|spherical360",
    "content-settings-muted": "true|false",
    "content-audio-language": "unknown|lang-code",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
    "publisher-profile-followers-count": "233",
    "publisher-profile-library-count": "22",
    "publisher-profile-library-total-views": "234001",
    "publisher-profile-library-total-likes": "2333",
    "publisher-profile-library-total-comments": "33",
    "publisher-profile-library-total-reported": "0"
}
```

#### Stats Feed entity

```json
{
    "content-type-live": "12",
    "content-type-capsule": "132",
    "content-projection-flat": "12",
    "content-projection-spherical360": "222",
    "rate-last-minute": "23",
    "rate-last-hour": "45",
    "region-own-gdpr": "23",
    "region-all": "435",
    "region-us": "23",
    "region-uk": "12",
    "region-other": "123"
}
```

#### Stats Source entity

```json
{
    "source-content-type": "live|capsule|photo",
    "source-content-projection": "flat|spherical360",
    "source-rate-last-minute": "23",
    "source-rate-last-hour": "45",
    "region-all": "435",
    "region-us": "23",
    "region-uk": "12",
    "region-other": "123"
}
```

### Output DTO

#### Relevancy

```json
{
    "relevancy_index": "0|1",
}
```

#### Distirbution policy

```json
{
    "distribution_policy": "0|0.5|1"
}
```
0.0 - ignore, 0.5 - byffer by time, 1.0 - realtime

Examples
--------

#### Run NN with DTO inputs
```bash
$ vrenetic-ai nn-run "name-of-registered-nn" '{ "user": "DTO", "content": "DTO", "stat-source": "DTO", "stat-feed": "DTO" }'
{ "relevancy_index": "1" }
```

Integration
-----------

![Integration v.1](/docs/assets/integration-v1.png)

Models and data
---------------
Business logic specific meta-data for AI/NN projects, expressions, mappings are provided via `data/db.json` file.

VRenetic AI File
----------------

### Example
```json
{
    "id": "vresh-feed-06c180564e5934837c7c137d130fdf6d-v1",
    "version": "0.0.1",
    "application": "vresh",
    "name" : "vresh feed item relevancy for population for us market",
    "description": "recommends items for sources for users from US region",
    "regions": [ "US" ],
    "tags": [ "population", "feed", "us" ],
    "status": "published",
    "type": "nn",
    "projects": [
        {
            "language": "neural-editor",
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/neural-editor/project.ndo",
            "type": "edit"
        }
    ],
    "expressions": [
        {
            "language": "python",
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/python/expression.py",
            "type": "compute",
            "default": "true"
        },
    ],
    "mappers": [
        {
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/python/mapping.py",
            "language": "python",
            "default": "true"
        }
    ],
    "inputs": [
        {
            "name": "user_age",
            "type": "integer"
        }
    ],
    "output": [
        {
            "name": "conversion",
            "type": "float"
        }
    ]
}
```

TODO
----
* Move "data" storage to the Cloud eg AWS/S3
* Introduce "workflows" as chain of NNs
* Introduce "dataset" storage support
* Introduce "dataset" training support
* Introduce "NN" training support with multiple backends
* CI/CD deployment for package - maybe Travis?
