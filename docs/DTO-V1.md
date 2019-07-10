
VRenetic AI DTO
===============

Definition
----------

Full definition of [v1.0.0](/data/dtos/v1.0.0.json)

Example
-------

## Transaction

```json
{
    "transaction_id": "string"
}
```

## Input

### Entity

#### Standard IO

```json
{
    "input0": "string",
    "input1": "string",
    "output": "string",
    "error": "string"
}
```

#### User

```json
{
    "user_name": "Chris",
    "user_age": "36",
    "system_user_role": "user|trial|studio|afu",
    "region_legal_gdpr": "Poland",
    "region_registration_signup": "UK",
    "region_session_datacenter": "Germany",
    "region_relatime_gps": "Switzerland",
}
```

#### Content

```json
{
    "content_type": "live|capsule|photo",
    "content_age": "1436s",
    "content_projection": "flat|spherical360",
    "content_settings_muted": "true|false",
    "content_audio_language": "unknown|lang_code",
    "publisher_region_legal_gdpr": "Poland",
    "publisher_region_registration_signup": "UK",
    "publisher_region_session_datacenter": "Germany",
    "publisher_region_relatime_gps": "Switzerland",
    "publisher_profile_followers_count": "233",
    "publisher_profile_library_count": "22",
    "publisher_profile_library_total_views": "234001",
    "publisher_profile_library_total_likes": "2333",
    "publisher_profile_library_total_comments": "33",
    "publisher_profile_library_total_reported": "0"
}
```

### Context

#### Context

```json
{
    "ownership_user_to_content": "true",
    "relation_user_to_content_publisher_friends": "true",
    "relation_user_to_content_publisher_follower": "true",
    "relation_content_publisher_to_user_follower": "true"
}
```

### Statistic

#### User Feed Activity

```json
{
    "content_type_live": "12",
    "content_type_capsule": "132",
    "content_projection_flat": "12",
    "content_projection_spherical360": "222",
    "rate_last_minute": "23",
    "rate_last_hour": "45",
    "region_own_gdpr": "23",
    "region_all": "435",
    "region_us": "23",
    "region_uk": "12",
    "region_other": "123"
}
```

#### Source Activity

```json
{
    "source_content_type": "live|capsule|photo",
    "source_content_projection": "flat|spherical360",
    "source_rate_last_minute": "23",
    "source_rate_last_hour": "45",
    "region_all": "435",
    "region_us": "23",
    "region_uk": "12",
    "region_other": "123"
}
```

#### User Behaviours

This will be used for future re-training of Neural Netowrk.
```json
{
    "date_form": "timestamp",
    "date_to": "timestamp",
    "behaviours_count": "1",
    "behaviours": [
        {
            "type": "like|view|comment|play|report|block|flag",
            "entity_type": "video-flat|video-360|photo|comment|user",
            "entity_dto": {}
        }
    ]
}
```

### Configuration

#### User Preferences

This will be used for future re-training of Neural Netowrk.
```json
{
    "prefer_region_own_max": "70%",
    "prefer_source_type_spherical360_max": "40%"
}
```

## Output

#### Relevancy

```json
{
    "relevancy_index": "0|1",
}
```

#### Distirbution

```json
{
    "distribution_policy": "0|0.5|1"
}
```
0.0 - ignore, 0.5 - byffer by time, 1.0 - realtime
