
vrenetic-ai
===========

VRenetic AI Cli tools.

Contract v.1
------------

## Input DTOs

### User entity

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

### User Prefernces entity

```json
{
    "region-own-max": "70%",
    "source-type-spherical-max": "40%"
}
```

### Content entity

```json
{
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
}
```

### Stats Feed entity

```json
{
    "content-type-flat": "12",
    "content-type-spherical": "222",
    "rate-last-minute": "23",
    "rate-last-hour": "45",
    "region-own-gdpr": "23",
    "region-all": "435",
    "region-us": "23",
    "region-uk": "12",
    "region-other": "123"
}
```

### Stats Source entity

```json
{
    "source-content-type": "spherical",
    "source-rate-last-minute": "23",
    "source-rate-last-hour": "45",
    "region-all": "435",
    "region-us": "23",
    "region-uk": "12",
    "region-other": "123"
}
```

## Output DTO

### Relevancy

```json
{
    "relevancy_index": "0|1",
}
```

### Distirbution policy

```json
{
    "distribution_policy": "0|0.5|1" // ignore, byffer by time, realtime
}
```

VResh Models Specific
---------------------
Keeps VResh business logic specific data for NN models in `data/vresh`

Examples
--------

```bash
$ vrenetic-ai nn-run "name-of-registered-nn" '{ "user": "DTO", "content": "DTO", "stat-source": "DTO", "stat-feed": "DTO" }'
```

Integraton
----------

![Integration v.1](/docs/assets/integration-v1.png)