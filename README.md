
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
  {workflow-run,workflow-show,ann-run,ann-show}
                        Commands help
    workflow-run        AI Worfklow Run
    workflow-show       AI Worfklow Show
    ann-run             ANN Run
    ann-show            ANN Show

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         set loglevel to INFO
  --version             show program's version number and exit
  -vv, --very-verbose   set loglevel to DEBUG
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

### Show available ANNs
```bash
$ vrenetic-ai ann-show
5cfe0db269e0ba0001bfb7df / 0.0.1  -  Vresh Feed Item Relevancy Index for global population market
5b9fa90171d4f00001bc863e / 0.0.1  -  Dummy PassThrough NN Relevancy Index with always Positive 1.0 response
5b21f94435a6a400013c6eca / 0.0.1  -  Dummy PassThrough NN Relevancy Index with always Negative 0.0 response
```

### Show available Workflows
```bash
$ vrenetic-ai workflow-show
604f08de52ad6365011c4aa7 / 0.0.1  -  Serial passthrough via 2 dummy ANNs
```

#### Run ANN with DTO inputs
```bash
$ vrenetic-ai ann-run "ann-ID" '{ "user": "DTO", "content": "DTO" }'
{ "relevancy-index": "1" }
```

#### Run Workflow with DTO inputs
```bash
$ vrenetic-ai workflow-run "workflow-ID" '{ "user": "DTO", "content": "DTO", "statistic-source-activity": "DTO", "statistic-user-feed-activity: "DTO" }'
{ 
  "relevancy-index": "1",
  "distribution-policy": "0.5",
}
```

Contract 
--------

#### DTOs v1.0.0
Follow link to [see document](/docs/DTO-V1.md)

#### ANN Manifest v1.0.0
Follow link to [see document](/docs/MANIFEST-V1.md)

#### Workflow Manifest v1.0.0
Follow link to [see document](/docs/WORKFLOW-V1.md)

Data storage
------------
Business logic specific meta-data for AI/NN projects, expressions, mappers are provided via [db.json](/data/db.json) file using `JSON` local DB provider.

Integration
-----------

![Integration v.1](/docs/assets/integration-v1.png)

REST API
--------

Please see [VRenetic AI API](https://github.com/vrenetic-inc/vrenetic-api-ai) repository for more details.

Develop and distro
------------------

It's based on [PyScaffold](https://pyscaffold.org)

Limitations
-----------

* ANN can have only single output
* Workflow assumes unique ANN outputs on the same layer

TODO
----

#### PoC
* Introduce "workflows" as topology of ANNs
* Add dummy Workflows with serial, parallel and mixed topology
* Add dummy ANNs with 2 inputs for AND, OR, NAND, NOR, XOR expressions and 1 input NOT expression

#### MVP
* Add [OpenCL](https://www.khronos.org/opencl/) generic support
* Add PoC simple OpenCL support for python expressions
* Add GPU support for OpenCL on Linux
* CI/CD deployment for package - maybe Travis for testing and Nexus for packages?

#### Beta
* Add [OpenCV](https://opencv.org/) generic support
* Add GPU support for OpenCV on Linux
* Add PoC simple OpenCV for Facial Recognition, Object Indentification, Segementation and Recognition, AR
* Move "data" storage to the Cloud eg AWS/S3

#### Public
* Introduce "dataset" storage support
* Introduce "dataset" training support
* Introduce supervised, semi-supervised and unsupervised "ANN" training mode with multiple backend providers
