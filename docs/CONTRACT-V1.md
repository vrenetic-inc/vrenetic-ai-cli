
VRenetic AI DTO V.1
===================

Definition
----------

Full definition of [v1.0.0](/data/contracts/v1.0.0.json)

Example
-------

## Input

### Entity

#### User

```json
{
    "user-name": "Chris",
    "user-age": "36",
    "system-user-role": "user|trial|studio|afu",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
}
```

#### Content

```json
{
    "content-type": "live|capsule|photo",
    "content-age": "10m",
    "content-projection": "flat|spherical360",
    "content-settings-muted": "true|false",
    "content-audio-language": "unknown|lang-code",
    "region-legal-gdpr": "Poland",
    "region-registration-signup": "UK",
    "region-session-datacenter": "Germany",
    "region-relatime-gps": "Switzerland",
    "publisher-profile-followers-count": "233",
    "publisher-profile-library-count": "22",
    "publisher-profile-library-total-views": "234001",
    "publisher-profile-library-total-likes": "2333",
    "publisher-profile-library-total-comments": "33",
    "publisher-profile-library-total-reported": "0"
}
```

### Statistic

#### User Feed Activity

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

#### Source Activity

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

#### User Behaviours

This will be used for future re-training of Neural Netowrk.
```json
{
    "date-form": "timestamp",
    "date-to": "timestamp",
    "behaviours-count": "1",
    "behaviours": [
        {
            "type": "like|view|comment|play|report|block|flag",
            "entity-type": "video-flat|video-360|photo|comment|user",
            "entity-dto": {}
        }
    ]
}
```

### Configuration

#### User Preferences

This will be used for future re-training of Neural Netowrk.
```json
{
    "prefer-region-own-max": "70%",
    "prefer-source-type-spherical360-max": "40%"
}
```

## Output

#### Relevancy

```json
{
    "relevancy-index": "0|1",
}
```

#### Distirbution policy

```json
{
    "distribution-policy": "0|0.5|1"
}
```
0.0 - ignore, 0.5 - byffer by time, 1.0 - realtime
