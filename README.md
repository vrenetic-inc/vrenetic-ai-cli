
vrenetic-ai
===========

VRenetic AI Cli tools.

Usage
-----

```bash
$ vrenetic-ai -h
usage: ai.py [-h] [-v] [--version] [-vv] {nn-run,nn-list,nn-show} ...

VRenetic AI Cli

positional arguments:
  {nn-run,nn-list,nn-show}
                        Sub-command help
    nn-run              Neural Network Run
    nn-list             Neural Network List
    nn-show             Neural Network Show

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         set loglevel to INFO
  --version             show program's version number and exit
  -vv, --very-verbose   set loglevel to DEBUG
```

Contract v.1
------------

### Input DTOs

#### User entity

```json
{
    "name": "Chris",
    "age": "36",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
}
```

#### User Preferences entity

```json
{
    "region-own-max": "70%",
    "source-type-spherical360-max": "40%"
}
```

#### Content entity

```json
{
    "content-type": "live|capsule|photo",
    "content-projection": "flat|spherical360",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
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

VResh Models Specific
---------------------
Keeps VResh business logic specific data for NN models in `data/vresh`

VRenetic AI File
----------------

### Example
```json
{
    "name" : "vresh feed item relevancy for population for us market",
    "descrition": "recommends items for sources for users from US region",
    "regions": [ "US" ],
    "tags": [ "population", "feed", "us" ],
    "status": "published",
    "type": "nn",
    "models": [
        {
            "language": "python",
            "path": "./models/model_optimisation_1.py",
            "type": "compute"
        },
        {
            "language": "neural-ide",
            "path": "./pyton/vresh-feed-population-us.ndo",
            "type": "edit"
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
