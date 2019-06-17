
VRenetic AI Workflow File
=========================

Definition
----------

Full definition of [v1.0.0](/data/manifests/workflow/v1.0.0.json)

Example
-------

* `output` links single ANN output on layer to the final buffer of `outputs`

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
                    "5b21f94435a6a400013c6eca:relevancy-index"
                ]
            },
            {
                "layer": "1",
                "ann": [
                    "5b9fa90171d4f00001bc863e"
                ],
                "wiring": [
                    "5b9fa90171d4f00001bc863e::output---5b9fa90171d4f00001bc863e::input0"
                ],
                "output": [
                    "5b21f94435a6a400013c6eca:relevancy-index"
                    "5b9fa90171d4f00001bc863e:distribution-policy"
                ]
            }
        ]
    }
}
```
