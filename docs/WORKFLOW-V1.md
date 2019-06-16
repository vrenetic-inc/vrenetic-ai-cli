
VRenetic AI Workflow File
=========================

Definition
----------

Full definition of [v1.0.0](/data/manifests/workflow/v1.0.0.json)

Example
-------

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
                "id": "ann1",
                "ann": [
                    "5b21f94435a6a400013c6eca"
                ],
                "output": [
                    "5b21f94435a6a400013c6eca:relevancy-index"
                ]
            },
            {
                "id": "ann2",
                "ann": [
                    "5b9fa90171d4f00001bc863e"
                ],
                "wiring": {
                    "ann1:output": "5b9fa90171d4f00001bc863e:input0"
                },
                "output": [
                    "5b21f94435a6a400013c6eca:relevancy-index"
                    "5b9fa90171d4f00001bc863e:distribution-policy"
                ]
            }
        ]
    }
}
```
