
VRenetic AI Manifest File
=========================

Definition
----------

Full definition of [v1.0.0](/data/manifests/ann/v1.0.0.json)

Example
-------
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
    "learning": "supervised",
    "type": "ann-default",
    "projects": [
        {
            "language": "neural-editor",
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/neural-editor/project.ndo",
            "type": "edit"
        }
    ],
    "trainers": [
        {
            "language": "python",
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/python/trainer.py",
            "default": "true"
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
            "path": "./assets/06c180564e5934837c7c137d130fdf6d/python/mapper.py",
            "language": "python",
            "default": "true"
        }
    ],
    "contract": [
        {
            "version": "1.0.0",
            "type": "dto",
            "path": "./dtos/v1.0.0.json"
        }
    ],
    "inputs": [
        {
            "name": "user_age",
            "type": "integer",
            "contract": {
                "dto": "user",
                "param": "user-age"
            }
        }
    ],
    "output": [
        {
            "name": "relevancy_index",
            "type": "float",
            "contract": {
                "dto": "relevancy-index",
                "param": "relevancy-index"
            }
        }
    ]
}
```
