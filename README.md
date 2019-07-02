
vrenetic-ai
===========

VRenetic AI Cli tools.

See [TODO](https://github.com/vrenetic-inc/vrenetic-ai-cli#todo) section

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
    ann-run             ANN Run
    ann-show            ANN Show
    workflow-run        AI Worfklow Run
    workflow-show       AI Worfklow Show
    info                General setup information

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
  "stdio": {},
  "user": {},
  "content": {},
  "statistic-user-feed-activity": {},
  "statistic-source-activity": {},
  "statistic-user-behaviour": {},
  "configuration-user-preference": {},
  "relevancy": {},
  "distribution": {}
}
```

### Show available ANNs
```bash
$ vrenetic-ai ann-show
5cfe0db269e0ba0001bfb7df / 0.0.1  -  Vresh Feed Item Relevancy Index for global population market
5b9fa90171d4f00001bc863e / 0.0.1  -  Analog PassThrough ANN with always Positive 1.0 response
5b21f94435a6a400013c6eca / 0.0.1  -  Analog PassThrough ANN with always Negative 0.0 response
9c21f99999a6a400013c6321 / 0.0.1  -  Binary logical negation (NOT) as ANN with always inverted input value as output
0021f99999a6a400013c0000 / 0.0.1  -  Binary logical conjunction (AND) as ANN with two inputs and single output
bc21f99999a6a400013c6666 / 0.0.1  -  Binary logical disjunction (OR) as ANN with two inputs and single output
acacf99999a6a400013c4321 / 0.0.1  -  Binary logical exclusive disjunction (XOR) as ANN with two inputs and single output
```

### Show available Workflows
```bash
$ vrenetic-ai workflow-show
604f08de52ad6365011c4aa7 / 0.0.1  -  Serial passthrough via 2 dummy ANNs
704f08de52ad6365011c4abc / 0.0.1  -  Serial Inverters with 3 layers (NOT::NOT::NOT)
111108de52ad6365011caabb / 0.0.1  -  Parallel topology with 1 layer (AND+OR+XOR)
885608de52ad636501mmaa9a / 0.0.1  -  Mixed serial&parallel topology with 3 layers (AND+OR::OR+AND::XOR)
```

### Show environment info
```bash
$ vrenetic-ai info
----- Environment details ----
Version: 0.0.2
OpenCL support: YES
OpenCV support: YES

------- OpenCL details -------
Portable Computing Language
 - Profile:  FULL_PROFILE
 - Version:  OpenCL 1.2 pocl 1.3 Release, LLVM 8.0.0, SLEEF, DISTRO, POCL_DEBUG
 - Devices:
   -  pthread
Apple
 - Profile:  FULL_PROFILE
 - Version:  OpenCL 1.2 (Apr  7 2019 18:38:19)
 - Devices:
   -  Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz
   -  Intel(R) UHD Graphics 630
   -  AMD Radeon Pro 560X Compute Engine

------- OpenCV details -------
General configuration for OpenCV 3.4.2 =====================================
  Version control:               unknown

  Extra modules:
    Location (extra):            /opt/concourse/worker/volumes/live/9523d527-1b9e-48e0-7ed0-a36adde286f0/volume/opencv-suite_1535558719691/work/opencv_contrib-3.4.2/modules
    Version control (extra):     unknown

  Platform:
    Timestamp:                   2018-08-29T16:23:50Z
    Host:                        Darwin 14.5.0 x86_64
    CMake:                       3.12.0
    CMake generator:             Unix Makefiles
    CMake build tool:            /opt/concourse/worker/volumes/live/9523d527-1b9e-48e0-7ed0-a36adde286f0/volume/opencv-suite_1535558719691/_build_env/bin/make
    Configuration:               Release

  CPU/HW features:
    Baseline:                    SSE SSE2 SSE3 SSSE3
      requested:                 DETECT
    Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
      requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
      SSE4_1 (3 files):          + SSE4_1
      SSE4_2 (1 files):          + SSE4_1 POPCNT SSE4_2
      FP16 (1 files):            + SSE4_1 POPCNT SSE4_2 FP16 AVX
      AVX (5 files):             + SSE4_1 POPCNT SSE4_2 AVX
      AVX2 (9 files):            + SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
      AVX512_SKX (1 files):      + SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_SKX
```

#### Run ANN with DTO inputs
```bash
$ vrenetic-ai ann-run "ann-ID" '{ "user": "DTO", "content": "DTO", "stdio": "DTO", "relevancy": "DTO" }'
{ "relevancy-index": "1" }
```

#### Run ANN with binary logical negation (NOT)
```bash
$ vrenetic-ai ann-run 9c21f99999a6a400013c6321 '{ "stdio": { "input0": "1" }'
{ "output": 0 }
```

#### Run ANN with binary logical conjunction (AND)
```bash
$ vrenetic-ai ann-run 0021f99999a6a400013c0000 '{ "stdio": { "input0": "1", "input1": "1" } }'
{ "output": 1 }
```

#### Run ANN with binary logical disjunction (OR)
```bash
$ vrenetic-ai ann-run bc21f99999a6a400013c6666 '{ "stdio": { "input0": "0", "input1": "1" } }'
{ "output": 1 }
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

#### AI Package v1.0.0
Follow link to [see document](/docs/AI-PACKAGE-V1.md)

Data storage
------------
Business logic specific meta-data for AI/NN projects, expressions, mappers are provided via [db.json](/data/db.json) file using `JSON` local DB provider.

Integration
-----------

![Integration v.1](/docs/assets/integration-v1.png)

OpenCL and OpenCV
-----------------

For OpenCL/CV it's required to support [miniconda](https://docs.conda.io/en/latest/miniconda.html) and configure environment.

#### Bootstrap
```bash
conda create --name vrenetic-ai
conda install pip
```

#### Installation
```bash
conda install -c conda-forge pyopencl
conda install -c anaconda py-opencv
pip install -r requirements.txt
```

REST API
--------

Please see [VRenetic AI API](https://github.com/vrenetic-inc/vrenetic-api-ai) repository for more details.

Develop and distro
------------------

It's based on [PyScaffold](https://pyscaffold.org)

TODO
----

#### PoC
* Add "transactionID" to input DTOs (optional)
* Convert all "-" into "_" in DTOs
* Packages - define and standardise VRenetic AI Package
* Introduce configurable data storage `--data-path`
* Introduce Provider/Backend abstraction: Frameworks (OpenCL, OpenCV), Libraries (Darknet/...), Hardware (GPU/CPU/FPGA), APIs (Monkeylearn/...)
* Add PoC simple OpenCL support for python expressions with `--opencl-enable`

#### MVP
* Add PoC [text classification](https://monkeylearn.com/) support (topic: scam, spam, auto tags; sentiment: positive, negative; intent: complaint, feedback, request)
* Add GPU support for OpenCL on Linux with `--opencl-device=[from-the-list]`
* CI/CD deployment for package - maybe Travis for testing and Nexus for packages?

#### Beta
* Add GPU support for OpenCV on Linux with `--opencv-enable` and `--opencv-device=[from-the-list]`
* Add PoC simple OpenCV for Facial Recognition, Object Indentification, Segementation and Recognition, AR
* Integrate [Darknet](https://github.com/pjreddie/darknet) with OpenCV for 80 default objects detection

#### Public
* Introduce ANN learning support with provided dataset and ANN model
* Introduce supervised, semi-supervised and unsupervised "ANN" learning
* Introduce multiple backend providers for ANN learning
