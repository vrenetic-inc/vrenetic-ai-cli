
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

#### Run NN with DTO inputs
```bash
$ vrenetic-ai nn-run "name-of-registered-nn" '{ "user": "DTO", "content": "DTO", "stat-source": "DTO", "stat-feed": "DTO" }'
{ "relevancy_index": "1" }
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
Business logic specific meta-data for AI/NN projects, expressions, mappers are provided via `data/db.json` file using `JSON` local DB provider.

Integration
-----------

![Integration v.1](/docs/assets/integration-v1.png)

TODO
----
* Add dummny NNs - return always 1, return always 0, return always 0.5
* Move "data" storage to the Cloud eg AWS/S3
* Introduce "workflows" as chain of NNs
* Introduce "dataset" storage support (for future auto re-train of NN)
* Introduce "dataset" training support
* Introduce "NN" training support with multiple backends
* CI/CD deployment for package - maybe Travis?
