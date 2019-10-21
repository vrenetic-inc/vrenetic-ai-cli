
VRenetic AI Workflow File
=========================

Definition
----------

Full definition of [v1.0.0](/data/manifests/workflow/v1.0.0.json)

Example
-------

* `output` links ANNs outputs on layer to the final buffer of `outputs` with support for `alias`
* `output` of value `5b21f94435a6a400013c6eca::output->>-myoutput` means ANN of id `5b21f94435a6a400013c6eca` without existing output `output` should be mapped to global output as alias `myoutput`
* `wiring` of value `5b9fa90171d4f00001bc863e::output->>-5b9fa90171d4f00001bc863e::input0` means to link ANN of id `5b9fa90171d4f00001bc863e` with existing output `output` into ANN of id `5b9fa90171d4f00001bc863e` with existing input `input0`

#### Serial wiring
```json
{
    "id": "604f08de5b2ad818ce686365011c4aa7",
    "version": "0.0.1",
    "name": "Serial passthrough via 2 dummy ANNs",
    "type": "ann-workflow",
    "contract": "./dtos/v1.0.0.json",
    "topology": {
        "layers": [
            {
                "layer": "0",
                "ann": [
                    "5b21f94435a6a400013c6eca"
                ],
                "wiring": null,
                "output": [
                    "5b21f94435a6a400013c6eca::relevancy_index->>-outputAliasName"
                ]
            },
            {
                "layer": "1",
                "ann": [
                    "5b9fa90171d4f00001bc863e"
                ],
                "wiring": [
                    "5b9fa90171d4f00001bc863e::output->>-5b9fa90171d4f00001bc863e::input0"
                ],
                "output": [
                    "5b9fa90171d4f00001bc863e::distribution_policy->>-outputAliasName"
                ]
            }
        ]
    }
}
```
