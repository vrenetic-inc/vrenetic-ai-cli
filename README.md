
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

### Examples

#### Command line input param structure

```json
{
  "user": {},
  "content": {},
  "statistic-user-feed-activity": {},
  "statistic-source-activity": {},
  "statistic-user-behaviour": {},
  "configuration-user-preference": {}
}
```

### Show available NNs
```bash
$ vrenetic-ai nn-show
5cfe0db269e0ba0001bfb7df / 0.0.1  -  Vresh Feed Item Relevancy Index for global population market
5b9fa90171d4f00001bc863e / 0.0.1  -  Dummy PassThrough NN Relevancy Index with always Positive 1.0 response
5b21f94435a6a400013c6eca / 0.0.1  -  Dummy PassThrough NN Relevancy Index with always Negative 0.0 response
```

#### Run NN with DTO inputs
```bash
$ vrenetic-ai nn-run "nn-ID" '{ "user": "DTO", "content": "DTO", "statistic-source-activity": "DTO", "statistic-user-feed-activity: "DTO" }'
{ "relevancy-index": "1" }
```

Contract 
--------

#### DTOs V.1
Follow link to [see document](/docs/CONTRACT-V1.md)

AI Manifest
-----------

#### Manifest V.1
Follow link to [see document](/docs/MANIFEST-V1.md)

Data storage
------------
Business logic specific meta-data for AI/NN projects, expressions, mappers are provided via [db.json](/data/db.json) file using `JSON` local DB provider.

Integration
-----------

![Integration v.1](/docs/assets/integration-v1.png)

REST API
--------

Please see [VRenetic AI API](https://github.com/vrenetic-inc/vrenetic-api-ai) repository for more details.

TODO
----
* Add full GPU support for expressions
* Introduce "workflows" as chain of NNs
* CI/CD deployment for package - maybe Travis?
* Move "data" storage to the Cloud eg AWS/S3
* Introduce "dataset" training support
* Introduce "NN" training support with multiple backends
* Introduce "dataset" storage support (for future auto re-train of NN)
